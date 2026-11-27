---
description: Turn a rough draft into a clean, ready-to-use prompt for a target model, with role, context, task, format and checks
argument-hint: [rough draft, target model (e.g. Fable), what good output looks like]
---

Input: $ARGUMENTS

Use `prompt-master`, `prompt-optimizer` and `claude-prompt-formula-10part`.

1. Restate the goal in one line and list what is missing (audience, inputs, format, length, constraints). Ask up to three questions only if essential.
2. Write the prompt: role, context, task, inputs with [placeholders], output format, quality checks, and what to do when information is missing. Tune wording for the target model; do not claim model-specific tricks you cannot verify.
3. Add two test inputs and a pass/fail check. Return the prompt in a code block.
