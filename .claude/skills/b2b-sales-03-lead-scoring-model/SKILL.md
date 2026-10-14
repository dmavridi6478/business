---
name: b2b-sales-03-lead-scoring-model
description: Build a transparent, rule-based lead scoring model (fit points, behaviour points, decay, thresholds) from past conversion data and a plan to test it on held-out leads. Use when the user wants to prioritise leads from their own history.
---

# 03. Lead Scoring Model

Stage 1 of 7: ICP and targeting. Skill 3 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has historical leads with outcomes. With fewer than 50 leads or fewer than 10 conversions, say the model is a hypothesis and give a manual checklist instead.

## Inputs

- Required: historical leads, one row each, with attributes, behaviours (with dates) and whether the lead converted
- Required: the definition of "converted" and the time window used
- Optional: lead source cost
- Optional: sales capacity per week
- Optional: current informal scoring rules
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Check data size: at least 50 leads and 10 conversions. If not, stop at a manual checklist and say why.
2. Split by time: the earliest 70% of leads train the model, the latest 30% test it `[calc: counts]`. Do not shuffle.
3. For each attribute value in the training set, compute the conversion rate and the lift against the overall rate. Ignore values with fewer than 10 leads.
4. Turn lift into whole-number points: larger lift, more points; no negative points unless a value is a clear disqualifier.
5. Score behaviours (pricing page, demo request, reply) with a decay: points halve after N days, where N comes from the data or is tagged `[assumption]`.
6. Set thresholds from the training set (hot, warm, cold) and say what action each triggers.
7. Evaluate on the test set: of the leads above the hot threshold, how many converted, and what share of all converted leads fell in that group. Report counts, not just rates.
8. Describe how to monitor drift: re-run quarterly and compare the top bucket's conversion with the rest.

## Output

Use these headings, in this order:

- `## Data check`
- `## Attribute lift table`
- `## Scoring rules`
- `## Thresholds and routing`
- `## Test results`
- `## Monitoring plan`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The train/test split is by time and its counts are shown.
- No rule rests on fewer than 10 leads.
- Test results are counts with the denominators.
- The model is called a hypothesis when the data size is below the minimum.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not claim predictive accuracy from the training data.
- Do not use protected personal characteristics as scoring inputs.
- Do not hide a weak test result.

## Related

- `b2b-sales-01-icp-from-closed-won` (skill 1, ICP From Closed-Won)
- `b2b-sales-04-inbound-lead-qualifier` (skill 4, Inbound Lead Qualifier)
- `zoominfo:score-leads`
- `sales:lead-triage`
