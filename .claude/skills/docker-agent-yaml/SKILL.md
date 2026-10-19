---
name: docker-agent-yaml
description: Notes and a starter YAML sketch for Docker Agent (open source) from the @tiborczekay video 'AI agents as YAML files' - docker agent new / run agent.yaml / run org/agent:tag, a lead agent delegating to specialist agents, built-in MCP and memory, Docker Desktop 4.63 or newer, plus the video's own caveats (crowded space, thin security docs, data-collection terms). Use when someone asks how to define, share or version an AI agent as a file. Run via /docker-agent. Not a replacement for reading the official docs.
---

# Docker Agent - agents as YAML files

Source: ~80-second TikTok video (@tiborczekay, "How to - 18 Oct 2026, AI voice"). The video gives the shape, not the full schema: **verify every key against the official docs before use.**

## What the video says

- Open source. An agent is a YAML file; it runs with `docker agent run`.
- Sketch shown on screen: `agents:` -> `helper:` -> `model: your-provider/model`, `instruction: what it does`, `tools: [shell, memory]`.
- A team of agents: a lead agent hands work to specialists (research, code, review).
- Setup: Homebrew or Docker Desktop (4.63 or newer) and a model API key.
- Commands shown: `docker agent new`, `docker agent run agent.yaml`, `docker agent run myorg/agent:tag` (agents packaged and shared as container images).
- Built in: any MCP server, local or remote, plus memory.
- "The honest part": the space is crowded; documentation is thin on security; read the data-collection terms.
- Take: agents as files you can version and share.

## Starter sketch (from the on-screen example; not validated against the schema)

```yaml
agents:
  root:                       # lead agent
    model: your-provider/model
    instruction: Route work to the specialists and return one answer.
    # sub-agent wiring key: check the docs (not shown in the video)
  researcher:
    model: your-provider/model
    instruction: Find sources and quote them.
    tools: [memory]
  reviewer:
    model: your-provider/model
    instruction: Check claims against the sources and list gaps.
```

## Before using it

1. Check the real schema with `docker agent new` (it scaffolds one) rather than this sketch.
2. A `shell` tool gives the agent command execution: run it only in a sandbox without secrets.
3. Read what is sent to the model provider; do not put client data in an unreviewed agent.
4. This repo's own agents (`.claude/agents/`) are drafts-only with human approval; keep that rule for any Docker agent too.

Overlap: `docker-patterns` covers general Docker; nothing here duplicates it.
