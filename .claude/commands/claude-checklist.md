---
description: Audit your Claude workflow against the 9-section checklist (setup, skills, prompting, connectors, Cowork, projects, design and code, writing, token economy)
argument-hint: '[section name or "all"] [describe your current habits, or paste your instructions]'
---

Use the skill `claude-checklist`. Input: "$ARGUMENTS".

1. Read `.claude/skills/claude-checklist/SKILL.md`. If no section is named, audit all nine.
2. Ask at most 4 yes/no questions about the user's current habits for the section(s), or read pasted instructions/settings if given. Never read credentials or private files.
3. For each item give: already doing / not yet / not applicable. Keep the skill's [Certain]/[Likely]/[Guessing] tags on claims and do not present a [Guessing] item as fact.
4. Output the three highest-value changes, each with the exact setting or habit to change, and a reminder that product behaviour (models, prices, peak hours) changes and should be checked against current documentation.
