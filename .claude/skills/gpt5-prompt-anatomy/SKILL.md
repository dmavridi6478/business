---
name: gpt5-prompt-anatomy
description: A six-part prompt structure (role, task, context, reasoning, output format, stop conditions) taken from an @ai_slacker carousel titled "OpenAI just shared how to write GPT-5 prompts that feel like magic", with an original reusable template, a worked example, and notes that the "OpenAI shared" claim is not verified and the structure works on any model. Use when a prompt returns vague or sprawling answers and you want a checklist to tighten it.
---

# Anatomy of a strong prompt in six parts (Batch 135)

Source: a carousel by @ai_slacker, which says the structure comes from OpenAI. [Guessing] It matches general prompting guidance, but the slides give no link, so treat the attribution as unverified. The structure is model-agnostic: it works for Claude too.

| Part | What it does | Question to answer |
|---|---|---|
| 1. Role | Sets the perspective | Who should the model act as? |
| 2. Task | States the action or outcome, with steps to follow and exclusions | What exactly must be done, and what must be left out? |
| 3. Context | Gives background, constraints, quality bar | What does it need to know to do this well? |
| 4. Reasoning | Asks it to check its work before answering | How should it vet options before replying? |
| 5. Output format | Fixes the shape of the answer | Bullets, steps, table, narrative? Which columns? |
| 6. Stop conditions | Says when it is finished | What makes the answer complete? |

The slides' worked example is a learning-methods coach: a role, a short checklist of steps, "top 3 less-known methods for a new skill in 90 days", exclusions (generic videos, mainstream courses, a standard textbook), accuracy rules, a vet-before-reply step, a Markdown table with set columns, and a stop rule ("three verified, unique methods").

## Original template
```
ROLE: Act as [role] focused on [domain].
TASK: [Outcome]. Before answering, list 3-7 steps you will follow. Exclude: [list].
CONTEXT: [Audience, constraints, sources you trust, quality bar, time or length limits].
REASONING: Check each item against the constraints and cite the source for each factual claim. If something cannot be verified, say so.
OUTPUT FORMAT: [Table with these columns: ...] followed by [one-line summary].
STOP WHEN: [Number] items are returned, each verified and different, and the checks above are met.
```

## Cautions
- "Think step by step" may not help models that already reason; asking for a short checklist of steps and a verification pass is usually safer than asking for long visible reasoning.
- A stop condition does not make a model verify: it still needs sources you can open.
- Exclusion lists can over-constrain; keep only exclusions you care about.

Run with `/gpt5-prompt <rough request>`. Related: `prompt-engineering-patterns`, `claude-prompt-frameworks`, `claude-prompt-formula-10part`, `prompt-master`, `fable-prompter`.
