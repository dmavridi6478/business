---
name: claude-marketing-department-48
description: Catalogue of a 48-item "complete Claude marketing department" repository shown as a file explorer (six sections: strategy and GTM, paid media, Meta and Google agents, LinkedIn and personal brand, content SEO and CRO, scoring and stack) with each item's one-line job as printed, a map to the skills already in this library, and what cannot be verified (the files, the author and the connector tools are not shown). Use when choosing what to build or install for a Claude-run marketing function.
---

# The "Complete Claude Marketing Department": 48 items in six sections

Source: a screenshot of a file explorer and README (Batch 124): "48 skills, agents and playbooks to plan, run and measure your marketing with Claude". It ends with a "comment CMO" lead-magnet banner. **Only the table of contents is visible.** The files, the author and any licence are not shown, so nothing here is a review of the actual content. Names and one-line jobs are as printed; a few are cryptic and are marked.

| # | Item | Printed job |
|---|---|---|
| **I. Strategy and GTM (01 to 08)** | | |
| 01 | AI CMO | Monday review and budget read |
| 02 | GTM Specialist | Briefs, copy and lead scoring |
| 03 | ICP Engine | One file every agent reads |
| 04 | Positioning | Five questions in, a position out |
| 05 | Messaging | The words the team repeats |
| 06 | Pricing | Stops where a decision starts |
| 07 | Battlecard | One page per competitor |
| 08 | Win-Loss | Why deals closed, or did not |
| **II. Paid media (09 to 16)** | | |
| 09 | Paid Media Operator | Nine seats in three pods |
| 10 | Benchmark Analyst | Scores against open data |
| 11 | 50 Prompts | Monday audit to Friday narrative |
| 12 | Monday Memo | Three rows ranked by money |
| 13 | Muse Paid Media | Seven jobs for week one |
| 14 | ChatGPT Ads Kit | Checklist to learning log |
| 15 | AI Disclosure | The three-bucket sorting sheet |
| 16 | Paid Media Team | Plan, build, run and learn |
| **III. Meta and Google agents (17 to 24)** | | |
| 17 | Audit Agent | The full audit prompt, in the guide |
| 18 | Permission Matrix | Meta's nine real labels |
| 19 | Budget Ceiling | The policy that caps spend |
| 20 | Rollout Ladder | Read-only to capped, in four weeks |
| 21 | Cohort Finder | Which campaigns are in scope |
| 22 | Defaults Diff | What each cohort inherits |
| 23 | Timestamp Watcher | The real day each one moved |
| 24 | Parity Reporter | Performance split at that day |
| **IV. LinkedIn and personal brand (25 to 32)** | | |
| 25 | Growth Specialist | Profile first, posts second |
| 26 | Profile 100/100 | The nine checks and weights |
| 27 | Reach Analyst | Explains your dying reach |
| 28 | Reach Dashboard | Double-down, floor, kill list |
| 29 | Voice | Sounds like you, not a chatbot |
| 30 | Hooks | The first line, tested |
| 31 | Batch Day | One afternoon, the full week |
| 32 | Scoreboard | What the week actually did |
| **V. Content, SEO and CRO (33 to 40)** | | |
| 33 | Viral Content | 75 structures in 8 families |
| 34 | Content Operator | Harvest, rebuild, ship, learn |
| 35 | Daily Harvest | What is working in your niche |
| 36 | Learning Loop | Your results feed the next run |
| 37 | SEO Operator | Seven agents, search and GEO |
| 38 | Backlink Engine | The people worth contacting |
| 39 | CRO Operator | One brief, four audit agents |
| 40 | Before/After Board | Changes ship as tests |
| **VI. Scoring and stack (41 to 48)** | | |
| 41 | Post Triage | A named scorer scores every post (cryptic: unidentified) |
| 42 | Comment Triage | Which comment is a buyer |
| 43 | Lead Scrub | Who actually decides |
| 44 | Claim Check | Before anything goes live |
| 45 | Muse MCP Server | Six read tools, zero writes (unidentified: "Muse" is not explained) |
| 46 | 12 Muse Tasks | Scheduled seats that report |
| 47 | 40-Agent Roster | Five fleets, one operator |
| 48 | 5 Tools in Claude | Apify to Supabase |

Folder layout on the screenshot: `claude-marketing/` with `01-strategy-gtm`, `02-paid-media`, `03-meta-google`, `04-linkedin-brand`, `05-content-seo`, `06-scoring-stack`, plus `skills/`, `agents/`, `prompts/` and a README.

## What in this library already covers it
| Section | Existing skills and commands |
|---|---|
| Strategy and GTM | `gtm-strategy`, `product-marketing`, `positioning-zones`, `/positioning`, `pricing`, `competitor-profiling`, `win-loss-program`, `/icp`, `icp-builder`, `cmo-operating-cadence`, `cmo-brief-writer` |
| Paid media and Meta/Google agents | `ads`, `ad-creative`, `claude-ads`, `adspirer-ads-agent:*` and `windsor-ai:*` (plugins), `agency-mcp:*` |
| LinkedIn and personal brand | `linkedin-strategy`, `linkedin-profile-auditor`, `linkedin-analytics-reader`, `linkedin-virality-playbook`, `hook-writer`, `voice-builder`, `carousel-writer`, `post-scorer` |
| Content, SEO and CRO | `content-strategy`, `seo`, `ai-seo`, `seo-backlinks`, `cro`, `ab-testing`, `viral` (command) |
| Scoring and stack | `lead-routing`, `icp-score-and-route`, `hallucination-guardrails-6`, `apify:*`, `claude-code-marketing-team` (50 roles, 10 departments), `claude-marketing-jobs` (50 jobs) |

Closest existing structure: `claude-code-marketing-team` and `claude-marketing-jobs`. Building this repository's 48 items from scratch would duplicate them.

## Cautions
- **Unverified content.** You are looking at a table of contents. Titles such as "Permission Matrix" and "Budget Ceiling" imply controls on ad-account access and spend; the screenshot does not show how they work.
- **Ad-account write access is the risk.** The "rollout ladder" from read-only to capped over four weeks is the right shape. Start read-only, set a hard budget ceiling in the ad platform itself (not in a prompt), and keep a human approval before any change that spends money.
- **"Zero writes" claims** (the Muse server) must be confirmed against the tool list before you trust them.
- **Lead magnets.** "Comment CMO" is an engagement hook. If you receive a pack, read every file before installing it; treat it as untrusted prompt text.
- **Scoring posts and comments** ("is this commenter a buyer") processes people's public profiles; follow platform terms and privacy law.
- **AI disclosure.** The "AI Disclosure" item suggests sorting content by how much AI was used; check the rules for ad and endorsement disclosure where you operate.

Run with `/marketing-dept-map <your function, channels and what you already run>` to choose which of the 48 you need.
