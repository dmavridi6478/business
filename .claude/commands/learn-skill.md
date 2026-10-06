---
description: 'Build a learning plan and tutor session for any skill from 22 Claude prompts - diagnose level, roadmap, teach-back, flashcards, projects, weekly review, coach mode.'
argument-hint: '<skill> [level] [hours per week] [deadline]'
---

Use the `claude-skill-tutor-25` skill for "$ARGUMENTS". Ask once for skill, current level, hours per week and deadline if missing. Run: skill-level analysis (one question at a time), then the roadmap and 30-minute daily plan, then start tutor mode (explain, ask one question, wait). Save the plan to `data/agent-drafts/YYYY-MM-DD-learn-<skill>.md`. Do not invent book titles or sources; mark any as `[verify]`. Strict coach mode only if the user asks and chooses its consequences.
