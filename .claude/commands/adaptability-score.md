---
description: Score marketing adaptability across Signal, Decision, Experiment, Adoption and Learning, find the bottleneck stage, and propose one mechanism to fix it
argument-hint: [period, e.g. "Q3 2026"] [optional: team or market]
---

Use the `marketing-adaptability-score` skill. Period: "$ARGUMENTS"

1. Ask me for the 3–5 market signals of the last two quarters (competitor moves, price changes, regulation, demand shifts). For each, ask for the dates: event, first logged internally, decision made, first test live, change adopted as standard. Accept "never" as an answer. Ask in one table.
2. Ask for last quarter's decision log (or list of decisions) to compute the Learning %.
3. Compute median days per stage and score 1–5 with the skill's thresholds. State the thresholds are a starting calibration.
4. Name the bottleneck (lowest stage) and propose one mechanism for it, with owner and start date.
5. Output in the skill's format, then add one line: which performance metric this bottleneck is most likely to hurt next quarter, marked [Guessing] or [Likely].
