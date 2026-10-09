#!/usr/bin/env python3
"""PreToolUse guard for Read/Grep/Glob (hostile-review finding 3, exfiltration).

The web-capable agents (os-seo, os-market, os-pain-point, os-prospect) can reach the network, so they must not be
able to see private data. They may read only docs/ai-os/ops|rules, docs/marketing-context and the OS skill - never
data/ai-os/** (leads, drafts, approvals, logs), the rest of the repo, or anything outside the project.
Grep and Glob must name an explicit in-scope path; patterns may not be absolute or contain '..'.
Fails closed (exit 2) on any error. Other agents and the main session are not restricted here.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os_common as C  # noqa: E402


def deny(root, data, target, why):
    try:
        C.log_event(root, {"event": "deny", "tool": data.get("tool_name"), "agent_type": data.get("agent_type") or "",
                           "agent_id": data.get("agent_id") or "", "target": target or "(none)", "why": why})
    except Exception:
        pass
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": "OS read-scope: " + why}}))
    sys.exit(0)


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name")
    agent = data.get("agent_type") or ""
    if tool not in C.READ_TOOLS or agent not in C.WEB_AGENTS:
        return
    ti = data.get("tool_input") or {}
    root = C.project_root(data)
    raw = ti.get("file_path") if tool == "Read" else ti.get("path")
    if not raw:
        deny(root, data, None, "%s must name an explicit path inside %s (a default of the whole project is not allowed)"
             % (tool, ", ".join(C.WEB_READ_ROOTS)))
    if tool == "Glob":
        pat = ti.get("pattern") or ""
        if os.path.isabs(pat) or ".." in pat.replace("\\", "/").split("/"):
            deny(root, data, pat, "Glob pattern may not be absolute or contain '..'")
    rel = C.rel_path(root, raw, data.get("cwd"))
    if rel is not None and os.path.isdir(os.path.join(root, rel)):
        rel = rel.rstrip("/") + "/"
    if not C.read_allowed(agent, rel):
        deny(root, data, rel, "%s is a web-capable agent and may read only: %s" % (agent, ", ".join(C.WEB_READ_ROOTS)))


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write("OS read-scope error, blocking the call: %r\n" % (exc,))
        sys.exit(2)
