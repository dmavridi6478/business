---
name: gtm-plays-12
description: Twelve go-to-market plays as signal-to-action flows with the tools named for each step (website visitors, LinkedIn engagement, hiring-signal outbound, champion job changes, closed-lost revival, email waterfall, lookalike expansion, competitor engagement, inbound orchestration, awareness scoring, webinar follow-up, AI call prep), each mapped to what this stack already has and to the consent and platform-rule checks the card omits. Use when someone has a buying signal and wants the matching play, is designing outbound or inbound automation, or asks how to use Clay, HubSpot, Claude or an enrichment waterfall together. Source Growth Today (Nikola Siljanoski), "12 GTM Plays I Recommend" (Batch 115). Tools were read from the image, not verified.
---

# 12 GTM plays: from signal to meeting

Source: infographic "12 GTM Plays I Recommend" by Nikola Siljanoski (Growth Today). Each play is a signal, a few enrichment or routing steps, and an outcome. Tool names are read from the card; vendors, prices and results were **not** verified, and the one numeric claim (play 5, "30% come back") has no source on the card.

Stack already here: Clay, HubSpot, Apollo.io (needs your authorisation), Common Room, Vibe Prospecting, ZoomInfo (connected or authorisable in claude.ai), plus `gtm-api-stack`, `gtm-outbound-engine`, `abm-gtm-layers` and `/gtm-weekly-loop`.

| # | Play | Signal | Steps (tools named on the card) | Outcome |
|---|---|---|---|---|
| 1 | Website visitors | Someone visits your site | People and company identification (RB2B, factors.ai) -> ICP check (Clay) -> Tier 1: LinkedIn DM; Tier 2: email; not a fit: nurture | Meeting booked |
| 2 | LinkedIn engagement | Likes, comments, reposts, profile views on your post | Captured by Trigify + Clay -> enrich and ICP filter (Clay) -> DM (Expandi) | Warm conversation |
| 3 | Hiring-signal outbound | A target company posts a relevant role | TheirStack finds the new role -> Clay finds the buyer -> Instantly emails about the role | Meeting booked |
| 4 | Champion job changes | A past champion moves to a new company | UserGems catches the move -> Clay matches the new account -> HubSpot first touch | Warm intro |
| 5 | Closed-lost revival | Deal lost on timing or budget | Wait and watch signals -> refresh data (Clay) -> re-engage | Back into pipeline |
| 6 | Email waterfall | You need an email address | Prospeo -> BetterContact -> Apollo, each only if the last found nothing -> verify (Clay) | Verified email |
| 7 | Lookalike expansion | Your best customers | Lookalike search (Ocean.io, Apollo) -> tier 1-3 and rank (Clay) | Prioritised list |
| 8 | Competitor engagement | People engage with competitor posts | Competitor A and B posts -> enrich and de-duplicate (Clay) -> DM (Expandi) | In-market prospect |
| 9 | Inbound orchestration | A form fill | Enrich and score (Clay + Claude) -> ICP fit? yes: route to rep (HubSpot); no: nurture | Rep in minutes |
| 10 | Awareness scoring | Behaviour over time | Identified (visit) -> Aware (content) -> Interested (repeat visits) -> Considering (pricing page) -> Selecting (demo request), scored in HubSpot and Clay | Stage score |
| 11 | Webinar follow-up | Registrants (Luma) | Attended: recap and next step within 24 hours; no-show: replay link within 24 hours | Follow-up sent |
| 12 | AI call prep | A call is booked | Clay, HubSpot, LinkedIn and the website feed a Claude brief: company, buyer, signals, talking points | Call-ready brief |

## Checks the card omits (apply before any play runs)

- **Consent and data protection:** identifying anonymous site visitors (play 1) and scraping engagers (plays 2, 8) are personal-data processing. In the EU and UK you need a lawful basis, a privacy notice and an opt-out. Get legal advice for your markets.
- **Platform rules:** LinkedIn limits automation. Auto-DM tools (play 2, 8) can breach its terms and get accounts restricted. Prefer a human sending from the approved list.
- **Deliverability:** cold email volume needs authenticated domains and low spam rates (play 3, 6). Verify addresses; a catch-all domain accepts anything.
- **Cost and stack creep:** a waterfall of three paid providers charges per lookup. Cap credits per run.
- **Evidence:** run each play on a small segment with a written success metric and kill date before scaling. The "30% come back" figure is unsupported.

## How to use
1. Name the signal you can already see. If none, pick play 12 (call prep) or 10 (scoring): they need no new data source.
2. Take the matching row, keep only the steps you can run with tools you already have.
3. Draft only: stop before anything is sent. A human approves every outbound message.

Use `/gtm-play <signal>`. Related: `ai-gtm-tools-20`, `gtm-outbound-engine`, `abm-gtm-layers`, `tal-build-7-steps`.
