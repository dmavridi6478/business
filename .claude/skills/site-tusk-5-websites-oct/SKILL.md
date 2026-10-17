---
name: site-tusk-5-websites-oct
description: Five websites from a @sitetusk "5 websites they don't want you to know about" carousel (sandspiel.club, befunky.com, networthify.com, omnara.com, actualbudget.org) with what each is, reachability checked on 16 October 2026, licences for the two open-source projects, and the caution on telling an agent to read a remote SKILL.md.
---

# Site Tusk, "5 websites they don't want you to know about"

Source: a 7-slide carousel (cover with a grey astronaut, an intro slide showing the TikTok "Bookmark Playlist" button, and five website slides). The title is clickbait: all five are public sites. Reachability was checked on 16 October 2026 (HTTP 200 for each); page content was not reviewed.

| Site | What the slide says it is | Notes |
|---|---|---|
| sandspiel.club | Browser falling-sand simulator; mix water, fire, lava, acid | A toy; no account needed on the slide |
| befunky.com | Online photo editor, collage maker and graphic designer with AI-assisted tools and templates | Freemium; check what is free and what happens to uploaded photos |
| networthify.com | Early-retirement calculator that tracks net worth and savings rate and shows working days left until financial independence | Calculators give estimates, not advice; the page shows a "beta" tag |
| omnara.com | Open-source agent deployment platform: run AI agents on any model or machine through one API, "the open-source alternative to Claude Managed Agents" (Backed by Y Combinator; about 2.9k stars on the slide) | Repo `omnara-ai/omnara`, Apache-2.0 (LICENSE read). The slide shows `npx omnara agents launch --name ... --source ... --message ...` and "Read omnara.com/SKILL.md to set up my agent" |
| actualbudget.org | Open-source, privacy-focused budgeting app: envelope budgeting, local-first storage, multi-device sync, optional end-to-end encryption | Repo `actualbudget/actual`, MIT (LICENSE read). "Set up on PikaPods in 2 minutes" is a paid hosting partner |

## Cautions
- **"Read omnara.com/SKILL.md to set up my agent"** asks your agent to fetch a remote file and follow it. That is third-party text acting as instructions, so read the file yourself first and run only the steps you understand. The same applies to any "paste this URL to your agent" setup line.
- "Alternative to Claude Managed Agents" is a positioning claim; compare features and hosting before moving workloads.
- A budgeting app holds financial data: back it up, and prefer end-to-end encryption if you sync.
- Star counts and "Backed by" labels on the slides are unverified.

The TikTok "Bookmark Playlist" step is an instruction to the viewer; nothing was bookmarked or followed. The beige card layout is `design-templates/templates/repo-card-beige-grunge.html`.
