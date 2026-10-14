---
name: b2b-sales-07-decision-maker-mapper
description: Map who decides, influences, blocks and uses a purchase at one target account from facts the user supplies, show the gaps, and plan how to confirm each role. Use when planning outreach into an account where the buying group is not yet known.
---

# 07. Decision-Maker Mapper

Stage 1 of 7: ICP and targeting. Skill 7 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for one target account, early in prospecting, to decide whom to approach and what to verify.

## Inputs

- Required: the account name and what is being sold
- Required: people already known: name, title, source of that information
- Required: the typical price level of the deal
- Optional: an org chart or notes from a champion
- Optional: the buyer roles seen in past won deals
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each known person with the source of the information. Business facts only.
2. Assign a role (economic buyer, champion, technical evaluator, user, blocker, legal or procurement) only where evidence exists. Otherwise write "unknown".
3. For unfilled roles, list title patterns that often hold them as hypotheses, marked `[assumption]`.
4. Show the gaps: roles needed for this deal size that no one fills.
5. For each gap, propose how to confirm it: ask your champion, read the company's public pages by hand, or ask in the first call. Do not scrape or buy personal data.
6. Sequence the next two conversations: who first, with what question, and why.

## Output

Use these headings, in this order:

- `## People and evidence`
- `## Role map`
- `## Gaps`
- `## How to confirm each gap`
- `## Next two conversations`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every role assignment cites evidence or is marked unknown.
- Hypothesised titles are tagged `[assumption]`.
- The plan contains no scraping or personal-data purchase.
- The next two conversations each have a stated question.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not guess a person's influence from seniority alone.
- Do not store private details such as personal social media.
- Do not contact a named person unless the user decides to.

## Related

- `b2b-sales-20-buying-committee-mapper` (skill 20, Buying Committee Mapper)
- `b2b-sales-21-champion-identifier` (skill 21, Champion Identifier)
- `sales:stakeholder-map`
- `zoominfo:buying-committee`
