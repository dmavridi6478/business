---
name: b2b-sales-12-linkedin-outreach
description: Draft a short connection note and up to two follow-ups for one prospect from facts the user supplies, in line with platform rules and with a stop rule. Use when prospecting on LinkedIn by hand.
---

# 12. LinkedIn Outreach

Stage 2 of 7: Prospecting and outreach. Skill 12 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use for one prospect when the user will send the messages manually.

## Inputs

- Required: the prospect's role and company
- Required: one cited, public reason to connect
- Required: what the user offers or shares
- Optional: mutual context the user truly has
- Optional: a useful resource to share
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Write a connection note that states who you are and the one real reason you are connecting. Keep it short; check LinkedIn's current note-length limit yourself.
2. Write a first follow-up after acceptance that offers something useful (an insight, resource or question) without a pitch.
3. Write a second follow-up only if the user wants one, with a different angle and an easy way to decline.
4. State the stop rule: no further messages after the second follow-up or any request to stop.
5. Remind the user: automation, scraping and bulk tools may breach the platform's terms; send by hand.
6. Mark all messages "draft, needs approval".

## Output

Use these headings, in this order:

- `## Connection note`
- `## First follow-up`
- `## Second follow-up`
- `## Stop rule`
- `## Platform and privacy notes`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The connection reason is supplied and public.
- No message pitches before acceptance.
- A stop rule is stated.
- The platform-terms reminder is present.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not invent mutual connections or shared events.
- Do not recommend automation tools that breach terms.
- Do not reuse private information.

## Related

- `b2b-sales-08-prospect-research` (skill 8, Prospect Research)
- `b2b-sales-13-cadence-designer` (skill 13, Cadence Designer)
- `linkedin-signal-outreach`
- `linkedin-prospecting-8-systems`
