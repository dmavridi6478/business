---
name: b2b-sales-17-meddic-call-prep
description: Prepare the next call on a deal using MEDDICC (metrics, economic buyer, decision criteria, decision process, identified pain, champion, competition): current map, call objective, questions, agenda draft and evidence to capture. Use before a qualification or follow-up call.
---

# 17. MEDDIC Call Prep

Stage 3 of 7: Qualification. Skill 17 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a call is scheduled and the deal facts so far are available.

## Inputs

- Required: deal facts and notes so far
- Required: the next call's attendees, date and purpose
- Optional: the previous call's notes
- Optional: the competitor names known
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Fill the MEDDICC map from the facts with evidence or "unknown". Use these seven elements: metrics, economic buyer, decision criteria, decision process, identified pain, champion, competition.
2. Choose the three elements this call should advance. Explain the choice from the gaps.
3. Write open questions per chosen element, in neutral wording. No leading questions.
4. Draft a short agenda the buyer could agree to, with times. Label it "draft, needs approval".
5. List the evidence to capture during the call (quotes, numbers, names, dates).
6. List risks: who may be missing from the call, what could derail it, and the fallback.

## Output

Use these headings, in this order:

- `## Current MEDDICC map`
- `## Call objective`
- `## Questions by element`
- `## Agenda draft`
- `## Evidence to capture`
- `## Risks`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The map shows "unknown" for unsupported elements.
- Exactly the three chosen elements have questions.
- Questions are open, not leading.
- The agenda is marked draft.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not assume the person on the call is the economic buyer.
- Do not ask the buyer to quantify a number you would invent.
- Do not write a script of what the buyer will say.

## Related

- `b2b-sales-16-sales-methodology-implementer` (skill 16, Sales Methodology Implementer)
- `b2b-sales-26-pain-quantifier` (skill 26, Pain Quantifier)
- `b2b-sales-22-deal-review-framework` (skill 22, Deal Review Framework)
- `sales:call-prep`
