---
name: b2b-sales-04-inbound-lead-qualifier
description: Qualify one inbound lead from its form fields and message into a route (sales now, nurture, redirect, reject) using explicit criteria, and draft the reply for approval. Use when a new inbound lead, form submission or demo request arrives.
---

# 04. Inbound Lead Qualifier

Stage 1 of 7: ICP and targeting. Skill 4 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for a single inbound submission when the user needs a consistent decision and a draft response.

## Inputs

- Required: the lead submission: form fields and message text
- Required: the qualification criteria or ICP
- Required: the routing options and any response-time targets
- Optional: the existing customer list to check duplicates
- Optional: the product's price floor
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Extract facts from the submission and tag each with its source: form field or message.
2. Check each criterion as pass, fail or unknown, citing the fact. Never infer budget or authority from the company name or title alone.
3. Detect non-buyer types: student, job seeker, vendor pitching you, existing customer needing support, competitor research. Say which, with the cue.
4. Choose the route by the stated rules: sales now, nurture, redirect to the right team or resource, or polite decline.
5. Draft a reply that matches the route, uses only facts the lead gave, and asks at most two questions to resolve unknowns. Label it "draft, needs approval".
6. Note any personal data in the submission that should not be copied into other systems.

## Output

Use these headings, in this order:

- `## Facts extracted`
- `## Criteria check`
- `## Route and reason`
- `## Draft reply`
- `## Questions to ask`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every fact is tagged with its source.
- Unknown criteria are shown as unknown, not as pass.
- The reply contains no claim the lead did not make and no invented product detail.
- At most two questions are asked in the draft.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not promise a response time, price or feature in the draft.
- Do not add the lead to a mailing list without a lawful basis.
- Do not score on the sender's name, nationality or gender.

## Related

- `b2b-sales-03-lead-scoring-model` (skill 3, Lead Scoring Model)
- `b2b-sales-06-disqualifier-writer` (skill 6, Disqualifier Writer)
- `sales:lead-triage`
- `salesforce-for-sales:lead-triage`
