---
name: b2b-sales-15-outreach-diagnostic
description: Diagnose an underperforming outbound programme from funnel counts and message samples: compute stage rates, find the weakest stage, list hypotheses with the evidence each needs, and choose one test. Use when reply or meeting rates are low.
---

# 15. Outreach Diagnostic

Stage 2 of 7: Prospecting and outreach. Skill 15 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has counts for sent, delivered, replied, positive replies and meetings, plus samples of messages and the list source.

## Inputs

- Required: counts by step for a stated period: sent, delivered, replied, positive replies, meetings
- Required: samples of the messages sent
- Required: the source and age of the contact list
- Optional: bounce and spam-complaint counts
- Optional: open data (note that open tracking is unreliable)
- Optional: previous periods for comparison
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Compute stage-to-stage rates `[calc: n/N]` and show the funnel.
2. Compare only with the user's own earlier periods. Use no outside benchmark unless the user supplies one, and name it.
3. Find the largest drop and the stage it belongs to: deliverability, targeting, message, offer or follow-up.
4. For that stage, list hypotheses and the evidence that would confirm or reject each (for example bounce rate for list quality, reply content for offer fit).
5. Choose one test that changes one variable, with the sample size needed to see a difference and the caution that small samples mislead.
6. List what not to change at the same time.

## Output

Use these headings, in this order:

- `## Funnel`
- `## Weakest stage`
- `## Hypotheses and evidence needed`
- `## One test`
- `## What not to change`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every rate shows its counts.
- Comparisons use the user's own data or a named supplied benchmark.
- Exactly one test is recommended.
- Open rates are not treated as proof of reading.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not blame copy before ruling out list quality and deliverability.
- Do not change several things at once.
- Do not quote industry benchmarks from memory.

## Related

- `b2b-sales-10-cold-email-sequence` (skill 10, Cold Email Sequence)
- `b2b-sales-13-cadence-designer` (skill 13, Cadence Designer)
- `b2b-sales-09-signal-based-targeting` (skill 9, Signal-Based Targeting)
