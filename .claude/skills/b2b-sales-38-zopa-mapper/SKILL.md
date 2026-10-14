---
name: b2b-sales-38-zopa-mapper
description: Map the zone of possible agreement: the seller's reservation point, the buyer's inferred reservation range from evidence, overlap or gap, and the moves that could create overlap (scope, terms, timing, risk). Use when price and budget seem far apart.
---

# 38. ZOPA Mapper

Stage 6 of 7: Proposal and close. Skill 38 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the seller knows the walk-away point and has some evidence of the buyer's budget and priorities.

## Inputs

- Required: the seller's reservation point (lowest acceptable terms)
- Required: what the buyer has said about budget, constraints and priorities, with sources
- Optional: the buyer's alternatives (including doing nothing)
- Optional: the buyer's approval limits
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. State the seller's reservation point exactly and the target.
2. Infer the buyer's range from evidence only. Give a low and a high, tagged `[assumption]` with the evidence behind each; if none exists, say the range is unknown and list questions to learn it.
3. Compare the ranges `[calc: overlap or gap in currency]`.
4. If there is overlap, show where in the zone a good agreement lies and how to reach it.
5. If there is a gap, list moves that could change the zone: scope, terms, timing, risk sharing, volume, non-price value.
6. Name the buyer's best alternative to a deal and how it limits their range.
7. List what to learn before the next conversation.

## Output

Use these headings, in this order:

- `## Seller range`
- `## Buyer range with evidence`
- `## Overlap or gap`
- `## Moves to create overlap`
- `## Buyer's alternatives`
- `## What to learn next`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The buyer's range is evidenced or marked unknown.
- The overlap or gap is computed and shown.
- Moves are non-price as well as price.
- The seller's reservation point is not disclosed in any buyer-facing text.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not guess the buyer's budget from company size.
- Do not recommend deception about your reservation point.
- Do not share this map with the buyer.

## Related

- `b2b-sales-37-pricing-negotiation` (skill 37, Pricing Negotiation)
- `b2b-sales-26-pain-quantifier` (skill 26, Pain Quantifier)
- `b2b-sales-41-closing-plan` (skill 41, Closing Plan)
