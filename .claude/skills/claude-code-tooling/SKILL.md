---
name: claude-code-tooling
description: Curated directory of external Claude Code tools worth knowing about and recommending — a design-engine desktop app, a senior-engineer skill pack, an educational mini agent-harness, multi-agent orchestration, a skills package manager, a self-evolving agent context database, five AI browser-automation frameworks (Playwright MCP, Stagehand, Skyvern, Magentic-UI, Steel Browser), a hive-mind team workspace (Buzz) that gives Claude Code/Codex/Goose agents a persistent presence alongside humans in shared channels, five open-source AI video-generation model repos (Wan 2.2, LTX-Video, HunyuanVideo, CogVideo, Mochi), a live-verified 22-repo "skills to install in Claude" collection grouped by Build/Design/Research/Marketing (superpowers, impeccable, taste-skill, hyperframes, i-have-adhd, and others, with per-entry verification status), and 5 power-user CLI/MCP tools (token-cost tracker, multi-model router, multi-model consult server, multi-agent terminal manager, a community skills/agents/commands hub). These are standalone software projects, not skills to load — reach for this when the user asks what to install to improve their Claude Code setup, or is looking for a specific capability (multi-agent orchestration, agent memory, a skills package manager, browser automation, agents-in-team-chat, open video generation, anti-AI-slop design skills, cost tracking, model routing) that a plain skill file can't provide.
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

## Team/agent collaboration platforms

