---
description: Write a failure-and-recovery runbook for an agent: detect, understand, recover, resume safely, learn
argument-hint: <agent or workflow name>
---

Use the `agent-production-readiness` skill. Input: "$ARGUMENTS"

1. Ask which tools and write actions the agent has.
2. For each write action define: failure signal, root-cause check, recovery option (retry, roll back, safe point, alternative tool, escalate), and resume condition.
3. Define the human escalation trigger and the named owner.
4. End with the incident-to-improvement step: which prompt or tool changes after each class of failure.
