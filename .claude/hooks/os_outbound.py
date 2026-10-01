#!/usr/bin/env python3
"""PreToolUse policy for WebFetch and connector (mcp__*) calls (hostile-review findings 3 and 4).

  os-* agents    WebFetch only to hosts in docs/ai-os/rules/fetch-allowlist.txt (https, no IP/port/credentials,
                 short query, no long encoded chunks). Any connector call is denied outright.
  every caller   a connector tool that can send, change or spend asks the human for confirmation. Clearly read-only
                 tools (get/list/search/read/query...) pass. Unknown verbs ask.
  OS_OUTBOUND_MODE=off in the environment that LAUNCHED Claude Code switches the connector prompts off; a session
  cannot change its own launch environment.
Fails closed (exit 2) on any error.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import os_common as C  # noqa: E402


def out(decision, reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                             "permissionDecisionReason": "OS outbound guard: " + reason}}))
    sys.exit(0)


def main():
    data = json.load(sys.stdin)
    tool = data.get("tool_name") or ""
    ti = data.get("tool_input") or {}
    agent = data.get("agent_type") or ""
    is_os = agent.startswith(C.AGENT_PREFIX)
    root = C.project_root(data)

    def log(kind, target, why):
        try:
            C.log_event(root, {"event": kind, "tool": tool, "agent_type": agent, "agent_id": data.get("agent_id") or "",
                               "target": target, "why": why})
        except Exception:
            pass

    if tool == "WebFetch" and is_os:
        url = ti.get("url") or ""
        why = C.fetch_verdict(url, C.load_allowlist(root))
        if why:
            log("deny", url[:200], why)
            out("deny", "fetch blocked: " + why)
        return
    if tool.startswith("mcp__"):
        if is_os:
            if C.connector_allowed(root, agent, tool):
                return  # exact, read-only, owner-allow-listed for this agent; the logger records the call
            log("deny", tool, "connector not allow-listed for this agent")
            out("deny", "%s may not call %s. Connectors are off for agents unless the owner lists this exact read-only tool "
                "for this agent in %s (never for web agents)" % (agent, tool, C.CONNECTOR_ALLOWLIST))
        if os.environ.get("OS_OUTBOUND_MODE", "ask").lower() == "off":
            return
        if C.connector_verdict(tool) == "ask":
            log("ask", tool, "connector tool can send, change or spend; human confirmation required")
            out("ask", "%s can send, change or spend. Confirm you want this exact action." % tool)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write("OS outbound guard error, blocking the call: %r\n" % (exc,))
        sys.exit(2)
