---
name: b2b-sales-26-pain-quantifier
description: Quantify the cost of a buyer's stated problem using only buyer-supplied numbers: cost drivers, a transparent formula, a low and high range, hard versus soft costs, and the questions that would fill gaps. Use when a buyer describes a problem but no number has been agreed.
---

# 26. Pain Quantifier

Stage 4 of 7: Discovery. Skill 26 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a discovery conversation produced a problem statement and some figures, and the seller wants a business case the buyer can confirm.

## Inputs

- Required: the buyer's own statements about the problem, with any numbers they gave
- Required: the process or activity affected
- Optional: the buyer's ranges (low and high)
- Optional: the team size and loaded cost per hour, if the buyer gave them
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Name the cost drivers: time lost, errors, delays, lost revenue, risk events, tool or labour spend.
2. For each driver, write the formula (frequency times cost per occurrence) and mark which inputs the buyer supplied.
3. For missing inputs, write the question to ask the buyer. Do not fill them with your own numbers; if an illustration is needed, label it `[assumption]` and keep it out of the totals.
4. Compute the annual cost `[calc: ...]` as low, base and high using the buyer's ranges.
5. Separate hard costs (money, hours) from soft costs (morale, reputation) and exclude soft costs from totals.
6. Check for double counting: the same hour or error must not appear in two drivers.
7. Write a one-line summary in the buyer's own words for the buyer to confirm or correct.

## Output

Use these headings, in this order:

- `## Cost drivers`
- `## Formulas and inputs`
- `## Annual cost range`
- `## Hard and soft costs`
- `## Questions to fill gaps`
- `## Summary to confirm`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every input is buyer-supplied or tagged `[assumption]` and kept out of totals.
- Each total shows its formula.
- Low, base and high are shown.
- Double counting is checked and stated.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not present a seller-built number as the buyer's.
- Do not use benchmark "industry averages" you cannot cite.
- Do not count soft costs in the total.

## Related

- `b2b-sales-23-discovery-question-designer` (skill 23, Discovery Question Designer)
- `b2b-sales-27-current-vs-future-state` (skill 27, Current vs Future State)
- `b2b-sales-36-proposal-writer` (skill 36, Proposal Writer)
- `b2b-sales-37-pricing-negotiation` (skill 37, Pricing Negotiation)
