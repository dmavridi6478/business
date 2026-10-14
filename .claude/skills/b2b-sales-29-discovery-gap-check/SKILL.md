---
name: b2b-sales-29-discovery-gap-check
description: Check whether discovery is complete enough to move to a demo: problem and impact, current process, stakeholders, decision process, timeline driver and success criteria, each with evidence, plus the missing items and a go or not-yet recommendation. Use before scheduling a demo or proposal.
---

# 29. Discovery Gap Check

Stage 4 of 7: Discovery. Skill 29 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the notes from one or more discovery calls exist and the user must decide whether to advance.

## Inputs

- Required: notes from the discovery conversations so far
- Optional: the user's own discovery requirements list
- Optional: the deal size
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List the six required areas: problem and impact, current process, stakeholders, decision process, timeline driver, success criteria. Use the user's list if given.
2. For each, record the evidence (quote) and a status: complete, partial or missing.
3. For partial and missing items, write the question that would complete it and who could answer.
4. Recommend: advance to demo, run another discovery call, or pause. Tie it to the statuses.
5. If advancing with gaps, list the risks and what to ask in the demo.

## Output

Use these headings, in this order:

- `## Requirement table`
- `## Gaps and questions`
- `## Recommendation`
- `## Risks if advancing`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each status cites a quote or says missing.
- Every gap has a question and an answerer.
- The recommendation follows from the table.
- Risks are listed when advancing with gaps.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not advance because the calendar says so.
- Do not mark an area complete from one vague sentence.
- Do not invent buyer answers.

## Related

- `b2b-sales-23-discovery-question-designer` (skill 23, Discovery Question Designer)
- `b2b-sales-27-current-vs-future-state` (skill 27, Current vs Future State)
- `b2b-sales-28-call-notes-extractor` (skill 28, Call Notes Extractor)
- `b2b-sales-30-demo-script-builder` (skill 30, Demo Script Builder)
