---
description: Run one of the six one-shot LinkedIn profile prompts (experience ROI, 30-second pitch, keywords, full fix, headline, About) - asks for your text and real job ads first, never invents numbers, drafts only
argument-hint: [prompt number 1-6] - no args lists the six
---

Input: "$ARGUMENTS". If empty, list the six prompts from `.claude/skills/linkedin-six-profile-prompts-abby/SKILL.md` and suggest the order.

1. Ask for the profile text and, for the keyword prompts, five target job ads. Tell the user to remove third-party names and confidential figures.
2. Run the chosen prompt. Use only numbers the user gave; mark gaps as questions. Take keywords only from the pasted job ads.
3. Show the original beside the rewrite and flag every claim the user must verify.
4. Draft only: do not edit, post or message anything on LinkedIn.
