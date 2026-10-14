---
name: b2b-sales-46-qbr-builder
description: Build a quarterly business review from the customer's goals and supplied data: goals versus results, usage and value delivered, issues, roadmap items the customer asked for (only those the user can discuss), and recommendations with the customer's decision requests. Use before a customer review meeting.
---

# 46. QBR Builder

Stage 7 of 7: Onboarding and expansion. Skill 46 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has the customer's goals and this quarter's data.

## Inputs

- Required: the customer's goals from the sale or the last review
- Required: this quarter's results and usage data
- Required: open issues and requests
- Optional: last quarter's review
- Optional: the customer's stakeholders and their interests
- Optional: the contract renewal date
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Open with the customer's goals in their words.
2. Show goals versus results using only supplied numbers; compute changes `[calc: this quarter versus last]`.
3. Show value delivered, separated into what the data proves and what the customer reports.
4. List issues and how each was handled, honestly, including those not resolved.
5. List the customer's requests and the user's status for each. Do not promise roadmap items; label unconfirmed items as such.
6. Write three recommendations with the evidence for each and the decision you need from the customer.
7. Write a one-page agenda and a short pre-read as drafts needing approval.

## Output

Use these headings, in this order:

- `## Customer goals`
- `## Goals versus results`
- `## Value delivered`
- `## Issues`
- `## Requests and status`
- `## Recommendations and decisions needed`
- `## Agenda and pre-read`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- All numbers come from the supplied data or are calculated and tagged.
- Unresolved issues are shown.
- No roadmap promise is made.
- Every recommendation names a decision.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not present usage as value without the customer's goals.
- Do not hide bad quarters.
- Do not use another customer's results as comparison without permission.

## Related

- `b2b-sales-45-first-value-tracker` (skill 45, First Value Tracker)
- `b2b-sales-47-health-score-model` (skill 47, Health Score Model)
- `b2b-sales-48-renewal-predictor` (skill 48, Renewal Predictor)
- `/cs-qbr`
