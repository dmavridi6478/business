---
description: Run one of the nine Claude Head of Sales routines (Mon pipeline review, Tue target accounts, Wed message review, Thu deal clinic, Fri week in numbers, monthly forecast, win/loss, territory, coaching) - asks for the data first, drafts only
argument-hint: [routine name or day] - no args lists the nine
---

Input: "$ARGUMENTS". If empty, list the nine routines from `.claude/skills/claude-head-of-sales-routines/SKILL.md` with the data each needs and ask which to run.

1. Ask the user for the sales context file (or the facts it holds: customer, offer, stages, targets, rules) and the data the chosen routine needs. Do not start without them; if the user cannot supply a part, say which part of the answer would be a guess.
2. Run the routine using only the pasted data. Never invent deals, amounts, buyer facts, triggers or forecast numbers. Mark judgement calls.
3. Output: at most five bullets in the routine's own job (what moved, who and why now, the tightened message, the three riskiest deals, five lines of numbers, a range, reasons, where effort goes, one coaching point per seller), then `Not checked:` and one action for today.
4. Do not send, post, update a CRM or contact anyone. Do not process personal data or call recordings the user is not entitled to share.
