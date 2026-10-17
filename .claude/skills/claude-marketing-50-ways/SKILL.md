---
name: claude-marketing-50-ways
description: The "50 ways to use Claude for marketing" graphic as a 50-verb index (research, analyze, summarize, compare, extract and so on) grouped into eight stages with a starter prompt pattern per group and the installed skills that cover each. Use to find which Claude move fits a marketing task. Not a tutorial and no claims about results.
---

# 50 ways to use Claude for marketing (graphic, Batch 111)

Source: a two-column graphic of 50 one-word verbs, each with a short benefit line (for example "30 sources, one answer", "Raw CSV, actual insights", "Stop copy-pasting your context", "Turn repeat workflows into Skills"). I could read the verbs reliably but not every benefit line, so the table keeps the **verbs as printed** and the starter prompts are **mine**.

| Stage | Verbs on the graphic | Starter prompt pattern |
|---|---|---|
| Research and learn | RESEARCH, ANALYZE, SUMMARIZE, COMPARE, EXTRACT, INTERVIEW | "Research [topic] using these [sources]. Give one answer, list the claims and the source of each." |
| Think and challenge | BRAINSTORM, CHALLENGE, CRITIQUE, VALIDATE, SIMULATE, DISPROVE, VERIFY | "Here is my plan. List the 3 weakest assumptions and what evidence would disprove each." |
| Audience and positioning | POSITION, SEGMENT, PERSONALIZE, CLASSIFY, SCORE, CLUSTER, MINE | "Segment these [responses or leads] into groups; name each, size it, say what they want." |
| Data and spreadsheets | CALCULATE, FORMULA, CLEAN, DEDUPE, DASHBOARD, AUDIT | "Clean this CSV: list problems first, then output the cleaned file and the rules applied." |
| Content and copy | EDIT, SCRIPT, HOOK, HEADLINE, REPURPOSE, FAQ, SEO, AEO, PITCH | "Give 10 hooks for [offer] for [ICP], each in a different style; mark the 2 you would test." |
| Meetings and customers | MEETING, SURVEY, DEBRIEF, SYNTHESIZE | "Turn these notes into decisions, owners and dates; flag what is unclear." |
| Production | BRIEF, PLAN, ORGANIZE, VISUALIZE, BUILD, CREATE, SCHEDULE | "Write a brief for [asset]: goal, audience, message, format, constraints, review criteria." |
| Systems | CONNECT, REMEMBER, REUSE, MONITOR | "Turn the steps we just did into a reusable skill with inputs, steps and a check." |

## Where this repo already covers it
- Prompts and roles: `claude-50-use-cases`, `claude-sales-prompts-20`, `claude-seo-10-prompts`, `one-person-marketing-team-map`, `one-person-content-system`.
- Connect: `n8n-workflow-patterns`, `brand-brain`; REMEMBER and REUSE = write a skill (`skill-creator`).
- AEO and SEO verbs: `ai-seo`, `seo`, `claude-seo`.

## Guardrails
- **[Certain]** VERIFY, VALIDATE and DISPROVE are only as good as the sources you give Claude; with no sources it will agree with you fluently.
- **[Likely]** SIMULATE (synthetic audiences) produces plausible opinions, not measured demand; confirm with real customers before spending.
- CONNECT, MONITOR and SCHEDULE touch live accounts; keep a human approval step before anything publishes or spends.
