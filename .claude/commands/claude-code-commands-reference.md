---
description: Claude Code Slash Commands Reference — 12 core commands (/init /compact /clear /rewind /plan /model /context /mcp /agents /doctor /review /batch) plus bonus (/btw /usage /loop) with explanations
argument-hint: [command name] — or run with no args for the full reference card
---

You are a Claude Code expert. Display the slash command reference below. If a specific command name is given as an argument, explain it in detail with usage examples.

---

## CORE COMMANDS (12)

| Command | What it does |
|---------|-------------|
| `/init` | Initialise the project — creates CLAUDE.md with project context, tech stack, and conventions |
| `/compact` | Compress the conversation context to free up token space while keeping key decisions |
| `/clear` | Clear the conversation history and start a fresh context window |
| `/rewind` | Roll back to an earlier point in the conversation and branch from there |
| `/plan` | Enter plan mode — Claude proposes a plan and waits for your approval before acting |
| `/model` | Switch the active model (e.g. Opus, Sonnet, Haiku) mid-session |
| `/context` | Show what's currently in context — files, memory, and conversation state |
| `/mcp` | Manage MCP (Model Context Protocol) servers — list, connect, and configure tools |
| `/agents` | View and manage active sub-agents spawned in the current session |
| `/doctor` | Run a health check — diagnoses config issues, missing env vars, and permission problems |
| `/review` | Trigger a code review of staged changes or a specified file/diff |
| `/batch` | Run a command across multiple files or inputs in one shot |

---

## BONUS COMMANDS

| Command | What it does |
|---------|-------------|
| `/btw` | Add a side note or background context without triggering a full response |
| `/usage` | Show token usage for the current session |
| `/loop` | Enter autonomous loop mode — Claude iterates on a task without waiting for prompts |

---

## QUICK PICKS

**Starting a project:** `/init` → sets up CLAUDE.md with project context

**Running long tasks:** `/plan` → approve → `/loop` for autonomous execution

**Context getting full:** `/compact` to compress, `/clear` if starting fresh

**Something went wrong:** `/rewind` to branch from a safe point

**Debug Claude itself:** `/doctor` for config issues, `/context` to inspect state

**Using external tools:** `/mcp` to connect APIs, databases, and services

---

## USAGE TIPS

- Commands work in any Claude Code interface: CLI, desktop app, VS Code / JetBrains extension
- `/plan` is safest for destructive operations — Claude waits for your go-ahead
- `/loop` is most effective after a clear CLAUDE.md is in place (`/init` first)
- `/compact` preserves key decisions; `/clear` wipes everything — use `/compact` first
- Stack `/review` with `/batch` to review multiple files in one pass

Source: @korolev.timm — "5 Must Have Plugins / Commands for Claude Code"
