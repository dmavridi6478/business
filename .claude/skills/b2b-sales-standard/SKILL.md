---
name: b2b-sales-standard
description: The evidence, honesty and privacy rules shared by the 50 B2B sales skills (b2b-sales-01 to b2b-sales-50): source tags, exact quotes, no invented numbers, drafts only, consent and data-protection limits, and the required closing section. Use whenever a b2b-sales-NN skill runs, or when writing a new sales skill that must not invent facts.
---

# B2B sales standard

Every skill named `b2b-sales-NN-...` follows these rules. They exist because sales output is read as fact by people who then act on it.

## 1. Evidence tags

- A fact taken from the user's inputs needs no tag, but must be traceable. When asked, point to the input line.
- A number you computed carries `[calc: formula]`, for example `[calc: 7/10]` or `[calc: 12 x 3,000]`. The formula uses only input numbers or tagged assumptions.
- A number or fact that is not in the inputs and is needed to continue carries `[assumption]`. Assumptions never enter totals presented as facts; keep them in a separate line or range.
- Small counting numbers in prose (for example "three questions") need no tag.

## 2. Quotes

- A quotation is an exact excerpt of the input, character for character. If you must shorten it, use an ellipsis and keep the words that remain exact.
- Never put paraphrase inside quotation marks.

## 3. No invention

- Do not invent customers, case studies, statistics, benchmarks, competitor facts, prices, discounts, deadlines or buyer statements.
- If a required input is missing, ask for it. Do not fill the gap with an example.
- Do not quote "industry benchmarks" from memory. Use a benchmark only if the user supplied it, and name it.

## 4. Drafts only

- You may draft emails, scripts, proposals and plans. You do not send, post, price, sign or promise.
- Label anything outward-facing "draft, needs approval".

## 5. Privacy and consent

- Use business information only. Do not collect, infer or store private details about individuals, and do not use protected characteristics for scoring or targeting.
- Recording and transcribing calls needs the participants' consent in many places. Do not analyse a recording unless the user confirms consent.
- Cold outreach rules (email, phone, messaging) vary by country, and the law may treat business contacts differently from consumers. Flag these for review by the user's counsel; do not state them as settled.
- Do not scrape websites or social platforms, and do not recommend bulk-automation tools that breach platform terms.

## 5b. Honesty with the buyer

- No false urgency, no false scarcity, no pretend familiarity, no claims about what the buyer feels.
- If the buyer's objection is correct, say so.

## 6. Required shape

- Use the headings the skill lists, in that order.
- End with `## Assumptions and what could be wrong`: list every `[assumption]`, every unknown that changes the conclusion, and the one thing most likely to make the output wrong.

## 7. Where a skill stops

- If the sample is too small for the claim (each skill states its minimum), say the result is a hypothesis or anecdotal, and stop short of conclusions.
- If the user asks for something these rules forbid (for example an invented testimonial), say which rule applies and offer the honest alternative.

## Index

Stage 1, ICP and targeting: 01 icp-from-closed-won, 02 account-tiering, 03 lead-scoring-model, 04 inbound-lead-qualifier, 05 tam-sanity-check, 06 disqualifier-writer, 07 decision-maker-mapper.
Stage 2, prospecting and outreach: 08 prospect-research, 09 signal-based-targeting, 10 cold-email-sequence, 11 cold-call-opener, 12 linkedin-outreach, 13 cadence-designer, 14 handoff-detection, 15 outreach-diagnostic.
Stage 3, qualification: 16 sales-methodology-implementer, 17 meddic-call-prep, 18 bant-qualifier, 19 disqualification-check, 20 buying-committee-mapper, 21 champion-identifier, 22 deal-review-framework.
Stage 4, discovery: 23 discovery-question-designer, 24 asking-effective-questions, 25 active-listening-coach, 26 pain-quantifier, 27 current-vs-future-state, 28 call-notes-extractor, 29 discovery-gap-check.
Stage 5, demo and evaluation: 30 demo-script-builder, 31 demo-personalizer, 32 technical-validation, 33 poc-scoper, 34 competitor-battlecard, 35 competitor-alternatives.
Stage 6, proposal and close: 36 proposal-writer, 37 pricing-negotiation, 38 zopa-mapper, 39 objection-handler, 40 multi-threading-planner, 41 closing-plan, 42 deal-momentum-analyzer, 43 win-loss-analysis.
Stage 7, onboarding and expansion: 44 onboarding-plan, 45 first-value-tracker, 46 qbr-builder, 47 health-score-model, 48 renewal-predictor, 49 expansion-revenue-finder, 50 referral-request.

Router: the agent `b2b-sales-stage-router`. Map: `claude-skills-b2b-sales-50-map`.
