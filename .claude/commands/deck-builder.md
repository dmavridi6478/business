---
description: Build a finished slide deck from an outline, using the Gamma connector if connected, otherwise a slide-by-slide spec
argument-hint: [outline, audience, length, tone]
---

Input: $ARGUMENTS

Use `claude-presentation-prompts`, `presentation-frameworks-5` and `pptx`.

1. Check whether a Gamma connector is available in this session. If yes, ask me to confirm the title, slide count and theme, then generate and give the link. If not, say so and continue.
2. Otherwise write a slide-by-slide spec: message title, one visual idea, three or fewer bullets and speaker notes per slide, with one source per number.
3. Open with the answer, close with the ask. Flag any slide that needs data I have not given. Do not invent figures.
