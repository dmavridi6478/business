---
name: claude-code-cheatsheet-2026
description: 'Twelve-panel Claude Code workflow cheatsheet (install, CLAUDE.md, memory hierarchy, best practices, file structure, skills, skill ideas, hooks, permissions, 4-layer architecture, daily workflow, quick reference) with corrections where the infographic is wrong or outdated. Use when onboarding someone to Claude Code, setting up a project, or checking hooks and permission syntax. Source: "Claude Code Workflow Cheatsheet - 2026 Edition" infographic.'
---

# Claude Code cheatsheet (corrected)

| # | Panel | Content from the infographic | My correction or note |
|---|---|---|---|
| 1 | Getting started | Needs Node.js 18+; `curl -fsSL https://claude.ai/install.sh \| bash`; `cd your-project`, `claude`, `/init` | The native installer needs no Node. Read the script before piping it to a shell, or use the documented package-manager route |
| 2 | CLAUDE.md | Persistent project memory loaded each session: tech stack, directory map, architecture, build/test/lint commands, gotchas | Correct |
| 3 | Memory hierarchy | `~/.claude/CLAUDE.md` global; parent dir (monorepo); `./CLAUDE.md` project (in git); subfolder files add scoped context. Keep each short | "Under 200 lines" is a guideline, not a limit |
| 4 | Best practices | `/init` first then refine; be specific; add gotchas Claude cannot infer; reference docs with `@filename`; keep concise; commit to git | Correct |
| 5 | File structure | `CLAUDE.md`, `.claude/settings.json`, `settings.local.json` (not committed), `skills/<name>/SKILL.md`, `commands/*.md`, `agents/*.md` | Correct. This repo follows it |
| 6 | Skills | Markdown guides Claude auto-invokes by description; project `.claude/skills/<name>/SKILL.md`, personal `~/.claude/skills/<name>/SKILL.md`; the description field drives activation | Correct. Quote descriptions that contain `: ` |
| 7 | Skill ideas | code-review, testing patterns, commit messages, docker-deploy, database-visualizer, api-design | Ideas only |
| 8 | Hooks | PreToolUse, PostToolUse, Notification; exit 0 allow, exit 2 block | Correct in principle. The example JSON drops the `"matcher"` nesting details; use the settings documentation for the exact shape |
| 9 | Permissions | `"allow": ["Read:*","Bash:git:*"]`, `"deny": [..., "Read:env:*", "Bash:sudo:*"]` | **Wrong syntax.** Rules are written as `Tool(specifier)`, for example `Bash(git status:*)` or `Read(./.env)`. Do not copy the infographic's colon form |
| 10 | Four layers | CLAUDE.md (context) -> Skills (knowledge) -> Hooks (gates) -> Agents (subagents) | Good mental model; settings and MCP servers are the missing layer |
| 11 | Daily workflow | Plan mode (Shift+Tab) -> describe intent -> auto-accept -> `/compact` -> Esc Esc to rewind -> commit often -> new session per feature | Auto-accept removes review; use it only on a branch |
| 12 | Quick reference | `/init`, `/doctor` (printed as "/doccat"), `/compact`, Shift+Tab modes, Tab toggles extended thinking, Esc Esc rewind | Key bindings change between versions; check `/help` |

## Use
Walk a newcomer through panels 1-6 first, then hooks and permissions with the corrected syntax. For this repo's own hooks see `.claude/settings.json`.

Related: `claude-code-mod-builder`, `claude-code-tooling`, `claude-code-setup-plugin`. Template: `cheatsheet-pastel-grid` in `design-templates`.

## Keywords
Claude Code, CLAUDE.md, hooks, permissions, memory, skills, subagents, cheatsheet
