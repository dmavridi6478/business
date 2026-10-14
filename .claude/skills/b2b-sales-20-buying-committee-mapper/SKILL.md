---
name: b2b-sales-20-buying-committee-mapper
description: Map the buying committee of a live opportunity: each member's role, stance (supporter, neutral, opponent, unknown) with evidence, concerns, influence, missing members and an engagement plan. Use when a deal involves several stakeholders.
---

# 20. Buying Committee Mapper

Stage 3 of 7: Qualification. Skill 20 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for an active opportunity where more than one person affects the decision.

## Inputs

- Required: the known stakeholders with title and what they have said or done, each with a source
- Required: the deal stage and the product being bought
- Optional: the procurement and legal process, if known
- Optional: organisation chart notes
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each stakeholder with evidence of what they said or did. Business facts only.
2. Assign role and stance only on evidence. Otherwise write "unknown".
3. Record each person's stated concern in their words, or "not yet heard".
4. Rate influence as high, medium or low with the reason (budget control, technical veto, daily user, legal review).
5. Identify missing members: roles that usually take part at this deal size and have not appeared.
6. Write an engagement plan: for each key person, the next contact, the purpose, and the question to ask.
7. Flag single-threading risk: if one contact carries most of the relationship.

## Output

Use these headings, in this order:

- `## Stakeholder table`
- `## Concerns`
- `## Influence`
- `## Missing members`
- `## Engagement plan`
- `## Single-threading risk`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every stance cites evidence or is "unknown".
- Concerns are quoted or marked not yet heard.
- Missing members are listed.
- Every key person has a next contact and question.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not label someone an opponent from tone alone.
- Do not map private lives or personal social media.
- Do not plan to go around the champion without telling the user to decide.

## Related

- `b2b-sales-07-decision-maker-mapper` (skill 7, Decision-Maker Mapper)
- `b2b-sales-21-champion-identifier` (skill 21, Champion Identifier)
- `b2b-sales-40-multi-threading-planner` (skill 40, Multi-Threading Planner)
- `sales:stakeholder-map`
