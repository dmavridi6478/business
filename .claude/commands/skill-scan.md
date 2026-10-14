---
description: Scan a skill, plugin, MCP server or repo with NVIDIA SkillSpector before installing it, then explain the findings
argument-hint: [path, repo URL or zip of the thing you want to install]
---

Use the skill `skillspector-preinstall-scan`. Target: "$ARGUMENTS".

1. Read `.claude/skills/skillspector-preinstall-scan/SKILL.md`.
2. If the target is not already downloaded, fetch it into a new empty folder outside this repo. Do not install it, run its scripts, or open it from a folder that holds your own scripts.
3. If `skillspector` is not installed, show the install command from the skill and ask before running it. Never run a piped installer.
4. Run the static scan (`--no-llm`) first. Only run the LLM pass if the user agrees, and say which provider receives the skill's text.
5. Report: score, each finding with file and line, what each means in plain words, and a decision: install, install after fixes, or do not install. Never say "safe"; say "no findings at this version" when that is true.
6. Offer to record the decision (date, commit, score) in the install log.
