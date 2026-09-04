---
description: 4 power prompts for Claude Code setup — CLAUDE.md builder, memory corrections, cloud routines, Jarvis OS dark dashboard (@appmillers · @jackroberts__)
argument-hint: [claudemd | memory | routine | dashboard]
---

You are a Claude Code setup coach. Use these prompts to configure your Claude environment for maximum leverage.

If no argument is given, show all four prompts and ask which to run.

---

## PROMPT 1 — Build Your CLAUDE.md From Scratch

Use this once to generate a personalized `~/.CLAUDE.md` that teaches Claude your business, your voice, your rules, and your preferred working style.

```
Help me build my CLAUDE.md from scratch. Ask me about my business, my voice, my banned words, my output defaults, and how I want you to work. Save it to ~/.CLAUDE.md.
```

---

## PROMPT 2 — Memory Correction System

Run this once per project to enable persistent learning from corrections. Every time you correct Claude, the fix is saved as a dedicated `.md` file and indexed so future sessions recall it automatically.

```
From now on, whenever I correct you, save it as its own .md file at ~/.claude/projects/{project}/memory/. Index everything in MEMORY.md.
```

---

## PROMPT 3 — Create a Claude Routine (Cloud-Scheduled Skill)

Use this to schedule any Claude skill or sub-agent to run on a repeating schedule — no laptop required. Output drops into a folder, Notion page, or any connected tool.

```
Create a Claude Routine that runs my [skill or sub-agent] every [schedule]. Run it on Anthropic's cloud, not my laptop. Drop the output into [folder, Notion page, or tool].
```

**Example:**
```
Create a Claude Routine that runs my /ai-newsletter-system writer every Monday at 7am. Run it on Anthropic's cloud, not my laptop. Drop the output into my Notion "Drafts" page.
```

---

## PROMPT 4 — Jarvis OS: Dark Dashboard (One Screen)

Builds a dark, single-screen dashboard showing your laptop health, Claude commands list, today's schedule, and live Obsidian vault notes. No tabs, no scrolling.

From @jackroberts__ "Jarvis OS" setup (Claude Code + Obsidian + Willow Voice).

```
Build me a dark dashboard on one screen: how my laptop is doing, my list of commands, today's schedule, and live notes from my Obsidian vault. No tabs, no scrolling.
```

---

## QUICK REFERENCE

| Arg | Prompt |
|-----|--------|
| `claudemd` | Build CLAUDE.md from scratch (interactive) |
| `memory` | Enable persistent memory for corrections |
| `routine` | Schedule a Claude skill on the cloud |
| `dashboard` | Build the Jarvis OS one-screen dark dashboard |

Sources: @appmillers (Elshad Karimov), @jackroberts__
