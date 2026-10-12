---
name: oss-repo-cards-batch-115
description: Open-source repo cards from batch 115 - @githubnow 17 Sep trio (tinycast, n8n, coder), @replace.so cards (Figranium, OpenFlowKit, ScrapeCraft, BridgeClip, Listmonk) and a "repos every developer should know" video list (roadmap.sh, build-your-own-x, public-apis, system-design-primer, awesome-python, free-programming-books, Coding-Interview-University) - with slide stars, what each does, licence or safety notes and which are already covered by other skills. Use when scouting self-hosted automation, scraping, diagramming, video-clipping or newsletter tools, or picking learning repos.
---

# OSS repo cards (batch 115)

Stars are the slides' own at capture time. Read README and LICENSE; prefer official releases; never run a piped installer.

## @githubnow, 17 Sep 2026: "tools that give developers 10 extra hours weekly"
| Repo | What | Slide | Note |
|---|---|---|---|
| abue-ammar/tinycast | native macOS Raycast-style launcher: app launching, file search, clipboard history, window management; SwiftUI + AppKit, zero third-party deps, under 100 MB RAM; runs real Raycast extensions as native views | +1,076 stars today | macOS only; extension runtime executes third-party code, so vet extensions |
| n8n-io/n8n | visual and code (JS/Python) AI workflows, 1,500+ integrations, self-host or cloud | 51,309 stars | fair-code licence (not OSI open source); skills `n8n-*` exist here |
| coder/coder | cloud dev environments on your infrastructure: Terraform templates (EC2, Kubernetes, Docker), idle auto-shutdown, AI agents in the control plane with audit logging and no LLM credentials inside workspaces | +83 today | heavy to operate; real value is agent governance |
The slide's "start with tinycast, README gets you running in ten minutes" line is template filler (it recurs across unrelated slides).

## @replace.so cards
| Repo | What | Stars | Licence / notes | Covered by |
|---|---|---|---|---|
| figranium/figranium | self-hosted visual browser-automation platform: block editor, scheduling, proxy rotation, REST API | 762 | check licence | `github-trending-oct8-repos` |
| Vrun-design/openflowkit | local-first diagramming studio: AI generation, diagram-as-code, structured canvases, Figma export | 833 | MIT | `replace-so-agent-repos` |
| ScrapeGraphAI/scrapecraft | AI scraping editor (Cursor-style) on the ScrapeGraphAI API; export JSON/CSV; Python + TypeScript | 708 | MIT; needs an API key | this skill |
| bridge-mind/bridgeclip | desktop app: long videos to captioned short clips, find moments, refine framing, export; own OpenRouter key; bundles Python, FFmpeg, yt-dlp | 364 | MIT; downloading videos you do not own raises copyright issues | this skill |
| knadh/listmonk | self-hosted newsletter and mailing-list manager, single binary | 23,708 | AGPL-3.0 (verify); needs SMTP; consent and unsubscribe duties (GDPR) | `self-hosted-docker-stack` |
Scraping caution: respect robots.txt and each site's terms; LinkedIn and X forbid most scraping.

## Video: "GitHub repos every developer should know" (@valeridoesai? handle unclear)
roadmap.sh (developer roadmaps), codecrafters-io/build-your-own-x (~552k stars), public-apis list (screen showed a wrong 1-star repo, use `public-apis/public-apis`), donnemartin/system-design-primer (~374k), vinta/awesome-python, EbookFoundation/free-programming-books (~399k), jwasham/coding-interview-university. CTA "pinned comment for the link" is a lead magnet. Low confidence (frames only); verify each owner/name before cloning.
Optional clones are in `scripts/batch115-install.sh`. Related: `dev-repos-to-clone`, `replace-so-oss-repos-10-oct`, `data-ai-github-25`.
