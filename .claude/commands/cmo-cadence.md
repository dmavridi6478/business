---
description: Run one routine from the CMO operating cadence (daily, weekly, monthly or ad hoc) with the right prompt, connectors and safety rule
argument-hint: <daily|weekly|monthly|adhoc|list> [routine number 01-12]
---

Use the `cmo-operating-cadence` skill. Request: "$ARGUMENTS"

1. `list` (or no argument): print the 12-routine table and stop.
2. A rhythm without a number: run the routines of that rhythm in order, one at a time, asking for any missing input once.
3. A number: run that routine with the prompt from `docs/batch-99-prompts.md` section B.
4. Check which connector is needed; if it is not connected, say which and continue with pasted input.
5. Never send, post or schedule anything. Output drafts and tables only.