| Repo | What it's for | Install / link |
|---|---|---|
| `block/buzz` | A free, open-source "hive mind" workspace (built by Block, Jack Dorsey's company) where Claude Code, Codex, and Goose agents join the same channels as a human team — agents get their own persistent presence, added to a channel like a person, rather than being called as a stateless prompt-in/answer-out tool. Built on the Nostr protocol: every message, reaction, workflow step, review approval, and git event is a signed event in one log, the same shape whether a human or an agent produced it. Ships native `.claude/skills`, `.codex/skills`, and `.goose/skills` folders built into the repo, so each agent framework gets first-class support instead of a bolt-on integration. 19.8K stars, Apache-2.0, 84 contributors, still shipping daily. Desktop app for Mac, plus a one-click Railway deploy for self-hosting. | `git clone github.com/block/buzz` — https://github.com/block/buzz |

**Why this is a different category from the rest of this list**: the other tools above extend what a single agent session can do (design engine, orchestration, memory). Buzz instead changes *where* an agent operates — inside a persistent, shared, multi-member channel alongside people, with its actions logged in the same event stream as everyone else's — which is a different integration shape worth knowing about specifically when the ask is "how do I get my agents working alongside my team," not "how do I make one session smarter."

## Open-source AI video-generation models

Five open video-generation model repos (from another "AI Power User Stack" carousel, @zhiprompts) — each a self-hosted, weights-and-code model family for text-to-video/image-to-video generation, positioned as a stand-in for a real production/shoot day rather than a hosted SaaS tool:

| Repo | What it's for | Install / link |
|---|---|---|
| `Wan-Video/Wan2.2` | Alibaba's open Wan video-model family — text-to-video and image-to-video workflows — 17k stars, Python | https://github.com/Wan-Video/Wan2.2 |
| `Lightricks/LTX-Video` | Lightricks' video models, tuned for generation speed and creator-oriented workflows over raw fidelity — 11k stars, Python | https://github.com/Lightricks/LTX-Video |
| `Tencent-Hunyuan/HunyuanVideo` | Tencent's open video-model family for text-driven generation and research workflows — 12k stars, Python | https://github.com/Tencent-Hunyuan/HunyuanVideo |
| `zai-org/CogVideo` | Open-source text-to-video and image-to-video model family with open research tooling — 13k stars, Python | https://github.com/zai-org/CogVideo |
| `genmoai/mochi` | Genmo's open video-generation model, weights, and inference code for prompt-driven motion generation — 3.7k stars, Python | https://github.com/genmoai/mochi |

None of these are cloned into this repo — same standalone-software rule as the rest of this list, and running any of them requires real GPU infrastructure this environment doesn't provide. Before picking one for a real project, run the `video-model-evaluation` skill's five-clip test rather than choosing based on a single hand-picked demo clip or star count alone.

## "22 Skills to Install in Claude" collection (Elshad Karimov / appmillers.com)

A 22-repo carousel grouped into Build (6), Design (6), Research (6), and Marketing (4). **This list was independently verified against live GitHub search before being documented here** — this ecosystem has heavy name-collisions (many unrelated forks share the same short repo name), so a name and star count from a carousel alone isn't enough to safely point someone at "the" repo. Status per entry:

### Build

| Repo | What it's for | Status |
|---|---|---|
| `obra/superpowers` | Agentic skills framework enforcing brainstorm → design → plan → TDD → review before writing code | ✅ Verified — 270k+ stars, matches carousel's claim |
| `ayghri/i-have-adhd` | Action-first output shaping — stops an agent from burying the answer in preamble | ✅ Verified — real repo, ~19.7k stars (carousel said 9.4k; the repo is real, the exact count differs — re-check before quoting a number) |
| "gstack" (23 dev skills in one install) | Claimed bundle of 23 dev skills | ⚠️ Not verified — the repo matching that name/description on GitHub has 0 stars and a different description than claimed; the canonical high-star repo the carousel meant wasn't locatable by search. Don't install without finding and reviewing the actual source first |
| "caveman" (answer-only, no fluff) | Output-compression skill | ⚠️ Not independently located as a standalone canonical repo — real forks reference it as a source (e.g. `skthewimp/caveman-adhd` merges it with `i-have-adhd`), but the original wasn't confirmed directly |
| "ponytail" (forces short, one-line replies) | Output-brevity skill | ⚠️ Not found via search — verify existence before recommending |
| OpenAI Codex CLI | Runs OpenAI's Codex inside/alongside Claude Code | Real, well-known official OpenAI tool — not a small community skill, a full separate CLI product |

### Design

| Repo | What it's for | Status |
|---|---|---|
| `pbakaus/impeccable` | "The design language that makes your AI harness better at design" — a final polish pass | ✅ Verified — 58k+ stars, matches carousel's ballpark. **Overlaps with this repo's `design-review-audit` skill** — both exist to catch generic-AI-slop output; compare before adding both to a workflow |
| `Leonxlnx/taste-skill` | Stops an agent generating generic/boring UI | ✅ Verified — 75k+ stars, matches carousel's ballpark. **Overlaps with `design-review-audit` and `frontend-design`** in this repo — same anti-slop goal from a different angle |
| `heygen-com/hyperframes` | Write HTML, render an actual video, built for coding agents | ✅ Verified — 40k+ stars, matches carousel's ballpark. Real HeyGen product |
| "ui-ux-pro-max" (67 styles, 96 palettes, 57 font pairings) | Design-token/style intelligence skill | ⚠️ Multiple forks exist under this name, none matching the carousel's claimed 110k-star scale in search results — canonical repo unclear. **Overlaps with `design-token-extractor` and `theme-factory`** in this repo regardless of which fork is real |
| "emil" (Emil Kowalski-style interface animation) | Smooth interface-animation guidance, referencing real designer Emil Kowalski's work | ⚠️ Not independently confirmed at a specific repo path — multiple other repos reference "Emil Kowalski's design-engineering skills" as a real source, but the canonical repo wasn't pinned down directly. **Overlaps with this repo's `ui-motion-design` skill** — that skill already deliberately avoids attributing unverified quotes to Emil Kowalski specifically, for the same reason: no confirmed primary source |
| GSAP (GreenSock) | Production-grade JavaScript animation library | Real, well-known npm library (greensock.com). **Update**: GreenSock also ships an official 8-part Claude Code skill pack for it (`greensock/gsap-skills`, MIT) — vendored for real in this repo as `gsap-core` + 7 siblings (see below), not just referenced externally |

### Research

| Repo | What it's for | Status |
|---|---|---|
| Anthropic Skill Creator | Builds custom skills from examples/preferences | Already covered — see `docs/procedures/personal-voice-skill.md`. It's Anthropic's own built-in meta-tool, not a separate repo to vendor; the carousel's specific star count for it wasn't independently confirmed |
| "graphify" (turns messy notes into a visual map) | Note-to-diagram tool | ⚠️ Not found via search — verify existence before recommending |
| "last30days" (what the internet said this month) | Trend/news summarization skill | ⚠️ Not found via search |
| "agent-browser" (lets Claude use any website) | Browser-automation tool | ⚠️ Not found via search under that name — if browser automation is the actual need, this repo's existing **browser-automation frameworks** section above (Playwright MCP, Stagehand, Skyvern, Magentic-UI, Steel Browser) are independently verified alternatives |
| "find-skills" (finds and installs any skill you need) | Skill discovery/installer | ⚠️ Not independently verified. **Overlaps conceptually with `vercel-labs/skills`**, already documented above as a real, verified skills package manager |
| "claude-hub" (shows what Claude is doing, live) | Live observability dashboard for Claude Code | ⚠️ Not found via search — verify existence before recommending |

### Marketing

| Repo | What it's for | Status |
|---|---|---|
| `remotion-dev/remotion` | Build full videos programmatically in React | Real, well-known open-source library — not a Claude-specific skill, a production video framework |
| "marketingskills" (40 growth/marketing skills bundled) | Marketing skill bundle | Same source org as the `marketingskills/copywriting` and `marketingskills/marketing-psychology` skills already installed in this repo (see those skills) — `content-strategy` (already installed, pre-existing) covers that org's content-strategy skill too. The other ~37 skills in the bundle weren't individually reviewed; install additional ones from it only after reading each one's actual content, per this repo's standing vendoring discipline |
| `blader/humanizer` | Strips robotic AI tone from text | ✅ Verified — 35k+ stars, matches carousel's ballpark. **Already installed** in this repo as the `humanizer` skill |
| "social-media-skills" (Elshad Karimov's own content pack) | Personal skill pack behind the carousel author's own posts/reels/captions | Lower confidence — a named individual's personal, self-promotional repo with no independently verifiable popularity signal (carousel itself shows "mine" instead of a star count) |

**Bottom line for installing from this list**: `superpowers`, `i-have-adhd`, `impeccable`, `taste-skill`, and `hyperframes` are real, verified, and safe to point someone at directly. The ⚠️-flagged entries need the actual canonical repo located and its content reviewed before installing — don't vendor a skill based on a carousel screenshot's name and star count alone, since this specific ecosystem has many unrelated same-named forks.

## Power-user CLI/MCP tools

Five repos from "5 repos every Claude power user installs first" (@zhiprompts) — each independently verified against live GitHub search before being listed:

| Repo | What it's for | Install / link |
|---|---|---|
| `ccusage/ccusage` | One `npx ccusage` command shows exactly what Claude Code sessions cost, down to the token — 17.8k stars, Rust | `npx ccusage` — https://github.com/ccusage/ccusage |
| `musistudio/claude-code-router` | A local control plane that routes Claude Code requests to any model (including free/local ones), fusing capabilities and orchestrating tools without giving up control — 36.5k stars, TypeScript | https://github.com/musistudio/claude-code-router |
| `BeehiveInnovations/pal-mcp-server` | Formerly "Zen" — an MCP server that has Claude consult Gemini/GPT (or GeminiCLI/CodexCLI/OpenRouter/Azure/Grok/Ollama) mid-task and keeps the best answer, instead of relying on one model's take | https://github.com/BeehiveInnovations/pal-mcp-server |
| `smtg-ai/claude-squad` | Runs multiple AI terminal agents (Claude Code, Codex, OpenCode, Amp) in isolated workspaces, so different agents can attempt the same task and the best result gets merged | https://github.com/smtg-ai/claude-squad |
| `davepoon/buildwithclaude` | A single community hub for finding Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections, with web search built in — a browsable alternative/companion to `vercel-labs/skills`' install-from-CLI approach | https://github.com/davepoon/buildwithclaude |

`pal-mcp-server` in particular is worth flagging alongside `night-shift-workflow`: a tool that lets Claude consult other models mid-task and keep the best answer is exactly the kind of unattended-but-consequential decision that skill's Claude-may/human-approval boundary should be applied to if it's running as part of a scheduled workflow rather than an interactive session.

## Motion-skill packages ("4 Secret Claude Skills for Motion," @hiitzroman)

Four `npx skills add <owner>/<repo>` packages (the same `vercel-labs/skills` installer documented above). Each was actually cloned and inspected before deciding what to do with it — the carousel's one-line pitch didn't always match what was inside:

| Repo | Carousel's pitch | What inspection actually found |
|---|---|---|
| `greensock/gsap-skills` | "The library everyone uses" | ✅ Clean, single-source, MIT, 8 well-formed skills. **Vendored for real** — see `gsap-core` and its 7 siblings above. |
| `boraoztunc/skills` (specifically its `waapi` folder) | "Your browser has had its own animation engine all along" — framed as general Web Animations API guidance | The actual `waapi/SKILL.md` says explicitly: "Web Animations API adapter patterns **for HyperFrames**" — it's a narrow runtime adapter scoped to the `heygen-com/hyperframes` tool (documented above), not general-purpose WAAPI guidance. The wider `boraoztunc/skills` repo also bundles multiple other authors' work under separate `LICENSE-hyperframes`/`LICENSE-mengto-skills`/Apache-2.0 files — an aggregator, not a single-source repo. Not vendored; if HyperFrames-based motion work comes up, point at the real repo directly (`github.com/boraoztunc/skills`, `waapi` folder) rather than treating it as general WAAPI instruction. |
| `AThevon/genjutsu` | "Reveal-on-scroll with no JavaScript" (billed as "css-animations") | The repo has no top-level `css-animations` skill — its actual structure is a large personal aggregator (17+ sub-skills spanning SwiftUI, Compose Multiplatform, Three.js/R3F, Framer Motion, GSAP, and more), and at least one sub-skill (`ui-ux-pro-max`) carries its own `UPSTREAM.md` marker showing it's re-vendored from elsewhere — the same `ui-ux-pro-max` already flagged as canonical-repo-unclear in the 22-repo collection above. Not vendored; MIT-licensed and real, but review the specific sub-skill needed before pulling anything from it, not the repo as a whole. |
| `remotion-dev/skills` | "Same skills, except an MP4 comes out the end" | Confirmed as a real part of the official Remotion monorepo (`remotion-dev/remotion/tree/main/packages/skills`), but its `package.json` marks it `"private": true` and the carousel itself flags "see licence" rather than a clean license tag like the other three. `remotion-dev/remotion` (the base library) is real and well-known, but its license terms should be read directly before vendoring or relying on the skills package commercially — not assumed permissive from the carousel alone. Not vendored. |

**Lesson from this batch**: a carousel's one-line pitch for a skill repo can describe a different (often narrower or differently-licensed) thing than what's actually in the repo — `waapi` and `css-animations` are both examples here. Clone and read before vendoring or recommending, the same discipline already applied to the 22-repo collection above.

## How to use this list

- These are **not** cloned into this repo (except `humanizer` and the 8 `gsap-*` skills) — the rest are separate software projects (a desktop app, a CLI, an orchestration framework, a database) that don't fit as markdown skill files, and vendoring foreign codebases into a business-skills repo would be out of scope.
- When recommending one, check current star count/activity/license at the link before suggesting it as production-critical — this list is a snapshot, not a live-verified endorsement.
- `vercel-labs/skills` in particular is relevant to *how* this repo's skills got here: it's a real package manager for the same file-based skill convention this repo hand-installs skills into.

## Related skills in this repo

- **humanizer**: The one skill from the same source that's actually installed here.
- **attachment-intake**: This whole entry followed that procedure — inspect first, confirm the content is genuinely useful, then act.
- **web-task-scoping**: The governance procedure (Target/Limit/Run/Review) to apply before running any of the five browser-automation frameworks above against a real site.
- **night-shift-workflow**: If a Buzz-connected agent is also running on a schedule (not just responding live in a channel), apply that skill's Claude-may/human-approval boundary to decide what it can post/act on unattended vs. what needs a person to approve first.
- **video-model-evaluation**: The fair-comparison procedure (same brief, same edit, same rubric) to run before picking one of the five open video models above for a real project.
- **design-review-audit** / **frontend-design**: `impeccable` and `taste-skill` in the 22-repo collection above target the same anti-AI-slop goal as these two skills, from an external-tool angle rather than a checklist angle.
- **ui-motion-design**: The "emil" entry in the 22-repo collection references the same real designer (Emil Kowalski) that skill already deliberately avoids quoting without a confirmed primary source — same caution applies here.
- **design-token-extractor** / **theme-factory**: The "ui-ux-pro-max" entry in the 22-repo collection covers similar ground (style/palette/font-pairing intelligence) to these two skills.
- **copywriting** / **marketing-psychology**: Installed from the same `marketingskills` source org referenced in the 22-repo collection's Marketing section.
- **personal-voice-skill** (procedure): Covers the same Anthropic Skill Creator tool referenced in the 22-repo collection's Research section.
- **night-shift-workflow**: Apply its Claude-may/human-approval boundary if `pal-mcp-server`'s multi-model-consult pattern runs as part of a scheduled/unattended workflow rather than an interactive session.
- **vercel-labs/skills** (above): `davepoon/buildwithclaude` is a browsable community hub covering similar ground to that CLI-based skills package manager — different interface, same "find and install a skill" job. It's also the exact tool the `npx skills add` commands in the motion-skill packages below use.
- **gsap-core** and its 7 siblings: The one skill pack from the motion-skills batch below that was actually clean enough to vendor for real — see those skills directly rather than this entry, which now just documents the source.

## Notes

Sources: a "7 Claude Code repos I can't work without" screenshot carousel (@joshualevi.ai) for the first six tools; "AI Power User Stack — 5 AI browser agents that can do the clicking for you" carousel (@zhiprompts) for the browser-automation frameworks; "Buzz — The Hive Mind for Humans + Agents" carousel (@iunlockedai, Tool Drop 15) for `block/buzz`; "AI Power User Stack — 5 open AI video models that can replace a production day" carousel (@zhiprompts) for the video-generation model repos; "22 Skills to Install in Claude" carousel (Elshad Karimov, appmillers.com) for the Build/Design/Research/Marketing collection — each entry live-checked against GitHub search before being documented, given this ecosystem's heavy same-name-fork collisions; "5 repos every Claude power user installs first" carousel (@zhiprompts) for the power-user CLI/MCP tools, also live-verified before documenting; "4 Secret Claude Skills for Motion" carousel (@hiitzroman) for the motion-skill packages — all 4 were actually cloned and read before deciding to vendor (`gsap-core` + 7 siblings) or document-only (the rest).

A companion upload in the same batch ("AI Unlocked, Tool Drop 19 — your subagents stopped nesting 5 levels deep") included only its cover/teaser slide, with no actual content slides explaining the referenced setting — not enough real information to document without guessing at specifics, so it was flagged to the user rather than turned into a skill.
