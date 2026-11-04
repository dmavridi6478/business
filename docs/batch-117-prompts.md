# Batch 117 prompts (plain text, copy and paste)

Sources: the Natan Mohart McKinsey framework graphics, the Richard Yu "6 prompts" infographic, the Automated Digital Make-to-n8n cards. Prompts 1 to 6 and 7 are verbatim from the graphics; 8 and 9 are original.

## 1 to 6. Build a digital product (verbatim)

1. Act as a digital product strategist. My buyer is [who]. They want to go from [before] to [after]. Write this transformation as one clear sentence.
2. Build a 5-module digital product teaching [result] to [avatar]. For each module give a title, 3 to 5 lessons, and the key takeaway.
3. Here's my outline. Remove anything that doesn't directly help the buyer reach [result], and reorder the rest into the simplest logical path.
4. Write Module [X]: [title]. Make it a clear step-by-step lesson with one worked example. Keep it simple enough for a beginner to follow.
5. Rewrite this in a direct, personal voice. Keep the structure, but leave space for me to add my own story and examples. Flag where my experience would strengthen it.
6. For each module, suggest where a real result, screenshot, or before-and-after example would make the lesson more convincing.

Slash command: `/digital-product-6`.

## 7. Make blueprint to n8n (verbatim, from the card)

Convert this Make blueprint to n8n. First map each module to an n8n node and flag gaps. Then output importable workflow JSON.

Add before sending: attach the exported blueprint .json; say the target is n8n and that every Make module should become a native n8n node where one exists; ask for the mapping table first and approve it before any JSON is written. Slash command: `/make-to-n8n`.

## 8. Four-lever change check (original; Influence Model)

I am leading this change: [describe the change, who is affected, the date]. Score each of the four levers from 1 to 5 with one sentence of evidence from what I tell you: (1) understanding and conviction, (2) formal mechanisms (KPIs, incentives, structure), (3) talent and skills, (4) role modelling. For each lever answer the "ask your team" question, list the red flags that apply, and propose one move. Name the weakest lever and say what would change your score. Do not invent facts; list what you need to ask me.

## 9. Pick the right McKinsey framework (original)

My decision is: [one sentence]. Data I have: [list]. From these ten frameworks pick the best fit and one runner-up, and say why: Influence Model, Consumer Decision Journey, Three Horizons, Business System, 7S, Portfolio of Initiatives, Strategic Control Map, Industry Cost Curve, GE-McKinsey Matrix, SCP. List the inputs it needs, which I have and which are missing, then run it step by step with the arithmetic shown. Finish with one action, an owner, a review date and what would make the result wrong. Slash command: `/mckinsey-framework`.
