---
name: b2b-sales-47-health-score-model
description: Build a transparent customer health score from the user's own history of renewed and churned customers: candidate signals, how each relates to outcomes, weights, thresholds, a test on held-out customers and the limits. Use when the user wants an early-warning system for churn.
---

# 47. Health Score Model

Stage 7 of 7: Onboarding and expansion. Skill 47 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has historical accounts with outcomes and signals. With fewer than 30 accounts or 8 churn events, produce a manual checklist and label it a hypothesis.

## Inputs

- Required: historical accounts with renewal or churn outcome and the signals measured (usage, support tickets, engagement, sponsor changes, payment history)
- Optional: contract values
- Optional: the time between signal and outcome
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Check the data: at least 30 accounts and 8 churn events. If not, give a manual checklist and say why.
2. Split by time: earlier accounts train, later accounts test `[calc: counts]`.
3. For each signal, compare churn rates above and below a sensible cut in the training set. Ignore signals with fewer than 10 accounts in a group.
4. Assign weights by strength of relationship. Keep the model simple enough to explain to a customer manager.
5. Set green, amber and red thresholds and the action each triggers.
6. Test on the later accounts: of the accounts rated red, how many churned, and what share of all churners were rated red. Show counts.
7. State limits: small data, changes in product, and signals that cause churn versus merely accompany it.

## Output

Use these headings, in this order:

- `## Data check`
- `## Signal analysis`
- `## Weights and thresholds`
- `## Actions by band`
- `## Test results`
- `## Limits`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The train and test split is by time and shows counts.
- No weight rests on groups under 10 accounts.
- Test results are counts with denominators.
- Correlation is not described as cause.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not claim accuracy from the training data.
- Do not use a black-box score the customer team cannot explain.
- Do not use a customer's personal data beyond what is needed.

## Related

- `b2b-sales-03-lead-scoring-model` (skill 3, Lead Scoring Model)
- `b2b-sales-45-first-value-tracker` (skill 45, First Value Tracker)
- `b2b-sales-48-renewal-predictor` (skill 48, Renewal Predictor)
- `churn-prevention`
