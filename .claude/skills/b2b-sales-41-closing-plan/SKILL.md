---
name: b2b-sales-41-closing-plan
description: Build a mutual closing plan: the steps from now to signature with owners and dates on both sides, approvals needed, legal and procurement steps, risks and the buyer's confirmation. Use when a deal is approaching a decision.
---

# 41. Closing Plan

Stage 6 of 7: Proposal and close. Skill 41 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the buyer has shown intent to buy and the remaining steps must be made explicit.

## Inputs

- Required: the agreed scope and price status
- Required: the buyer's approval, legal, security and procurement steps if known
- Required: the target decision and start dates, with who set them
- Optional: the proposal
- Optional: the champion's view of the internal calendar
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Work backwards from the target date set by the buyer, not by the seller.
2. List every step to signature: evaluation sign-off, security review, legal review, procurement, budget approval, signature, kick-off. Mark each known or unknown.
3. Assign an owner on each side and a date for each step. Where the date is unknown, write the question to ask.
4. List dependencies and what could delay each.
5. Write the plan as a shared document the buyer can edit. Draft it for approval.
6. List the risks to the date and the early-warning signs.
7. Write the confirmation message asking the buyer to review and correct the plan.

## Output

Use these headings, in this order:

- `## Target and basis`
- `## Steps with owners and dates`
- `## Unknowns and questions`
- `## Risks and early warnings`
- `## Shared plan draft`
- `## Confirmation message`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The target date is attributed to the buyer.
- Every step has an owner and a date or a question.
- Risks have early-warning signs.
- The plan is labelled a draft.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not invent an end-of-quarter deadline for the buyer.
- Do not skip legal or security steps.
- Do not treat the plan as agreed until the buyer confirms.

## Related

- `b2b-sales-33-poc-scoper` (skill 33, POC Scoper)
- `b2b-sales-36-proposal-writer` (skill 36, Proposal Writer)
- `b2b-sales-42-deal-momentum-analyzer` (skill 42, Deal Momentum Analyzer)
- `sales:close-plan`
