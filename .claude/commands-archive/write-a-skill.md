---
description: Turn a workflow you just ran into a reusable skill file (SKILL.md) with trigger description, steps and checks
argument-hint: <the workflow or conversation to bottle>
---

Use the skills `skill-creator` and `prompt-writing-9-skills` (step 08). Input: "$ARGUMENTS".

1. Read `skill-creator`. From the workflow described (or the recent conversation), extract: when the skill should trigger, inputs, the steps that worked, the mistakes to avoid, and the output format.
2. Draft `.claude/skills/<kebab-name>/SKILL.md` with frontmatter (`name`, a `description` that says what it does and when to use it) and a body under 120 lines. Show it and ask before writing the file.
3. Do not include secrets, personal data or one-off specifics.
