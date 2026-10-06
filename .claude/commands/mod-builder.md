---
description: 'Walk through the five-step Claude Code mod workflow - audit repeats, pick one, apply the five-question check, draft the build prompt - without running unverified plugin commands.'
argument-hint: '[the thing you keep asking Claude to do]'
---

Use the `claude-code-mod-builder` skill for "$ARGUMENTS". If a repeat is given, run the five-question check on it and draft the Prompt 2 build text for the user to review. If none is given, show the audit prompt and warn that session history can hold secrets. Do not run `/plugin enable ...@builtin` or any marketplace command; print them for the owner. Do not read other session histories.
