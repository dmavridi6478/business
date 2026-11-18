---
name: oss-dotdevs-ai-visibility-five-nov2026
description: Checked register of the second @dotdevs "5 GitHub projects worth exploring" set (5 Nov snapshot) - Mailcheap, FluidVoice, OneGlanse, Ansvisor, Omnara - plus the same creator's analytics-tool slides (Google Search Console, PostHog, Microsoft Clarity, Pirsch, OpenPanel), with licences read from the repos, what each README actually claims, the cautions the slides omit (saved AI-account logins, AGPL, a Mac app with a closed AI runtime), and what was already covered. Use before installing any of them, when choosing a free analytics or AI-visibility tracker, or when asked what is new versus covered.
---

# @dotdevs, second set (read 16 November 2026)

Checked 16 November 2026: all five repos exist (`git ls-remote`, default branch `main`), licences read from the repo files, claims compared with the READMEs. Star counts are the cards' "5 Nov snapshot" and were not checked (GitHub API blocked). The first @dotdevs set (AFFiNE, Traefik, Keila, Instatic, Automa) is in `oss-finds-eight-creators-nov2026`; the "I built Springback" and "I built Slothy" slides are the creator's own apps (Springback is in `oss-finds-three-carousels-nov2026`) and are promotions, not assessed.

## The five repos

| Project | Repo | Card (stars, line) | Licence (read) | What the README says | Caution the card omits |
|---|---|---|---|---|---|
| Mailcheap | `marclou/mailcheap` | 1,635; write newsletter issues and manage delivery from a self-hosted app | AGPL-3.0 | Whole newsletter app; self-host with your own Amazon SES; works from the dashboard, REST API or an AI agent through MCP; has a paid MailCheap Cloud | Sending email needs list consent, DKIM/DMARC records and bounce handling; README sets pause limits (2.5% hard bounces, 0.08% complaints); AGPL: offer source if you run a modified copy as a service |
| FluidVoice | `altic-dev/FluidVoice` | 12,829; speech into edited text with a Mac dictation workflow | GPL-3.0 (macOS app) | macOS 15+, Apple Silicon local models, dictation and meeting transcripts | "Fluid Intelligence", the on-device AI runtime in official downloads, is separate and privately maintained, not in the repo's source build; needs microphone and accessibility permissions; recording meetings needs consent |
| OneGlanse | `oneglanse/oneglanse` | 250; compare how assistants describe a brand over time | MIT | Runs your prompts on ChatGPT, Perplexity, Gemini, Claude and Google AI Overview websites (not model APIs) and saves the answers | Uses your own AI accounts and saved browser logins; the scores come from a model you configure reading the saved text, not from the AI sites; results vary by account, place and time; check each site's terms before automated use |
| Ansvisor | `ansvisor/ansvisor` | 231; inspect brand mentions and citations in AI answers | MIT | "Open-source agentic AI Search Execution Platform"; tracks prompts, mentions, citations, competitors; a Content Agent drafts and fixes pages; self-host or paid Ansvisor Cloud | The vendor sells the cloud version; "agentic" drafts need review before anything ships; its own README says people stay in charge of what ships |
| Omnara | `omnara-ai/omnara` | 3,357; run agents with explicit permissions, tools and persistent state | Apache-2.0 | "Open-source, self-hostable alternative to Claude Managed Agents and OpenAI's Agents API"; SDK on npm | Giving an agent tools and persistent state is a security decision; start with read-only tools and a throwaway environment |

## The analytics slides (tools, not repos)

| Tool | Slide line | Real use | Notes |
|---|---|---|---|
| Google Search Console | The searches that find your site | Queries, clicks, indexing problems for sites you own | Free; needs site verification |
| PostHog | Funnels and replays, generous free tier | Product analytics with funnels, replays, flags | Has an open-source and a paid cloud edition; check limits and EU hosting for GDPR |
| Microsoft Clarity | Free heatmaps and session recordings | Where users click and drop off | Recordings capture user behaviour: consent and masking of sensitive fields apply |
| Pirsch | Website analytics with "privacy settings you still need to configure" | Cookie-light web analytics | The slide's own warning is right: privacy settings are not automatic compliance |
| OpenPanel | Product analytics without the bloat | Open-source alternative to Google Analytics (its own tagline) | Already listed in `datawarlord-oss-repos` |

"Find where users drop off" needs a funnel with defined steps and enough traffic; a tool does not supply either.

## Licence flags

AGPL-3.0 (Mailcheap): source must be offered if you run a modified copy as a network service. GPL-3.0 (FluidVoice): copyleft on distributed changes. MIT and Apache-2.0: permissive.

## Not done

Nothing cloned, installed or run; star counts, tool pricing and free-tier limits not verified; the claim that AI visibility scores predict traffic is not shown anywhere in these sources. Use `/repo-vet owner/repo` and `/repo-licence-check` first, and `ai-search-visibility` and `aeo-diagnostic-metrics` for method.
