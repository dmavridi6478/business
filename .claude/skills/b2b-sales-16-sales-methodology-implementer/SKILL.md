---
name: b2b-sales-16-sales-methodology-implementer
description: Apply a named sales methodology (for example MEDDICC, BANT, SPICED, Challenger or Sandler) to one deal: fill its elements with evidence, grade the evidence, list gaps and choose next actions. Use when a team wants a methodology used on a real deal instead of described in the abstract.
---

# 16. Sales Methodology Implementer

Stage 3 of 7: Qualification. Skill 16 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user names a methodology and has deal facts. Definitions of these methods vary between teams, so use the user's element list if given.

## Inputs

- Required: the methodology name, and the user's own element list if it differs from the common one
- Required: the deal facts and notes so far
- Optional: the stage definitions
- Optional: the deal value and close date
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. State the element list you will use and say the definitions vary; ask the user to correct it if theirs differs.
2. Fill each element with what the deal facts show, quoting the note. Write "unknown" where there is no evidence.
3. Grade the evidence for each element: stated by the buyer, observed by the seller, or seller belief only.
4. List the gaps: elements that are unknown or rest on seller belief.
5. Choose at most three elements to advance next and say why those three.
6. Write the next actions per chosen element: who, what, by when, and what evidence would close the gap.
7. Note where the methodology does not fit this deal instead of forcing the facts into it.

## Output

Use these headings, in this order:

- `## Element list used`
- `## Element map`
- `## Evidence grades`
- `## Gaps`
- `## Priorities`
- `## Next actions`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every filled element quotes a note or says unknown.
- Each element has an evidence grade.
- No more than three priorities are chosen.
- A methodology mismatch is stated when it exists.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not mark an element complete on seller belief.
- Do not reproduce a vendor's proprietary training text.
- Do not invent buyer statements.

## Related

- `b2b-sales-17-meddic-call-prep` (skill 17, MEDDIC Call Prep)
- `b2b-sales-18-bant-qualifier` (skill 18, BANT Qualifier)
- `sales-methodologies-20`
- `sales:deal-review`
