---
description: Plan a game project with a studio chain of command (directors, leads, specialists), starting on the lightest process - writes a plan file, installs nothing
argument-hint: [engine: godot | unity | unreal] [game idea]
---

Input: "$ARGUMENTS". If the engine or the idea is missing, ask for it in one question.

Run the `game-studio-planner` agent with this input. It reads `.claude/skills/game-studio-chain-of-command/SKILL.md` and writes `docs/game-plan-YYYY-MM-DD.md`.

Report the plan's file name, the engine and process level chosen, the roles needed, and the first five stories. Do not clone the Game Studios template, install an engine or run a build. If the user wants the full template, point to the clone steps in the skill.
