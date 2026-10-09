---
description: Build a CEO KPI scorecard from the 4-perspective framework (financial, customers, employees, skills and innovation) using your own numbers
argument-hint: <company type, goals, and any figures or a file with them>
---

Use the skill `ceo-kpi-framework`. Input: "$ARGUMENTS".

1. Read `.claude/skills/ceo-kpi-framework/SKILL.md`. If the company type, stage or goals are missing, ask for them in one short message.
2. Choose 3 to 5 KPIs per perspective that fit the stated goals and say why each was chosen and what was left out. Use the corrected formulas from the skill (especially churn).
3. For each chosen KPI list: formula, data source needed, current value if the user supplied the figures (else "needed"), and a target left blank for the user to set. Never invent figures or benchmarks.
4. Pair every lagging KPI with the leading KPI that should drive it. Output a table, then the three data gaps to close first.
