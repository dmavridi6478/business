---
name: b2b-sales-43-win-loss-analysis
description: Analyse won and lost deals for the real reasons: structured interview or note review, buyer's stated reasons versus seller beliefs, patterns with counts, and changes to test. Use after a quarter or after a notable win or loss.
---

# 43. Win-Loss Analysis

Stage 6 of 7: Proposal and close. Skill 43 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has deal notes or interview notes for several decided deals.

## Inputs

- Required: decided deals with outcome, the buyer's stated reasons where available, the competitor, and the seller's belief about why
- Required: at least five deals, or the result is labelled anecdotal
- Optional: buyer interview transcripts
- Optional: deal value and cycle length
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each deal with the buyer's stated reason and the seller's belief side by side. Mark where they differ.
2. Code the reasons into categories (price, fit, product gap, timing, trust, process, champion, competitor) and count them `[calc: n of N]`.
3. Report patterns only with their counts. Under five deals, call the result anecdotal.
4. Separate what the buyer said from what the seller inferred.
5. Find the reasons that appear in both wins and losses and do not discriminate.
6. Propose at most three changes to test, each with the measure that would show whether it worked.
7. List the limits: who was interviewed, who declined, and what bias that adds.

## Output

Use these headings, in this order:

- `## Deal table`
- `## Reason counts`
- `## Buyer versus seller view`
- `## Patterns`
- `## Changes to test`
- `## Limits`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Counts show numerators and denominators.
- Buyer reasons and seller beliefs are kept apart.
- Fewer than five deals are labelled anecdotal.
- Each change has a measure.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not trust the seller's version over the buyer's.
- Do not draw a rule from two deals.
- Do not name individual buyers in a shared report.

## Related

- `b2b-sales-01-icp-from-closed-won` (skill 1, ICP From Closed-Won)
- `b2b-sales-06-disqualifier-writer` (skill 6, Disqualifier Writer)
- `b2b-sales-22-deal-review-framework` (skill 22, Deal Review Framework)
- `sales:win-loss-review`
