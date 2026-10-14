---
name: b2b-sales-05-tam-sanity-check
description: Test a TAM, SAM or SOM claim by rebuilding it bottom-up from account counts, price and adoption, show sensitivity, and compare it with the claim and with sales capacity. Use when a market-size number appears in a plan, deck or pitch.
---

# 05. TAM Sanity Check

Stage 1 of 7: ICP and targeting. Skill 5 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user or a document asserts a market size and the user wants to know whether it holds.

## Inputs

- Required: the claim exactly as stated, with its source
- Required: the segment definition (who counts as a customer)
- Required: price points or revenue per customer
- Required: a source for the number of accounts in the segment, or permission to use a ranged assumption
- Optional: current revenue and customer count
- Optional: quota and seller headcount
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Quote the claim and say how it was built (top-down percentage or bottom-up).
2. Define the segment in one sentence and count what qualifies. Every account count must come from an input or a named source; otherwise give a low-base-high range tagged `[assumption]`.
3. Build bottom-up: accounts times realistic annual revenue per account `[calc: accounts x price]`.
4. Run sensitivity with low, base and high values for account count, price and adoption; show the three results side by side.
5. Compare with the claim: ratio of claim to bottom-up base `[calc]`.
6. Capacity check for SOM: sellers times quota times years versus the obtainable figure.
7. Give a verdict: supported, overstated or unsupported, and the one input that would change it most.

## Output

Use these headings, in this order:

- `## The claim`
- `## Segment definition`
- `## Bottom-up build`
- `## Sensitivity table`
- `## Gap versus claim`
- `## Capacity check`
- `## Verdict`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every account count is sourced or shown as a range with `[assumption]`.
- The three sensitivity cases are shown.
- The verdict names the single most influential input.
- No figure from outside the inputs is stated as fact.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not accept "1% of a big market" as a method.
- Do not use a market-research number you cannot cite.
- Do not present a single point estimate.

## Related

- `b2b-sales-01-icp-from-closed-won` (skill 1, ICP From Closed-Won)
- `market-sizing-analysis`
- `zoominfo:tam-sizer`
