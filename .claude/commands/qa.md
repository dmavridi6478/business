---
description: Test a result against every requirement — show failures first
argument-hint: [result and requirements to test against]
---

Run a QA pass on the result in "$ARGUMENTS". Show failures first, then passes.

For each requirement or expectation (stated or implied):
1. **PASS** or **FAIL** — verdict first, then reasoning
2. **Severity** (for failures only) — Blocking / Serious / Minor
3. **Specific evidence** — quote or point to what passes or fails, not a general impression

After the itemized review, give:
- A top-line pass/fail verdict for the result overall
- The single highest-priority fix (if any)
- Any requirement that is genuinely unclear and needs to be defined before QA is meaningful

Do not soften a FAIL into a "could be improved." If it fails, say it fails and say why. Do not pad the PASS column — a result that meets the bar is not an achievement worth dwelling on.

If "$ARGUMENTS" is empty, ask what result and requirements to test before proceeding.

Source: @theusefulshift "20 Claude Commands That Feel Illegal" — Command 09 (qa).
