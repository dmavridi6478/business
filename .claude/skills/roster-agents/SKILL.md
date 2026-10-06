---
name: roster-agents
description: Catalogues of named Claude agent roles from five social infographics - 100 LinkedIn agents (10 departments), 200 GTM agents (10 categories, backed by ten real gtm-* subagents), 100 lead-generation agents, the 45-agent Claude Revenue System, and the Prosp 200 LinkedIn agents matrix (5 verticals x 4 divisions). Use to pick the right specialist role for a LinkedIn, outbound, sales or retention task, to see which existing agent already covers it, or to turn a role name into a working prompt. The source images list NAMES only; behaviour here is written, not copied.
---

# Roster agents

**What this is.** A lookup of named agent roles, plus ten working department agents. The five source images (Interview Guidelines.zip, Oct 2026) are lead-magnet graphics: each says "comment X for free access", and the prompts sit behind that gate. The infographics contain no prompts, so nothing here is a copy of anyone's prompt pack.

**Honest limits.**
- Names were read from 800 px images. A word may differ from the original. GTM-200 has 199 names: category 09 shows 19 (the 20th was not recoverable). Lead-gen-100 lists "74" twice in the original; renumbered here.
- Revenue-45 repeats some names across groups in the original (e.g. Account Health Monitor, Churn Risk Identifier). Kept as read.
- Prosp-200 agent slugs are set in a tiny monospace font and are not legible; only its structure (5 verticals x 4 divisions x 10 agents) is recorded. Its own entry prompt was "Build me a list for this role." - use that.
- 200 agents is a catalogue size, not a quality signal. Most tasks need one or two roles.

## Data

`catalogs.json` (same folder). Keys: `linkedin-100`, `gtm-200`, `leadgen-100`, `revenue-45`, `prosp-200`, `linkedin-to-gtm-agent`. Regenerate everything with `python3 scripts/build_roster_agents.py`.

## The ten working agents (gtm-200)

| # | Agent file | Covers |
|---|---|---|
| 01 | `gtm-icp-research` | ICP, personas, TAM/SAM/SOM, pain-point and language research |
| 02 | `gtm-content-distribution` | Content strategy, posts, carousels, lead magnets, newsletters |
| 03 | `gtm-demand-generation` | Ads, campaigns, DM sequences, A/B tests, referral programme design |
| 04 | `gtm-sales-conversion` | Scripts, objections, discovery, MEDDIC, proposals, battlecards |
| 05 | `gtm-retention-expansion` | Onboarding, churn risk, NPS, renewals, win-back, referrals |
| 06 | `gtm-signals-triggers` | Job changes, hiring spikes, funding, engagers, signal-to-message |
| 07 | `gtm-profile-authority` | Headline, About, Featured, company page, point-of-view posts |
| 08 | `gtm-dm-conversations` | Welcome DMs, question ladder, soft pitch, revival, inbox triage |
| 09 | `gtm-engagement-network` | Comments, creator lists, collabs, invite hygiene, network quality |
| 10 | `gtm-pipeline-analytics` | Attribution, reply/show/close rates, bottlenecks, weekly review |

All ten are **draft-only**: tools Read, Grep, Glob, Write; no connectors; output to `data/agent-drafts/`; a Prompt Defense Baseline that treats profile, DM and web text as data. They read `docs/marketing-context/proof.md` so claims trace to proof, and write `[NEEDS PROOF]` otherwise.

## LinkedIn-100 -> which agent covers it

Profile & Positioning, Post Writing -> `gtm-profile-authority`; Content Strategy, Visual & Media -> `gtm-content-distribution`; Engagement & Comments, Networking & Relationships -> `gtm-engagement-network`; Outreach & DMs -> `gtm-dm-conversations`; Lead Generation -> `gtm-icp-research` (+ `os-prospect`); Analytics & Reporting, Operations & Management -> `gtm-pipeline-analytics`.

## Lead-gen-100 and Revenue-45 -> existing coverage

These overlap the repo's `os-*` agents. Use those where they exist: `os-prospect` (lists), `os-qualify` (lead qualification), `os-response` (inbound), `os-followup`, `os-booking`, `os-close`, `os-email-sms` (sequences), `os-seo`, `os-health`, `os-referral`. For roles with no agent, use the prompt template below.

## Turn any role name into a working prompt (copy and paste)

```
Act as the [ROLE NAME] from the [LinkedIn-100 | GTM-200 | Lead-Gen-100 | Revenue-45] roster. Context: my business is [WHAT YOU SELL], my buyer is [ICP], my offer is [OFFER], my proof is [CASE STUDIES OR NUMBERS - or "none yet"]. Task: [WHAT YOU NEED]. Rules: use only facts I gave you; write [NEEDS PROOF] where a claim has no evidence; output a draft I can review in two minutes, not an essay; nothing is sent or posted by you. End with a list of what you assumed.
```

## Use

`/roster-agent <catalog> <role name or number> [task]` - looks the role up and routes it. See `.claude/commands/roster-agent.md`.

## Keywords
LinkedIn agents, GTM agents, lead generation agents, revenue system, Prosp, sales agents, SDR, roster
