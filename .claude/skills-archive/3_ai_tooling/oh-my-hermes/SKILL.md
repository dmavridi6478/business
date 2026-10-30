---
name: oh-my-hermes
description: oh-my-hermes (OMH) — a governance, memory, and skill-routing layer on top of NousResearch Hermes Agent. Adds OMH Specialists (sub-agents with defined roles), Evidence Gates (quality checks before output), and Skill Routing (matching tasks to the right skill automatically). Companion to the hermes-nousresearch skill. Repo rlaope/oh-my-hermes.
---

## What oh-my-hermes adds

Hermes Agent gives you a local AI runtime. oh-my-hermes (OMH) wraps it with:

1. **OMH Specialists** — purpose-built sub-agents, each with a defined role, toolset, and authority scope
2. **Evidence Gates** — checkpoints that audit a Specialist's output before it reaches you
3. **Skill Routing** — automatic matching of incoming tasks to the right Specialist or Hermes skill

Think of it as the governance and memory layer that turns a general-purpose agent into a structured, auditable system.

---

## Installation

```bash
# Install Hermes first (if not already done)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Clone oh-my-hermes
git clone https://github.com/rlaope/oh-my-hermes
cd oh-my-hermes

# Follow repo setup
cat README.md
```

Repo: `https://github.com/rlaope/oh-my-hermes`

---

## Core concepts

### OMH Specialists

Specialists are sub-agents defined in the OMH config. Each has:

| Field | Purpose |
|-------|---------|
| `name` | Human-readable identifier |
| `role` | Single-sentence scope definition |
| `tools` | Which Hermes tools it can invoke |
| `authority` | What it can do without asking you |
| `gate` | Which Evidence Gate applies to its output |

Example Specialist definition (YAML):
```yaml
specialists:
  - name: researcher
    role: "Gather and summarise information from web and local files"
    tools: [web_search, file_read, summarise]
    authority: read-only
    gate: evidence-basic

  - name: coder
    role: "Write, review, and test code in the current repo"
    tools: [code_write, code_run, git_commit]
    authority: write-local
    gate: evidence-code

  - name: planner
    role: "Break tasks into steps and route sub-tasks to other Specialists"
    tools: [task_create, specialist_invoke]
    authority: orchestrate
    gate: evidence-plan
```

---

### Evidence Gates

Gates run before a Specialist's output is returned to you. They enforce quality.

| Gate | Checks |
|------|--------|
| `evidence-basic` | Is the answer grounded? Any hallucinated facts? |
| `evidence-code` | Does the code run? Are there obvious bugs or security issues? |
| `evidence-plan` | Is the plan actionable? Are dependencies identified? |
| `evidence-strict` | Full audit: sources, reasoning chain, alternative paths considered |

Configure gate thresholds in `omh.config.yaml`:
```yaml
gates:
  evidence-basic:
    require_sources: false
    hallucination_check: true
  evidence-code:
    require_tests: true
    run_linter: true
```

---

### Skill Routing

OMH intercepts incoming tasks and routes them to the best Specialist automatically.

Routing is based on:
1. **Keyword matching** — task text matched against Specialist role descriptions
2. **Tool availability** — does the Specialist have the tools the task needs?
3. **Authority scope** — is the required action within the Specialist's authority?

Override routing manually:
```bash
hermes task "write a report on X" --specialist researcher
```

---

## OMH Commands

```bash
# List configured Specialists
hermes omh specialists list

# Run a task through OMH routing
hermes omh run "your task here"

# Run with a specific Specialist
hermes omh run "your task" --specialist coder

# View Evidence Gate results for the last task
hermes omh gates last

# Add a new Specialist interactively
hermes omh specialists add

# View OMH memory (what the system has retained)
hermes omh memory show

# Clear stale memory entries
hermes omh memory clean
```

---

## Memory layer

OMH maintains a persistent memory store separate from Hermes's session context:

- **Short-term:** current session, cleared on exit
- **Long-term:** written to `~/.omh/memory/`, survives restarts
- **Skill memory:** task→Specialist mappings learned over time (improves routing accuracy)

```bash
# Export memory to review
hermes omh memory export > omh-memory.json

# Inject a memory entry manually
hermes omh memory add "When user asks about pricing, always use the finance Specialist"
```

---

## munder-difflin integration

oh-my-hermes is conceptually compatible with `chaitanyagiri/munder-difflin` (see `munder-difflin` skill). Where munder-difflin wraps multiple CLI agents (Claude Code, Codex, Grok, Kimi, Gemini) into a 2D office floor with roles, oh-my-hermes adds the governance layer to a single Hermes instance. The two can be combined:

- munder-difflin handles **multi-agent orchestration across CLI tools**
- oh-my-hermes handles **intra-Hermes Specialist routing and quality gates**

---

## Related skills

- `hermes-nousresearch` — base Hermes Agent install and CLI commands
- `build-claude-agent-7-steps` — architectural patterns for designing Specialists
- `ceo-daily-brief` — practical use case: route brief steps to different OMH Specialists
