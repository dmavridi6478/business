---
name: outreach-list-building
description: Build a targeted, deduplicated outbound contact list from a defined ICP — company sourcing (Apollo/Clay/lemlist-style filters), people sourcing (Sales Navigator/LinkedIn), intent/niche signal sourcing (G2, Product Hunt, review sites), and final list assembly with dedup and CSV formatting. Use once an ICP exists (from outreach-strategy) and the task is turning that definition into an actual list of companies and contacts to reach.
---

# Outreach List-Building

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`company-finder.md`, `people-finder.md`, `niche-data-finder.md`, `list-builder.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same four concerns as one skill.

Runs after `outreach-strategy` (needs the trigger-based ICP and personas as input) and feeds `outreach-copywriting` and `outreach-channels` (the list is what gets messaged). Check `outreach-data-connections` first for which of the tools below are actually wired up in this environment versus need manual export.

## 1. Company sourcing

Filter on the ICP's firmographics *and* triggers from `outreach-strategy` — tools in this space (Apollo, Clay, lemlist-style enrichment) let you combine standard filters (industry, size, geography) with trigger filters (recent funding, headcount growth rate, technology adoption/removal) in one pass. Pull more candidates than needed and let step 4's qualification bar cut the list down, rather than under-filtering and inheriting noise.

## 2. People sourcing

Once companies are selected, find the specific people matching each persona card from `outreach-strategy` — title-match loosely (titles vary by company size/industry) and verify against the persona's actual responsibility, not just title string-matching. Sales Navigator / LinkedIn search operators (boolean title + seniority + function) are the standard tool here; pull multiple contacts per company across different buying-committee roles rather than one contact per account, since B2B outbound rarely converts on a single touchpoint.

## 3. Niche/intent-data sourcing

Review sites (G2, Capterra) and launch platforms (Product Hunt) surface **active intent**, not just fit — a company leaving a review for a competitor, or a persona upvoting/commenting on a relevant Product Hunt launch, is a stronger trigger than firmographic fit alone. Treat this as a supplementary trigger source layered onto step 1's ICP, not a replacement for it.

## 4. List assembly: dedup + qualify + format

Before this list goes anywhere: dedupe on email domain + name (catches near-duplicates that exact-match dedup misses), verify email deliverability where the source doesn't already guarantee it, and drop any contact that fails a basic ICP/persona sanity check even if the source tool included them. Output as a clean CSV with consistent columns (company, contact name, title, verified trigger, source) — the trigger column matters downstream, since `outreach-copywriting`'s first-touch skill needs the specific signal to reference, not just a generic company name.

## What this skill does NOT do

- Message anyone — that's `outreach-channels`.
- Decide the ICP — that's `outreach-strategy`'s job; this skill executes against a given ICP, it doesn't define one.
- Guarantee data accuracy from third-party sources — flag stale or unverifiable data rather than passing it through silently.

## Related skills in this repo

- **outreach-strategy**: supplies the ICP/trigger definitions and persona cards this skill filters against.
- **outreach-data-connections**: check which sourcing tools are actually connected in this environment before assuming a step here can run end-to-end.
- **outreach-copywriting** / **outreach-channels**: consume the finished list, including the trigger column used for personalization.
- **outreach-automation**: the `website-scraper` capability there can supplement sourcing when a target isn't covered by the standard tools.
