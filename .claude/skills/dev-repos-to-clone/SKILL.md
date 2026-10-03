---
name: dev-repos-to-clone
description: Five open-source repos worth cloning as a starting point before building common product infrastructure from scratch — self-hosted analytics (plausible/analytics), a scheduling/booking system (calcom/cal.diy), a copy-into-your-repo UI component library (shadcn-ui/ui), a Postgres/auth/storage backend (supabase/supabase), and a virtual whiteboard/diagramming tool (excalidraw/excalidraw). Use when scoping a new product build and deciding whether to write analytics, scheduling, a component library, backend auth/storage, or diagramming from zero versus forking a mature, actively-maintained OSS project.
---

# Dev Repos Worth Cloning Before Writing Code

Five categories of infrastructure that almost never need a from-scratch build.
Each repo below is real, actively maintained, and was live-verified (star
count, commit recency) at the time this skill was written — check current
numbers before quoting them, they move fast.

| Repo | Category | What it replaces building | Clone |
|---|---|---|---|
| [`plausible/analytics`](https://github.com/plausible/analytics) | Web analytics | A cookie-free, GDPR-friendly Google Analytics alternative — one clean dashboard, no cookie banner, no vanity-metric bloat. Elixir/Phoenix. AGPL-3.0 | `git clone https://github.com/plausible/analytics` |
| [`calcom/cal.diy`](https://github.com/calcom/cal.diy) | Scheduling / booking | A complete booking system you host and control (the open-source core behind Cal.com), instead of building calendar-sync + availability + booking-page logic from zero. Next.js/Prisma. MIT | `git clone https://github.com/calcom/cal.diy` |
| [`shadcn-ui/ui`](https://github.com/shadcn-ui/ui) | UI component library | Accessible, beautifully-designed components you copy directly into your repo (not an npm dependency) — you own and can edit every line instead of fighting a component library's API. React/Tailwind/Radix | `npx shadcn@latest init` (or `git clone https://github.com/shadcn-ui/ui` to browse source) |
| [`supabase/supabase`](https://github.com/supabase/supabase) | Backend (DB/auth/storage) | Postgres database, authentication, storage, and realtime subscriptions as one dedicated backend, instead of hand-rolling auth and file storage around a raw database. Apache-2.0 | `git clone https://github.com/supabase/supabase` |
| [`excalidraw/excalidraw`](https://github.com/excalidraw/excalidraw) | Diagramming / whiteboard | A hand-drawn-style virtual whiteboard with real-time collaboration and one-link sharing, for embedding diagram/sketch capability instead of building a canvas editor. MIT | `git clone https://github.com/excalidraw/excalidraw` |

## When to reach for one instead of building

- Need analytics but don't want to hand Google a copy of your traffic data or make visitors click a cookie banner → `plausible/analytics` (self-host or use their cloud).
- Need "book a call" / appointment scheduling on your own domain, not an embedded third-party widget → `calcom/cal.diy`.
- Starting a new frontend and don't want to be locked into a component library's theming API → `shadcn-ui/ui` (copy components in, they become your code).
- Need a Postgres database with auth and file storage wired together, fast, without standing up three separate services → `supabase/supabase` (self-host or their managed cloud).
- Need users to sketch a flow, wireframe, or diagram together in the browser → `excalidraw/excalidraw` (also embeddable as a React component: `@excalidraw/excalidraw`).

## Additional repos (Batch 83 — @replace.so and @githubnow, Sep 2026)

Repos identified from a second @replace.so "open-source alternatives" carousel and @githubnow daily briefings. License and GitHub handle verified where possible — notes inline where a handle needs confirming before cloning.

| Repo | Category | What it is | Notes |
|---|---|---|---|
| [`marin-community/marin`](https://github.com/marin-community/marin) | LLM training | Open research framework for training and evaluating large language models — from a community research group | Apache 2.0 (not MIT) |
| [`freestylefly/awesome-gpt-image-2`](https://github.com/freestylefly/awesome-gpt-image-2) | AI image prompts | 500+ reverse-engineered GPT Image 2 prompt cases + 20+ industrial templates — see `awesome-gpt-image-2` skill | MIT — **vendored as a skill** |
| [`jo-inc/camofox-browser`](https://github.com/jo-inc/camofox-browser) | Browser automation | Anti-detection browser server for AI agents (Firefox + C++-level fingerprint spoofing via Camoufox) — blocks Playwright detection | MIT — **vendored as a skill** |
| T3code | AI coding scaffold | Claimed Cursor/IDE replacement from @replace.so carousel — **exact GitHub handle unverified**; search `t3-oss` org or `T3code` before cloning | License unverified |
| Flexprice | Usage-based billing | Open-source usage-based billing and metering infrastructure — @replace.so alternative to Stripe Billing | **GitHub handle unverified**; search `flexprice` on GitHub |
| Paseo | Polkadot wallet | Native Polkadot browser wallet — @replace.so "open source" entry | **GitHub handle unverified**; try `paseo-network` or `getpaseo` |

## Additional repos (Batch 84 — @replace.so and @githubnow, Sep 2026)

Repos identified from a third @replace.so "open-source alternatives" carousel and @githubnow daily briefings. License and GitHub handle verified by cloning each repo and reading its LICENSE file; notes inline where the license situation is non-trivial.

### MIT — vendored as skills

| Repo | Category | What it is | Skill |
|---|---|---|---|
| [`inovector/mixpost`](https://github.com/inovector/mixpost) | Social media management | Self-hosted Hootsuite alternative — schedule, publish, and manage social posts across platforms. PHP/Laravel/Vue 3. ~3,673★ | `mixpost` |
| [`openwhispr/openwhispr`](https://github.com/openwhispr/openwhispr) | Speech-to-text | Local real-time speech-to-text via OpenAI Whisper — browser extension, CLI, and desktop app. Python. ~7,935★ | `openwhispr` |
| [`public-apis/public-apis`](https://github.com/public-apis/public-apis) | API directory | Curated list of 1,400+ free public APIs with auth, HTTPS, and CORS info — the canonical reference. ~340k+★ | `public-apis` |
| [`drakulavich/kesha-voice-kit`](https://github.com/drakulavich/kesha-voice-kit) | Voice I/O for AI | Plug-and-play voice input/output toolkit for AI agents — STT, TTS, audio streaming. Python. | `kesha-voice-kit` |
| [`NousResearch/Hermes-Agent-Self-Evolution`](https://github.com/NousResearch/Hermes-Agent-Self-Evolution) | Self-evolving agents | DSPy + GEPA framework for agents that rewrite their own prompts/tools to improve performance. ICLR 2026 Oral. ~5k★ | `hermes-agent-self-evolution` |
| [`pascalorg/editor`](https://github.com/pascalorg/editor) | 3D architectural editor | Browser-based 3D building/space editor for architectural design workflows. TypeScript/Three.js/React. | `pascalorg-editor` |
| [`ManimCommunity/manim`](https://github.com/ManimCommunity/manim) | Mathematical animation | 3Blue1Brown's animation engine — programmatic math animations from Python code. Python/Cairo/OpenGL. | `manim` |

### Non-MIT — document only (see `claude-code-tooling/SKILL.md` for full table)

| Repo | License | What it is |
|---|---|---|
| `nashsu/llm_wiki` | GPL v3 | LLM-powered wiki / knowledge-base builder |
| `getmaxun/maxun` | AGPL v3 | No-code web scraping platform |
| `webstudio-is/webstudio` | AGPL v3 | Open-source Webflow alternative |
| `coollabsio/shoutrrr` | Apache 2.0 | Notification library for Go (Slack, Discord, Teams, etc.) |
| `plasmicapp/plasmic` | MIT core + AGPL platform | Visual page builder (open-core — confirm which layer you depend on) |
| `liquidslr/system-design-notes` | No license | System-design interview notes — all-rights-reserved |
| `openai/skills` | Per-skill mixed | OpenAI agent skills — check LICENSE.txt per skill before use |
| `duongductrong/Snapzy` | BSD 3-Clause | Image/screenshot annotation and sharing tool |
| `0xsline/OpenChatCut` | AGPL v3 | Open-source chat session clipping and sharing |
| `armory3d/armorpaint` | zlib/libpng | Open-source GPU-accelerated 3D texture painting |
| `llvm/llvm-project` | Apache 2.0 + LLVM Exception | The LLVM compiler infrastructure |

## Before adopting any of them

Check current license terms and hosting costs (self-hosted vs. the vendor's
paid cloud tier) against the project's actual requirements — a mature repo
being free and open-source doesn't mean self-hosting it is free in
infrastructure/ops time. Read each project's own `CONTRIBUTING.md`/deployment
docs before going to production with it, since setup steps and dependencies
(Elixir/Phoenix for Plausible, a Postgres instance for Supabase and Cal.diy)
vary a lot from a typical Node/Python app.

## Additional repos (Batch 85)

**MIT-licensed — vendored as skills:**

| Skill name | Source repo | What it is |
|---|---|---|
| `chatterbox` | `resemble-ai/chatterbox` | Open-source TTS and voice cloning; replaces ElevenLabs |

**Original-content skills (no source repo):**

| Skill name | Source | What it is |
|---|---|---|
| `ai-agent-founding-team` | @theromanknox (pages 2–4) | Org chart + first six AI agent hires + Chief of Staff orchestrator pattern |

**Duplicates from Batch 84 (no new action):** All content from @replace.so, @githubnow, @swblessed, @alexfishhh1, @your.ai.mentor, and @skilldropai carousels was already processed in Batch 84.

## Additional repos (Batch 86 — @replace.so "Open-source repos" video, week series)

| Repo | Category | What it is | Clone |
|---|---|---|---|
| [`pocketbase/pocketbase`](https://github.com/pocketbase/pocketbase) | Backend (DB/auth/realtime) | Open-source realtime backend in a single Go file/binary — auth, a SQLite-backed DB with a built-in admin UI, realtime subscriptions, and file storage, embeddable as a Go library or run standalone. MIT. ~61K★, 3.7K forks | `git clone https://github.com/pocketbase/pocketbase` |
| [`heyform/heyform`](https://github.com/heyform/heyform) | Forms / surveys | Open-source Typeform alternative — conversational forms, surveys and quizzes with conditional logic, picture-choice/date fields, webhook/Zapier/Make.com integrations, and brand theming. Self-hostable | `git clone https://github.com/heyform/heyform` |

`openwhispr/openwhispr` (voice dictation) also appeared in this same video — already tracked above (Batch 84 row) and vendored as the `openwhispr` skill; no new action.

Not a repo — skip: the same source zip also showed a `bytedance/seedance-2` AI video-ad generation demo via the paid `kie.ai` API (@imjonathanacuna, "Create ADs With Seedance 2.0"). It's a hosted model/API, not something to clone or self-host, so it's noted here for reference only.


## Additional repos (Batch 98 — @githubnow daily briefings, 29–30 Sep 2026)

All six verified live with `git ls-remote` on 2026-10-01; the first five were also cloned shallowly for reading. Star figures on the source cards are "today/month" deltas and were not re-verified.

| Repo | Category | What it is | Licence | Status here |
|---|---|---|---|---|
| [`VectifyAI/PageIndex`](https://github.com/VectifyAI/PageIndex) | Vectorless RAG | Tree-index + LLM-reasoning retrieval for long documents; `pip install -U pageindex` (0.2.20) | **MIT** | **vendored** as the `pageindex` skill + `/pageindex-ask` |
| [`NVIDIA/OpenShell`](https://github.com/NVIDIA/OpenShell) | Agent sandbox | Kernel-level policy enforcement for autonomous agents; formally verified policy changes; CLI + gateway + SDKs; ships 4 agent skills (`npx skills add NVIDIA/OpenShell`) | Apache-2.0 | documented only; install in `scripts/batch98-install.sh` (needs Docker/Podman) |
| [`t8y2/dbx`](https://github.com/t8y2/dbx) | Database client | 100+ databases in one small Tauri app, CLI, Docker web, built-in AI + MCP server (`@dbx-app/mcp-server`, npm 0.4.102); ships 1 agent skill | Apache-2.0 | documented only; MCP line in install script, **start read-only** |
| [`rakyll/hey`](https://github.com/rakyll/hey) | Load testing | Tiny HTTP load generator with HTTP/2, CSV export (`go install github.com/rakyll/hey@latest`); last commit 2026-01-10 | Apache-2.0 | documented only; wrapped by `/loadtest` with an ownership gate |
| [`longbridge/gpui-kit`](https://github.com/longbridge/gpui-kit) | Rust desktop UI | 75+ components on GPUI, 120 FPS, WASM, code editor, dock layout; ships 2 agent skills | Apache-2.0 (docs separate) | documented only — only relevant if you build a native Rust app |
| [`firebase/firebase-ios-sdk`](https://github.com/firebase/firebase-ios-sdk) | Mobile SDK | Firebase for iOS/macOS/tvOS/watchOS (Auth, Firestore, Messaging, Crashlytics…) | not checked | **not cloned** — large, and irrelevant unless you ship an Apple app |

**Already tracked (no new action):** SearXNG, Home Assistant, Pi-hole, Vaultwarden, Nextcloud — see `self-hosted-docker-stack`, `oss-ai-alternatives`, `homelab-*` skills and Batch 97.

## Additional repos (Batch 99 - @joshualevi.ai, @replace.so, @dotdevs, @githubnow, 30 Sep - 1 Oct 2026)

Verified live with `git ls-remote` (or `npm view`) on 2026-10-01. Four were also cloned shallowly into `repos/` (git-ignored) to read the licence and README: brigade, hindsight, codegraph, nanochat (all MIT). Star counts on the cards are screenshots, not re-verified.

| Repo | Category | What it is | Licence | Status here |
|---|---|---|---|---|
| [`spinabot/brigade`](https://github.com/spinabot/brigade) | Agent ecosystem | Self-hosted crew of AI agents with shared memory, multiple model providers and messaging channels; `npm i -g @spinabot/brigade` (npm 1.39.0) | MIT | cloned for reading; **not installed** (run it only in a sandbox: it ships a gateway and tunnel features) |
| [`vectorize-io/hindsight`](https://github.com/vectorize-io/hindsight) | Agent memory | retain / recall / reflect memory for agents; `pip install hindsight-api`, Docker image, Python and TS clients | MIT | cloned for reading; documented only |
| [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph) | Code index MCP | Local semantic code graph that agents query over MCP; installer auto-configures Claude Code and others | MIT | cloned for reading; **not installed**: the README installs with `curl ... | sh`, read it first |
| [`karpathy/nanochat`](https://github.com/karpathy/nanochat) | LLM training | Minimal full pipeline to train a small ChatGPT-style model on one GPU node; `runs/speedrun.sh` | MIT | cloned for reading; needs a multi-GPU node, documented only |
| [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | Course | 523 lessons / 20 phases per the card; every lesson ends with a prompt, skill, agent or MCP server | MIT (card) | verified, not cloned |
| [`microsoft/mcp-for-beginners`](https://github.com/microsoft/mcp-for-beginners) | Course | MCP curriculum with .NET, Java, TypeScript, JavaScript, Rust, Python code | not checked | verified, not cloned |
| [`microsoft/generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners) | Course | 21 lessons, Python and TypeScript | not checked | verified, not cloned |
| [`huggingface/agents-course`](https://github.com/huggingface/agents-course) | Course | 4 units: smolagents, LlamaIndex, LangGraph; free certificate | not checked | verified, not cloned |
| [`anthropics/courses`](https://github.com/anthropics/courses) | Course | Anthropic's own courses (API, prompt engineering, evals, tool use) | not checked | verified; skill `anthropic-courses` already exists |
| [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | Projects | 93 projects across LLMs, RAG and agents | not checked | verified; already tracked in README |
| [`stablyai/orca`](https://github.com/stablyai/orca) | Agent IDE | Parallel coding agents in isolated worktrees | not checked | verified; **README had it as `stab1yai/orca` (OCR typo) - corrected** |
| [`Skyvern-AI/skyvern`](https://github.com/Skyvern-AI/skyvern) | Browser automation | AI browser agents; MCP integration for Claude Code, Cursor, Codex; free tier 5,000 credits per the video | not checked | verified; **README had it as `Skyvern-AutoGPT/skyvern` - corrected** |
| [`n8n-io/n8n`](https://github.com/n8n-io/n8n) | Workflow automation | Fair-code platform; **check the licence before embedding or reselling** (the card says so) | fair-code | verified; many `n8n-*` skills already exist |
| [`langfuse/langfuse`](https://github.com/langfuse/langfuse), [`ollama/ollama`](https://github.com/ollama/ollama), [`expo/expo`](https://github.com/expo/expo), [`supabase/supabase`](https://github.com/supabase/supabase) | App stack | the @dotdevs "start with one missing piece" set: mobile (Expo), backend (Supabase), AI quality (Langfuse), local models (Ollama), workflows (n8n) | MIT / Apache-2.0 / MIT / Apache-2.0 (check each) | verified; too large to clone, documented only |
| `paperclipai/paperclip`, `ComposioHQ/awesome-claude-skills`, `alirezarezvani/claude-skills`, `public-apis/public-apis`, `VectifyAI/PageIndex` | various | seen again on these slides | - | already tracked in earlier batches; no new action |

**Could not verify from the card alone (no repo, package or owner shown):** iFixAi ("audits AI agents for mistakes", 17k stars on the card), Magpie ("one local gateway for agents' models", 3.7k), fframes ("video vibe coding framework", Rust + SVG, 1.4k). The npm names `fframes`, `ifixai` and `magpie-ai` do not exist. Find the real repo from the source video before cloning.

**Not a repo:** the SkillDrop AI and aicareersuite carousels (see `event-planner`, `claude-11-ways`), and the @entrp0 tool-stack video (see `docs/ai-os/ops/tool-stack.md`).

## Additional repos (Batch 100 - @joshualevi.ai security list, @replace.so, @githubnow, @ai.easily; 1-2 Oct 2026)

All 15 verified live with `git ls-remote` on 2026-10-02. Licences were read from each repo's root LICENSE file where one exists. None were cloned: the scanners are installed or documented in `agent-output-scanners`, and the apps are large.

| Repo | Category | What it is | Licence | Status here |
|---|---|---|---|---|
| [`gitleaks/gitleaks`](https://github.com/gitleaks/gitleaks) | Secret scanning | Keys and tokens in code and history; pre-commit hook | MIT | **installed and run** (`go install github.com/zricethezav/gitleaks/v8@latest`: the `gitleaks/` path fails) |
| [`google/osv-scanner`](https://github.com/google/osv-scanner) | Dependency scanning | Checks lockfiles against OSV; guided remediation | Apache-2.0 | **installed and run** (v2.6.0) |
| [`trufflesecurity/trufflehog`](https://github.com/trufflesecurity/trufflehog) | Secret scanning | Finds leaked credentials and verifies them against the provider | **AGPL-3.0** | documented; active verification sends credentials to providers |
| [`semgrep/semgrep`](https://github.com/semgrep/semgrep) | Static analysis | ~30 languages, your own rules | LGPL-2.1 (rules separate) | documented |
| [`snyk/agent-scan`](https://github.com/snyk/agent-scan) | Agent security | Scans agents, MCP servers and skills for injection; `uvx snyk-agent-scan`; needs `SNYK_TOKEN` | Apache-2.0 | documented; not run (needs your account) |
| [`NVIDIA/garak`](https://github.com/NVIDIA/garak) | LLM red-teaming | Probes a model with jailbreaks and injection | Apache-2.0 | documented |
| [`getsops/sops`](https://github.com/getsops/sops) | Secrets in git | Encrypted YAML/JSON/ENV files (KMS, age, PGP) | MPL-2.0 | documented |
| [`FlowiseAI/Flowise`](https://github.com/FlowiseAI/Flowise) | Visual agent builder | Drag-and-drop AI agents and workflows; 55k stars on the card | no root LICENSE file found | verified. **The screenshot of its site shows a banner "We're sunsetting Flowise". I could not confirm it in the README, so check before building on it.** |
| [`hexastack/hexabot`](https://github.com/hexastack/hexabot) | Chat automation | Self-hosted workflows for conversations, tasks and schedules, MCP support (v3) | no root LICENSE file found | verified |
| [`lfnovo/open-notebook`](https://github.com/lfnovo/open-notebook) | Research notebook | Private NotebookLM-style tool with podcast generation | MIT | verified |
| [`dyad-sh/dyad`](https://github.com/dyad-sh/dyad) | App builder | Local open-source AI app builder with your own API keys | mixed (the LICENSE says "portions" differ) | verified |
| [`robbietilton/Compositor`](https://github.com/robbietilton/Compositor) | Mac image editor | Layers, masks, filters, PSD support | MIT | verified; macOS only |
| [`pablostanley/yoinks`](https://github.com/pablostanley/yoinks) | Terminal video downloader | yt-dlp front end with an Ink UI | MIT | verified; **documented only**: downloading from most video sites breaks their terms or the owner's copyright unless you own or are licensed the content |
| [`androoAGI/starnet`](https://github.com/androoAGI/starnet) | Agent desktop | Runs several agents at once in a pixel-art station; default branch `feat/harness-backend` | MIT | verified |
| [`flutter/flutter`](https://github.com/flutter/flutter) | App SDK | One Dart codebase for iOS, Android, web and desktop | not checked | verified; too large to clone |

Also seen, already covered: `anthropics/skills` (see `claude-5-official-skills`).

## Additional repos (Batch 101 - @githubnow daily briefings 2-3 Oct 2026, @replace.so, @joshualevi.ai, @ai.easily)

Verified live with `git ls-remote` on 2026-10-03. Licences read from the root LICENSE of the cloned copies. Star deltas on the cards ("+1,141 today") are the creator's screenshots and were not re-verified.

| Repo | Category | What it is | Licence | Status here |
|---|---|---|---|---|
| [`humanlayer/skills`](https://github.com/humanlayer/skills) | Claude Code skills | Six skills: `show-me`, `visual-pr`, `improve-claude-md`, `narrow-react-prop-types`, `build-iterated-agentic-loop`, `design-control-loop` | MIT | **installed** with `npx skills add humanlayer/skills`; scanned first for risky patterns (none found) |
| [`mvschwarz/openrig`](https://github.com/mvschwarz/openrig) | Agent teams | Define persistent agent teams in YAML and boot them with one command; Claude Code, Codex and Pi in one rig; `npm install -g @openrig/cli` (needs Node 22 or 24 and tmux) | Apache-2.0 | cloned for reading; **not installed** (it runs agents and needs tmux; try in a sandbox) |
| [`TencentCloud/Octop`](https://github.com/TencentCloud/Octop) | Self-hosted agents | Private multi-agent assistant with web dashboard, CLI, knowledge base and IM channels; single-process deployment | MIT | cloned for reading; **not installed**: its documented installer is `curl ... install.sh | bash` from a Tencent COS bucket, so read the script first |
| [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) | Token optimiser | Strips prose from agent output; the card claims 65% fewer tokens and a JetBrains test on 86 tasks (unverified) | MIT (card) | already tracked; skill `caveman` exists |
| [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem) | Agent memory | Captures tool use and context, compresses and re-injects it in later sessions | not checked | verified; already tracked |
| [`cloudflare/cloudflare-os`](https://github.com/cloudflare/cloudflare-os) | Agent workspace | Per-user sandboxed "gadgets" behind capability-based gatekeepers with human approval; +9,562 stars this month per the card | not checked | verified; already tracked |

The @replace.so repo cards in these zips (Flowise, Hexabot, Dyad, Open-notebook, Compositor) and the @joshualevi.ai scanners were registered in Batch 100. `Flowise`: its site screenshot again shows the banner "We're sunsetting Flowise"; still unconfirmed, check before building on it.

**Not repos:** the @the.wealth.lab MCP carousel (see `mcp-dev-team-6`), @tinrovicai (`grok-bot-guide`), @jeanbbttyct (`ai-app-stack-2026`), @clicksandranks (`five-websites-business`), @shiva.bytes loops (`claude-code-4-loops`), 51ultron motion sheet (`motion-16-effects`).

## Additional repos (Batch 102 - @replace.so, @githubnow, Obsidian video; 3 Oct 2026)

Verified live with `git ls-remote` on 2026-10-03. Licences read from the root licence file of a blobless shallow clone (no install, no code run). Star counts on the cards are the creator's screenshots and were not re-verified. Three repo owners were not on the slides and were found by web search, then confirmed with `git ls-remote`.

| Repo | Category | What it is (card) | Licence | Status here |
|---|---|---|---|---|
| [`unslothai/unsloth`](https://github.com/unslothai/unsloth) | Local LLM studio | Run and fine-tune models on your machine; card claims 2x faster, 70% less VRAM | AGPL-3.0 (root COPYING; check per folder) | verified; **not installed** |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | Self-improving agent | Learning loop that builds skills from use; Telegram/Discord/Slack/Signal gateway, cron | MIT | already tracked (`hermes-nousresearch`) |
| [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | Marketing skills | 100+ markdown skills (CRO, copy, SEO, analytics) | MIT | already installed (`*-corey-haines` skills) |
| [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp) | Local inference | C/C++ LLM and vision inference; card shows `irm https://llama.app/install.ps1 \| iex` | MIT | verified; the slide's installer pipes a script into the shell, so use a package manager or build from source |
| [`CopilotKit/OpenBot`](https://github.com/CopilotKit/OpenBot) | Agent workplace | AI coworkers on your infrastructure with browser, files and tools; actions governed and recorded via AG-UI | MIT | verified; not installed |
| [`makeev/alphai-tui`](https://github.com/makeev/alphai-tui) | Terminal dashboard | Rust TUI: quotes, candlesticks, AI-scored news, SEC Form 4; free AlphAI key for news (20 req/min, 100/day per its listing) | MIT | verified; not installed |
| [`ChatbotXIO/ChatbotX`](https://github.com/ChatbotXIO/ChatbotX) | Chat marketing | Open-source omnichannel platform: flows, AI agents, inbox, CRM, broadcasts, CLI, MCP | **custom licence** (AhaChat LLC; read before self-hosting or reselling) | verified; not installed |
| [`busabase/busabase`](https://github.com/busabase/busabase) | Agent workspace | Open-source database and workspace for AI agents; works with Claude Code, Codex, Cursor | MIT | verified; not installed |
| [`jamiedavenport/capd`](https://github.com/jamiedavenport/capd) | Capture app (macOS 26+) | Local-first capture and full-text search, on-device OCR, CLI, read-only MCP | MIT | verified; macOS only; not installed |
| [`svix/svix-webhooks`](https://github.com/svix/svix-webhooks) | Webhook service | Send webhooks through one API call with retries and signing handled | MIT | verified; not installed |
| [`robbietilton/Compositor`](https://github.com/robbietilton/Compositor) | Image editor (macOS, Apple silicon) | Photoshop-style layers, masks, adjustments | MIT | already registered in Batch 100 |
| [`owncloud/ocis`](https://github.com/owncloud/ocis) | File sync and sharing | ownCloud Infinite Scale: web, desktop and mobile clients, WebDAV, OpenID Connect | Apache-2.0 | verified; not installed |
| [`athasdev/athas`](https://github.com/athasdev/athas) | Code editor | Lightweight cross-platform editor with agents, terminal, Git | AGPL-3.0 | verified; not installed |
| [`uptimepage/uptimepage`](https://github.com/uptimepage/uptimepage) | Uptime monitoring | Multi-region checks, status pages, on-call alerts, REST API, Terraform | AGPL-3.0 | verified; not installed |
| [`manaflow-ai/cmux`](https://github.com/manaflow-ai/cmux) | Terminal for agents (macOS) | Native terminal with attention rings and split panes for many agents (shown in the Obsidian video) | custom licence (read before use) | verified; not installed |

**Not repos:** the 7 photoshoot prompt cards (`photoshoot-prompts-7`), the SalesDaily, Cyberman, NipPro, Lever, Reno Perry and Partaker infographics (skills in this batch), and the 9-skills and 50-use-cases infographics (`prompt-writing-9-skills`, `claude-50-use-cases`). The Obsidian "Second Brain for All Your Agents" video is covered by the existing `ai-second-brain` skill; its narration was not legible in the frames, so no new claims were added.

