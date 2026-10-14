---
name: b2b-sales-14-handoff-detection
description: Decide from the replies in a thread whether a lead should be handed from the outbound rep to an account executive, kept in nurture, routed elsewhere or stopped, and write a facts-only handoff note. Use when replies arrive in outbound or inbound threads.
---

# 14. Handoff Detection

Stage 2 of 7: Prospecting and outreach. Skill 14 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when there is a reply or activity log and handoff criteria (or the user accepts the default list).

## Inputs

- Required: the reply thread or activity log
- Required: the handoff criteria, or permission to use the default list
- Required: who receives handoffs and the response-time target
- Optional: the ICP
- Optional: account ownership rules
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Classify the latest reply by intent: meeting request, pricing or product question, objection, out-of-office, referral to someone else, neutral, negative, unsubscribe.
2. Check the handoff criteria one by one against facts in the thread. The default list: stated need, a named timeframe, a request for a meeting or pricing, or involvement of a decision-maker.
3. Decide: hand off now, continue nurture, route to a referred contact, or stop.
4. If the reply is an unsubscribe or a clear refusal, stop all outreach and add the person to the suppression list immediately.
5. Write the handoff note with facts only: who, what was said (quoted), what was promised, open questions, next step and deadline.
6. Flag any promise the rep made that the receiving team must keep.

## Output

Use these headings, in this order:

- `## Reply classification`
- `## Criteria check`
- `## Decision`
- `## Handoff note`
- `## Suppression actions`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Quotes in the note are exact.
- The note separates facts from opinions.
- Unsubscribes trigger suppression, never a follow-up.
- The decision cites the criteria met or missed.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not hand off a lead on enthusiasm alone.
- Do not keep contacting someone who opted out.
- Do not embellish what the prospect said.

## Related

- `b2b-sales-04-inbound-lead-qualifier` (skill 4, Inbound Lead Qualifier)
- `b2b-sales-13-cadence-designer` (skill 13, Cadence Designer)
- `sales:route-lead`
