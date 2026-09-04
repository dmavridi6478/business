---
description: Build a pipeline from input to destination with retries and logging
argument-hint: [INPUT], [STEPS], [DESTINATION]
---

Build a pipeline that takes [INPUT], runs it through [STEPS], and drops the result in [DESTINATION] with no hand-holding. Handle edge cases, retry failures, log each run.

Fill in the bracketed placeholders above from "$ARGUMENTS" — ask for any that weren't provided rather than guessing. This is one of the 48 "Fable 5" agentic work-order prompts (@your.aimentor) — run it as a long-horizon, self-verifying pass: don't hand control back early, and don't stop at the first file/case/round if the prompt says to keep going.
