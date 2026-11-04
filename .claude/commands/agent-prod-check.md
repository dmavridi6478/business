---
description: Go/no-go production-readiness review of an AI agent against the six questions and the seven-part checklist
argument-hint: <agent description or repo path>
---

Use the `agent-production-readiness` skill. Input: "$ARGUMENTS"

1. Read what the user supplies (description, repo, config). Do not assume capabilities.
2. Fill the seven-part table with evidence or 'missing'; answer the six questions pass/fail.
3. Verdict: READY / READY WITH CONDITIONS / NOT READY, failing question first.
4. List the top five fixes in order, each with owner and test.
