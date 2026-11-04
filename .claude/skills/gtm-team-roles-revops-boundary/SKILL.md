---
name: gtm-team-roles-revops-boundary
description: Defines the four roles of a modern go-to-market team (GTM engineer, RevOps, SDR, account executive) with responsibilities and typical tools, and the boundary between RevOps and GTM on who owns the CRM - what starts and ends each side's work, how fast it changes, what breaks it, the pipeline-with-gates versus weekly-loop build patterns, and each side's scorecard. Includes two runnable workflows - the RevOps gated pipeline and the GTM weekly loop. Use when designing or auditing a GTM team, resolving "who owns this field or alert", or setting up weekly outbound and pipeline hygiene routines. Run via /gtm-team-roles, /gtm-weekly-loop and /revops-gate-check. Sources - "The Modern GTM Team Setup" (Muhammad Ahmad) and "RevOps vs GTM - Who Owns The CRM?" (Guerlain Nerestan).
---

# GTM team roles and the RevOps / GTM boundary

Sources: two infographics. Tool names are the authors' examples, not an endorsement or a tested stack.

## 1. Four roles

| Role | Responsibilities | Tools shown |
|---|---|---|
| GTM engineer | ICP modelling, data orchestration, signal tracking, TAM mapping, lead allocation, outbound campaigns | Claude Code (MCP-powered GTM terminal), n8n, Instantly, HeyReach, Snowflake, Freckle (CRM enrichment), Ocean.io (lookalike lists), Apollo (TAM mapping), Clay (data orchestration) |
| RevOps | Tech stack evaluation, inbound orchestration, revenue forecasting, CRM workflows, CRM admin, SDR enablement | Ergo (revenue automation), HubSpot, Freckle, Chili Piper (scheduling and routing), Intercom, Snowflake, Amplitude |
| SDRs | Appointment setting, discovery, cold calling, qualification, multi-threading, social selling | Nooks (parallel dialer), Findymail (email finding), Loom (video outreach), Apollo (sequencing, list building), BetterContact (waterfall phone enrichment) |
| Account executives | Product demo, discovery, business-case building, closing, multi-threading, negotiation | Claude (follow-up emails), Superhuman (email), Ergo (assistant), Qwilr (proposals and e-signatures), Nooks |

## 2. Who owns the CRM - where work splits and collides

| Dimension | RevOps | GTM |
|---|---|---|
| Starts with | A record change | A buying signal |
| Ends with | A clean, routed record | A live sequence |
| Change pace | Changed with sign-off | Tweaked every week |
| Breaks when | A rep skips a field | Data goes stale |
| Stack shown | Default, Salesforce, Fivetran, BigQuery, HubSpot, Ergo, DealHub, Omni, QuotaPath, Zapier | Exa, UserGems, Vector, Clay, FullEnrich, Octave, Unify, Instantly, Gojiberry, n8n |
| What pings them | #revops-help: forecast will not tie out; deal stuck 45 days; lead sent to wrong rep | #outbound-alerts: bounce rate over 5%; inbox flagged as spam; signal feed went quiet |
| What they build | **A pipeline with gates**: lead matched -> rep routed -> stage checked -> forecast rolled up | **A loop that ships weekly**: signal -> enrich -> write -> send |
| Scorecard | Forecast variance, speed-to-lead, pipeline coverage, close-date slippage | Positive reply rate, signal-to-meeting rate, cost per meeting, inbox placement |

Shared layer in the source: **MCP - every tool, one agent.** Collision rule: GTM may write to the CRM only through fields and objects RevOps has approved; RevOps may not change sequences. Decide the interface in writing (field list, owner, change process).

## 3. Workflow A - RevOps gated pipeline (`/revops-gate-check`)

Four gates, each with a pass condition, an owner and a stop action:

| Gate | Pass condition | If it fails |
|---|---|---|
| 1 Lead matched | Lead is matched to an account; duplicate check done | Hold in queue, alert #revops-help |
| 2 Rep routed | Owner assigned by rule; speed-to-lead timer running | Escalate to RevOps after the SLA |
| 3 Stage checked | Required fields complete for the stage; deal not stuck beyond N days (source example: 45) | Block stage change; ask rep |
| 4 Forecast rolled up | Close dates and amounts valid; variance vs last week computed | Exclude record; list it in the weekly exceptions |

Weekly output: the four scorecard numbers, the three oldest stuck deals, the count of records that failed each gate.

## 4. Workflow B - GTM weekly loop (`/gtm-weekly-loop`)

1. **Signal** - collect this week's signals (job change, funding, site visit, content engagement); say which feeds were quiet.
2. **Enrich** - add firmographics and verified contact data; drop rows without a lawful basis or a verified address.
3. **Write** - draft messages per segment using approved proof only (`docs/marketing-context/proof.md`).
4. **Send** - **human approval gate and a stated send cap before anything leaves**; check bounce rate (alert above 5%) and inbox placement first.
5. **Review** - the four scorecard numbers vs last week; change one variable next week.

Never run Send unattended. Reuse `gtm-outbound-engine`, `outbound-campaign-brief`, `scripts/clean_leads.py`.

## Connector status (19 Oct 2026)

Connected: HubSpot, Clay, Vibe Prospecting, Slack, Zapier, Amplitude, Notion, Fireflies. Available but not connected: Apollo.io, Outreach, RocketReach, Intercom, Snowflake, n8n. No connector found: HeyReach, Instantly, Smartlead, Nooks, Chili Piper, Freckle, Ergo, Qwilr.

Pairs with: `ai-gtm-maturity-levels`, `gtm-stack-20person-b2b`, `revops`, `claude-sales-by-role`, `gtm-six-levels-strategy`.

## Keywords
GTM engineer, RevOps, SDR, account executive, CRM ownership, gated pipeline, weekly loop, scorecard

## GTM is eight parts (Batch 113)

Source: "GTM isn't a role. It's eight parts", a wheel from the GTM Operating System (GTM Partners). The eight parts: Total Relevant Market; Market Investment Map; Brand and Demand; Pipeline Velocity; Customer Time-to-Value; Customer Expansion; Revenue Operations; Leadership and Management. The caption says a great GTM engineer mostly moves Revenue Operations.

Use: when someone asks to "hire a GTM person", check which of the eight parts is actually weak; revenue operations is one wedge, not the whole wheel. Related: `gtm-six-levels-strategy`, `revops`.
