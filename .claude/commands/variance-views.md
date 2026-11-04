---
description: Choose and specify the right variance views (donut, waterfall, column, cutoff, bar, line, table, KPI) for a budget-versus-actual-versus-forecast report
argument-hint: [categories or departments, audience, period, and the figures if you have them]
---

Use the `fpna-budget-actual-forecast` skill.

Input: $ARGUMENTS

1. Confirm the setup: a locked budget, a rolling forecast and actuals. If the budget is editable or the forecast overwrites it, say so first.
2. State the sign convention you will use for revenue and cost lines, and apply it to every figure.
3. If I gave figures, compute budget versus actual and rolling forecast versus actual per line, and flag lines above the materiality threshold (both a percentage and an amount).
4. Pick one primary view and at most two supporting views for my audience from the eight, with a reason and the view you rejected and why.
5. Specify each chart: axes, order, labels, the forecast months marked as forecast.
6. Write the variance commentary for each flagged line: what happened, why, does it repeat, action, owner, date. Mark any cause you cannot support as "to confirm".
7. End with the pre-send checks: ledger tie-out, locked budget unchanged, currency and period on the page.
