---
name: b2b-sales-45-first-value-tracker
description: Track a new customer's progress to first value: the milestone definition, evidence of each step completed, days elapsed against the plan, blockers, and the intervention to take if the customer is behind. Use during the first weeks after signature.
---

# 45. First Value Tracker

Stage 7 of 7: Onboarding and expansion. Skill 45 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when an onboarding plan exists and the user has dated evidence of progress.

## Inputs

- Required: the first-value definition
- Required: the onboarding plan with dates
- Required: dated evidence of steps completed (events, usage, confirmations)
- Optional: usage data
- Optional: customer sentiment notes
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Restate the first-value definition and the steps leading to it.
2. For each step, record the status (done, in progress, not started) with the evidence and its date. No evidence means "not started or unknown".
3. Compute days elapsed against the plan `[calc: today minus start; planned minus actual]`.
4. List blockers with who owns each.
5. Decide on the status: on track, at risk, or behind, from the evidence.
6. Write the intervention for at-risk or behind: who contacts whom, with what offer of help. Draft the message for approval.
7. Set the next check date.

## Output

Use these headings, in this order:

- `## First-value definition`
- `## Step status with evidence`
- `## Time against plan`
- `## Blockers`
- `## Status`
- `## Intervention`
- `## Next check`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each status cites dated evidence.
- Time against plan shows its dates.
- The status follows from the evidence.
- An intervention is drafted when the status is not on track.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not mark a step done on the customer's verbal word alone if a system event is available.
- Do not blame the customer in the message.
- Do not hide delays from the customer.

## Related

- `b2b-sales-44-onboarding-plan` (skill 44, Onboarding Plan)
- `b2b-sales-47-health-score-model` (skill 47, Health Score Model)
- `b2b-sales-46-qbr-builder` (skill 46, QBR Builder)
