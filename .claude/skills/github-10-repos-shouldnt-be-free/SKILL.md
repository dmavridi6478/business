---
name: github-10-repos-shouldnt-be-free
description: A @martiendejong_dev series "10 GitHub repos so good they shouldn't be free" (AutoHedge, Vibe Trading, Fincept Terminal, LibreChat, Open Higgsfield AI, Open LLM VTuber, Claude Ads, Agentic Inbox, Camofox Browser, HyperFrames) with repo slugs, licences read on 16 October 2026, which are already vendored here, and the risk or inflated claim on each card.
---

# 10 GitHub repos "so good they shouldn't be free" (@martiendejong_dev)

Source: 10 numbered cards plus an intro card ("GitHub is basically a website where developers share their code for free... Let's go"). Every card shows a GitHub page screenshot; star counts below come from those screenshots and are **unverified**. Licences were read from each repo's LICENSE file on 16 October 2026. The series uses a cartoon mascot; no character art was copied into this repo.

| Card | Repo | Licence | Stars on card | Already here |
|---|---|---|---|---|
| #1 AutoHedge | The-Swarm-Corporation/AutoHedge | MIT | about 3.1k | no |
| #2 Vibe Trading | HKUDS/Vibe-Trading | MIT | about 9.6k | no |
| #3 Fincept Terminal | Fincept-Corporation/FinceptTerminal | AGPL-3.0 | about 25k | README mention only |
| #4 LibreChat | danny-avila/LibreChat | MIT | about 38k | `oss-ai-alternatives` |
| #5 Open Higgsfield AI | Anil-matcha/Open-Generative-AI | MIT | about 17.9k | no |
| #6 Open LLM VTuber | Open-LLM-VTuber/Open-LLM-VTuber | MIT | about 8.5k | no |
| #7 Claude Ads | AgriciDaniel/claude-ads | MIT | about 5.6k | `claude-ads` (vendored) |
| #8 Agentic Inbox | cloudflare/agentic-inbox | Apache-2.0 | about 3.9k | no |
| #9 Camofox Browser | jo-inc/camofox-browser | MIT | about 6.2k | `camofox-browser` (vendored) |
| #10 HyperFrames | heygen-com/hyperframes | Apache-2.0 | about 23.7k | `hyperframes` (vendored) |

## What each card claims, and the catch
- **#1 AutoHedge:** "An AI hedge fund you can run from your laptop... Type one line of code. It starts trading on its own." This places real trades. Not financial advice. Paper-trade first, give any broker key the least permission, and expect to lose money.
- **#2 Vibe Trading:** "Like AutoHedge but with 64 finance skills... agents debate each other about trades." Same risk; a debate between models is not evidence that a trade is sound.
- **#3 Fincept Terminal:** "A Bloomberg Terminal. For free. Bloomberg charges $24,000 a year... 20+ AI agents pretending to be Buffett, Soros, Ray Dalio... 100+ data sources." Not equivalent: Bloomberg sells licensed data; each data source here has its own terms and keys. AGPL-3.0.
- **#4 LibreChat:** "OpenAI charges $20/month. This is free." The app is free; the model APIs you connect are not.
- **#5 Open Higgsfield AI:** "200+ AI models... No subscription. Your files stay on your computer." The repo's own tags say "uncensored" and "unrestricted". You are responsible for consent, likeness and copyright; model calls usually go to a provider and cost money [Likely].
- **#6 Open LLM VTuber:** "Runs 100% offline. Never forgets you." Offline only if you choose local models; it hears your voice and sees your screen, so review what it can capture.
- **#7 Claude Ads:** "Runs 190 checks... Agencies charge $4,000/month." The repo's own README snapshot says 250+ checks, so the slide and repo disagree; the price is unsourced.
- **#8 Agentic Inbox:** "AI reads and replies to your emails for you... emails never leave your own account." It runs on Cloudflare Workers, so mail is processed by Cloudflare and the AI provider you configure. Keep a human approval step before anything sends.
- **#9 Camofox Browser:** "Fools bot detectors... also cuts AI costs by 90%." The 90% is unverified. Evading a site's bot protection can breach its terms and some laws; use only on sites you own or are allowed to automate.
- **#10 HyperFrames:** "Write basic web code (HTML). It turns it into an actual MP4 video." Deterministic render; Apache-2.0.

## Use
Clone for reading only (see `scripts/batch113-install.sh`). Run `/repo-licence-check` on any repo before using it commercially. Nothing was installed or run.
