---
name: b2b-sales-27-current-vs-future-state
description: Build a current-state versus desired-state table from the buyer's own words (process, tools, people, measures, risks), define the gap, what must be true to close it, and a bridge to the offer without pitching. Use after discovery to structure the buyer's case.
---

# 27. Current vs Future State

Stage 4 of 7: Discovery. Skill 27 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the notes contain enough of the buyer's description of today and of what they want to build the table.

## Inputs

- Required: discovery notes with the buyer's statements about how things work now and what they want
- Optional: the buyer's success measures
- Optional: known constraints (budget, regulation, systems)
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Write the current state under five headings: process, tools, people, measures, risks. Use the buyer's words; quote where possible.
2. Write the desired state under the same headings, again from the buyer.
3. Mark any cell the buyer has not described as "not yet discussed".
4. State the gap per heading in one line.
5. List what must be true for the desired state to be reached (data, people, approvals, timing). Separate what the product affects from what it does not.
6. Draft a bridge: which gaps the offer addresses and which it does not. Say plainly if some gaps are outside the offer.

## Output

Use these headings, in this order:

- `## Current state`
- `## Desired state`
- `## Gaps`
- `## What must be true`
- `## Bridge to the offer`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Cells use the buyer's words or say "not yet discussed".
- The bridge names gaps the offer does not close.
- No product feature is described as a fact about the buyer.
- Constraints are listed.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not fill a cell with what the buyer probably thinks.
- Do not turn the table into a feature list.
- Do not promise a result.

## Related

- `b2b-sales-26-pain-quantifier` (skill 26, Pain Quantifier)
- `b2b-sales-29-discovery-gap-check` (skill 29, Discovery Gap Check)
- `b2b-sales-30-demo-script-builder` (skill 30, Demo Script Builder)
- `b2b-sales-33-poc-scoper` (skill 33, POC Scoper)
