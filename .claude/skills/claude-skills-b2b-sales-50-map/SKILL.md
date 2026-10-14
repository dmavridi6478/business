---
name: claude-skills-b2b-sales-50-map
description: The Prosp "Claude Skills for B2B Sales" graphic (50 skills in 7 stage folders from ICP and targeting to onboarding and expansion), with every skill title, which installed skills in this workspace already cover each stage, what is gated behind "Comment SALES" and was not obtained, and a safe way to run any of the 50 as a prompt. Use when the user wants the 50-skill list, wants to run a B2B sales step (ICP, prospecting, qualification, discovery, demo, proposal, onboarding) or asks which existing skill covers it.
---

# Claude Skills for B2B Sales (50 skills, 7 folders)

Source: one graphic attached in chat, branded Prosp, mocked as a code editor showing `claude-skills-for-b2b-sales/` with seven numbered folders and `skill-01.md` to `skill-50.md`, closing with "COMMENT SALES". Read 14 October 2026.

**What was and was not obtained.** The graphic shows only titles. No repository link is shown, and the skill files are offered in exchange for a comment, so their contents were not obtained and were not invented. All 50 titles are now written as full skills in this repository (`b2b-sales-01-...` to `b2b-sales-50-...`, with the shared rules in `b2b-sales-standard`). They are original to this repository, not the author's text. Test method and results: `tests/b2b-sales/README.md` and `docs/b2b-sales-skills-test-report.md`. A sibling graphic from the same account (100 lead-gen skills) is in `lead-gen-skill-map-10x10`.

## The 50 titles, by folder

| Folder | Skills |
|---|---|
| 01-icp-targeting (1 to 7) | 01 ICP From Closed-Won, 02 Account Tiering, 03 Lead Scoring Model, 04 Inbound Lead Qualifier, 05 TAM Sanity Check, 06 Disqualifier Writer, 07 Decision-Maker Mapper |
| 02-prospecting (8 to 15) | 08 Prospect Research, 09 Signal-Based Targeting, 10 Cold Email Sequence, 11 Cold Call Opener, 12 LinkedIn Outreach, 13 Cadence Designer, 14 Handoff Detection, 15 Outreach Diagnostic |
| 03-qualification (16 to 22) | 16 Sales Methodology Implementer, 17 MEDDIC Call Prep, 18 BANT Qualifier, 19 Disqualification Check, 20 Buying Committee Mapper, 21 Champion Identifier, 22 Deal Review Framework |
| 04-discovery (23 to 29) | 23 Discovery Question Designer, 24 Asking Effective Questions, 25 Active Listening Coach, 26 Pain Quantifier, 27 Current vs Future State, 28 Call Notes Extractor, 29 Discovery Gap Check |
| 05-demo-evaluation (30 to 35) | 30 Demo Script Builder, 31 Demo Personalizer, 32 Technical Validation, 33 POC Scoper, 34 Competitor Battlecard, 35 Competitor Alternatives |
| 06-proposal-close (36 to 43) | 36 Proposal Writer, 37 Pricing Negotiation, 38 ZOPA Mapper, 39 Objection Handler, 40 Multi-Threading Planner, 41 Closing Plan, 42 Deal Momentum Analyzer, 43 Win-Loss Analysis |
| 07-onboarding-expansion (44 to 50) | 44 Onboarding Plan, 45 First Value Tracker, 46 QBR Builder, 47 Health Score Model, 48 Renewal Predictor, 49 Expansion Revenue Finder, 50 Referral Request |

Counts: 7 + 8 + 7 + 7 + 6 + 8 + 7 = 50. Checked.

## What already exists in this workspace (so you do not need the gated files)

| Stage | Closest installed skills (verify the one you use fits) |
|---|---|
| ICP and targeting | `/icp`, `ideal-customer-profile`, `sales:account-tiering`, `zoominfo:score-leads`, `zoominfo:score-accounts`, `zoominfo:tam-sizer`, `market-sizing-analysis`, `sales:lead-triage` |
| Prospecting | `sales:account-research`, `sales:draft-outreach`, `cold-email`, `outreach-planning`, `outreach-execution`, `linkedin-signal-outreach`, `linkedin-prospecting-8-systems`, `zoominfo:personalize-email` |
| Qualification | `sales-methodologies-20`, `sales:deal-review`, `sales:stakeholder-map`, `zoominfo:buying-committee`, `sales:deal-signals` |
| Discovery | `sales:call-prep`, `sales:call-summary`, `zoominfo:call-recap`, `zoominfo:call-coaching` |
| Demo and evaluation | `sales:competitive-intelligence`, `evermuse:competitive-battlecard`, `competitor-alternatives`, `sales:create-an-asset` |
| Proposal and close | `/proposal-writer`, `sales:close-plan`, `sales:handle-objection`, `zoominfo:mutual-action-plan`, `sales:win-loss-review` |
| Onboarding and expansion | `/cs-onboarding`, `/cs-qbr`, `/cs-renewal`, `churn-prevention`, `sales:renewal-radar`, `sales:expansion-whitespace`, `referrals` |

Related maps already in the repo: `lead-gen-skill-map-10x10`, `claude-sales-by-role`, `claude-sales-prompts-20`, `outbound-sales-system-5stage`.

## How to run one of the 50

0. Preferred: ask for the skill by name, for example `b2b-sales-26-pain-quantifier`, or use `/b2b-sales-skill`. The steps below are the fallback if you only want the short prompt.
1. Name the skill and the stage. Paste only the facts you have: the product, the buyer role, the deal stage, the real notes.
2. Ask for the output with its evidence: every claim about the buyer must point to a line you pasted, or be marked "assumption".
3. Stop before anything is sent. Messages, proposals and prices are drafts for a human to approve.

```
Run B2B sales skill [number and title, e.g. "26 Pain Quantifier"] for this deal. Here is what I know: [paste notes, role, product, deal stage, numbers]. Give: (1) the output for this step, (2) for each claim, the line of my notes that supports it, or "assumption", (3) the three questions I still need to ask, (4) what could be wrong. Do not invent numbers or buyer statements. Do not draft anything to send.
```

## Rules

- Never paste customer personal data you are not allowed to process into a prompt.
- Titles such as "Pricing Negotiation" or "Objection Handler" produce suggestions, not facts about your market.
- The Prosp graphic is marketing for a lead-generation product; no connector or install is needed for anything here.

Command: `/b2b-sales-skill <stage or skill number, and your deal facts>`. Agent: `b2b-sales-stage-router`.
