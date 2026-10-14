---
name: b2b-sales-01-icp-from-closed-won
description: Derive an ideal customer profile from the user's own closed-won deals: shared firmographics, buying triggers, buyer roles, deal size and cycle, and what separates the best customers from the rest. Use when defining or refreshing an ICP from real customer data.
---

# 01. ICP From Closed-Won

Stage 1 of 7: ICP and targeting. Skill 1 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a list of won deals (and ideally lost deals or retention data) and wants an evidence-based ICP. If there are fewer than 10 won deals, say the result is a hypothesis, not a profile.

## Inputs

- Required: closed-won deals, one row each, with company size, industry, region, buyer role, deal value, sales cycle days and lead source (at least 10 rows)
- Optional: closed-lost deals with the loss reason
- Optional: churned or low-usage customers
- Optional: retention or expansion data per customer
- Optional: notes on why each customer bought
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. State the sample size. Under 10 won deals: label everything below "hypothesis".
2. Tabulate every attribute across the won deals as counts (for example 7 of 10), never as impressions.
3. Split attributes into three groups: common to most won deals, common to won and lost alike (does not discriminate), and common in won but rare in lost. If no lost deals were supplied, say discrimination cannot be tested.
4. If outcome quality is supplied (retention, expansion, short cycle), profile the best third separately from the rest.
5. List buying triggers (events before purchase) only if they appear in at least two deals' notes; quote the note.
6. Write the ICP statement using only attributes that appear in your table: firmographic fit, situation or trigger, buyer roles, and disqualifiers.
7. List what the ICP excludes and the evidence each exclusion rests on.
8. Propose one validation test: apply the ICP to the next 20 opportunities and compare win rates in and out of profile.

## Output

Use these headings, in this order:

- `## Sample and confidence`
- `## Attribute table`
- `## Discriminating attributes`
- `## Triggers`
- `## ICP statement`
- `## Exclusions`
- `## Validation test`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The sample size is stated, with "hypothesis" if under 10 won deals.
- Every percentage shows numerator and denominator as `[calc: 7/10]`.
- The ICP statement uses only attributes present in the attribute table.
- If no lost deals were supplied, the output says discrimination was not tested.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not use market size or revenue potential as evidence that a customer fits.
- Do not include personal characteristics of individual buyers.
- Do not present a pattern from three deals as a rule.

## Related

- `b2b-sales-02-account-tiering` (skill 2, Account Tiering)
- `b2b-sales-03-lead-scoring-model` (skill 3, Lead Scoring Model)
- `/icp` command
- `ideal-customer-profile`
- `b2b-sales-standard`
