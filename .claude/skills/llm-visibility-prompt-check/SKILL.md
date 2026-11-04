---
name: llm-visibility-prompt-check
description: Free 25-prompt check of whether a brand is named, recommended or cited by AI assistants (ChatGPT, Claude, Gemini, Perplexity) - discovery and fit, budget and trust, comparisons and alternatives, and the brand itself - plus a recording sheet and the limits of what one run proves. Use when someone asks "do AI tools mention us", wants a no-tool AI visibility baseline, or needs the prompts to copy. Run via /llm-visibility-check. Source @amanpreet "25 Prompts to Check Your Visibility in LLMs"; deeper strategy lives in ai-search-visibility.
---

# 25 prompts to check your visibility in LLMs

Source: one-page infographic ("without paying for any tool"). Prompts are reproduced verbatim in `docs/batch-113-prompts.md`; fill every [bracket] before use.

## The four groups

| Group | Prompts | What it tests |
|---|---|---|
| Discovery and fit | 01-06 | Are you named when a buyer asks for the best option in a category, a place, an industry, a use case, or for a problem? |
| Budget, features and trust | 07-12 | Do you appear under a budget, a feature, an integration, a team size, "most reliable", "best support"? |
| Comparisons and alternatives | 13-16 | Do you make the shortlist, and are you named as an alternative to a competitor? |
| Your brand | 17-25 | What does the assistant say about you: what you offer, who you suit, strengths and weaknesses, comparisons, alternatives, customer opinion, what to know before buying, which sources it would use |

## Procedure

1. Fill the brackets once (category, location, audience, industry, use case, problem, budget, feature, tool, team size, competitor, requirement, brand). Keep the same values for every re-test.
2. Run each prompt in a fresh chat on each assistant you care about, logged out or in a clean profile if you can.
3. Run each prompt at least three times. Assistants vary between runs; one answer proves little. [Certain]
4. Record per answer: brand named (yes/no), position in the list, competitors named, sources cited, sentiment (positive / neutral / negative), anything false.
5. Compute **your own** rates from the sheet: share of runs where the brand is named per group; share where a source on your site is cited. These are working numbers, not industry-standard metrics.
6. Fix, then re-run monthly: false statements first (correct the source page), then missing groups (build the page type that group needs; see `ai-search-visibility/references/aeo-glossary-and-funnels.md`: authority, decision, money pages).

## Recording sheet (copy into a spreadsheet)

| date | assistant | prompt # | run # | named? | position | competitors named | cited sources | sentiment | false claim |
|---|---|---|---|---|---|---|---|---|---|

## Limits

- Answers depend on the assistant, model version, location, language, login state and memory. Treat results as a sample.
- Prompts 17-25 ask about your brand by name, so a positive result there does not mean you are found by buyers who do not know you; groups 01-16 do.
- Do not paste confidential information into any assistant to run these.
- The infographic gives no evidence about how often these prompts match real buyer questions; replace them with questions from your sales calls where you can.
