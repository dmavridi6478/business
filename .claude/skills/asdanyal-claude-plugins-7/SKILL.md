---
name: asdanyal-claude-plugins-7
description: The @asdanyal "Claude plugins" 7-slide series - 01 cover "Top 5 plugins", 02 summary list, 03 OmniRoute (model router), 04 Superpowers (plan, build, review pipeline), 05 Caveman (terse output), 06 Claude Code Setup (official project scanner), 07 Claude Security (scan codebase, scan changes, suggest patches) - with what each does, which are installed here and the risk of OmniRoute-style routers. Use when choosing Claude Code plugins for workflow, security scanning or limit management.
---

# @asdanyal "Claude plugins" (7 slides)

| # | Plugin | Slide claim | Status here |
|---|---|---|---|
| 01 | cover: "Top 5 plugins to install in Claude" | | |
| 02 | summary | OmniRoute "never hit a usage limit again"; Superpowers "plans, builds and reviews before you see it"; Caveman "same code, 65% fewer tokens"; Claude Code Setup "Anthropic's official project scanner"; Claude Security "Anthropic's official vulnerability hunter" | |
| 03 | **OmniRoute** | routes each request to the best model across 357+ providers through one endpoint; switches automatically when Claude hits its limit; "~1.62 billion free tokens a month"; "no API key required"; dashboard with providers, API key manager, endpoints, webhooks, proxy, cloud agents | **not installed; caution below** |
| 04 | **Superpowers** | brainstorm until the spec is clear, write a plan, subagents execute and cross-review, code review before you see output | installed (user scope) |
| 05 | **Caveman** | terse answers, ~65% fewer output tokens | skill `caveman` exists |
| 06 | **Claude Code Setup** | official project scanner recommending hooks, skills, MCP servers | skill `claude-code-setup-plugin` exists |
| 07 | **Claude Security** | three modes: scan codebase (full or scoped), scan changes (branch, PR, commit), suggest patches (patch files verified before you see them); shown as `plugins/claude-security` in anthropics/claude-plugins-official, front-desk menu 1/2/3 | see `defending-code-reference-harness`; install via `/plugin` (marketplace here: `anthropic-plugin-directory`) |

## Caution on OmniRoute
A router sits between you and every model: it sees all prompts, code and keys. "Free" tiers from many providers may log or train on your data, and "no API key required" combined with "free billions of tokens" is a red flag, not a feature. Do not route private code or client data through it. If you want fallback when you hit limits, use your own provider keys behind a gateway you host and audit.

## Use
Install order that costs least risk: Superpowers (workflow), Claude Security (read-only scans first), then measure token use before adding compressors (`token-saver-repos-top5`). Related: `claude-code-tooling`, `claude-official-plugins-3`, `claude-plugins-top5-installs`.
