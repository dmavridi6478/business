---
name: b2b-sales-18-bant-qualifier
description: Qualify an opportunity on budget, authority, need and timeline with evidence and unknowns, recommend continue, pause or exit, and state what BANT does not cover. Use for a quick, honest first-pass qualification.
---

# 18. BANT Qualifier

Stage 3 of 7: Qualification. Skill 18 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use early in a deal, when the user needs a fast read and knows BANT's limits.

## Inputs

- Required: the facts and notes on the opportunity
- Optional: the price range of the offer
- Optional: previous deals' typical timelines
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. For each of the four elements, record the status: confirmed by the buyer, implied, or unknown. Quote the note that supports it.
2. Budget: distinguish "has money" from "approved for this". Do not infer from company size.
3. Authority: say who decides, and whether you have met that person or only heard of them.
4. Need: write it in the buyer's words if quoted; otherwise mark it as the seller's reading.
5. Timeline: look for an event that sets it (a contract end, a regulation, a launch) rather than a vague "this quarter".
6. Recommend continue, pause or exit with the reason, and list the two questions that would most change the recommendation.
7. State what BANT misses here (for example competition, buying process, champion) and point to the skill that covers it.

## Output

Use these headings, in this order:

- `## BANT table`
- `## Recommendation`
- `## Questions that would change it`
- `## What BANT does not cover`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each element has a status and a quote or "unknown".
- Budget is not inferred from size.
- The recommendation cites the evidence.
- Gaps outside BANT are named.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not disqualify on a single "unknown".
- Do not treat a stated budget as an approved one.
- Do not use BANT alone for complex deals.

## Related

- `b2b-sales-17-meddic-call-prep` (skill 17, MEDDIC Call Prep)
- `b2b-sales-19-disqualification-check` (skill 19, Disqualification Check)
- `b2b-sales-20-buying-committee-mapper` (skill 20, Buying Committee Mapper)
