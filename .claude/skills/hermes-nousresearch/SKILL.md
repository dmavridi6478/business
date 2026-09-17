---
name: hermes-nousresearch
description: Hermes Agent by NousResearch — open-source, local-first AI agent with 300+ model support and self-improving skill system. Covers one-line install, core CLI commands, 5 pro tips, and integration with the Hermes Content Factory. Use when the task is to install or operate the Hermes agent, or when the user asks about a local, model-agnostic AI agent runtime.
---

# Hermes Agent (NousResearch)

Source: @aigenesis.official
License: MIT · Local-first · 300+ models supported

---

## What Is Hermes

Hermes is an open-source AI agent runtime that runs locally on your machine.

- Connects to 300+ models (Claude, GPT-4, Llama, Mistral, Gemini, etc.)
- Self-improving skill system — the agent learns from every session
- MIT licensed — free to use, modify, and deploy
- No cloud dependency — all data stays on-device
- Agent-to-agent communication (multi-agent workflows)

---

## Install in One Line

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Requirements:** macOS or Linux. Node.js 18+ recommended.

After install, verify with:
```bash
hermes doctor
```

---

## Core CLI Commands

| Command | What it does |
|---|---|
| `hermes model` | Switch the active model |
| `hermes start` | Start the agent runtime |
| `hermes doctor` | Diagnose installation issues |
| `hermes --continue` | Resume a previous session |
| `hermes skills browse` | Browse and install community skills |

---

## In-Session Slash Commands

| Command | What it does |
|---|---|
| `/voice on` | Enable voice input/output |
| `/k8s` | Activate Kubernetes skill |
| `/github-pr` | Activate GitHub PR skill |
| `/debug` | Enable verbose debug mode |

---

## 5 Pro Tips

### Tip 1 — Mix Models, Not Just Prompts
Use a fast model (e.g. Haiku, Mistral-7B) for initial research and a powerful model (e.g. Claude Opus, GPT-4o) for synthesis. Switch mid-session with `hermes model`.

### Tip 2 — Build Reusable Skills
Every repeatable workflow is a skill candidate. Skills persist across sessions and get better over time.
```
Turn this workflow into a reusable Hermes skill:
[DESCRIBE YOUR WORKFLOW]
```

### Tip 3 — Use Agent-to-Agent Communication
Run parallel sub-agents for independent tasks, then synthesise their outputs:
```
Spawn three agents:
- Agent A: Research [TOPIC A]
- Agent B: Research [TOPIC B]
- Agent C: Research [TOPIC C]
Synthesise their outputs into one report.
```

### Tip 4 — Set Session Context Once
Give Hermes your business context at the start of every session so you don't repeat yourself:
```
Context for this session:
Business: [DESCRIPTION]
Audience: [WHO]
Constraints: [RULES]
Today's goal: [TASK]
```

### Tip 5 — Use `--continue` for Long Projects
`hermes --continue` resumes the previous session with full memory. Useful for multi-day projects where context matters.

---

## Hermes + Claude Code (Combined Setup)

```bash
# Install Hermes
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Install Claude Code
npm install -g @anthropic/claude-code

# Run Hermes with Claude as the backend model
hermes model --set claude-opus-4-5
hermes start
```

---

## Repos to Watch

| Repo | Purpose |
|---|---|
| `NousResearch/hermes-agent` | Core Hermes agent runtime |
| `cline/cline` | Autonomous coding agent (VS Code / CLI) |
| `tashfeenahmed/freellmapi` | 34 free LLM providers via one OpenAI-compatible endpoint |
| `home-assistant/core` | Local-first home automation platform |

Clone command:
```bash
gh repo clone NousResearch/hermes-agent
gh repo clone cline/cline
gh repo clone tashfeenahmed/freellmapi
```
