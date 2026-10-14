---
description: Run the eight-area SEO team routing for a site and return one prioritised plan
argument-hint: [site URL and goal]
---

Use the agent `seo-team-orchestrator` and the skill `claude-seo-team-8-areas`. Input: "$ARGUMENTS".

1. Read `.claude/skills/claude-seo-team-8-areas/SKILL.md`.
2. Ask for the site, goal, market and data access if missing.
3. Route to the specialists in the skill's run order. Use Ahrefs or Semrush only for numbers, and date every figure.
4. Return the plan with order, owners, evidence needed, and the first two actions this week. Separate "found" from "suggested".
