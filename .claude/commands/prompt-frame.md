---
description: Pick the right prompting framework (TRACE, TAG, RTF, CLEAR, PACT, STAR, RISE, RASCEF) for a task and rewrite a rough prompt into it, plain-text and copy-paste ready
argument-hint: [rough prompt or task]
---

Use the `prompting-frameworks-8` skill. Input: "$ARGUMENTS"

1. If no input is given, ask for the task or paste the rough prompt.
2. Choose ONE framework with a one-line reason; show which slots are filled and which are missing.
3. Ask for missing slots in one batch (max 4). If I say "just do it", fill with assumptions labelled ASSUMED.
4. Output the finished prompt as plain text in one code block. Do not stack frameworks.
