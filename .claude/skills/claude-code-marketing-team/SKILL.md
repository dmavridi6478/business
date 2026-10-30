---
name: claude-code-marketing-team
description: A marketing team of 50 specialist roles in 10 departments (market intelligence, strategy and positioning, SEO and search, content, social and LinkedIn, demand generation, email and lifecycle, conversion, analytics and insights, marketing operations) coordinated by one orchestrator that turns goals into results, with the full roster, a routing table and the rules that keep draft-only work behind a human gate. Implemented as 10 department agents (mkt-*) plus the /marketing-team command. Use when a marketing goal spans several functions, when someone asks "who on the team does X", or to delegate a campaign end to end as drafts. Source - "Claude Code Marketing Team" org chart infographic (full book gated behind a comment keyword; role descriptions below are the one-liners printed on the chart).
---

# Claude Code marketing team - 10 departments x 5 roles

**Design decision.** The source shows 50 sub-agents. Fifty separate agent files would add 50 descriptions to every session's context for little gain, since each role is a one-line brief. This repo implements **one department agent per column (10)**, each carrying its five role briefs, and the main-session command `/marketing-team` acts as the CEO/orchestrator. To get a single role, ask the department agent to "act as `role-name`". If you later need 50 files, they can be generated from this roster.

## Roster (role - job as printed)

| Department (agent) | Roles |
|---|---|
| Market intelligence (`mkt-market-intelligence`) | market-research - analyse markets, trends, opportunities; icp-research - detailed ideal customer profiles; competitor-intel - track and analyse competitors; customer-insights - customer feedback and pain points; trend-analysis - emerging trends and market shifts |
| Strategy and positioning (`mkt-strategy-positioning`) | marketing-strategy - go-to-market strategies and 90-day plans; positioning - positioning and differentiation; messaging - key messages and brand narratives; offer-strategy - compelling offers and value propositions; brand-strategy - brand strategy and guidelines |
| SEO and search (`mkt-seo-search`) | keyword-research - high-value keywords and search opportunities; content-gap - content gaps and clustering; onpage-seo - optimise for search intent and rankings; technical-seo - technical issues and fixes; link-building - internal linking strategies and opportunities |
| Content (`mkt-content`) | content-strategy - calendars and topics; content-brief - detailed briefs; longform-content - in-depth articles and guides; content-editor - edit and improve existing content; repurposing - turn content into multiple formats across channels |
| Social and LinkedIn (`mkt-social-linkedin`) | social-strategy - social and LinkedIn strategies; linkedin-posts - high-performing LinkedIn posts; hook-creator - scroll-stopping hooks and angles; thought-leadership - thought-leadership content; social-repurposing - posts, threads and carousels from content |
| Demand generation (`mkt-demand-gen`) | campaign-strategy - multi-channel campaigns; lead-magnets - high-value lead magnets; distribution - content and campaign distribution; nurture-campaigns - nurture sequences and follow-ups; audience-growth - grow and engage your audience |
| Email and lifecycle (`mkt-email-lifecycle`) | email-strategy - email and lifecycle strategies; newsletter - plan and write newsletters; email-copy - high-converting email copy; lifecycle - automated lifecycle sequences; email-optimisation - analyse performance and improve results |
| Conversion (`mkt-conversion`) | landing-page - create and optimise landing pages; cta-analysis - analyse and improve conversion rates; cta-optimiser - write and test high-converting CTAs; funnel-analysis - analyse funnels and find drop-offs; experiment-design - organise tests and conversion experiments |
| Analytics and insights (`mkt-analytics-insights`) | data-analyst - analyse marketing data; campaign-analysis - assess campaign performance; content-performance - content performance and ROI; reporting - clear reports and dashboards; analysis-optimisation - areas for improvement and growth |
| Marketing operations (`mkt-marketing-ops`) | workflow-architect - design workflows and processes; systems-integration - set up tools, MCP connections and automation; marketing-qa - review and quality-check outputs; documentation - marketing docs and playbooks; marketing-systems - organise assets, folders and knowledge bases |

