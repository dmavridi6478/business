---
name: oss-repo-register-105
description: 'Verified register of repos and tools from the third iCloud batch (6 Oct 2026): Agency Agents (230+ agent personas), Papermorph (PDF to animated web book skill), Colibri (runs 744B-2.8T MoE models on consumer hardware), Open Reality (phone video to AI-queryable 3D scenes, MCP), Mural (open-source voice language app), the SoL-Pi research paper, and four cards whose repo could not be identified (Elm-simple-server, runs-on.dev, Liquid-glass-screens and the seventh). Real licence, stars, install route and warnings; read the licence and account requirement before cloning.'
---

# Repo register - batch 105

Checked on GitHub pages or by search on 6 Oct 2026; stars move daily. **Nothing was cloned or installed in the cloud session.** Install steps are in the user-run `scripts/batch105-install.sh`.

| Repo | What it really is | Licence | Stars | Install / use | Notes |
|---|---|---|---|---|---|
| `msitarzewski/agency-agents` | Collection of 230+ specialist agent personas (engineering, design, marketing, sales, product, PM, testing, support, spatial, finance, games, academic) | MIT | ~158k | `./scripts/install.sh --tool claude-code` copies them into `~/.claude/agents/` | Installing all 230 into a project dilutes agent routing; install one division, read the files first. Not vendored here |
| `DozenTwelve/Papermorph` | A Claude skill that turns a PDF into an animated, narrated, interactive web book with quizzes | MIT | ~385 | `npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code`, then `/papermorph Turn /path/book.pdf into an animated interactive web book` | README says it needs Opus 5.5; no image models, multilingual or music yet. Do not run on PDFs you do not have rights to |
| `JustVugg/colibri` | Pure-C inference engine that streams Mixture-of-Experts models (744B-2.8T parameters) from RAM and disk on consumer hardware | Apache-2.0 | ~39.9k | Prebuilt release, or `git clone ... && cd colibri/c && ./setup.sh`; `./coli chat`, `./coli web`, `./coli serve` | Needs 16 GB RAM minimum and about 372 GB disk for GLM-5.2; speed depends on expert-cache hit rate; use gs64 quantised weights. Not a cloud-session tool |
| `reality-opened/openreality` | Turns phone video into AI-queryable 3D scenes; 41 MCP tools (measure, route-plan, scene Q&A, robot-dataset export) | BSD-2-Clause | ~231 | `/plugin marketplace add reality-opened/openreality` then `/plugin install openreality@openreality`; or `claude mcp add openreality -- npx -y openreality-mcp serve` after `npx -y openreality-mcp login` | Needs a browser sign-in (revocable API key) or self-hosting. Uploads your video to their service unless self-hosted. **Not added to `.mcp.json`**: it runs a third-party npm package at session start |
| `Chuloo/mural` | Native iPhone and Android app for voice-based language practice | MIT | ~1.6k | iOS: Xcode 26+, open `apps/ios/Mural.xcodeproj`; Android: `./gradlew :app:assembleDebug` | Needs an OpenAI API key; iOS 26.1+, Android 8+ |
| SoL-Pi | Research paper (arXiv 2609.20519, NVIDIA/NTU/MIT): harness mechanisms that cut token traffic 44.7-49.0% and API cost about one third on a 51-task benchmark | n/a | n/a | Paper and project page only; no repo URL confirmed | Card shows ~3.1k stars on a code link I could not open |
| Elm-simple-server | Card: runs Elm programs as HTTP servers | ? | card: 54 | Not found by that name | Do not clone by guessing; similar: `eeue56/servelm` (deprecated) |
| runs-on.dev | Card: free `yourname.runs-on.dev` subdomain by managed DNS record or pull request | ? | card: 336 | Not found | Free-subdomain services are common (js.org, is-a.dev); read the terms and the owner before pointing DNS at it |
| Liquid-glass-screens | Card: React Native/Expo cookbooks for liquid-glass welcome screens | ? | card: 296 | Not found | For the effect itself see Expo `expo-glass-effect` (iOS 26+, falls back to a plain View elsewhere) |
| (7th repo) | Title says 7; six cards were in the upload | | | | Missing |

## How to read a repo before installing
Licence (AGPL and Elastic restrict services), account or API-key need, what leaves your machine, install script content, last commit date, open issues about security.

## Keywords
agency agents, papermorph, colibri, openreality, mural, SoL-Pi, repo register, licence
