---
description: Ask your configured personal advisory board a question, answered in each advisor's genuine voice/framework plus a synthesized recommendation.
argument-hint: [question]
---

The user is asking their personal advisory board a question. The question is: $ARGUMENTS

## Before answering

1. Look for advisor reference files under `knowledge/advisory-board/` (or wherever the `advisory-board` skill's setup stored them — check that skill if unsure of the location).
2. If no advisor files exist yet, do not improvise generic advisor impressions. Tell the user the board isn't set up yet and point them to the `advisory-board` skill to run the setup first.
3. If advisor files exist but seem stale or too thin to ground a real answer to this specific question, say so before answering rather than papering over the gap.

## Answering

For each configured advisor:

- Answer the question as that advisor would, grounded specifically in the frameworks, language, and positions found in their reference file — not a generic impression of someone with their reputation.
- Keep each advisor's answer distinct: different advisors should disagree or emphasize different things when their real frameworks would actually lead to different advice. Don't flatten them into saying the same thing in different words.
- Cite which specific idea/framework from their material the answer is drawing on.

Then close with:

- **Synthesis**: where the advisors agree, where they genuinely conflict, and — if asked for a recommendation — a specific point of view on what to do, not a hedge that just restates all sides.
