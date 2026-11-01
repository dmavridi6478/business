---
description: Run the 8-step "workflow, not one prompt" method on a real input and stop for approval between steps
argument-hint: [paste or describe the raw material and what you want to achieve]
---

Use the skill `claude-workflow-8-steps`. Input: "$ARGUMENTS".

1. Read `.claude/skills/claude-workflow-8-steps/SKILL.md`.
2. Step 01 to 02: say what the input contains, then list what matters most, what is missing, and what needs the user's attention. Do not create the final output yet.
3. Step 03: turn the analysis into a prioritised plan with owners and deadlines where known; flag decisions. Stop and ask the user to approve the plan.
4. After approval, step 04 and 05: create the deliverable, critique it (unclear, missing, repetitive, misleading), then improve it.
5. Step 07 to 08: final version in the requested format plus next steps. Say which facts were checked against the input and which were not.
