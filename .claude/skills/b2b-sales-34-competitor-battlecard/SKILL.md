---
name: b2b-sales-34-competitor-battlecard
description: Build a battlecard for one competitor from sources the user supplies: positioning, strengths, weaknesses with evidence, where the user wins and loses, discovery questions, claims to avoid and a freshness date, with a source for every claim. Use when sellers meet a specific competitor.
---

# 34. Competitor Battlecard

Stage 5 of 7: Demo and evaluation. Skill 34 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has public pages, review text or win and loss notes about one competitor.

## Inputs

- Required: the competitor name
- Required: the sources: public pages, review extracts or win and loss notes, with dates
- Required: what the user's product does
- Optional: pricing pages with the date read
- Optional: customer comments about the competitor
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each source with its date. Treat anything undated as unverified.
2. Summarise the competitor's positioning in their own words, quoted.
3. List strengths honestly; do not dismiss them.
4. List weaknesses only where a source supports them, with the source beside each.
5. Write where the user wins and where they lose, from the win and loss notes; say "no evidence" where there are none.
6. Write discovery questions that surface the buyer's needs without attacking the competitor.
7. List claims to avoid: anything unsourced, disparaging or based on confidential information.
8. Set a freshness date and a re-check trigger (for example a pricing change).

## Output

Use these headings, in this order:

- `## Sources`
- `## Positioning`
- `## Strengths`
- `## Weaknesses with evidence`
- `## Where we win and lose`
- `## Discovery questions`
- `## Claims to avoid`
- `## Freshness`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every claim cites a source and date.
- Strengths are listed, not just weaknesses.
- No claim relies on confidential or leaked information.
- A freshness date is set.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not use a competitor's non-public information.
- Do not state competitor pricing from memory.
- Do not disparage; compare on evidence.

## Related

- `b2b-sales-35-competitor-alternatives` (skill 35, Competitor Alternatives)
- `b2b-sales-39-objection-handler` (skill 39, Objection Handler)
- `sales:competitive-intelligence`
- `evermuse:competitive-battlecard`
