---
name: replace-so-repos-4-plasmic-brightbean
description: The @replace.so "Open-source picks - 4 free repos to explore" 27-second video (Oct 2026) - Plasmic (open-source visual builder for your React codebase), BrightBean Studio (self-hosted social media management, AGPL-3.0, Python/Django) and Maxun (no-code web scraping to structured API) - with what the video shows, the fourth repo that is never shown, licence and sponsor cautions, and a quick evaluation checklist. Use when comparing visual site builders, self-hosted social schedulers or no-code scrapers, or when someone asks what these repos are.
---

# Open-source picks: Plasmic, BrightBean Studio, Maxun

Source: one 27-second video with captions only (no audio was available to read). The opening card says "4 free repos" and "I found 4", but only three repos appear on screen; the fourth is not identifiable. Comment "REPOS" to the creator for links.

| Repo | What the screen shows | Notes | Already covered in |
|---|---|---|---|
| Plasmic (`plasmicapp/plasmic`) | "The open-source visual builder for your codebase": drag and drop your own React components, integrate with your codebase, "break through the low-code ceiling"; logos for React, Next, Gatsby, Vue, Nuxt | open-core: MIT core, AGPL platform per other notes here; confirm which layer you depend on | `dev-repos-to-clone`, `claude-code-tooling` |
| BrightBean Studio | open-source, self-hostable social media management for creators, agencies and SMBs; Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Threads, Bluesky, Google Business Profile, Mastodon, DEV.to; multi-workspace, approvals, calendar; AGPL-3.0, Python 3.12+, Django; free hosted version plus one-click Heroku, Render, Railway, Docker | uses your own platform developer credentials, so you must get API approval from each network; AGPL means modified network-served copies must publish source | README 46th addition |
| Maxun | "Turn any website into a structured API": no-code scraping, crawling and extraction; sponsor table of proxy vendors (Webshare, MangoProxy, Nodemaven) and TestMu AI | sponsor and discount codes in the README are advertising, not endorsements | `replace-so-oss-swap-6-oct`, `replace-so-dev-repos-6` |

## Checklist before adopting
1. Licence: AGPL components (BrightBean, Plasmic platform) have network-use obligations; check with `/repo-licence-check`.
2. Social tools post under your accounts: use a test workspace first, keep approval on, never auto-post (see `social-publishing`).
3. Scraping: respect robots.txt and each site's terms; avoid personal data without a lawful basis; proxies add cost and legal exposure.
4. Self-hosting means you own updates, backups and secrets (`self-hosted-docker-stack`).
Related: `/oss-repo-vet`, `/installer-safety-check`, `/self-host-swap`.
