---
name: b2b-sales-48-renewal-predictor
description: Assess the likelihood that one customer renews: evidence for and against, stakeholder status, value realised, open risks, commercial facts and a rating with the actions and dates that would improve it. Use 120 days or more before a renewal date.
---

# 48. Renewal Predictor

Stage 7 of 7: Onboarding and expansion. Skill 48 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for one account with a known renewal date.

## Inputs

- Required: the renewal date and contract terms
- Required: evidence of value realised and usage
- Required: stakeholder facts and sponsor status
- Required: open issues and any complaints
- Optional: the health score
- Optional: competitor contact reports
- Optional: budget cycle information
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Compute the days to renewal `[calc: renewal date minus today]`.
2. List evidence for renewal and evidence against, each with its source and date.
3. Check stakeholder status: sponsor in place, sponsor changed, champion silent, procurement involved.
4. Check value: results against the goals the customer set, not just usage.
5. List commercial factors: price change planned, term, notice period, auto-renewal terms.
6. Rate the renewal as likely, uncertain or at risk, using the evidence only. State that a rating is a judgement, not a probability.
7. List actions with owners and dates to strengthen the renewal, and the signs that would change the rating.

## Output

Use these headings, in this order:

- `## Days to renewal`
- `## Evidence for and against`
- `## Stakeholders`
- `## Value realised`
- `## Commercial factors`
- `## Rating`
- `## Actions and dates`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every evidence item has a source and date.
- The rating follows from the evidence.
- No percentage probability is invented.
- Actions have owners and dates.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not assume a renewal because there was no complaint.
- Do not give a percentage without a model and data.
- Do not hide a known risk from the account owner.

## Related

- `b2b-sales-47-health-score-model` (skill 47, Health Score Model)
- `b2b-sales-46-qbr-builder` (skill 46, QBR Builder)
- `b2b-sales-49-expansion-revenue-finder` (skill 49, Expansion Revenue Finder)
- `sales:renewal-radar`
- `/cs-renewal`
