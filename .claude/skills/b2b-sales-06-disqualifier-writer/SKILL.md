---
name: b2b-sales-06-disqualifier-writer
description: Write explicit disqualification criteria and polite exit scripts for deals that should not be pursued, based on the user's lost deals, churn and support-cost evidence. Use when sellers waste time on poor-fit prospects.
---

# 06. Disqualifier Writer

Stage 1 of 7: ICP and targeting. Skill 6 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has lost-deal or churn notes and wants a short list of observable reasons to stop early.

## Inputs

- Required: lost or churned deal notes with the stated reason
- Required: the ICP or fit criteria
- Optional: support cost or discount data per customer
- Optional: sales cycle lengths for lost deals
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Group the reasons and count them `[calc: n of N]`. Keep reasons that recur in at least three deals or carry high cost.
2. Turn each kept reason into an observable check: a question to ask and the answer that fails.
3. Mark each as hard (stop) or soft (continue only with a named exception and an approver).
4. Draft an honest, polite exit message per hard disqualifier. No false hope, no pressure. Label it "draft, needs approval".
5. Add a referral or alternative resource where a fair one exists in the inputs.
6. List the fields to log when a lead is disqualified, so the list can be improved.
7. Review each criterion for unlawful discrimination or refusal-to-deal risk; flag any that need legal review.

## Output

Use these headings, in this order:

- `## Evidence summary`
- `## Disqualifier list`
- `## Exit scripts`
- `## Logging fields`
- `## Review before use`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each disqualifier cites at least three examples or a cost figure from the inputs.
- Each has a question and a failing answer.
- Exit scripts make no promise and contain no invented reason.
- Criteria relying on protected characteristics are removed.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not disqualify on a single anecdote.
- Do not write scripts that blame the prospect.
- Do not use a criterion you cannot check by asking.

## Related

- `b2b-sales-01-icp-from-closed-won` (skill 1, ICP From Closed-Won)
- `b2b-sales-04-inbound-lead-qualifier` (skill 4, Inbound Lead Qualifier)
- `b2b-sales-19-disqualification-check` (skill 19, Disqualification Check)
