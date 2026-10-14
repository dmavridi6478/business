---
name: b2b-sales-25-active-listening-coach
description: Coach a seller on listening from a call transcript: talk share, questions asked, missed cues quoted, good moments quoted, three improvements and a short practice drill. Use after a recorded call when the participants have agreed to the recording.
---

# 25. Active Listening Coach

Stage 4 of 7: Discovery. Skill 25 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a transcript with speaker labels and permission to analyse it.

## Inputs

- Required: a transcript with speaker labels
- Required: confirmation that the call was recorded with the participants' consent
- Optional: the call goal
- Optional: the seller's own concern
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Compute talk share by words for each speaker `[calc: words/total words]`.
2. Count the seller's questions and the longest uninterrupted seller turn.
3. Find missed cues: places where the buyer mentioned a number, an event, a worry or a person and the seller moved on. Quote each exactly.
4. Find good moments: where the seller followed up, paraphrased or paused. Quote each exactly.
5. Name three improvements, each tied to a quoted moment.
6. Give one 10-minute practice drill the seller can do alone or with a colleague.
7. Remind the user that the transcript contains personal data and should be stored and shared accordingly.

## Output

Use these headings, in this order:

- `## Measures`
- `## Missed cues`
- `## Good moments`
- `## Three improvements`
- `## Practice drill`
- `## Data handling`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every quote is an exact excerpt of the transcript.
- Talk share shows its word counts.
- Each improvement refers to a quoted moment.
- The consent confirmation was received or the output stops.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not analyse a call recorded without consent.
- Do not judge the person, only the behaviour.
- Do not rank sellers against each other.

## Related

- `b2b-sales-24-asking-effective-questions` (skill 24, Asking Effective Questions)
- `b2b-sales-28-call-notes-extractor` (skill 28, Call Notes Extractor)
- `zoominfo:call-coaching`
