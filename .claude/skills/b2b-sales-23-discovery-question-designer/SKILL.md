---
name: b2b-sales-23-discovery-question-designer
description: Design an ordered discovery question set for one buyer type: current state, problem, impact, desired outcome and decision process, each question with its purpose and follow-up probes, tuned to the call length and to what the seller still needs to learn. Use when preparing a discovery call.
---

# 23. Discovery Question Designer

Stage 4 of 7: Discovery. Skill 23 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a discovery call is coming and the user knows the persona and what is still unknown.

## Inputs

- Required: the persona and company type
- Required: the product category and the problem it addresses
- Required: what the seller already knows and what is still unknown
- Required: the call length in minutes
- Optional: the buyer's earlier stated concerns
- Optional: the stakeholders attending
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List the learning goals from the unknowns. Each question must serve one goal.
2. Order the questions: context and current state first, then problem and impact, then desired outcome, then decision process and timing.
3. Write open questions only for the main line. Add one probe per question ("what happened then?", "how do you handle that today?").
4. Fit the set to the call length: one main question per 3 to 4 minutes `[assumption]`. Mark what to cut first.
5. Add one question that invites the buyer to say what you have not asked about.
6. List things not to do: pitching, filling silence, leading wording.

## Output

Use these headings, in this order:

- `## Learning goals`
- `## Question sequence`
- `## Probes`
- `## What to cut first`
- `## Closing question`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every question maps to a learning goal.
- The main questions are open.
- The set fits the call length with a stated cut order.
- No question pitches or leads.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not use a fixed script as if the buyer were predictable.
- Do not ask what you could have found in public sources.
- Do not stack two questions in one.

## Related

- `b2b-sales-24-asking-effective-questions` (skill 24, Asking Effective Questions)
- `b2b-sales-26-pain-quantifier` (skill 26, Pain Quantifier)
- `b2b-sales-29-discovery-gap-check` (skill 29, Discovery Gap Check)
- `sales:call-prep`
