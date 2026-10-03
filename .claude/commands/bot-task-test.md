---
description: Decide whether a recurring task suits an autonomous agent, a fixed workflow (Zapier or n8n) or a person, and draft a 5-run pilot
argument-hint: <the recurring task, in a sentence>
---

Use the skill `grok-bot-guide` on the task: "$ARGUMENTS". If it is empty, ask for the task and stop.

1. Apply the junior-employee test: could this be handed to a junior with a checklist? Answer YES, PARTLY or NO and say why in two lines.
2. Classify: RULE-BASED (fixed triggers, high volume, predictable: Zapier or n8n), JUDGMENT-HEAVY (needs decisions mid-workflow: an agent), or KEEP HUMAN (money movement, legal, regulated claims, anything irreversible).
3. List what the agent would need access to, and the minimum credential scope for each. Flag anything that needs a login handed over.
4. Draft a pilot: goal, one clean example to record, trigger or schedule, 3 to 5 test runs with a pass condition for each, the approval points, and how you will measure hours saved.
5. State the biggest risk and what would make you stop the pilot. Do not run the pilot; draft only.
