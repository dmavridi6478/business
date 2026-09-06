---
description: Give an agent a goal and let it plan/execute/check its own steps, capped
argument-hint: [GOAL], [N]
---

Give an agent this goal: [GOAL]. Let it plan its own steps, work through them, check its own output, and surface only when it's done or genuinely stuck. Cap it at [N] steps.

Fill in the bracketed placeholders above from "$ARGUMENTS" — ask for any that weren't provided rather than guessing. This is one of the 48 "Fable 5" agentic work-order prompts (@your.aimentor) — run it as a long-horizon, self-verifying pass: don't hand control back early, and don't stop at the first file/case/round if the prompt says to keep going.
