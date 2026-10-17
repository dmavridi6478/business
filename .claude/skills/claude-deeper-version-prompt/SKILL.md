---
name: claude-deeper-version-prompt
description: A one-paragraph Claude prompt shared by @nextpath.ai and Evolving AI that asks for a deeper version of a task instead of a bigger one, with the exact wording, how it works, the attribution caveat, and how to use it as /deeper-version. Use before rewriting any prompt you plan to reuse.
---

# "A deeper version, not a bigger one"

Source: two slides from @nextpath.ai reposting Evolving AI. The cover says "Anthropic lead engineer shares a prompt he uses to get better results from Claude" and names no one. The second slide is headed "A simple prompt that often helps me:". **The attribution is unverified**; judge the prompt on its own merit.

## The prompt (verbatim from the slide)
```
I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.
```

## Why it can work [Likely]
- Step 1 surfaces what you did not know to ask for.
- Step 2 pushes toward primary sources instead of summaries.
- Step 3 turns a vague task into named methods.
- Step 4 requires an external check, which guards against the model grading its own work.

## How to use
1. Paste the prompt, then your task on a new line (or run `/deeper-version <task>`).
2. Review the rewritten prompt before running it; delete anything you cannot verify or do not want.
3. Run the rewritten prompt in a fresh conversation and test the result against the external check from step 4.

Limits: the model's "top professional" is its guess, not a real expert; for medical, legal or financial tasks have a qualified person check the method.
