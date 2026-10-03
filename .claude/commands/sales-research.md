---
description: Run one of the 10 sales-research prompts (1 overview, 2 news, 3 earnings, 4 pains, 5 competitors, 6 stakeholders, 7 trends, 8 tech stack, 9 buying signals, 10 champion) with web search and sources
argument-hint: <1-10> <company / title / industry / competitor / person as the prompt needs>
---

Use the skill `perplexity-sales-research-10`. Arguments: "$ARGUMENTS". The first word is the prompt number.

1. Read `.claude/skills/perplexity-sales-research-10/SKILL.md` and take that prompt exactly as written; fill the {braces} from the arguments, asking once for any that are missing.
2. Answer with WebSearch (and WebFetch for the key pages). Every claim needs a source link and a date. If a claim has no source, say "not found" instead of filling the gap.
3. Prompts 6 and 10 concern named people: use public professional sources only (press, talks, podcasts, the company site). Do not log in anywhere and do not gather personal or private details.
4. End with: the 3 facts most worth opening with, and what you could not verify.
