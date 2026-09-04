# Procedure: Source Verification for AI-Generated Reading Lists

## When this applies

Any time a response hands someone a list of things to read or watch —
resource recommendations from `learn`, sources under `research-synthesis`,
citations in a competitor or market report, "further reading" appended to
an answer. Models are at their worst here: titles, chapters, and course
names get invented wholesale, and a confidently formatted citation looks
identical whether it's real or fabricated.

## The check

For every source recommended:

1. **Say who it's for and what it assumes the reader already knows.** A
   source with no stated audience or prerequisite is a sign it wasn't
   actually vetted, just generated to fill a slot.
2. **Include a link, and only a link that was actually verified** —
   fetched or confirmed to resolve, not just pattern-matched from a
   plausible-sounding title. A title with no link, or a link that wasn't
   checked, doesn't get included as if it were verified.
3. **Say which sources are official docs/primary sources** versus
   secondary explainers — don't flatten that distinction, since it's part
   of what makes a source trustworthy.
4. **Treat anything unverifiable as fiction, not as a lower-confidence
   recommendation.** Don't hedge with "I believe this exists" — either
   confirm it and include it, or drop it and say the search didn't turn up
   a verified source for that gap.

## Note

This isn't a request to fabricate more carefully — it's a rule that only
verified sources get listed, full stop. If a reading-list request can't be
satisfied with sources that were actually checked, say so explicitly
rather than filling the list with plausible-looking invented ones.

## Source

Synthesized from prompt 05 of a 6-prompt "Make AI Teach You Anything"
carousel (@hiitzroman) — the one prompt not already covered by this
environment's `learn` skill, which handles the rest of that carousel's
pedagogy (diagnosis, guided discovery, testing, spaced review) more
thoroughly than the carousel's fixed prompts do.
