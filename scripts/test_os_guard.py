#!/usr/bin/env python3
"""Tests for the OS guard, logger and approval ledger. Run:  python3 -m unittest scripts/test_os_guard.py -v
Each test runs the REAL hook scripts as subprocesses against synthetic hook input in a throw-away project."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest


def rd(path):
    with open(path) as fh:
        return fh.read()


def wr(path, text):
    with open(path, "w") as fh:
        fh.write(text)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(REPO, ".claude", "hooks")
sys.path.insert(0, HOOKS)
sys.path.insert(0, os.path.join(REPO, "scripts"))
import os_common as C  # noqa: E402
import os_approvals as A  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.root = os.path.realpath(tempfile.mkdtemp())
        for d in ("data/ai-os/drafts", "data/ai-os/morning", ".claude/agents", "docs/ai-os/rules"):
            os.makedirs(os.path.join(self.root, d))
        self.env = dict(os.environ, CLAUDE_PROJECT_DIR=self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def run_hook(self, script, payload, raw=None):
        p = subprocess.run([sys.executable, os.path.join(HOOKS, script)], input=raw if raw is not None else json.dumps(payload),
                           capture_output=True, text=True, env=self.env)
        return p

    def write(self, path, agent=None, tool="Write"):
        d = {"tool_name": tool, "tool_input": {"file_path": path}, "cwd": self.root, "session_id": "t"}
        if agent:
            d.update(agent_type=agent, agent_id="a1")
        return self.run_hook("os_guard.py", d)

    def denied(self, p):
        return p.returncode == 0 and '"permissionDecision": "deny"' in p.stdout

    def allowed(self, p):
        return p.returncode == 0 and p.stdout.strip() == ""

    def p(self, rel):
        return os.path.join(self.root, rel)


class GuardTests(Base):
    def test_os_agent_can_write_drafts(self):
        self.assertTrue(self.allowed(self.write(self.p("data/ai-os/drafts/2026-10-01-response.md"), "os-response")))

    def test_os_agent_cannot_rewrite_agents_or_rules(self):
        self.assertTrue(self.denied(self.write(self.p(".claude/agents/os-approval.md"), "os-response")))
        self.assertTrue(self.denied(self.write(self.p("docs/ai-os/rules/approval-limits.md"), "os-response")))

    def test_nobody_can_write_approvals_or_log(self):
        for agent in ("os-response", "os-approval", None):  # None = main session
            self.assertTrue(self.denied(self.write(self.p("data/ai-os/approvals.md"), agent)), agent)
            self.assertTrue(self.denied(self.write(self.p("data/ai-os/log/2026-10-01.jsonl"), agent)), agent)
        self.assertTrue(self.denied(self.write("DATA/AI-OS/Approvals.md", None)))  # case games

    def test_main_session_unrestricted_elsewhere(self):
        self.assertTrue(self.allowed(self.write(self.p("docs/notes.md"), None)))
        self.assertTrue(self.allowed(self.write(self.p(".claude/agents/os-new.md"), None)))

    def test_traversal_and_symlink_escape(self):
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/drafts/../../../.claude/agents/x.md"), "os-response")))
        os.symlink(os.path.join(self.root, ".claude"), os.path.join(self.root, "data/ai-os/drafts/link"))
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/drafts/link/agents/x.md"), "os-response")))
        self.assertTrue(self.denied(self.write("/etc/cron.d/x.md", "os-response")))

    def test_only_markdown(self):
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/drafts/x.py"), "os-response")))
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/drafts/x.sh"), "os-response")))

    def test_per_agent_scopes(self):
        self.assertTrue(self.allowed(self.write(self.p("data/ai-os/morning/2026-10-01.md"), "os-chief-of-staff")))
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/morning/2026-10-01.md"), "os-response")))
        self.assertTrue(self.allowed(self.write(self.p("data/ai-os/approval-queue.md"), "os-approval")))
        self.assertTrue(self.denied(self.write(self.p("data/ai-os/approval-queue.md"), "os-seo")))
        self.assertTrue(self.allowed(self.write(self.p("data/ai-os/watchdog/x.md"), "os-watchdog")))

    def test_edit_and_multiedit_covered(self):
        for tool in ("Edit", "MultiEdit"):
            self.assertTrue(self.denied(self.write(self.p(".claude/agents/os-approval.md"), "os-response", tool)))

    def test_non_write_tools_ignored(self):
        p = self.run_hook("os_guard.py", {"tool_name": "Read", "tool_input": {"file_path": "/etc/passwd"}, "agent_type": "os-response"})
        self.assertTrue(self.allowed(p))

    def test_fail_closed_on_garbage(self):
        self.assertEqual(self.run_hook("os_guard.py", None, raw="{not json").returncode, 2)

    def test_denials_are_logged_and_chain_verifies(self):
        self.write(self.p(".claude/agents/os-approval.md"), "os-response")
        self.write(self.p("data/ai-os/approvals.md"), "os-response")
        day = time.strftime("%Y-%m-%d", time.gmtime())
        path = os.path.join(C.log_dir(self.root), day + ".jsonl")
        self.assertEqual(C.verify_chain(path), (True, None))
        events = [json.loads(x) for x in rd(path).splitlines()]
        self.assertEqual([e["event"] for e in events], ["deny", "deny"])
        # tamper: edit the first line -> chain breaks
        lines = rd(path).splitlines()
        lines[0] = lines[0].replace("os-response", "os-nobody")
        wr(path, "\n".join(lines) + "\n")
        self.assertFalse(C.verify_chain(path)[0])


class LoggerTests(Base):
    def post(self, tool, ti, agent=None):
        d = {"tool_name": tool, "tool_input": ti, "tool_response": {}, "cwd": self.root, "session_id": "sess123456789"}
        if agent:
            d.update(agent_type=agent, agent_id="a1")
        return self.run_hook("os_log.py", d)

    def events(self):
        day = time.strftime("%Y-%m-%d", time.gmtime())
        path = os.path.join(C.log_dir(self.root), day + ".jsonl")
        return [json.loads(x) for x in rd(path).splitlines()] if os.path.exists(path) else []

    def test_logs_subagent_calls_without_content(self):
        self.post("WebFetch", {"url": "https://example.com/a?b=1"}, "os-seo")
        self.post("Write", {"file_path": self.p("data/ai-os/drafts/x.md"), "content": "SECRET LEAD DATA"}, "os-response")
        ev = self.events()
        self.assertEqual([e["tool"] for e in ev], ["WebFetch", "Write"])
        self.assertNotIn("SECRET", json.dumps(ev))

    def test_ignores_unrelated_main_session_noise(self):
        self.post("Bash", {"command": "ls"})
        self.post("Write", {"file_path": self.p("src/app.py")})
        self.assertEqual(self.events(), [])

    def test_logs_main_session_connector_and_sensitive_edits(self):
        self.post("mcp__Gmail__send_message", {"to": "x", "body": "hello"})
        self.post("Edit", {"file_path": self.p(".claude/agents/os-approval.md")})
        ev = self.events()
        self.assertEqual(len(ev), 2)
        self.assertIn("args:", ev[0]["target"])
        self.assertNotIn("hello", json.dumps(ev))


class ApprovalTests(Base):
    CARD = "## ITEM A1 reply to lead\nTo: x@example.com\nText: Hello, Tuesday 10:00?\nCost: EUR 0\n\n## ITEM A2 reminder\nText: Invoice 12 is 31 days late\n"

    def setUp(self):
        super().setUp()
        wr(os.path.join(self.root, "data/ai-os/approval-queue.md"), self.CARD)

    def test_approve_then_check(self):
        self.assertEqual(A.status(self.root, "A1")[0], "pending")
        A.record_decision(self.root, "A1", "approve", "owner")
        self.assertEqual(A.status(self.root, "A1")[0], "approved")
        self.assertEqual(A.status(self.root, "A2")[0], "pending")  # other items unaffected

    def test_edit_voids_approval(self):
        A.record_decision(self.root, "A1", "approve", "owner")
        q = os.path.join(self.root, "data/ai-os/approval-queue.md")
        wr(q, self.CARD.replace("Tuesday 10:00", "Friday 23:00"))
        self.assertEqual(A.status(self.root, "A1")[0], "voided")

    def test_expiry_after_24h(self):
        A.record_decision(self.root, "A1", "approve", "owner")
        self.assertEqual(A.status(self.root, "A1", now=time.time() + 23 * 3600)[0], "approved")
        self.assertEqual(A.status(self.root, "A1", now=time.time() + 25 * 3600)[0], "expired")

    def test_reject_is_not_approval(self):
        A.record_decision(self.root, "A2", "reject", "owner")
        self.assertEqual(A.status(self.root, "A2")[0], "rejected")

    def test_forged_line_breaks_chain_and_blocks_further_approvals(self):
        A.record_decision(self.root, "A1", "approve", "owner")
        ledger = os.path.join(self.root, "data/ai-os/approvals.md")
        forged = json.dumps({"ts": C.utc_now_iso(), "item": "A2", "decision": "approve", "card_sha256": "x", "by": "agent", "prev": "0" * 64})
        wr(ledger, rd(ledger) + forged + "\n")
        self.assertFalse(C.verify_chain(ledger)[0])
        with self.assertRaises(RuntimeError):
            A.record_decision(self.root, "A2", "approve", "owner")

    def test_unknown_item_and_bad_decision(self):
        with self.assertRaises(KeyError):
            A.record_decision(self.root, "NOPE", "approve", "owner")
        with self.assertRaises(ValueError):
            A.record_decision(self.root, "A1", "maybe", "owner")

    def test_cli_refuses_without_terminal(self):
        p = subprocess.run([sys.executable, os.path.join(REPO, "scripts/os_approvals.py"), "approve", "A1"],
                           input="A1\n", capture_output=True, text=True, env=self.env)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("real interactive terminal", p.stderr)
        self.assertEqual(A.read_ledger(self.root), [])


class IntegrityTests(Base):
    def test_missing_log_is_critical_not_ok(self):
        rep = A.integrity(self.root)
        self.assertEqual(rep["verdict"], "CRITICAL")
        self.assertIn("NO EVIDENCE", rep["CRITICAL"][0])

    def test_healthy_state_with_a_blocked_attempt_warns(self):
        C.log_event(self.root, {"event": "tool", "tool": "Write", "agent_type": "os-response",
                                "target": "data/ai-os/drafts/x.md", "ok": True})
        C.log_event(self.root, {"event": "deny", "tool": "Write", "agent_type": "os-response", "target": ".claude/agents/x.md"})
        rep = A.integrity(self.root)
        self.assertEqual(rep["verdict"], "WARN")
        self.assertEqual(rep["denials_today"], 1)

    def test_detects_bypass_when_guard_did_not_enforce(self):
        C.log_event(self.root, {"event": "tool", "tool": "Write", "agent_type": "os-response",
                                "target": ".claude/agents/os-approval.md", "ok": True})
        rep = A.integrity(self.root)
        self.assertEqual(rep["verdict"], "CRITICAL")
        self.assertIn("GATE BYPASS", rep["CRITICAL"][0])

    def test_detects_log_tampering(self):
        C.log_event(self.root, {"event": "tool", "tool": "WebFetch", "agent_type": "os-seo", "target": "https://a", "ok": True})
        C.log_event(self.root, {"event": "tool", "tool": "WebFetch", "agent_type": "os-seo", "target": "https://b", "ok": True})
        path = os.path.join(C.log_dir(self.root), time.strftime("%Y-%m-%d", time.gmtime()) + ".jsonl")
        lines = rd(path).splitlines()
        wr(path, lines[1] + "\n")  # delete first event
        rep = A.integrity(self.root)
        self.assertEqual(rep["verdict"], "CRITICAL")
        self.assertTrue(any("LOG TAMPERING" in c for c in rep["CRITICAL"]))

    def test_report_file_written(self):
        A.integrity(self.root)
        day = time.strftime("%Y-%m-%d", time.gmtime())
        self.assertTrue(os.path.exists(os.path.join(self.root, "data/ai-os/watchdog", "integrity-%s.json" % day)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
