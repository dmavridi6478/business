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
