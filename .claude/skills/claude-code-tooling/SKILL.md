---
name: claude-code-tooling
description: Curated directory of external Claude Code tools worth knowing about and recommending — a design-engine desktop app, a senior-engineer skill pack, an educational mini agent-harness, multi-agent orchestration, a skills package manager, a self-evolving agent context database, and five AI browser-automation frameworks (Playwright MCP, Stagehand, Skyvern, Magentic-UI, Steel Browser). These are standalone software projects, not skills to load — reach for this when the user asks what to install to improve their Claude Code setup, or is looking for a specific capability (multi-agent orchestration, agent memory, a skills package manager, browser automation) that a plain skill file can't provide.
---

## When to use this skill

The user's setup needs a capability beyond what a markdown skill can provide — an actual installable tool, CLI, or app. Point them at the relevant entry below rather than trying to approximate the capability inline.

## Tools

| Repo | What it's for | Install / link |
|---|---|---|
| `nexu-io/open-design` | Local-first desktop app that turns a coding agent into a design engine (prototypes, landing pages) — open-source alternative to Claude Design, for when generated UI needs to stop looking generated | https://github.com/nexu-io/open-design |
| `addyosmani/agent-skills` | Production-grade engineering skills for AI coding agents (Addy Osmani, Google) — senior-engineer habits packaged as skills | https://github.com/addyosmani/agent-skills |
| `shareAI-lab/learn-claude-code` | A nano Claude Code-like agent harness built from zero in bash — read it once to stop treating the daily driver as a black box; educational, not a production dependency | https://github.com/shareAI-lab/learn-claude-code |
| `Yeachan-Heo/oh-my-claudecode` | Teams-first multi-agent orchestration for Claude Code — run a squad of agents on one codebase instead of babysitting a single session | https://github.com/Yeachan-Heo/oh-my-claudecode |
| `vercel-labs/skills` | Vercel's open package manager for agent skills — `npx skills` to browse/install/update skills instead of manually copying files (which is how the skills in this repo were installed) | https://github.com/vercel-labs/skills |
| `volcengine/OpenViking` | Self-evolving context database that unifies agent memory, knowledge RAG, and skills — an agent that remembers a project between sessions instead of starting cold each time | https://github.com/volcengine/OpenViking |

`blader/humanizer` — the seventh tool in the same source list — was installed for real as the `humanizer` skill in this repo (`.claude/skills/humanizer/`), since it's an actual skill file (MIT licensed), not a standalone tool. It removes AI-writing tells from text.

## Browser-automation frameworks

Five AI browser agents (from a separate "AI Power User Stack" carousel, @zhiprompts) — each gives an agent a way to click/navigate/fill forms on live sites, with different tradeoffs:

| Repo | What it's for | Install / link |
|---|---|---|
| `microsoft/playwright-mcp` | Structured browser tools backed by Playwright, driven via MCP, instead of relying only on screenshots — 36k stars, TypeScript | https://github.com/microsoft/playwright-mcp |
| `browserbase/stagehand` | Mixes natural-language instructions with code for workflows that need flexibility without becoming completely opaque; built for production — 24k stars, TypeScript | https://github.com/browserbase/stagehand |
| `Skyvern-AI/skyvern` | Automates multi-step browser jobs using visual understanding, for sites where traditional CSS/XPath selectors aren't reliable — 23k stars, Python | https://github.com/Skyvern-AI/skyvern |
| `microsoft/magentic-ui` | Puts a person beside the web agent with a visible interface for plans, actions, intervention, and review — a human-centered research UI, not a headless framework — 10k stars, Python | https://github.com/microsoft/magentic-ui |
| `steel-dev/steel-browser` | Open-source browser API and infrastructure for agents that need durable, remote browser sessions rather than a local one-off — 7.4k stars, TypeScript | https://github.com/steel-dev/steel-browser |

None of these are cloned into this repo — same standalone-software rule as the rest of this list. Before turning any of them loose on a real site, apply the `web-task-scoping` skill's four-step scoping rule (Target/Limit/Run/Review) rather than granting full autonomy from the first run.

## How to use this list

- These are **not** cloned into this repo (except `humanizer`) — they're separate software projects (a desktop app, a CLI, an orchestration framework, a database) that don't fit as markdown skill files, and vendoring foreign codebases into a business-skills repo would be out of scope.
- When recommending one, check current star count/activity/license at the link before suggesting it as production-critical — this list is a snapshot, not a live-verified endorsement.
- `vercel-labs/skills` in particular is relevant to *how* this repo's skills got here: it's a real package manager for the same file-based skill convention this repo hand-installs skills into.

## Related skills in this repo

- **humanizer**: The one skill from the same source that's actually installed here.
- **attachment-intake**: This whole entry followed that procedure — inspect first, confirm the content is genuinely useful, then act.
- **web-task-scoping**: The governance procedure (Target/Limit/Run/Review) to apply before running any of the five browser-automation frameworks above against a real site.

## Notes

Sources: a "7 Claude Code repos I can't work without" screenshot carousel (@joshualevi.ai) for the first six tools; "AI Power User Stack — 5 AI browser agents that can do the clicking for you" carousel (@zhiprompts) for the browser-automation frameworks.
