---
name: advisory-board
description: Set up a personal "council of experts" inside Claude Code — interview the user to pick a small set of named advisors relevant to their goals, gather each advisor's real content/frameworks as reference material, and store it so the /ask-the-board command can answer questions grounded in their actual thinking rather than a generic impression. Use this when the user wants a personal board of advisors, mentions wanting expert perspectives on a decision, or asks to set up /ask-the-board.
---

## What this is

A repeatable setup process for a personal advisory board — a small panel of real people (or well-documented personas) whose actual frameworks and writing get loaded as reference material, so `/ask-the-board <question>` answers in their genuine voice instead of a shallow "as Naval Ravikant would say" impression.

## Setup workflow

1. **Let Claude run the interview.** Ask the user about their goals, domain, and the kinds of decisions they need input on — don't ask them to design the board cold.
2. **Choose advisors.** Pick 3-5 *specific, named* people whose expertise genuinely matches the decisions identified in step 1 — not generic roles ("a marketing expert"). Push back if the user names someone whose actual body of work doesn't clearly apply.
3. **Provide their content.** For each advisor, gather real source material — essays, transcripts, interviews, books they've written — not just what Claude already "knows" about them from training. Save each advisor's material as its own reference file, e.g. `knowledge/advisory-board/<advisor-slug>.md`, with enough real quotes/frameworks that answers can be grounded in it.
4. **Confirm the `/ask-the-board` command exists.** This repo ships one at `.claude/commands/ask-the-board.md` — it reads the advisor files from step 3. If advisor files don't exist yet, the command should say so rather than answering with generic impressions.
5. **Pose the question.** Once set up, the user runs `/ask-the-board <question>` any time and gets a synthesized panel response.

## Guardrails

- If asked to "add an advisor" without real source material, ask for at least some real content (a link, a book title, a transcript) before creating the reference file — an advisor file with no real material defeats the point of the whole system.
- Keep the board small (3-5). More advisors dilutes the panel into noise rather than sharpening it.
- Re-run step 3 (refresh source material) if an advisor's file goes stale relative to the decisions being asked about.

## Related skills in this repo

- **the-specific-knowledge-excavator** / **the-productize-yourself-blueprint**: If the user is asking the board about their own business/product direction, these skills are natural companions for a "setting up a new business" board question.
- **product-strategy-session**, **saas-idea-validator**: Good candidates for questions to route through the board when validating a new idea.
- **quarterly-okr-architect**, **business-decision-frameworks**: The board is a good sanity-check step before committing to goals or prioritization produced by these skills.

## Notes

Source: a "Claude Code builds" screenshot carousel (@theromanknox), which demonstrated `/ask-the-board Based on everything you know about me, what should I do to leverage AI?` as the payoff of this setup. Treat the specific 5-step sequence as a repeatable template, not a fixed script — the core discipline is real advisor source material in, not just names.
