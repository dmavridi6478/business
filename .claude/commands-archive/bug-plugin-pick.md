---
description: Choose which bug-catching Claude Code plugins to install for a project, with the licence and data caveats
argument-hint: [describe the project and whether it handles customer data]
---

Use the skill `claude-bug-plugins-5`. Input: "$ARGUMENTS".

1. Read `.claude/skills/claude-bug-plugins-5/SKILL.md`.
2. Recommend at most three of the five plugins and say why; mark any that overlap with `.mcp.json` (context7, sentry).
3. For each, state licence, what it sends where, and what account it needs. Flag Sentry as FSL source-available.
4. Give the exact `/plugin install` lines for the user to run themselves. Do not install anything.
