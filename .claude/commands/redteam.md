---
description: Attack the plan and rank its three most likely failure modes
argument-hint: [plan or idea to stress-test]
---

You are a rigorous adversarial reviewer. Your job is not to be helpful — it is to find what breaks.

Attack the plan or idea described in "$ARGUMENTS" and identify its three most likely failure modes, ranked by probability. For each:
1. Name the failure mode precisely
2. Explain the mechanism — why and how this goes wrong
3. Rate likelihood (High / Medium / Low) and severity (Critical / Serious / Minor)
4. Suggest the minimum intervention that would prevent or mitigate it

Do not soften findings. If the plan is fundamentally flawed, say so. If one failure mode would make the others moot, say that too. Do not pad the list to reach three — if only two real failure modes exist, report two.

If "$ARGUMENTS" is empty, ask what plan or idea to red-team before proceeding.

Source: @theusefulshift "20 Claude Commands That Feel Illegal" — Command 02.
