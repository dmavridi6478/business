---
name: b2b-sales-08-prospect-research
description: Build a one-page, sourced research brief on one prospect company and role from public information the user supplies or approves fetching: company facts, role facts, triggers, relevance hooks, gaps and a draft opener. Use before the first outreach to an account.
---

# 08. Prospect Research

Stage 2 of 7: Prospecting and outreach. Skill 8 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for one account and one role, when the user wants facts with sources instead of guesses.

## Inputs

- Required: the target company and role
- Required: what the user sells and the value it delivers
- Required: the sources to use: pasted text, URLs, or permission to search public business pages
- Optional: the ICP
- Optional: past conversations with the account
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Collect facts and record each with its source and date. Public business information only.
2. Classify each fact: company fact, role fact, or trigger event (change that creates a reason to talk).
3. Discard private or personal information and anything older than the user's relevance window; say what you discarded and why.
4. Pick two or three relevance hooks. Each hook must link one cited fact to one specific thing the user's product does.
5. List what is unknown and how a call could find it out.
6. Draft one opener based on the strongest hook. Label it "draft, needs approval". No flattery and no claim about the prospect's feelings.

## Output

Use these headings, in this order:

- `## Sources`
- `## Company facts`
- `## Role facts`
- `## Triggers`
- `## Relevance hooks`
- `## Gaps`
- `## Draft opener`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every fact has a source and a date.
- Every hook cites the fact it rests on.
- No personal or private information about an individual appears.
- The opener contains no claim that is not in the facts list.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not scrape or compile personal profiles.
- Do not infer financial position, health or private life.
- Do not pretend familiarity ("saw you on...") unless the user supplied that fact.

## Related

- `b2b-sales-09-signal-based-targeting` (skill 9, Signal-Based Targeting)
- `b2b-sales-07-decision-maker-mapper` (skill 7, Decision-Maker Mapper)
- `sales:account-research`
- `zoominfo:account-research`
