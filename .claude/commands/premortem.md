---
description: Run the 5-step @ai_slacker premortem on a plan - autopsy, verdict, rebuild, adversary, tripwires - one step at a time with the exact prompts
argument-hint: <the plan, with timeline, budget and what success looks like>
---

Use the skill `ai-slacker-premortem`. Input: "$ARGUMENTS".

1. If the plan has no timeline, budget or success definition, ask for the missing ones first (one question at a time). Do not invent details: every failure must trace to something the user said.
2. Run the five prompts in order from the skill (premortem, verdict, rebuild, adversary, tripwire), pausing after each so the user can push back. Never reassure.
3. Finish with: the most dangerous failure, the hidden assumption, the 3-5 walk-away checks, and each tripwire with its calendar week.
4. For a wider framework menu (pre-mortem inside other decision methods) see `exec-problem-solving`.
