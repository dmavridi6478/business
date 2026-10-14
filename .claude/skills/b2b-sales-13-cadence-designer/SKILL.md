---
name: b2b-sales-13-cadence-designer
description: Design a multi-channel outreach cadence with day offsets, channels, purpose per touch, stop rules and a capacity check, matched to tier and region. Use when the user needs a repeatable contact plan.
---

# 13. Cadence Designer

Stage 2 of 7: Prospecting and outreach. Skill 13 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a tier or persona, the channels they may legally and practically use, and a weekly capacity.

## Inputs

- Required: the tier or persona
- Required: channels allowed (email, phone, LinkedIn, other)
- Required: capacity: touches per week the team can make
- Required: the region and any contact restrictions
- Optional: past reply data by channel
- Optional: the number of accounts per tier
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. State the objective of the cadence and its length in days.
2. Lay out the steps: day offset, channel, purpose, asset. Vary channel and purpose, not just the wording.
3. Match intensity to tier: more personalised touches for higher tiers.
4. Write stop rules: reply, bounce, opt-out, a "not now" with a date, and a do-not-contact list that overrides everything.
5. Capacity check: accounts times touches per account divided by weeks `[calc]` must not exceed the stated capacity; adjust the cadence if it does.
6. Add compliance notes per channel and region.
7. Define the measures: reply rate per step, meetings per 100 accounts, unsubscribes, and the review date.

## Output

Use these headings, in this order:

- `## Objective`
- `## Cadence table`
- `## Stop rules`
- `## Capacity check`
- `## Compliance notes`
- `## Measurement plan`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Capacity arithmetic is shown and holds.
- Stop rules include opt-out override.
- Each step has a different purpose.
- No channel is used where the inputs say it is not allowed.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not plan more touches than capacity allows.
- Do not continue after an opt-out.
- Do not copy a cadence from the internet as if it were evidence.

## Related

- `b2b-sales-02-account-tiering` (skill 2, Account Tiering)
- `b2b-sales-10-cold-email-sequence` (skill 10, Cold Email Sequence)
- `b2b-sales-11-cold-call-opener` (skill 11, Cold Call Opener)
- `b2b-sales-12-linkedin-outreach` (skill 12, LinkedIn Outreach)
- `outreach-planning`
