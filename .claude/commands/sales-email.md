---
description: Run one of the 9 sales-email prompts (1-9 or name) on your own inputs, with checks and compliance gates
argument-hint: <1-9 or name, then your inputs>
---

Use the `sales-email-prompt-pack` skill. Input: "$ARGUMENTS"

1. If no number or name is given, list the nine prompts in one line each and ask which.
2. Collect the bracketed inputs for that prompt; refuse to guess personal or case-study facts.
3. Run the prompt text verbatim, then the five checks (no invented facts, word count, one CTA, banned phrases, deliverability reality).
4. Output is a draft; list the compliance gates before sending.
