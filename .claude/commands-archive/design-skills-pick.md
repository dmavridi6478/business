---
description: Pick which of the verified Claude Code design skills to use for a project, with the correct install steps and licence, without installing anything
argument-hint: [project type, e.g. "marketing site" or "admin dashboard"] [what looks wrong today]
---

Use the skill `claude-design-skills-top5`. Input: "$ARGUMENTS".

1. Read `.claude/skills/claude-design-skills-top5/SKILL.md`.
2. Recommend one primary skill and at most one backup for the project, from the five plus the four Anthropic skills. Say which are already installed in this repo and so need no install.
3. Give the install route from the README column (including the marketplace step the slides skip), the licence, and the risk of running a third-party skill.
4. Do not run `npx skills add`, `npx impeccable install` or `/plugin install`. Give the commands for the user to run.
5. Keep the [Certain]/[Likely] tags and say star counts are unverified.
