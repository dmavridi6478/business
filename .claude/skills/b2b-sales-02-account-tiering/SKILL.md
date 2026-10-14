---
name: b2b-sales-02-account-tiering
description: Sort a list of target accounts into tiers (1:1, 1:few, 1:many) using fit and timing criteria taken from the ICP, then size the effort per tier against real capacity. Use when the user has more target accounts than time to work them.
---

# 02. Account Tiering

Stage 1 of 7: ICP and targeting. Skill 2 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when there is an account list and an ICP or fit criteria, and the user must decide where to spend limited selling time.

## Inputs

- Required: account list with the attributes the criteria need
- Required: the ICP statement or fit criteria
- Required: capacity: number of sellers and hours per week available for outreach
- Optional: dated intent or timing signals with their source
- Optional: deal value estimates
- Optional: existing relationship notes
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Restate the fit criteria exactly as supplied; do not add new ones.
2. Score each account 0, 1 or 2 per criterion (0 fails, 1 partial, 2 clear) and cite the input value behind each score. Use "unknown" where the data is missing.
3. Add timing points only for signals that have a date and a source from the inputs; treat undated signals as unknown.
4. State the tier rule in one sentence before applying it (for example total score and number of 2s).
5. Assign tiers. Tier 1 gets individual research and multi-threaded contact; Tier 2 gets semi-custom outreach; Tier 3 gets templated outreach.
6. Check capacity: accounts per tier times planned touches per week must not exceed available hours `[calc: ...]`. Move overflow down a tier and say so.
7. List accounts with too many unknowns separately as "unscored"; do not tier them by guess.

## Output

Use these headings, in this order:

- `## Criteria used`
- `## Tier rule`
- `## Tiered list`
- `## Effort plan by tier`
- `## Capacity check`
- `## Unscored accounts`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every score cites an input value or says "unknown".
- The tier rule is stated before the tiers appear.
- The capacity arithmetic is shown and respected.
- Unscored accounts are listed, not tiered.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not infer intent from company size or funding alone.
- Do not put more accounts in Tier 1 than capacity allows.
- Do not rank by gut feeling and then invent scores to match.

## Related

- `b2b-sales-01-icp-from-closed-won` (skill 1, ICP From Closed-Won)
- `b2b-sales-03-lead-scoring-model` (skill 3, Lead Scoring Model)
- `sales:account-tiering`
- `zoominfo:score-accounts`
