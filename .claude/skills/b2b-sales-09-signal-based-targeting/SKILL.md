---
name: b2b-sales-09-signal-based-targeting
description: Turn dated buying signals (hiring, funding, leadership change, technology change, regulation, expansion) into a ranked target list with a message angle per signal, being clear that a signal is not proof of intent. Use when building a timely outreach list.
---

# 09. Signal-Based Targeting

Stage 2 of 7: Prospecting and outreach. Skill 9 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the user has a set of signals with sources and dates and wants to decide whom to contact first and why.

## Inputs

- Required: signals: account, what happened, date, source
- Required: the ICP
- Required: a map from signal type to the problem it may create for the buyer
- Optional: the user's relevance window in days
- Optional: past win rates by signal type
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Normalise each signal to account, type, date, source. Drop signals without a date or source and list them as dropped.
2. Apply the relevance window. If none was given, use 90 days and tag it `[assumption]`.
3. Map each remaining signal to a hypothesised problem. Mark the mapping as a hypothesis.
4. Score each account by rule: ICP fit points plus signal relevance plus recency. State the rule before the scores.
5. Rank. Give each ranked account one message angle that refers to the public event neutrally, without suggesting surveillance.
6. State clearly that signals show timing, not intent, and propose how to test: reply rates by signal type after 20 sends.

## Output

Use these headings, in this order:

- `## Signals used and dropped`
- `## Scoring rule`
- `## Ranked list`
- `## Message angle per account`
- `## How to test`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- The scoring rule appears before the ranking.
- Dropped signals are listed with the reason.
- Each angle refers only to the cited public event.
- The window default, if used, is tagged `[assumption]`.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not call a signal "buying intent" without evidence.
- Do not reference non-public information.
- Do not write angles that imply you tracked a person.

## Related

- `b2b-sales-08-prospect-research` (skill 8, Prospect Research)
- `b2b-sales-02-account-tiering` (skill 2, Account Tiering)
- `linkedin-signal-outreach`
