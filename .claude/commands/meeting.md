---
description: Extract decisions, owners, deadlines, and open questions from a meeting transcript or notes
argument-hint: [meeting transcript or notes]
---

Process the meeting transcript or notes in "$ARGUMENTS" and extract:

**DECISIONS** — what was agreed, with enough context to understand the reasoning
**OWNERS** — who is responsible for what (name + action, not just name)
**DEADLINES** — when each commitment is due; flag any action with no stated deadline
**OPEN QUESTIONS** — anything that came up but was not resolved; note who needs to answer it

Format as a clean, scannable summary — not bullet soup. If an owner or deadline is genuinely unclear, say so rather than guessing. Flag any decision that seems to contradict an earlier one.

If "$ARGUMENTS" is empty, ask for the transcript or notes to process before proceeding.

Source: @theusefulshift "20 Claude Commands That Feel Illegal" — Command 08 (meeting).
