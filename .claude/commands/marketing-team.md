---
description: Run the Claude Code marketing team: route a goal to up to three department agents, gate drafts through brand-reviewer, return an approval list
argument-hint: <marketing goal, audience, offer, deadline, success number>
---

Use the `claude-code-marketing-team` skill. Input: "$ARGUMENTS"

You are the orchestrator (CEO). Follow the skill's Orchestration steps exactly:
1. Ask once for any missing input.
2. Read docs/marketing-context/{voice,proof,banned,pillars}.md if present.
3. Route to at most three departments using the routing table and invoke the matching mkt-* agents one after another via the Agent tool, passing each output forward.
4. Send each customer-facing draft to the brand-reviewer agent; keep only PASS drafts.
5. Finish with the approval list. Nothing is sent, published or scheduled.
