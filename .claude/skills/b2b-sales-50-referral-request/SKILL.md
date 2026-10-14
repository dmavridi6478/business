---
name: b2b-sales-50-referral-request
description: Write a considerate referral or reference request for a customer who has achieved a result: the timing check, the specific ask, an easy way to say no, a draft message and the follow-up rule. Use when a satisfied customer could introduce or vouch for the user.
---

# 50. Referral Request

Stage 7 of 7: Onboarding and expansion. Skill 50 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when a customer has a documented success and a good relationship.

## Inputs

- Required: the customer's documented result and the date
- Required: the relationship status (any open issues)
- Required: the specific ask: introduction, reference call, review or case study
- Optional: the people the customer might introduce
- Optional: the customer's stated willingness to share
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Check the timing: result documented, no open escalation, recent positive contact. If any fails, advise waiting and say why.
2. Choose one specific ask and make it small. State what will be done for the customer in return only if the user has authority to offer it.
3. Write a message that thanks the customer for a named, true result, makes the one ask, says how little time it takes, and offers an easy way to say no.
4. For an introduction, offer to draft the forwardable note so the customer only has to forward it.
5. Set the follow-up rule: at most one reminder, then stop.
6. Check the rules: some companies forbid references or gifts; the customer's policy and the user's own rules apply. Flag for review where relevant.

## Output

Use these headings, in this order:

- `## Timing check`
- `## The ask`
- `## Message draft`
- `## Forwardable note`
- `## Follow-up rule`
- `## Policy notes`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The timing check is explicit.
- The ask is single and specific.
- The message includes an easy way to decline.
- At most one reminder is planned.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not ask during an open issue.
- Do not offer an incentive without authority and a policy check.
- Do not name the customer publicly without written permission.

## Related

- `b2b-sales-49-expansion-revenue-finder` (skill 49, Expansion Revenue Finder)
- `b2b-sales-46-qbr-builder` (skill 46, QBR Builder)
- `b2b-sales-50-referral-request` (skill 50, Referral Request)
- `referrals`
