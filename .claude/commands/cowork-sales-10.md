---
description: Print one of the 10 Claude Cowork sales prompts (SalesDaily.co) in plain text with the inputs and connector it needs, or list all ten
argument-hint: [1-10, or empty to list]
---

Use the skill `cowork-sales-prompts-10`. Input: "$ARGUMENTS".

1. Read `.claude/skills/cowork-sales-prompts-10/SKILL.md`.
2. If the input is empty, list the ten titles with one line each.
3. If it is a number, print that prompt exactly as written in a code block, then list the brackets to fill, the connector or Cowork feature required, and its caution.
4. For prompts 4 and 7 (scheduling), state that they create recurring work and ask for confirmation before running anything.
