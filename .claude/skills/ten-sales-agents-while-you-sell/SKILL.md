---
name: ten-sales-agents-while-you-sell
description: The salesdaily.co "10 AI sales agents that work while you sell" card - five daily agents (morning brief, account watch, inbox triage, speed-to-lead, call follow-up) and five weekly ones (stalled deals, competitor watch, past champions, CRM cleanup, pipeline report), each as a copy-paste instruction with its schedule or trigger, how to build them (Claude Cowork scheduled task, ChatGPT, Zapier Agents, n8n) and the drafts-only rule. Also the GTMs-toolkit "9 AI tools for GTM outbound" table (Common Room, Perplexity, Smartlead, Lavender, Lindy, Gong, Clay, Lusha, Surfe). Use when setting up recurring sales automations or choosing outbound tools.
---

# 10 sales agents (start with one, add the next when it works)

Rule from the card: **keep every agent on drafts. You read it and hit send.** In this repo outbound actions also go through `os-approval`.

| # | Agent | When | Instruction (paste as the agent's instructions) |
|---|---|---|---|
| 1 | Morning brief | 07:00 daily | Check my calendar. For every external meeting today, research the company and attendees and send me a 5-line brief. |
| 2 | Account watch | 06:00 daily | Scan news, job posts and leadership changes at [my top accounts]. Send only what's new, with one opener for each. |
| 3 | Inbox triage | hourly | Go through my inbox. Flag buyer replies, referrals and out-of-office return dates, and draft a reply to each. |
| 4 | Speed-to-lead | on new lead | When a demo request comes in, research the company and the person, check fit against [my ICP] and draft a personal reply. |
| 5 | Call follow-up | after calls | When a call recording is ready, draft the recap email with next steps and dates, and add the notes to the deal in my CRM. |
| 6 | Stalled deals | Monday | Find deals in my CRM with no activity in 14 days. Draft a check-in for each, based on the last conversation. |
| 7 | Competitor watch | Monday | Check [competitor]'s pricing page, launches and new reviews. Tell me what changed and how to answer it on calls. |
| 8 | Past champions | Wednesday | Check which champions from my won deals changed jobs. Draft a congrats note for each one. |
| 9 | CRM cleanup | Friday | List deals with no next step, a past close date or empty fields, and suggest the fix for each. |
| 10 | Pipeline report | Friday | Summarize what moved, what slipped and the 3 deals at highest risk. Draft my update for my manager. |

## How to build one (card)
- **Runs on a schedule:** a scheduled task in Claude Cowork or ChatGPT (here: `claude-automation-stack-3-tiers`, `/scheduled-routine`).
- **Starts when something happens:** build in Zapier Agents or n8n (`n8n-agent-builder`).
- Paste the line as instructions and connect the apps it mentions (calendar, inbox, CRM, call recorder).

## Critique
1. Agents 3 and 8 read personal data (inbox, job changes): check consent and your privacy notice before automating; "past champions changed jobs" often relies on scraped LinkedIn data.
2. Agent 5 writes to the CRM: allow it to add a note, not edit stages or amounts.
3. Start with 1 or 6; a noisy agent gets muted and then ignored.
4. Measure: replies per draft, minutes saved, drafts discarded.

## GTMs toolkit: 9 AI tools for GTM outbound
| # | Tool | Place in workflow | Best feature | Why it matters |
|---|---|---|---|---|
| 1 | Common Room | find ready-to-buy prospects | high-intent signal tracking (dark social) | warm leads instead of cold calls |
| 2 | Perplexity | pre-call or email intel | real-time account and market research | context for personalised messages |
| 3 | Smartlead | scaling outbound email infrastructure | multi-mailbox warm-up | inbox placement |
| 4 | Lavender | optimise copy before sending | real-time email scoring | reply rates |
| 5 | Lindy AI | niche admin GTM tasks | no-code custom agents | "swiss-army knife" |
| 6 | Gong | post-outreach analysis, closing | revenue intelligence from call recordings | aligns messaging with winning deals |
| 7 | Clay | lead research and list building | multi-source waterfall enrichment | personalised data at scale |
| 8 | Lusha | contact verification | direct mobile and email accuracy | reach a human |
| 9 | Surfe | social selling to CRM bridge | one-click CRM and LinkedIn sync | no manual entry |
Caveat: "psychological email scoring" and "guarantees you reach a human" are marketing claims. Multi-mailbox warm-up tools exist to evade spam filters: use them within CAN-SPAM/GDPR and your provider's terms. Common Room, Clay and Lusha connectors exist in this environment (`common-room:*`, `lusha:*`, Clay MCP). Related: `gtm-outbound-engine`, `outbound-flow-6stage-18tools`, `perplexity-sales-research-10`. Command: `/sales-agent`.
