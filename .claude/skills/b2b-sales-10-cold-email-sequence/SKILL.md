---
name: b2b-sales-10-cold-email-sequence
description: Draft a four-step cold email sequence for one persona, each step with a distinct purpose, plus a compliance checklist and a test plan. Use when the user needs outbound email copy that is honest and lawful.
---

# 10. Cold Email Sequence

Stage 2 of 7: Prospecting and outreach. Skill 10 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for one persona and one offer, when the user will review and send the emails themselves.

## Inputs

- Required: the persona (role and company type)
- Required: the offer and one concrete outcome
- Required: proof the user can cite: real customer results supplied by the user
- Required: sender name, company and postal address
- Required: the sending region
- Optional: signals that justify timing
- Optional: the user's previous best-performing email
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Define one goal for the sequence (for example a 20-minute call) and one ask per email.
2. Give the four steps distinct jobs: 1 relevance, 2 proof, 3 a different angle or a useful resource, 4 close the loop politely.
3. Write each email under 120 words with a plain subject line. No fake "Re:" or "Fwd:", no invented urgency, no invented personalisation.
4. Use proof only from the inputs, quoted exactly. If none was supplied, write the email without proof and say so.
5. Add sender identification and an opt-out line to each email.
6. Space the steps in days and state the stop rule: stop on any reply, bounce or opt-out.
7. Write the compliance checklist: lawful basis and local rules for business email in the region (these differ by country; flag for counsel review), suppression list, no purchased personal data without a lawful basis.
8. Give a test plan: one variable at a time, with a note that small samples prove little.

## Output

Use these headings, in this order:

- `## Goal and persona`
- `## Sequence`
- `## Compliance checklist`
- `## Test plan`
- `## Assumptions and what could be wrong`

Sequence: four drafts, each with day, subject, body and the one ask. Label each "draft, needs approval".

## Quality checks

The output fails if any of these is false:

- Each email has exactly one ask.
- No customer, statistic or quote appears that was not supplied.
- Every email carries sender identity and an opt-out line.
- The compliance checklist says rules vary by region and need counsel review.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not fake a previous conversation.
- Do not use deceptive subject lines.
- Do not claim results the user cannot document.

## Related

- `b2b-sales-08-prospect-research` (skill 8, Prospect Research)
- `b2b-sales-13-cadence-designer` (skill 13, Cadence Designer)
- `cold-email`
- `sales:draft-outreach`
