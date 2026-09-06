---
description: Build a feature and loop fix-run-fix until every test passes
argument-hint: [FEATURE]
---

Build [FEATURE], run it, read the errors, fix them, and loop until every test passes. Don't check in between rounds, keep going until it's green, then show me the diff.

Fill in the bracketed placeholders above from "$ARGUMENTS" — ask for any that weren't provided rather than guessing. This is one of the 48 "Fable 5" agentic work-order prompts (@your.aimentor) — run it as a long-horizon, self-verifying pass: don't hand control back early, and don't stop at the first file/case/round if the prompt says to keep going.
