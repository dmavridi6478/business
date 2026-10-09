---
description: Build a full client event plan from one brief (timeline, budget, vendors, communications, runbook)
argument-hint: <event type, date, guest count, budget> or a path to event-brief.md
---

Use the skill `event-planner` for: "$ARGUMENTS".

1. Read `.claude/skills/event-planner/SKILL.md`. If the arguments are a file path, read it as the brief.
2. Build the brief table from the arguments. Ask for any missing field in ONE message listing only what is missing (event type, goal, audience, date, location, guest count, budget, must-haves). Do not guess budget or guest count.
3. Write `event-brief.md`, then produce, in order: timeline, budget table (estimated / actual / remaining), vendor tracker, the five communications as drafts, and the hour-by-hour runbook. Use only numbers from the brief; mark unknowns `?`.
4. Finish with the three biggest risks (for example a negative remaining budget, a vendor with no deadline, a missing owner on a runbook row) and what the user must decide.
