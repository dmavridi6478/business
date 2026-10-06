---
name: oss-repo-register-104
description: Verified register of 19 open-source repos and tools from the Oct 2026 iCloud TikTok carousels (@replace.so, @joshualevi.ai, @martiendejong_dev, @dotdevs, @aiclawbots) - real owner, licence, stars, what the repo actually does, install route and a warning where the carousel's description does not match the repo. Use before cloning or recommending any of them; read the licence column first (AGPL, Elastic and hosted-API requirements matter).
---

# Repo register - iCloud Photos batch (6 Oct 2026)

Checked against each repo's GitHub page on 6 Oct 2026. Stars move daily. **Nothing here was cloned or installed**; the user-run `scripts/batch104-install.sh` does that, one confirmed step at a time.

## Carousel descriptions that do NOT match the repo
The @martiendejong_dev "red cat" cards use generated dashboards and stock descriptions. Two are plainly wrong:
- **Magnitude** (card: "time series database and analytics platform") - the repo describes itself as an open-source **inference engine** that compiles kernels for your hardware to run open models faster. Not a database.
- **paperclip** (card: "chat with your PDFs / knowledge base") - it is an **agent-orchestration platform** (org charts, budgets, governance for teams of AI agents). Not document chat.
The others are roughly right but the card star counts are stale (e.g. open-seo card 3.7k vs ~22.5k; gods-eye-view card 4.2k vs ~48.1k). Treat those cards as pointers to a repo name, never as documentation.

## Register
| Repo | Carousel | What it really is | Licence | Stars | Notes / install |
|---|---|---|---|---|---|
| `mem0ai/mem0` | replace.so | Memory layer for AI agents | Apache-2.0 | ~66.7k | `pip install mem0ai`; Claude skills: `npx skills add https://github.com/mem0ai/mem0 --skill mem0` (and `--skill mem0-cli`) |
| `rivet-dev/rivet` | replace.so | Orchestrator for agentic workloads; durable "Actors" (12 ms cold start, 72 KB each) | Apache-2.0 | ~6.2k | `npm install rivetkit`; skills: `npx skills add rivet-dev/skills` |
| `getpaseo/paseo` | replace.so | Control plane for coding agents: run Claude Code, Codex etc. from desktop/mobile/web/CLI, self-hosted | AGPL-3.0 | ~19.6k (card) | Native apps, Homebrew, npm. Source of licence/stars: web search, not the repo page |
| `better-auth/better-auth` | replace.so | Framework-agnostic TypeScript auth framework with plugins (MFA, SSO, passkeys, MCP auth) | MIT | ~30.2k | `npx auth init` |
| `lukevella/rallly` | replace.so | Meeting-time polls without participant accounts | **AGPL-3.0+** | ~5.3k | Docker image to self-host |
| `comet-ml/opik`, `confident-ai/deepeval`, `Arize-ai/phoenix`, `UKGovernmentBEIS/inspect_ai`, `Giskard-AI/giskard-oss`, `lmnr-ai/lmnr`, `traceloop/openllmetry` | joshualevi.ai | Agent tracing / evaluation / red teaming | Apache-2.0 (opik, deepeval, giskard, lmnr, openllmetry); MIT (inspect_ai); **Elastic-2.0 (phoenix)** | 2.9k-22.4k | See skill `agent-eval-repos-7` |
| `magnitudedev/magnitude` | martiendejong | Open-source inference engine (see warning) | Apache-2.0 | ~6.5k | Read the README before running |
| `debpalash/VoiceStudio` | martiendejong | Local ElevenLabs alternative: voice cloning, dubbing, transcription, audiobooks | **AGPL-3.0** | ~54k | Installer is `curl ... | sh` - read the script first; cloning a real person's voice needs their consent |
| `THU-MAIC/OpenMAIC` | martiendejong | Turns a topic or document into an interactive multi-agent classroom | MIT | ~40k | `pnpm install`, API keys in `.env.local`, PostgreSQL (docker `pnpm db:up`) |
| `bilawalsidhu/gods-eye-view` | martiendejong ("godseyeview") | Browser 3D globe with live aircraft, ships, satellites, public cameras | MIT | ~48.1k | Node 24/26 `npm ci && npm run dev`, or Pinokio |
| `HKUDS/Vibe-Trading` | martiendejong | AI trading-agent / backtesting framework | MIT | ~34.8k | Docker or pip. **Backtests are not predictions; no risk disclaimer was shown on the page** |
| `paperclipai/paperclip` | martiendejong | Agent-orchestration platform (see warning) | MIT | ~97.9k | `npx paperclipai@latest onboard --yes` |
| `every-app/open-seo` | martiendejong | Open-source alternative to Semrush/Ahrefs: keywords, rank tracking, audits | MIT | ~22.5k | Docker or Cloudflare. **Needs a paid DataForSEO API key**; already in `setup-repos.sh` |

## Not resolved
- **"hermes-startup-architect"** (@aiclawbots): no repo by that name found. `33hodl/hermes-startup` (MIT, "make your first dollar online") appeared in search but is not confirmed to be the same. The workflow was rebuilt natively as skill `startup-investor-kit`.
- **@replace.so "6 repos"**: only five appear in the photos (Mem0, Rivet, Paseo, Better-auth, Rallly). The sixth was not in the upload.
- **dotdevs "5 free tools"** (Vercel, Supabase, Figma, Canva, GitHub + GitHub Student Pack): hosted services, not repos. Already covered by `dev-repos-to-clone`; Figma and Canva are connected here, Supabase needs the owner's reconnect, Vercel exists in the registry but is not connected.

## Licence rules of thumb
AGPL-3.0 (paseo, rallly, VoiceStudio): fine to run for yourself; offering it as a network service means publishing your modifications. Elastic-2.0 (phoenix): source-available; you may not offer it as a managed service. Paid-API dependency (open-seo): the code is free, the data is not.
