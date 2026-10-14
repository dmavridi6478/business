---
name: b2b-sales-19-disqualification-check
description: Run a structured go or no-go on a live opportunity against a list of disqualifiers and the cost of continuing, then recommend continue, fix a gap, or exit, with an honest exit message draft. Use when a deal is consuming time without progress.
---

# 19. Disqualification Check

Stage 3 of 7: Qualification. Skill 19 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when an opportunity has stalled or looks weak, and the user has disqualifiers (for example from skill 6) or accepts a default list.

## Inputs

- Required: the opportunity facts and notes
- Required: the disqualifier list, or permission to use a default list
- Required: the time spent and still required, if known
- Optional: the lost-deal evidence behind the disqualifiers
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. Check each disqualifier as met, not met or unknown, citing the note.
2. Separate hard disqualifiers (stop) from soft ones (continue only with an exception and an approver).
3. Estimate the cost of continuing: hours so far and hours needed, using supplied figures or tagged assumptions.
4. Recommend one of: continue, fix a named gap by a date, or exit.
5. If exit: draft an honest, polite message, with no false hope or blame. Label it "draft, needs approval".
6. If continue: state the evidence that would trigger a re-check in 14 days `[assumption]`.

## Output

Use these headings, in this order:

- `## Disqualifier check`
- `## Cost of continuing`
- `## Recommendation`
- `## Exit message draft`
- `## Re-check trigger`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Each disqualifier cites a note or "unknown".
- Hard and soft are separated.
- The exit message promises nothing and blames no one.
- Assumed figures are tagged.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not exit a deal on an unknown that one question could settle.
- Do not keep a hard disqualifier open for revenue pressure.
- Do not hide the reason from the user.

## Related

- `b2b-sales-06-disqualifier-writer` (skill 6, Disqualifier Writer)
- `b2b-sales-18-bant-qualifier` (skill 18, BANT Qualifier)
- `b2b-sales-22-deal-review-framework` (skill 22, Deal Review Framework)
