---
description: Recommend at most one addition per category (MCP, skill, hook, subagent, command) for a repo, checking what already exists
argument-hint: <repo path or goal>
---

Use the `claude-code-setup-recommender` skill on: "$ARGUMENTS"

1. Inventory existing skills, commands, agents, hooks and MCP servers for this repo (counts only, plus the closest existing match per category).
2. Recommend at most one addition per category, and say "nothing needed" where the existing set already covers it.
3. Read-only; install nothing.
