---
name: b2b-sales-39-objection-handler
description: Handle a buyer's stated objection: classify it (misunderstanding, missing information, real concern, price, timing, authority, stall), restate it in the buyer's words, give questions that find the root, a truthful response and a check that it landed. Use when a buyer raises a concern in a call or email.
---

# 39. Objection Handler

Stage 6 of 7: Proposal and close. Skill 39 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for a specific objection quoted from the buyer, with the deal context.

## Inputs

- Required: the objection, quoted from the buyer
- Required: the deal context: stage, stakeholders, what has been agreed
- Optional: facts the user can cite to answer it (documents, customer results the user can share)
- Optional: the buyer's earlier concerns
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Quote the objection exactly and classify it: misunderstanding, missing information, real concern, price, timing, authority or stall.
2. Restate it in the buyer's words to confirm you understood. Draft the restatement.
3. Write two or three questions that find the root ("what would need to be true for this to work for you?").
4. Write a truthful response using only supplied facts. If the objection is correct, say so and describe what the user can offer.
5. Write a check that the response landed ("does that answer it?").
6. If the objection cannot be resolved with the facts at hand, write the follow-up: what to find out and by when.
7. Record the objection and outcome for the deal notes.

## Output

Use these headings, in this order:

- `## Objection and class`
- `## Restatement`
- `## Questions to find the root`
- `## Response`
- `## Check`
- `## Follow-up and record`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The objection is quoted exactly.
- The response contains no claim outside the supplied facts.
- A real concern is acknowledged, not argued away.
- A check question is included.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not argue with the buyer.
- Do not invent a case study or statistic.
- Do not push past a clear "no".

## Related

- `b2b-sales-24-asking-effective-questions` (skill 24, Asking Effective Questions)
- `b2b-sales-37-pricing-negotiation` (skill 37, Pricing Negotiation)
- `b2b-sales-34-competitor-battlecard` (skill 34, Competitor Battlecard)
- `sales:handle-objection`
