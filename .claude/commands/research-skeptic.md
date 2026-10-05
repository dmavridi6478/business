---
description: Run one of the 6 research-skeptic prompts (1 agree, 2 original source, 3 counter-evidence, 4 unknowns, 5 weakest source, 6 save-this)
argument-hint: <1-6> <topic, claim or conclusion>   (for 4 and 5, paste the research or sources after it)
---

Use the skill `research-skeptic`. The first word of "$ARGUMENTS" is the prompt number (1 to 6); the rest is the topic, claim or conclusion, and for prompts 4 and 5 the pasted research or sources.

1. Read `.claude/skills/research-skeptic/SKILL.md` and take that prompt exactly as written.
2. Fill the [BRACKETS] from the arguments. If the material for prompt 1, 4 or 5 is missing, ask the user to paste it; do not search the web unless they ask.
3. Answer the prompt. Mark every judgement CERTAIN (you can point to the text), LIKELY, or GUESSING, and say which of the user's sources you actually read. If a claim cannot be traced from what was provided, say "cannot trace from what you gave me" rather than inventing a source.
4. End with the single next piece of evidence that would most change the conclusion.
