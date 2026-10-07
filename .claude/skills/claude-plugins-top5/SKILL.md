---
name: claude-plugins-top5
description: Five Claude Code plugins from the official marketplace highlighted by @awayfromlovable - explanatory-output-style, playground, hookify, session-report, claude-security - with the install commands shown, what each does, and which are already present in this repo. Use when choosing Claude Code plugins for token visibility, safety rules, design exploration or security scanning.
---

# Top 5 Claude Code Plugins (Anthropic's marketplace)

Source: @awayfromlovable carousel "plugins Anthropic made that almost nobody installs". Install counts are the post's (design plugin 1,134,112; #1 here 8,580) and move daily.

| Plugin | Does | Installs (post) | Install (as shown) |
|---|---|---|---|
| claude-security | `/claude-security` scans the codebase, scans changes, suggests patches. Runs on your computer with your Claude plan. In beta | 8,580 | `/plugin install claude-security@claude-plugins-official` |
| session-report | "make me a session report" writes session-report.html: tokens by project, subagents, skills, most expensive prompts. Reads logs already on your computer (last 7 days) | 11,694 | `/plugin install session-report@claude-plugins-official` |
| hookify | `/hookify Warn me when I use rm -rf commands` turns plain-English rules into hooks; no code, no restart | 60,376 | `/plugin install hookify@claude-plugins-official` |
| playground | `/playground create a playground for button design styles` builds a live HTML page with sliders, presets and a copy-prompt button | 64,198 | `/plugin install playground@claude-plugins-official` |
| explanatory-output-style | Explains your own code while it builds; turns on every new session; costs a few more tokens | 64,377 | `/plugin install explanatory-output-style@claude-plugins-official` |

## Status in this repo

- hookify: already present (`.claude/commands/hookify*.md`, `skills/hookify-rules`, agent `conversation-analyzer`).
- The other four are not vendored. `/plugin install` is interactive and needs your terminal: run the lines above yourself.
- Check source and permissions before installing any plugin; claude-security reads your code.

Command: `/plugins-top5` prints the install list.
