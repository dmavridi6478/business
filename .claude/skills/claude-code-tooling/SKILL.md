---
name: claude-code-tooling
description: Curated directory of external Claude Code tools worth knowing about and recommending — a design-engine desktop app, a senior-engineer skill pack, an educational mini agent-harness, multi-agent orchestration, a skills package manager, a self-evolving agent context database, five AI browser-automation frameworks (Playwright MCP, Stagehand, Skyvern, Magentic-UI, Steel Browser), five AI agent-building frameworks (Pydantic AI, Agno, Mastra, Strands Agents, Google ADK) plus a framework-bakeoff evaluation method, and a hive-mind team workspace (Buzz) that gives Claude Code/Codex/Goose agents a persistent presence alongside humans in shared channels. These are standalone software projects, not skills to load — reach for this when the user asks what to install to improve their Claude Code setup, is choosing an agent-building framework, or is looking for a specific capability (multi-agent orchestration, agent memory, a skills package manager, browser automation, agents-in-team-chat) that a plain skill file can't provide.
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

## AI agent-building frameworks

Five agent-builder SDKs/frameworks (from an "AI Power User Stack — 5 AI agent builders to try before LangChain" carousel, @zhiprompts) — for writing the agent's own logic (tools, memory, state, evals), a different layer than the browser-automation frameworks above:

| Repo | What it's for | Install / link |
|---|---|---|
| `pydantic/pydantic-ai` | Model-agnostic agents with typed inputs, structured outputs, tools, and dependencies as testable Python code — from the Pydantic team, so validation is first-class rather than bolted on — 19k stars, Python | https://github.com/pydantic/pydantic-ai |
| `agno-agi/agno` | Compose agents and teams of agents with tools, memory, knowledge, reasoning, and model-provider flexibility (swap providers without a rewrite) — 42k stars, Python | https://github.com/agno-agi/agno |
| `mastra-ai/mastra` | Agents, workflows, RAG, memory, and evaluations in one integrated TypeScript application framework — the JS/TS-native option when the rest of the stack is already TypeScript — 27k stars, TypeScript | https://github.com/mastra-ai/mastra |
| `strands-agents/harness-sdk` | Lightweight, model-driven agent loop with tools and provider integrations from the Strands ecosystem (Python & TypeScript, Apache-2.0) — 6.7k stars | https://github.com/strands-agents/harness-sdk |
| `google/adk-python` | Google's open-source Python toolkit for building, evaluating, and deploying agents, with Google's model ecosystem as a first-party integration — 21k stars, Python | https://github.com/google/adk-python |

Star counts are as shown in the source carousel, not independently re-verified — check current counts before treating one as a production-scale endorsement.

**Choosing between them before defaulting to LangChain**: the source carousel's framing (LangChain isn't wrong, just often the default reached for without comparing alternatives first) pairs with a "build the same small agent twice" evaluation method from the same account: give two candidate frameworks the same job, the same tools/state/test set, the same approval rule, and the same deployment target, then compare the resulting code, execution traces, failure modes, and cost — a framework decision based on operational fit for the actual job, not GitHub stars alone. Worth running before committing a new agent build to any framework on this list (or to LangChain).

## Team/agent collaboration platforms

| Repo | What it's for | Install / link |
|---|---|---|
| `block/buzz` | A free, open-source "hive mind" workspace (built by Block, Jack Dorsey's company) where Claude Code, Codex, and Goose agents join the same channels as a human team — agents get their own persistent presence, added to a channel like a person, rather than being called as a stateless prompt-in/answer-out tool. Built on the Nostr protocol: every message, reaction, workflow step, review approval, and git event is a signed event in one log, the same shape whether a human or an agent produced it. Ships native `.claude/skills`, `.codex/skills`, and `.goose/skills` folders built into the repo, so each agent framework gets first-class support instead of a bolt-on integration. 19.8K stars, Apache-2.0, 84 contributors, still shipping daily. Desktop app for Mac, plus a one-click Railway deploy for self-hosting. | `git clone github.com/block/buzz` — https://github.com/block/buzz |

**Why this is a different category from the rest of this list**: the other tools above extend what a single agent session can do (design engine, orchestration, memory). Buzz instead changes *where* an agent operates — inside a persistent, shared, multi-member channel alongside people, with its actions logged in the same event stream as everyone else's — which is a different integration shape worth knowing about specifically when the ask is "how do I get my agents working alongside my team," not "how do I make one session smarter."

## How to use this list

- These are **not** cloned into this repo (except `humanizer`) — they're separate software projects (a desktop app, a CLI, an orchestration framework, a database) that don't fit as markdown skill files, and vendoring foreign codebases into a business-skills repo would be out of scope.
- When recommending one, check current star count/activity/license at the link before suggesting it as production-critical — this list is a snapshot, not a live-verified endorsement.
- `vercel-labs/skills` in particular is relevant to *how* this repo's skills got here: it's a real package manager for the same file-based skill convention this repo hand-installs skills into.

## Related skills in this repo

- **humanizer**: The one skill from the same source that's actually installed here.
- **attachment-intake**: This whole entry followed that procedure — inspect first, confirm the content is genuinely useful, then act.
- **web-task-scoping**: The governance procedure (Target/Limit/Run/Review) to apply before running any of the five browser-automation frameworks above against a real site.
- **night-shift-workflow**: If a Buzz-connected agent is also running on a schedule (not just responding live in a channel), apply that skill's Claude-may/human-approval boundary to decide what it can post/act on unattended vs. what needs a person to approve first.

## Notes

Sources: a "7 Claude Code repos I can't work without" screenshot carousel (@joshualevi.ai) for the first six tools; "AI Power User Stack — 5 AI browser agents that can do the clicking for you" carousel (@zhiprompts) for the browser-automation frameworks; "AI Power User Stack — 5 AI agent builders to try before LangChain" carousel (@zhiprompts) for the agent-building frameworks and the "build the same small agent twice" evaluation method; "Buzz — The Hive Mind for Humans + Agents" carousel (@iunlockedai, Tool Drop 15) for `block/buzz`.
