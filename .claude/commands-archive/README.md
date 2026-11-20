# Archived commands

Slash commands moved out of `.claude/commands/` because the skills they depend on
were archived to `.claude/skills-archive/` (developer, cloud, agent-tooling groups).
Restore one: `git mv .claude/commands-archive/<name>.md .claude/commands/<name>.md`
(and restore the skill it names if needed).
