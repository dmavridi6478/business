# Agent Memory Repos

7 open-source repos for giving AI agents persistent memory — so you never re-explain your project again. Curated by @joshualevi.ai.

## Repos

| # | Repo | Stars | What It Does |
|---|------|-------|--------------|
| 1 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | 30k | Graph-based AI memory — builds knowledge graphs from your docs and chat history |
| 2 | *(see notes below)* | — | — |
| 3 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 11k | Self-evolving memory OS — memory that learns and updates itself over time |
| 4 | [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | 6k | MCP + SQLite persistent memory — plug-and-play memory server for Claude Code |
| 5 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | 4k | Obsidian markdown memory for Claude Code — vault-based persistent context |
| 6 | *(see notes below)* | — | — |
| 7 | *(see notes below)* | — | — |

## Quick Install

### cognee (graph memory)
```bash
pip install cognee
```

### MemOS (memory OS)
```bash
git clone --depth 1 https://github.com/MemTensor/MemOS ~/repos/MemOS
cd ~/repos/MemOS && pip install -e .
```

### engram (MCP + SQLite)
```bash
git clone --depth 1 https://github.com/Gentleman-Programming/engram ~/repos/engram
cd ~/repos/engram && npm install
# Add to Claude Code MCP config:
# { "engram": { "command": "node", "args": ["~/repos/engram/server.js"] } }
```

### obsidian-second-brain (vault memory)
```bash
git clone --depth 1 https://github.com/eugeniughelbur/obsidian-second-brain ~/repos/obsidian-second-brain
```

## Claude Code Memory Prompt

```
Before starting any task, check your memory context:
1. Read CLAUDE.md for project-specific instructions
2. Check the memory store for relevant prior decisions
3. Summarize what you know about the current project before proceeding

After completing a task, save:
- What was built or changed
- Key decisions made and why
- What to remember for next time
```

## Choosing the Right Repo

| Use case | Best repo |
|----------|-----------|
| Complex knowledge graphs from docs | cognee |
| Self-improving agent memory | MemOS |
| Simple MCP memory for Claude Code | engram |
| Obsidian-based personal knowledge | obsidian-second-brain |
