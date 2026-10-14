---
name: b2b-sales-35-competitor-alternatives
description: Map the alternatives a buyer may choose, including doing nothing, an in-house build, spreadsheets and adjacent categories: the job each does, when each is the better choice, switching costs and an honest positioning, with the evidence still needed. Use when preparing for a buyer who is comparing options.
---

# 35. Competitor Alternatives

Stage 5 of 7: Demo and evaluation. Skill 35 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the buyer has said or the user suspects the buyer is considering other routes, not just named competitors.

## Inputs

- Required: the buyer's problem and context
- Required: the alternatives known or suspected
- Required: what the user's product does and does not do
- Optional: the buyer's stated criteria
- Optional: win and loss notes
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List every alternative, starting with "do nothing" and "build it ourselves", then spreadsheets or manual work, adjacent tools and named competitors.
2. For each, state the job it does for the buyer.
3. State when each alternative is the better choice. Be honest, including when it is the user's own product that is not the best fit.
4. State the switching costs for the buyer: data, retraining, contracts, risk.
5. Write a positioning for the user's product against each: one sentence from the buyer's perspective.
6. List the evidence still needed for each claim and where to get it.

## Output

Use these headings, in this order:

- `## Alternatives`
- `## Job each does`
- `## When each wins`
- `## Switching costs`
- `## Positioning`
- `## Evidence needed`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- "Do nothing" and "build in-house" are included.
- Each alternative has a case where it wins.
- Positioning is from the buyer's perspective.
- Claims needing evidence are listed.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not treat only named competitors as the alternatives.
- Do not claim superiority without evidence.
- Do not hide when the product is a poor fit.

## Related

- `b2b-sales-34-competitor-battlecard` (skill 34, Competitor Battlecard)
- `b2b-sales-27-current-vs-future-state` (skill 27, Current vs Future State)
- `competitor-alternatives`