## Orchestration (what `/marketing-team` does)

1. Read the goal; ask once for anything missing (audience, offer, deadline, channel, success number).
2. Load the context files if present: `docs/marketing-context/{voice,proof,banned,pillars}.md`. If `proof.md` is empty, no claim may be made.
3. Route to at most **three** departments using this table, in order:

| Goal type | Departments (in order) |
|---|---|
| Launch or campaign | market intelligence -> strategy -> demand gen -> content/social |
| Organic growth | SEO -> content -> social |
| Pipeline from existing leads | email/lifecycle -> conversion -> analytics |
| "What is working?" | analytics -> conversion |
| New market or segment | market intelligence -> strategy |
| Process or tooling | marketing ops |

4. Run departments one after another, passing each output to the next as input.
5. Send every customer-facing draft to the existing `brand-reviewer` agent; return only PASS drafts, with FAIL reasons listed.
6. Close with an **approval list**: what must be approved by a human, what was not measured, and what each claim's proof row is.

## Rules (shared by all department agents)

- **Draft only.** No agent sends, publishes, schedules, spends or edits a live system. Output goes to chat or a file in `data/` or `docs/`.
- State the role being used at the top of every output.
- No invented numbers, quotes, customers or competitor facts. Unknown = "not measured" or "[proof needed]".
- Use connected sources only when connected (Ahrefs, Semrush, HubSpot, Clay, Klaviyo, Supermetrics, Amplitude, Fireflies, Canva, Gamma are); say "not connected" otherwise.
- Greek-language outputs keep original product and place names; no punctuation in capital letters.

## Relationship to existing assets

`governed-marketing-team` (6 specialists + gates) is the stricter pipeline for single pieces of content; this team is for planning and multi-function work. Individual role depth lives in the existing skills: `content-strategy`, `ai-seo`, `cold-email`, `cro`, `analytics`, `positioning`, `linkedin-virality-playbook`.

## Keywords
marketing team, sub-agents, org chart, department agents, orchestrator, 50 roles, Claude Code

## Claude marketing setup: 6 steps, 7 commands, about 15 minutes (Batch 113)

Source: "Claude Marketing Setup" graphic (Muhammad Ayan), also in the uploads as an animated GIF. Labels FREE and PRO are from the graphic; check current plan terms.

| Setup step | Do |
|---|---|
| 01 Project (free) | Name it Marketing |
| 02 Brand files (free) | A guide plus your 5 best posts |
| 03 Memory (free) | Settings > Memory |
| 04 Connectors (free) | Canva, HubSpot, Notion |
| 05 Plugin (pro) | Install in Cowork |
| 06 Your voice (pro) | `/brand-review` one post |

| Stage | Command | Example on the graphic |
|---|---|---|
| 01 Plan (start here) | `/campaign-plan` | 200 signups, 6 weeks: channels, calendar, KPIs |
| 01 Plan | `/competitive-brief` | Compare us vs [Rival]: where rivals are weak |
| 02 Create | `/draft-content` | LinkedIn post, launch: a draft in your brand voice |
| 02 Create | Claude Design | 3 graphics on brand; visuals and decks |
| 03 Grow | `/email-sequence` | Onboarding, 5 emails |
| 03 Grow | `/seo-audit` | yoursite.com, 1 keyword: content gaps and page fixes |
| 04 Check | `/brand-review` | Paste any draft: line-by-line voice fixes |
| 04 Check | `/performance-report` | Connect HubSpot or paste: what to double down on |

Those commands match the `marketing:*` plugin skills (`marketing:campaign-plan`, `competitive-brief`, `draft-content`, `email-sequence`, `seo-audit`, `brand-review`, `performance-report`) that are available in this environment, so nothing new was built. Drafts only; the human publishes. Connectors (HubSpot, Canva, Notion) are authorised by the user in claude.ai connector settings.


See also (Batch 124): `claude-marketing-department-48`, a catalogue of a 48-item Claude marketing repository (titles only; contents unverified) mapped to the skills in this library.
