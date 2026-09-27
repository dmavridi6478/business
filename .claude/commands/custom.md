---
description: Create your own reusable slash command for a recurring task
argument-hint: [describe the recurring task this command should do]
---

Turn "$ARGUMENTS" into a new reusable Claude Code slash command:

1. Pick a short, memorable command name (kebab-case) that doesn't collide with an existing file in `.claude/commands/`.
2. Write `.claude/commands/<name>.md` with YAML frontmatter (`description`, and `argument-hint` if the command takes input) followed by the instruction body, matching the terse style of this repo's existing commands (one clear paragraph, `$ARGUMENTS` where user input is substituted, no filler).
3. Tell the user the command name and how to invoke it (`/<name> ...`).

If this repo already has a skill that does this same job (check `.claude/skills/`), point to that instead of creating a redundant command — a slash command is for a short, fixed recurring prompt, not a substitute for an existing multi-step skill.
