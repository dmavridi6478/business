---
description: Do a task, then have a fresh subagent verify and flag holes, loop to clean
argument-hint: [TASK], [GOAL]
---

Do [TASK], then spin up a fresh subagent to verify it against [GOAL] and flag every hole. Fix them and re-verify. Repeat until it passes clean, then show what changed.

Fill in the bracketed placeholders above from "$ARGUMENTS" — ask for any that weren't provided rather than guessing. This is one of the 48 "Fable 5" agentic work-order prompts (@your.aimentor) — run it as a long-horizon, self-verifying pass: don't hand control back early, and don't stop at the first file/case/round if the prompt says to keep going.
