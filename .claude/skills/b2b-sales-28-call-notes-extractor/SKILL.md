---
name: b2b-sales-28-call-notes-extractor
description: Turn a transcript or raw call notes into structured notes: a short factual summary, exact quotes, numbers, commitments with owners and dates, objections, next steps, open questions and a CRM update draft. Use after any sales call.
---

# 28. Call Notes Extractor

Stage 4 of 7: Discovery. Skill 28 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a transcript or notes and wants consistent, reusable call records.

## Inputs

- Required: the transcript or notes
- Required: the call date and attendees
- Required: the CRM fields to fill, or permission to use a default set
- Optional: the previous call's notes
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Write a summary of at most five sentences, facts only.
2. List exact quotes that carry meaning (needs, objections, decisions). Copy them character for character.
3. List every number mentioned with what it refers to and who said it.
4. List commitments: who promised what, by when. Include the seller's promises.
5. List objections in the buyer's words and whether they were resolved in the call.
6. List next steps with owner and date; if a date was not agreed, write "no date agreed".
7. List open questions the call did not answer.
8. Draft the CRM update from the above only. Label interpretations ("seems enthusiastic") separately as interpretation.

## Output

Use these headings, in this order:

- `## Summary`
- `## Quotes`
- `## Numbers`
- `## Commitments`
- `## Objections`
- `## Next steps`
- `## Open questions`
- `## CRM update draft`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every quote is an exact excerpt of the input.
- Every number appears in the input.
- Interpretations are labelled as such.
- Next steps without an agreed date say so.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not paraphrase inside quotation marks.
- Do not add facts that were not said.
- Do not record sensitive personal details that are not needed for the deal.

## Related

- `b2b-sales-25-active-listening-coach` (skill 25, Active Listening Coach)
- `b2b-sales-29-discovery-gap-check` (skill 29, Discovery Gap Check)
- `sales:call-summary`
- `zoominfo:call-recap`
