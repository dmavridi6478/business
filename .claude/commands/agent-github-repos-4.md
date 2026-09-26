---
description: 4 GitHub repos for AI agents (diagram design, harness engineering patterns, cybersecurity skills, browser control) not already covered elsewhere in this repo
argument-hint: [repo name or "all" for the full list]
---

# GitHub Repos for AI Agents (4 New)

Source: @aigenesis.official, "7 GitHub repos built for AI agents." Of the 7 repos in that carousel, **3 are already covered elsewhere in this repo** and are not re-added here:
- `volcengine/OpenViking` — already row 2 of `agent-memory-repos`
- `K-Dense-AI/scientific-agent-skills` — already documented in `github-trending-agent-repos-sep2026.md` with more detail
- The carousel's Repo 2 (Agent-Memory) — added as row 7 of `agent-memory-repos` (citing the canonical `rohitg00/agentmemory` upstream instead of the stale fork shown on screen)

The remaining 4 are new to this repo:

## 1. Diagram Design

[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — a curated library of architecture diagrams built specifically for cloud-code agent workflows (Capture → Research → Decide → Act → Measure → Learn, all feeding one shared-memory node). Drop diagrams directly into a workflow instead of using generic architecture diagrams that break down past a basic setup.

```bash
git clone --depth 1 https://github.com/cathrynlavery/diagram-design ~/repos/diagram-design
```

## 2. Awesome Harness Engineering

[yenanjing/awesome-harness-engineering](https://github.com/yenanjing/awesome-harness-engineering) — a curated pattern collection covering agent memory, skills, security, evals, and orchestration: "every production agent pattern in one repo." Replaces searching across dozens of blog posts and docs to figure out how production agents are supposed to be structured.

```bash
git clone --depth 1 https://github.com/yenanjing/awesome-harness-engineering ~/repos/awesome-harness-engineering
```

This is a curated *reading list/pattern reference*, not a skill package — complementary to this repo's own `agent-harness-construction` skill (which is the actionable ECC-origin skill for designing an agent's action space/tool definitions/observation format). Read this repo for patterns, use `agent-harness-construction` to apply them.

## 3. Anthropic Cybersecurity Skills

[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) — a structured library of cybersecurity skills built for AI coding agents, covering modern threat patterns rather than textbook theory. Replaces building security logic from scratch or shipping agents with zero guardrails.

```bash
git clone --depth 1 https://github.com/mukul975/Anthropic-Cybersecurity-Skills ~/repos/anthropic-cybersecurity-skills
```

**Note:** the source carousel showed a `liptonj-eng/anthropic-cybersecurity-skills` fork (33 commits ahead of, but 223 commits behind, this upstream) — cited here by the canonical upstream instead, per this repo's standing convention of preferring the maintained original over a stale fork.

## 4. Browser Use

[browser-use/browser-use](https://github.com/browser-use/browser-use) — lets agents browse, click, type, fill forms, and complete real tasks on real websites: full browser control, not just scraping. Replaces agents stuck in a sandbox that can read the web but can't touch it.

```bash
pip install browser-use
```

**Important — read before installing:** this repo already has a skill, `browser-use-to-stagehand`, built specifically to help you **migrate away from** browser-use to Stagehand v3 on Browserbase, because browser-use's LLM-decides-every-action design is less deterministic than Stagehand's `act`/`extract`/`observe` primitives. If you're starting a *new* browser-automation agent and determinism matters, read that skill first before reaching for browser-use directly. Use browser-use itself when you want the simpler, fully-agentic default and don't need Stagehand's tighter control.

## Plain-text prompt to evaluate any of these before adopting

```
I'm considering adding [REPO NAME] to my agent stack for [TASK]. Read its
README and tell me: (1) what it actually replaces in my current setup,
(2) the real install/dependency cost, not just the one-line pitch, (3)
whether an existing skill in this repo already covers the same job — check
[NAME THE SKILL YOU SUSPECT OVERLAPS] specifically before recommending it.
```
