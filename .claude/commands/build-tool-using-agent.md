---
description: Build a tool-using agent that asks before anything irreversible
argument-hint: [TASK], [TOOLS]
---

Build an agent that can [TASK] using [TOOLS]. It decides which tool to call when, handles failures, and stops to ask me only before anything irreversible. Show the decision log.

Fill in the bracketed placeholders above from "$ARGUMENTS" — ask for any that weren't provided rather than guessing. This is one of the 48 "Fable 5" agentic work-order prompts (@your.aimentor) — run it as a long-horizon, self-verifying pass: don't hand control back early, and don't stop at the first file/case/round if the prompt says to keep going.
