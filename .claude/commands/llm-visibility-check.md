---
description: Fill and run the 25-prompt LLM visibility check for a brand and set up the recording sheet
argument-hint: <brand, category, location, main competitor>
---

Use the `llm-visibility-prompt-check` skill for: "$ARGUMENTS"

1. Ask for any missing bracket values in one question (brand, category, location, audience, use case, competitor).
2. Print the 25 prompts with brackets filled, grouped as in the skill.
3. Give the empty recording sheet and the three-runs-per-prompt rule.
4. Do not run the prompts against any assistant yourself unless the user asks; do not invent results.
