---
description: Find ten realistic failures outside the happy path
argument-hint: [system, process, or feature to stress-test]
---

Given the system, process, or feature in "$ARGUMENTS", identify ten realistic edge cases — situations that fall outside the happy path and could produce a failure, error, or poor experience.

For each:
1. **The scenario** — describe the specific edge case concisely
2. **What breaks or degrades** — the failure mode or unintended consequence
3. **Severity** — Critical (data loss, security, show-stopper) / Serious (broken UX, wrong output) / Minor (degraded but recoverable)
4. **Whether it is already handled** — yes / no / unclear; if unclear, say what would confirm it

Rank by severity (Critical first). Do not invent edge cases that require exotic or vanishingly rare conditions — stick to realistic user behavior, plausible inputs, and known system constraints.

After the ten, name the single edge case that seems most likely to actually occur and hasn't been addressed.

If "$ARGUMENTS" is empty, ask what system, process, or feature to stress-test before proceeding.

Source: @theusefulshift "20 Claude Commands That Feel Illegal" — Command 17.
