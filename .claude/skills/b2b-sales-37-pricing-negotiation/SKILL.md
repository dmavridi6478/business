---
name: b2b-sales-37-pricing-negotiation
description: Prepare a pricing negotiation: the user's walk-away point and goals, what to trade, the buyer's likely asks, concession rules (get something for everything), scripts for common requests and the exact limits of what the seller may offer. Use before negotiating price or terms.
---

# 37. Pricing Negotiation

Stage 6 of 7: Proposal and close. Skill 37 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has pricing authority limits and a buyer has asked for a discount or different terms.

## Inputs

- Required: the price list and the approved discount authority
- Required: the user's walk-away point
- Required: what the buyer has asked for
- Required: what the buyer values, from discovery
- Optional: the buyer's budget statement
- Optional: the competing quote, if the buyer shared it
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. State the user's goals and walk-away point exactly as supplied.
2. List what is tradeable and what is not (term length, payment timing, volume, scope, reference rights, case study).
3. For each buyer ask, write a response that trades rather than gives: "if we do X, can you do Y?".
4. Set concession rules: order, size and a record of each concession `[calc: total concession against list]`.
5. Write scripts for three common requests: a discount, a longer payment term and a price match.
6. List what not to concede and what needs approval from someone else.
7. Prepare for silence and for the buyer's walk-away. Do not invent urgency.

## Output

Use these headings, in this order:

- `## Goals and limits`
- `## Tradeable items`
- `## Responses to asks`
- `## Concession rules`
- `## Scripts`
- `## Approvals needed`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Concessions never exceed the supplied authority.
- Each concession is paired with a request in return.
- Total concession is computed against list price.
- No false deadline or scarcity appears.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not invent a competing offer or an expiry.
- Do not give away the walk-away point.
- Do not negotiate against the buyer's stated budget without evidence.

## Related

- `b2b-sales-38-zopa-mapper` (skill 38, ZOPA Mapper)
- `b2b-sales-36-proposal-writer` (skill 36, Proposal Writer)
- `b2b-sales-39-objection-handler` (skill 39, Objection Handler)
- `sales:handle-objection`
