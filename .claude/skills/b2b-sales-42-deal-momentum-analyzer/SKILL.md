---
name: b2b-sales-42-deal-momentum-analyzer
description: Measure whether a deal is moving: dated buyer and seller activities, time between steps, stalled stages, slipped dates and a verdict of accelerating, steady, slowing or stalled with the evidence. Use when a deal feels slow or before a forecast call.
---

# 42. Deal Momentum Analyzer

Stage 6 of 7: Proposal and close. Skill 42 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has dated activity for the deal and the stage history.

## Inputs

- Required: a dated log of activities, marked buyer-side or seller-side
- Required: the stage history with dates
- Required: the close date history
- Optional: the median stage durations from the user's won deals
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Separate buyer-side activity (replies, meetings attended, documents shared, introductions) from seller-side activity. Only buyer-side counts as progress.
2. Compute the days between buyer-side activities and the days in the current stage `[calc: date differences]`.
3. Compare the current stage duration with the user's own won-deal stage durations, if supplied. Use no outside benchmark.
4. Count how many times the close date moved and by how much `[calc]`.
5. Give a verdict: accelerating, steady, slowing or stalled, with the evidence behind it.
6. List the three most useful actions to restart or verify momentum, such as a direct question about the decision timeline.
7. State what would change the verdict.

## Output

Use these headings, in this order:

- `## Activity log`
- `## Intervals and stage duration`
- `## Close date history`
- `## Verdict`
- `## Actions`
- `## What would change the verdict`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Buyer-side and seller-side activity are separated.
- Every interval shows its two dates.
- The verdict follows from the numbers.
- No external benchmark is used unless supplied.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not count seller emails as momentum.
- Do not call a deal healthy because the last meeting was friendly.
- Do not compare with industry averages.

## Related

- `b2b-sales-22-deal-review-framework` (skill 22, Deal Review Framework)
- `b2b-sales-41-closing-plan` (skill 41, Closing Plan)
- `b2b-sales-19-disqualification-check` (skill 19, Disqualification Check)
