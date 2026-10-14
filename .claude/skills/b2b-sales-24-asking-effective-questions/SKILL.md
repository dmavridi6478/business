---
name: b2b-sales-24-asking-effective-questions
description: Classify and rewrite a seller's questions (open, closed, leading, stacked, assumptive) into effective ones, with a probe for each and reasons the rewrite works. Use when reviewing a question list or call transcript for question quality.
---

# 24. Asking Effective Questions

Stage 4 of 7: Discovery. Skill 24 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user supplies a list of questions or a transcript with the seller's questions marked.

## Inputs

- Required: the questions, or a transcript with speaker labels
- Optional: the goal of the call
- Optional: the buyer's persona
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each question verbatim and classify it: open, closed, leading, stacked (two or more questions), assumptive, or a statement disguised as a question.
2. Count the types `[calc: n of N]`.
3. Rewrite each weak question so it is open, single and neutral, and say what it now invites.
4. Add one follow-up probe per rewritten question.
5. Replace accusatory "why" questions with "what" or "how" versions that keep curiosity without blame.
6. Give three habits: pause after the answer, repeat key words, ask for an example.

## Output

Use these headings, in this order:

- `## Question audit`
- `## Counts by type`
- `## Rewrites and probes`
- `## Habits to practise`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every original question is quoted exactly.
- Each rewrite is open, single and neutral.
- The counts show numerator and denominator.
- Each rewrite has a probe.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not rewrite the buyer's answers.
- Do not make every question open at the cost of clarity.
- Do not invent questions the seller never asked when auditing.

## Related

- `b2b-sales-23-discovery-question-designer` (skill 23, Discovery Question Designer)
- `b2b-sales-25-active-listening-coach` (skill 25, Active Listening Coach)
