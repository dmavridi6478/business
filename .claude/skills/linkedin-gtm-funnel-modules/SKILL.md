---
name: linkedin-gtm-funnel-modules
description: The 11-module LinkedIn go-to-market funnel for 2026 (Paolo Trivellato, starbornai.com) - content stack, comment routing, idea sources, post jobs, post review tests, weekly setup, lead readiness, DM handling, posting calendar, booking handoff and funnel rules - with the tools shown on each module and the rules in process.notes. Use when building or auditing a LinkedIn lead engine that turns posts into booked calls, or when setting up comment-to-DM routing.
---

# LinkedIn GTM funnel in 2026 - 11 modules

Source: animated infographic "How To Run a LinkedIn GTM Funnel in 2026" by Paolo Trivellato. Promise on the slide: turn posts into booked calls with one idea bank, one CTA per post and same-day DMs. Tool names are the author's picks, not recommendations.

| # | Module | What it does | Tools on the slide |
|---|---|---|---|
| 1 | Content stack | Every post starts from what you know. Three jobs: custom GPT (thinking), writing, visuals | Custom GPT, Claude (writing), a visual tool |
| 2 | Comment routing | New comment, then ICP fit check. Pass goes to resource plus DM; not ICP yet goes to nurture. Every commenter gets the same-day treatment | LinkedIn, CRM-style lookup |
| 3 | Idea sources | Six feeds into one idea bank: calls (objection bank), X (top tweet daily), backlog (top 10 outliers), assets (playbook bank), trends (last 6 months), comments (questions as posts) | Calls tool, X, Notion, YouTube, LinkedIn |
| 4 | Post jobs | 1 post a day, 3 jobs, 2 lead magnets a week. Types: Awareness (problem they do not see), Value (step by step, go deep), Opinion (tested first on X), Proof (client results), Lead magnet (comment KEYWORD), Case study (video breakdown) | LinkedIn, X, Notion, YouTube |
| 5 | Post review | Tabs: Ideas, Draft, Review, Schedule. Six tests per post: What am I saying (3 questions before a word); Shrink (60s, 30s, one sentence); So what (read it as a busy CEO); Buyer (would they forward it); Screenshot (one line worth sharing); CTA match (matched to awareness) | Idea bank search, writing tool |
| 6 | Weekly setup | 1 Idea bank, 2 Test on X, 3 Rewrite, 4 Visual, 5 Approve, 6 Post | GPT, X, Claude, LinkedIn, Notion, Slack |
| 7 | Lead readiness | ICP fit? Setter or Nurture, then Call booked. Lead depth rings: Commented, Opted in, Booked. Booking checklist: over $10k/mo; qualifying questions answered; VSL on landing page; pre-sell sent | CRM, Calendly |
| 8 | DM handling | Comment captured (opt-in link in the reply); Profile viewer (DM if ICP fits within 24h); Engager DM (check they got it, do not pitch) | DM tool, LinkedIn |
| 9 | Posting calendar | Mon value, Tue magnet, Wed opinion, Thu magnet, Fri proof; windows on LinkedIn, X and a DM tool; "rewrite top tweet" then Approved | LinkedIn, X |
| 10 | Booking handoff | Comment, Opt-in, DM, VSL, Book, Call. Calendly books, Notion records, Slack alerts | Calendly, Notion, Slack |
| 11 | Funnel rules (process.notes) | 01 post: 1 a day, 3 jobs. 02 cta: in the image. 03 dm: same day. 04 book: vsl + calendly. 05 under $10k/mo: cancel. Pre-sell before the call | n/a |

## How to run it here

- Module 1 to 6 (content): `linkedin-strategy`, `linkedin-post-types`, `/linkedin-week-content-plan`, `hook-writer`; drafting through Taplio or Typefully connectors.
- Module 2 and 8 (routing): the n8n draft workflow "LinkedIn comment routing (GTM funnel 2026)" sends ICP-fit commenters to a Slack approval and the rest to nurture. It needs a Slack credential and a webhook sender; it is not published.
- Module 7 and 10 (booking): Calendly connector for event types and availability; Notion for the record.
- Command: `/linkedin-gtm-funnel [offer, ICP, current monthly revenue of buyers]`.

## Reading it critically

- The "$10k/mo" disqualifier is the author's rule for his offer, not a universal threshold; set your own from your price and sales cycle.
- Same-day DMs to every commenter can breach LinkedIn automation limits and spam rules if automated; draft and approve, do not auto-send.
- Nothing on the slide shows results or conversion rates. Treat the structure as a hypothesis and measure comment-to-opt-in, opt-in-to-booked and booked-to-held.
