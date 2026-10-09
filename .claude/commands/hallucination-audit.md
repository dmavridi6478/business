---
description: Audit an AI workflow against the six groups and eighteen actions for reducing hallucination, marking each in place, partial or absent
argument-hint: [describe the AI workflow, its sources and who relies on its answers]
---

Use the skill `hallucination-guardrails-6`. Input: "$ARGUMENTS".

1. Read `.claude/skills/hallucination-guardrails-6/SKILL.md`. Ask at most 3 questions if the workflow description is thin. Never ask for credentials or personal data.
2. Score all eighteen actions: in place / partial / absent, quoting the evidence asked for. Do not mark an action as in place on assurance alone.
3. List the absent items in groups 1 to 4 first and name the three to fix this week, each with a concrete change.
4. State plainly that none of the actions removes hallucination, that self-review is weak and that confidence is not correctness.
