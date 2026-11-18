---
description: Pick which of the nine go-to-market models fits a situation, in what order, with the question each answers
argument-hint: [your situation, e.g. "too many segments, no usage data yet, need a price"]
---

Input: "$ARGUMENTS". If empty, ask for the product, stage and the one thing that feels stuck.

Use `.claude/skills/gtm-nine-models/SKILL.md`.

1. Name the one or two models that fit, with the question each answers and why it fits this situation.
2. Give the order from the skill's sequence (who, proof, message and price, growth) and mark which step the user is on.
3. For pricing, state which Van Westendorp convention is used and that OPP says nothing about volume or margin; hand off to `pricing`.
4. Name the first concrete action for each chosen model (a list, a call, a test), not a diagram to admire.
5. Say what the nine models do not give: sample sizes, sources, or evidence that one works better than another.

Plan only; run nothing. End with `Not verified:` for any claim not from the skill.
