---
name: b2b-sales-30-demo-script-builder
description: Build a demo script around the buyer's stated problems instead of features: a recap, up to three scenarios, time boxes, check-in questions, a list of what not to show and a close with a dated next step. Use when preparing a product demo after discovery.
---

# 30. Demo Script Builder

Stage 5 of 7: Demo and evaluation. Skill 30 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when discovery notes exist and the user has a list of what the product can really do.

## Inputs

- Required: discovery notes with the buyer's problems in their words
- Required: the list of product capabilities the user confirms are real and demoable
- Required: the demo length and attendees
- Optional: the buyer's success criteria
- Optional: features known to be unfinished
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Open with a recap of the buyer's problems in their words and ask them to correct it.
2. Choose at most three scenarios, each tied to one stated problem.
3. For each scenario write: the problem, what to show, the capability used (only from the confirmed list), and the outcome the buyer should recognise.
4. Allocate time per scenario and leave a quarter of the time for questions `[assumption]`.
5. Add a check-in question after each scenario ("is this how you would want it to work?").
6. List what not to show: unfinished features, irrelevant modules, anything not on the confirmed list.
7. Write the close: what was agreed, and a dated next step to propose. Label it "draft, needs approval".
8. Write a fallback for each scenario if the system fails during the demo.

## Output

Use these headings, in this order:

- `## Recap`
- `## Scenario plan`
- `## Time boxes`
- `## Check-in questions`
- `## What not to show`
- `## Close and next step`
- `## Fallbacks`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every scenario maps to a stated problem.
- Every capability named is on the confirmed list.
- There are at most three scenarios.
- The close proposes a dated next step.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not tour the whole product.
- Do not promise a roadmap item.
- Do not demo with a buyer's real data without permission.

## Related

- `b2b-sales-27-current-vs-future-state` (skill 27, Current vs Future State)
- `b2b-sales-31-demo-personalizer` (skill 31, Demo Personalizer)
- `b2b-sales-32-technical-validation` (skill 32, Technical Validation)
- `sales:call-prep`
