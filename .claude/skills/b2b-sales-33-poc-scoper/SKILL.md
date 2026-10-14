---
name: b2b-sales-33-poc-scoper
description: Scope a proof of concept: measurable success criteria set by the buyer, in and out of scope, timeline, responsibilities on both sides, data and security needs, a decision commitment agreed before the start, risks and exit criteria. Use before agreeing to a pilot or trial.
---

# 33. POC Scoper

Stage 5 of 7: Demo and evaluation. Skill 33 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a buyer asks for a pilot, trial or proof of concept.

## Inputs

- Required: the buyer's problem and what would convince them
- Required: the product capabilities the proof will use
- Required: the resources each side can commit
- Optional: the data the proof needs and its sensitivity
- Optional: a target decision date
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Write the objective in one sentence, in the buyer's terms.
2. Write success criteria that are measurable, agreed by the buyer and set before the start. If the buyer has not given a number, ask; do not invent one.
3. List in-scope and out-of-scope items explicitly.
4. Build the plan with dates and weekly checkpoints.
5. Assign responsibilities on both sides, including who provides data and access.
6. Write the decision commitment: who decides, by when, and what happens if the criteria are met (for example proceed to contract). A proof without this is a free trial.
7. List risks (data access, availability of people, scope creep) and the exit criteria for stopping early.

## Output

Use these headings, in this order:

- `## Objective`
- `## Success criteria`
- `## Scope in and out`
- `## Plan and dates`
- `## Responsibilities`
- `## Decision commitment`
- `## Risks and exit criteria`
- `## Assumptions and what could be wrong`

Plan dates are relative (week 1, week 2) unless the user supplied calendar dates.

## Quality checks

The output fails if any of these is false:

- Each success criterion is measurable and attributed to the buyer.
- A decision commitment is stated.
- Out-of-scope items are listed.
- No number is invented.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not start a proof without agreed criteria.
- Do not let scope grow without a written change.
- Do not use real customer data without a data agreement.

## Related

- `b2b-sales-32-technical-validation` (skill 32, Technical Validation)
- `b2b-sales-36-proposal-writer` (skill 36, Proposal Writer)
- `b2b-sales-41-closing-plan` (skill 41, Closing Plan)
- `sales:close-plan`
