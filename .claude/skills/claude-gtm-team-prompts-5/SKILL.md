---
name: claude-gtm-team-prompts-5
description: Five copy-ready Claude prompts for GTM teams (ICP lead list, account brief, pipeline follow-up, pitch deck and demo booking, sequence digest) with the connectors each needs and this account connection status. Source: Growth Today.
---

# Claude for GTM teams
| Stage | Use | Connectors | Command |
|---|---|---|---|
| Prospecting | ICP lead list builder | HubSpot, Clay, Notion | `/gtm-icp-lead-list` |
| Research | Account intel brief | Fireflies, Notion, Slack | `/gtm-account-brief` |
| Pipeline | Follow-up and QBR trigger | HubSpot, Gong, Slack | `/gtm-pipeline-followup` |
| Close | Pitch deck and demo booking | HubSpot, Calendly, Gmail | `/gtm-pitch-demo` |
| Review | Sequence performance digest | HubSpot, Notion, Slack | `/gtm-sequence-digest` |
**ICP lead list builder** (Prospecting)
> Pull my closed-won companies from HubSpot and find the shared pattern: industry, size, tech stack, triggers. Use Clay to find 300 lookalike accounts with 2-3 verified contacts each, score them against that ICP, and save the list to Notion sorted by fit.

**Account intel brief** (Research)
> Write a one-page brief on [company]. Pull recent call notes from Fireflies, summarize priorities, pains and objections, add hiring and tech-stack signals, and finish with the 3 best angles to open with. Save to the Notion account page and post the TL;DR in Slack.

**Follow-up and QBR trigger** (Pipeline)
> Review my open pipeline in HubSpot. Pull the latest Gong call for each deal, flag anything stalled over 14 days, draft a next-step follow-up for each, and update the deal stage in HubSpot. Post a summary of at-risk deals in Slack.

**Pitch deck and demo booking** (Close)
> Build a pitch deck for [company] using their HubSpot record and my template: their pain, our fit, pricing, proposal. Create a Calendly link for the demo and draft the cover email with the deck and link.

**Sequence performance digest** (Review)
> Pull last week's sequence data from HubSpot. Show open, reply and meeting rates by sequence and step, flag the worst steps, and suggest one fix per sequence. Save the digest to Notion and post the TL;DR in Slack.

**Connector status in this account (7 Oct 2026):** HubSpot connected; Clay connected; Notion connected; Fireflies connected; Slack connected; Calendly connected; Gmail connected; Gong not connected (needs sign-in).
**Safety:** these prompts write to live systems. Before any step that updates HubSpot, posts to Slack, creates a Calendly link or touches email, show the planned change and wait for approval; emails are drafts only. Never contact anyone from these prompts.
