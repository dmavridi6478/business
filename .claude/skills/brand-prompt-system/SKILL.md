---
name: brand-prompt-system
description: 'A repeatable way to make AI produce on-brand assets: set the visual language once with a brand-language prompt (asset, audience, brand rules, goal, content, hierarchy, one call to action, editable output, no invented claims), generate three layout directions (editorial, bold graphic, minimal) with a recommendation, feed the same brand system to Canva AI, then run a five-point quality check. Use when briefing Claude, Canva AI or any design tool for posts, decks, flyers or documents. Source: @earchoe AI playbook 12/21 "Make Canva AI work like your brand assistant".'
---

# Brand prompt system

"The goal is not 'make a pretty design'. Give AI a brand system, then refine the editable result." Brand context turns AI from a random generator into an assistant. Flow: input, AI, output, check.

## Prompt 1 - set the visual language
```
Create a [ASSET] for [AUDIENCE].

Brand rules: [COLOURS / FONTS / TONE / STYLE].
Goal: [OUTCOME].
Content: [TEXT / OFFER / DATA].

Use a clear hierarchy, strong spacing and one primary call to action. Keep every generated element editable. Do not add claims or statistics that I did not provide.
```
Before sending: replace every [BRACKET]; attach the source if needed; read and verify before use.

## Prompt 2 - generate the variations
```
Give me 3 layout directions: editorial, bold graphic and minimal. For each, explain the hierarchy and where the viewer's eye should go first. Then recommend the layout that best serves the information, not the one that merely looks decorative.
```

## Canva AI (feed it your brand system)
Give it three things: **brand** (colours, fonts, tone, audience, visual rules), **job** (what you are actually designing), **review** (check every generated element before publishing). In this workspace Canva is a connected connector (`mcp__Canva__*`), and the Canva brand kit can be listed with `list-brand-kits`. Use `docs/marketing-context/` (voice, banned phrases, proof) as the brand rules.

## Canva AI quality check
1. Give AI the brand rules. 2. Provide the actual content. 3. Keep claims grounded. 4. Make the hierarchy obvious. 5. Edit the final design yourself.

## Sellable version
Offer branded content systems to small businesses: define the brand rules once, then create repeatable social posts, presentations, flyers and documents. Sell a defined result, a repeatable process and a clear quality check, not "I know how to prompt".

## Procedure for Claude
Ask for the six bracket values; if brand rules are missing, read `docs/marketing-context/voice.md` and the design tokens in `design-templates`. Refuse to add statistics not supplied. Output the three directions with a one-sentence reason for the pick. Command: `/brand-prompt`. Rendering: `design-templates` > `playbook-workflow-beige.html`.

## Keywords
brand, Canva AI, visual language, layout, editorial, minimal, brand system, hierarchy
