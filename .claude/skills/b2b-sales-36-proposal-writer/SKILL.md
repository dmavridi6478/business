---
name: b2b-sales-36-proposal-writer
description: Write a proposal draft from agreed facts: the buyer's problem in their words, the solution scope, outcomes and measures agreed, timeline, responsibilities, investment lines supplied by the user, assumptions and next steps. Use when a buyer has asked for a proposal after discovery and evaluation.
---

# 36. Proposal Writer

Stage 6 of 7: Proposal and close. Skill 36 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when discovery notes, an agreed scope and the user's approved prices exist.

## Inputs

- Required: the buyer's problem and success measures in their words
- Required: the agreed scope and deliverables
- Required: the prices and terms approved by the user
- Required: the decision process and dates
- Optional: the pain quantification the buyer confirmed
- Optional: the proof of concept results
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Open with the problem and the success measures the buyer confirmed, quoting their wording.
2. Describe the solution as scope and deliverables, not as a feature list.
3. State the outcomes and how they will be measured. Use only numbers the buyer confirmed or the user approved.
4. Lay out the timeline and each side's responsibilities.
5. Write the investment section using only the prices and terms supplied. Do not invent discounts.
6. List assumptions and what is excluded.
7. Close with the decision process, the dates, and the next step. Label the whole document "draft, needs approval".

## Output

Use these headings, in this order:

- `## Problem and measures`
- `## Solution scope`
- `## Outcomes and measurement`
- `## Timeline and responsibilities`
- `## Investment`
- `## Assumptions and exclusions`
- `## Decision process and next step`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every number comes from the inputs or is tagged.
- Prices match the approved ones exactly.
- Exclusions are stated.
- The draft label is present.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not include a claim the buyer did not confirm.
- Do not invent a discount or a deadline.
- Do not promise outcomes the product cannot guarantee.

## Related

- `b2b-sales-26-pain-quantifier` (skill 26, Pain Quantifier)
- `b2b-sales-33-poc-scoper` (skill 33, POC Scoper)
- `b2b-sales-37-pricing-negotiation` (skill 37, Pricing Negotiation)
- `/proposal-writer`
