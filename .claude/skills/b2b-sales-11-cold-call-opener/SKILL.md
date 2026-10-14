---
name: b2b-sales-11-cold-call-opener
description: Write a short, permission-based cold call opener with a reason for calling, a first question, a response to "not interested" and a voicemail, for one persona. Use when preparing outbound calls.
---

# 11. Cold Call Opener

Stage 2 of 7: Prospecting and outreach. Skill 11 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a persona and a real reason to call (a signal or relevance fact).

## Inputs

- Required: the persona
- Required: the reason for calling: a cited fact or signal
- Required: the offer in one sentence
- Required: caller name and company
- Optional: the region (for call-recording and do-not-call rules)
- Optional: a past opener that worked
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Write three opener variants of about 20 seconds when spoken: identify yourself, give the reason, ask for permission to continue.
2. Use only the supplied reason. If none was given, say the opener will sound generic and ask for one.
3. Write the first question: open, about their situation, not a pitch.
4. Write a response to "not interested" or "send me an email" that respects the answer: one clarifying question at most, then an offer to send something short.
5. Write a voicemail under 25 seconds that states name, company, reason and a way to reach you, and no pressure.
6. List compliance notes: recording consent rules and do-not-call registers vary by region and must be checked before calling.

## Output

Use these headings, in this order:

- `## Opener variants`
- `## First question`
- `## If they decline`
- `## Voicemail`
- `## Compliance notes`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The reason for calling is a supplied fact.
- The decline response never argues or pressures.
- The voicemail includes a callback route.
- Compliance notes mention recording and do-not-call checks.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not use a trick opener ("Is this a bad time?" as a trap) or false familiarity.
- Do not claim to have spoken before if not.
- Do not pitch features in the opener.

## Related

- `b2b-sales-08-prospect-research` (skill 8, Prospect Research)
- `b2b-sales-12-linkedin-outreach` (skill 12, LinkedIn Outreach)
- `b2b-sales-13-cadence-designer` (skill 13, Cadence Designer)
