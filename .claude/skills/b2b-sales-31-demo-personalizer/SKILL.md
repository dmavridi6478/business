---
name: b2b-sales-31-demo-personalizer
description: Adapt a standard demo to one audience: reorder the outline to the attendees' concerns, use their vocabulary and examples, omit what they do not care about, and prepare one question per role. Use when attendees differ from the usual buyer or when several roles will attend.
---

# 31. Demo Personalizer

Stage 5 of 7: Demo and evaluation. Skill 31 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a standard demo outline exists and the attendee roles and concerns are known.

## Inputs

- Required: the standard demo outline
- Required: the attendees' roles and the concerns each has expressed
- Required: the buyer's own terms for their processes
- Optional: example data the buyer approved for use
- Optional: the order the buyer asked to see things
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each attendee role and its stated concern, quoting the source. Mark roles with no stated concern as unknown.
2. Reorder the outline so the concerns of the decision-maker come first, then the evaluators.
3. Replace generic wording with the buyer's own terms. List each replacement.
4. Cut or shorten sections no attendee cares about, and say what was cut and why.
5. Write one question per role that checks the demo is meeting their concern.
6. Flag any example data that needs the buyer's permission.

## Output

Use these headings, in this order:

- `## Attendees and concerns`
- `## Reordered outline`
- `## Language replacements`
- `## Cut or shortened`
- `## Question per role`
- `## Data permissions`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every concern cites a source or is marked unknown.
- Every reordering has a stated reason.
- Cuts are listed.
- Each role has one check question.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not assume what a role cares about from its title.
- Do not use another customer's data or name.
- Do not drop a section the buyer asked for.

## Related

- `b2b-sales-30-demo-script-builder` (skill 30, Demo Script Builder)
- `b2b-sales-20-buying-committee-mapper` (skill 20, Buying Committee Mapper)
- `b2b-sales-27-current-vs-future-state` (skill 27, Current vs Future State)
