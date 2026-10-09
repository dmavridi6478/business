# Decision-Making Frameworks

Source: reviewed from an uploaded infographic — "Making Decisions: Quick
guide on four methods" (Jonathan Butterworth). The infographic's fourth
method, SWOT, is already covered in `messaging-frameworks.md` in this same
skill — not duplicated here. These three are the ones not yet in this
library: two operate on *urgency/importance and OODA-style tempo*, the
third drills to a root cause rather than ranking options.

## Eisenhower Matrix — urgency vs. importance

A 2x2 grid for triaging a task list, not ranking a backlog (use
`prioritization-frameworks.md` for that):

| | Urgent | Not urgent |
|---|---|---|
| **Important** | Do — handle it yourself, now | Schedule — block time for it before it becomes urgent |
| **Not important** | Delegate — hand it off | Eliminate — drop it |

Best for: daily/weekly task triage, calendar audits, deciding what to say
no to. Failure mode: everything gets marked "urgent and important" because
the person doing the sorting is the same person who created the tasks —
have someone else sanity-check the quadrant placement, or apply it to a
calendar/time-tracking export instead of a mental list.

## OODA Loop — Observe, Orient, Decide, Act

A four-stage loop for making fast decisions under changing conditions,
originally a fighter-pilot doctrine (John Boyd), now used for competitive
strategy and incident response:

1. **Observe** — gather current information; don't skip this to save time.
2. **Orient** — update your mental model against what you just observed
   (this is the step people skip, and where good OODA looping actually
   wins: your last plan's assumptions may no longer hold).
3. **Decide** — choose a course of action from the updated picture.
4. **Act** — execute, then the loop restarts with Observe.

Best for: competitive/market moves, incident response, any situation where
conditions change faster than a quarterly-planning cadence can track.
Distinct from a single-pass decision: the loop is meant to run continuously,
faster than the competing loop (an opponent, a market, an incident) can
adapt to you.

## Five Whys — root-cause drill-down

Ask "why" five times (or until you hit a cause you can actually act on,
which may take fewer or more than five iterations) to move from a symptom
to its root cause:

> Problem: Sales dropped this quarter.
> Why? The main product's sales declined.
> Why? Customers are finding the product less relevant.
> Why? Competitor products have more features.
> Why? We haven't updated the product recently.

Best for: postmortems, recurring-problem diagnosis, before proposing a
fix. Failure mode: stopping at the first answer that names a person or
team ("the intern misconfigured it") instead of the process gap that let
that misconfiguration ship — keep asking why *that* was possible.

## How these three differ from this skill's other frameworks

- Eisenhower and OODA are about **when/whether to act**, not what to build
  — don't reach for RICE or MoSCoW here, those rank a backlog of already-
  agreed-on work.
- Five Whys is a **diagnostic**, not a prioritization or messaging tool —
  run it before a Minto Pyramid or a status report, to make sure the report
  names the real cause rather than the first visible symptom.
