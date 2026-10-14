---
name: b2b-sales-22-deal-review-framework
description: Run a structured review of one deal: verify the stage against exit evidence, check that the next step is dated and agreed by the buyer, list risks, recommend a forecast category with its reason and set questions for the rep. Use in pipeline reviews.
---

# 22. Deal Review Framework

Stage 3 of 7: Qualification. Skill 22 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a manager or the seller wants an honest check of a deal before forecasting it.

## Inputs

- Required: the opportunity record: stage, value, close date, last buyer activity date
- Required: call and email notes
- Required: the stage definitions with exit criteria
- Required: the forecast categories used
- Optional: the competitor, the champion, the procurement status
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. For the stated stage, check each exit criterion against evidence in the notes. Mark met, not met or unknown.
2. Check the next step: does it have an owner, a date and a buyer commitment (not just a seller intention)?
3. Compute days since the last buyer-side activity `[calc: today minus date]`.
4. List risks present: single-threaded, no economic buyer, no compelling event, no agreed process, no dated next step, slipped close date.
5. Recommend a forecast category with the reason. If evidence is thin, recommend the more cautious category.
6. Write five questions for the rep that would change the review if answered.
7. Write what you would expect to see in the next 14 days if the deal is real `[assumption]`.

## Output

Use these headings, in this order:

- `## Stage evidence`
- `## Next-step check`
- `## Days since buyer activity`
- `## Risks`
- `## Forecast category`
- `## Questions for the rep`
- `## What to expect next`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each exit criterion has a verdict and a note reference.
- The next-step check names owner, date and buyer commitment.
- The forecast category follows from the evidence.
- The days-since figure shows its dates.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not upgrade the forecast because the rep is confident.
- Do not count seller activity as buyer progress.
- Do not shame the rep in the written review.

## Related

- `b2b-sales-16-sales-methodology-implementer` (skill 16, Sales Methodology Implementer)
- `b2b-sales-41-closing-plan` (skill 41, Closing Plan)
- `b2b-sales-42-deal-momentum-analyzer` (skill 42, Deal Momentum Analyzer)
- `sales:deal-review`
- `sales:close-plan`
