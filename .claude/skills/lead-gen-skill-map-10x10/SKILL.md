---
name: lead-gen-skill-map-10x10
description: A working map of a "100 Claude lead generation skills" library organised as 10 folders of 10 (ICP targeting, signals and triggers, list building, enrichment, scoring, outreach copy, sequences, inbound, qualification, measurement), tied to the skills, agents and connectors already available here. Use when the user wants to build a lead-generation system end to end, find which lead-gen skill covers a step, or turn the folder structure from the Prosp "COMMENT LEAD GEN" graphic into their own library.
---

# Lead generation skill map (10 folders x 10)

Source: a Prosp graphic showing a repo `claude-lead-generation-skills/` with folders `01-icp-targeting` to `10-measurement` (10 skills each, `skill-01.md` onward), a README and a LICENSE, and the call to action "COMMENT LEAD GEN" (image supplied in chat, 12 October 2026).

**Read first.**
- The image shows only the folder names and the first two file names in each. **The contents of the 100 skills are not visible**, and the repo is released through a comment-for-link post from a vendor of a LinkedIn outreach tool. I did not obtain or reproduce them.
- Use the map as an organising scheme. Fill each folder from the skills and connectors you already have, and decide for each step whether a human or a skill does it.
- Outreach carries legal limits: GDPR and ePrivacy for EU contacts, the LinkedIn user agreement for automated messages, CAN-SPAM in the US. Do not automate cold messages to EU individuals without a documented basis.

## The ten folders, mapped

| # | Folder | The question it answers | Skills and agents here | Connectors |
|---|---|---|---|---|
| 01 | ICP targeting | Who is the best customer? | `ideal-customer-profile`, `pmm-positioning:ideal-customer-profile`, `claude-lead-gen` command | HubSpot (won deals), Clay |
| 02 | Signals and triggers | Who is likely to buy now? | `linkedin-signal-outreach`, `event-prospecting`, `zoominfo:company-intent-monitor` | Common Room, Clay, Vibe Prospecting |
| 03 | List building | Which accounts and people? | `os-prospect` agent, `lead-scraper`, `niche-prospecting`, `apollo:prospect` | Vibe Prospecting, Clay, Lusha |
| 04 | Enrichment | What do we know about them? | `company-research`, `lusha:enrich-contact`, `zoominfo:enrich-company` | Clay, Vibe Prospecting, Lusha |
| 05 | Scoring | Who goes first? | `lead-triage`, `zoominfo:score-leads`, `os-qualify` | HubSpot, Sheets |
| 06 | Outreach copy | What do we say? | `cold-email`, `colddm`, `sales-automator`, `brand-voice-enforcement` | Gmail drafts, Taplio |
| 07 | Sequences | In what order, how often? | `outreach-planning`, `lead-nurture` style flows, `follow-up-when-no-reply` | Gmail, Klaviyo |
| 08 | Inbound | How do we answer who finds us? | `os-response`, `speed-to-lead`, `lead-magnets` | HubSpot, Calendly |
| 09 | Qualification | Are they a real buyer? | `os-qualify`, `os-booking`, `sales:call-prep` | Calendly, Fireflies |
| 10 | Measurement | Is it working? | `attribution`, `revops`, `kpi-scorecard` | HubSpot, Supermetrics |

## How to build your own 100

1. Create one folder per row above under `docs/lead-gen/` (only if you want a separate library).
2. For each folder write ten one-page skills of the form: **when to use / inputs / steps / output / stop rule / a human check**.
3. Fill the first three skills of each folder from the repo skills named above; write the rest only when a real task needs them.
4. Every outbound skill ends in a **draft** that a person approves.

## Command

`/lead-gen-map <your offer and target market>` returns the ten-step plan and which existing skill to run at each step.
