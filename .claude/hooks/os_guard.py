#!/usr/bin/env python3
"""PreToolUse guard for Write/Edit/MultiEdit/NotebookEdit  (AI Entrepreneur OS, hostile-review fixes 1 and 2).

Rules
  A. ANY caller (subagent or main session): never write data/ai-os/approvals.md or data/ai-os/log/**.
     Those are written only by scripts/os_approvals.py (human, real terminal) and the hooks.
  B. A subagent whose agent_type starts with "os-": may write only its own allow-listed .md paths
     (default data/ai-os/drafts/**). Everything else - .claude/**, docs/**, other agents, anything outside
     the project, any non-.md file, any path that resolves through a symlink or '..' - is denied.
  C. Fail closed: any error in this script blocks the call (exit 2) instead of silently allowing it.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os_common as C  # noqa: E402


def deny(root, data, rel, why):
    try:
        C.log_event(root, {"event": "deny", "tool": data.get("tool_name"), "agent_type": data.get("agent_type") or "",
                           "agent_id": data.get("agent_id") or "", "target": rel or "(outside project)", "why": why})
    except Exception:
        pass  # the deny must still happen even if logging fails
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                             "permissionDecisionReason": "OS guard: " + why}}))
    sys.exit(0)


def main():
    data = json.load(sys.stdin)
    if data.get("tool_name") not in C.WRITE_TOOLS:
        return
    ti = data.get("tool_input") or {}
    raw = ti.get("file_path") or ti.get("notebook_path") or ""
    root = C.project_root(data)
    agent = data.get("agent_type") or ""
    is_os = agent.startswith(C.AGENT_PREFIX)
    if not raw:
        if is_os:
            deny(root, data, None, "write call without a target path")
        return
    rel = C.rel_path(root, raw, data.get("cwd"))
    if rel is not None and C.is_protected(rel):
        deny(root, data, rel, "%s is human/hook-only; agents and sessions may not write it" % rel)
    if is_os and not C.allowed_for(agent, rel):
        allowed = ", ".join(C.ALLOW.get(agent, C.DEFAULT_ALLOW))
        deny(root, data, rel, "%s may write only .md files under: %s" % (agent, allowed))


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # fail closed
        sys.stderr.write("OS guard error, blocking the call: %r\n" % (exc,))
        sys.exit(2)
