---
description: 5-stage outbound sales system (prospecting → research → outreach → conversations → pipeline), orchestrating this repo's already-vendored sales skills into one workflow
argument-hint: [stage name, or "run" to go through all 5 stages for one target/ICP]
---

# Outbound Sales System (5 Stages)

Source of the structure: a "50+ Sales Skills Inside Fable 5" promotional
graphic and "The Ultimate Claude LinkedIn Sales Department" carousel — both
lead-generation teasers (comment-to-unlock, no actual prompt/skill content
included in either image). The 5-stage taxonomy underneath is genuinely
useful, so it's rebuilt here as a real, working sequence using skills
**already vendored in this repo** — no content was copied from either
source since neither contained any.

## The 5 stages, mapped to real skills already in this repo

| Stage | Fable 5's file names (naming inspiration only) | This repo's skill that actually does it |
|---|---|---|
| **01 · Prospecting** | `icp-definition.md`, `target-accounts.md`, `decision-makers.md` | `prospecting` (vendored) — define ICP, build a target account list, find/qualify decision-makers |
| **02 · Research** | `account-research.md`, `buying-signals.md`, `personalization-angles.md` | `customer-research` (vendored) — account/prospect research, buying-signal detection, personalization angles |
| **03 · Outreach** | `cold-email.md`, `linkedin-messages.md`, `follow-up-sequences.md` | `cold-email` (vendored) for the first touch; `follow-up-when-no-reply` (this repo, Mo Bunnell's 4-stage cadence) for what happens when they go quiet |
| **04 · Conversations** | `reply-classifier.md`, `objection-handler.md`, `next-steps.md` | `sales-enablement-corey-haines`'s `references/objection-library.md` for objection handling; `sales-enablement` (this repo's own version) for the broader qualification/demo-script layer |
| **05 · Pipeline** | `conversation-analysis.md`, `pipeline-review.md`, `improvement-plan.md` | `revops` (vendored) — lead scoring/routing, pipeline-stage hygiene, marketing-to-sales handoff |

## How to run it

1. **Stage 1 (Prospecting)**: invoke the `prospecting` skill with your ICP
   description to get a qualified target list.
2. **Stage 2 (Research)**: invoke `customer-research` on that list to
   surface buying signals and personalization angles per account.
3. **Stage 3 (Outreach)**: invoke `cold-email` to draft first-touch
   sequences per account, using the research from Stage 2. When a thread
   goes quiet, switch to `/follow-up-when-no-reply` rather than re-running
   `cold-email` — it's a different message shape (re-surface, not re-pitch).
4. **Stage 4 (Conversations)**: once a reply comes in, use
   `sales-enablement-corey-haines`'s objection library to handle pushback
   and `sales-enablement` for demo scripts/next-step recommendations.
5. **Stage 5 (Pipeline)**: use `revops` weekly to review where deals are
   stalling, re-score leads, and decide what to fix in Stage 1-4 before
   the next cycle.

## Plain-text prompt to kick off the full cycle

```
Run the outbound sales system for [ICP DESCRIPTION / TARGET SEGMENT].
Start with prospecting to build a target list, then research each account
for buying signals, then draft the first-touch outreach. Tell me at each
stage what you need from me before moving to the next one.
```

## Not vendored — no real content existed to vendor

Neither source graphic contained actual prompt text, agent instructions,
or skill definitions for its named items ("60 Claude Sales Agents," "100
Claude Sales Prompts," "30 Claude Sales Workflows," "10 Claude Sales
Playbooks" in the LinkedIn Sales Department carousel; the individual
`.md` file contents implied by the Fable 5 terminal screenshot) — both are
"comment SALES/SEND to get it" lead-magnet teasers for a paid or gated
resource. The file/category **names** were useful as an organizing
structure (used above); the counts and claimed contents were not
reproducible and are not represented as real.
