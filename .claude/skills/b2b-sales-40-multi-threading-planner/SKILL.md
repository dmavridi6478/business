---
name: b2b-sales-40-multi-threading-planner
description: Plan how to build relationships with several stakeholders in a deal: who to reach, in what order, with what purpose and value for them, how to do it with the champion's knowledge, and the risk if the deal stays single-threaded. Use when one contact carries the deal.
---

# 40. Multi-Threading Planner

Stage 6 of 7: Proposal and close. Skill 40 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a live deal depends on one contact and the user knows (or can list) the other stakeholders.

## Inputs

- Required: the stakeholder list with roles and sources
- Required: the deal stage and the champion, if any
- Required: the timeline to the decision
- Optional: the buyer's internal process for approvals
- Optional: existing relationships the seller has
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Show the current thread count: how many stakeholders have had real contact with the seller `[calc]`.
2. List the stakeholders needed to close this deal size and mark which have not been reached.
3. For each unreached stakeholder, write the purpose of the contact and the value for that person.
4. Order the contacts: sequence them so each is made with the champion's knowledge or help where possible. Do not go around the champion without telling the user to decide.
5. Write the first message for each as a draft needing approval.
6. Name the risk if the deal stays single-threaded, in terms of what could stop it.
7. Set a review date.

## Output

Use these headings, in this order:

- `## Current threads`
- `## Stakeholders needed`
- `## Contact plan`
- `## Draft messages`
- `## Single-thread risk`
- `## Review date`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The thread count shows its basis.
- Each unreached stakeholder has a purpose and value.
- The champion is considered in the sequence.
- Messages are labelled drafts.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not bypass the champion silently.
- Do not contact people the user has not chosen.
- Do not use private contact details.

## Related

- `b2b-sales-20-buying-committee-mapper` (skill 20, Buying Committee Mapper)
- `b2b-sales-21-champion-identifier` (skill 21, Champion Identifier)
- `b2b-sales-41-closing-plan` (skill 41, Closing Plan)
- `sales:stakeholder-map`
