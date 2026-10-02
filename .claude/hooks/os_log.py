#!/usr/bin/env python3
"""PostToolUse logger (AI Entrepreneur OS, hostile-review fix 6).

Writes an append-only, hash-chained JSONL record to data/ai-os/log/YYYY-MM-DD.jsonl for:
  - every tool call made by an os-* subagent,
  - any write/edit touching data/ai-os/, docs/ai-os/, .claude/agents or .claude/commands (any caller),
  - any MCP connector call (any caller) - the outbound-capable surface.
It records WHO, WHAT tool and WHICH target. It never records file contents, message bodies or secrets.
Agents cannot write the log (os_guard.py denies it), so it is evidence they cannot erase.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os_common as C  # noqa: E402

SENSITIVE_DIRS = ("data/ai-os/", "docs/ai-os/", ".claude/agents/", ".claude/commands/")


def target_of(tool, ti):
    if tool in C.WRITE_TOOLS:
        return ti.get("file_path") or ti.get("notebook_path") or ""
    if tool == "Read":
        return ti.get("file_path") or ""
    if tool in ("Grep", "Glob"):
        return ti.get("path") or "(default: project root)"
    if tool == "WebFetch":
        return (ti.get("url") or "")[:300]
    if tool == "WebSearch":
        return (ti.get("query") or "")[:120]
    if tool == "Bash":
        cmd = ti.get("command") or ""
        return cmd[:60] + " #sha256:" + C.sha256_text(cmd)[:16]
    if tool.startswith("mcp__"):
        return "args:" + ",".join(sorted(ti.keys()))[:120]
    if tool in ("Agent", "Task"):
        return ti.get("subagent_type") or ""
    return ""


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name") or ""
    ti = data.get("tool_input") or {}
    agent = data.get("agent_type") or ""
    root = C.project_root(data)
    target = target_of(tool, ti)
    rel = None
    if (tool in C.WRITE_TOOLS or tool in C.READ_TOOLS) and target and not target.startswith("(default"):
        rel = C.rel_path(root, target, data.get("cwd"))
    sensitive = tool in C.WRITE_TOOLS and bool(rel) and any(rel.startswith(d) for d in SENSITIVE_DIRS)
    if not (agent.startswith(C.AGENT_PREFIX) or sensitive or tool.startswith("mcp__")):
        return
    resp = data.get("tool_response")
    ok = not (isinstance(resp, dict) and (resp.get("is_error") or resp.get("error")))
    C.log_event(root, {"event": "tool", "tool": tool, "agent_type": agent, "agent_id": data.get("agent_id") or "",
                       "target": rel if rel is not None else target, "ok": ok,
                       "session": (data.get("session_id") or "")[:12]})


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # logging must never break the work, but say so loudly
        sys.stderr.write("OS log hook error (event NOT recorded): %r\n" % (exc,))
        sys.exit(0)
