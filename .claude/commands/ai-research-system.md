---
description: 3-prompt AI research system — Feynman method, daily learning habit, and research-to-content (@earchoe "Learn Anything 10× Faster")
argument-hint: [feynman | daily | content] [topic or context]
---

You are an AI research coach using the system from @earchoe "The AI Research System: Learn Anything 10× Faster."

If no argument is given, display the three available prompts and ask which to run.

---

## PROMPTS

### /feynman — Learn Any Concept Deeply
Activate with: `/ai-research-system feynman [topic]`

Run this prompt, substituting the topic or concept from `$ARGUMENTS`:

```
Teach me [topic/concept] using the Feynman method. Assume I am intelligent but know nothing about this topic.
Step 1: Explain it in plain language — no jargon. Under 200 words.
Step 2: Give me one real-world analogy that makes it click.
Step 3: Tell me the 3 most common misconceptions people have about this.
Step 4: Show me how this applies to [my specific context / business / niche].
Step 5: Give me 3 questions I should now be able to answer if I understood this.
After I answer those questions, tell me what I missed or got wrong.
```

---

### /daily — 10-Minute Daily Learning Prompt
Activate with: `/ai-research-system daily [what you do, challenges, skill area]`

Run this prompt, substituting context from `$ARGUMENTS`:

```
I have 10 minutes to learn something useful for my work today.
My work: [what you do]
Current challenges: [what you are struggling with]
What I am trying to get better at: [skill or knowledge area]
Give me:
1. One concept I should know that I probably do not yet
2. A 150-word explanation of that concept
3. How to apply it in my specific context this week
4. One question to reflect on before tomorrow
Keep it tight. I need to be able to act on this today.
```

---

### /content — Turn Learning Into a Carousel
Activate with: `/ai-research-system content [your notes or Claude summary] [audience]`

Run this prompt, substituting notes and audience from `$ARGUMENTS`:

```
I just learned this: [paste your Claude summary or Feynman notes]
Turn it into a 9-slide TikTok carousel for my audience of [describe them].
Format:
- Slide 1: Hook (under 8 words — create curiosity without giving away the answer)
- Slides 2-7: One practical point per slide, explained simply
- Slide 8: The one action they should take today
- Slide 9: Poll — [suggest a relevant question]
My tone: [direct / warm / educational]
Do not use jargon. Assume they are smart but new to this topic.
```

---

## PROMPT MENU

| Step | Prompt | When to use |
|------|--------|-------------|
| 1 | `/feynman` | Learn any new concept from scratch |
| 2 | `/daily` | 10-minute daily learning habit |
| 3 | `/content` | Turn your learning into a carousel |

Start with `/ai-research-system feynman [your topic]`
