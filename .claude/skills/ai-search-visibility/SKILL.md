---
name: ai-search-visibility
description: Plan, audit, or improve marketing and search visibility in the AI-search era (2026+) — covering the five-discipline SEO wheel (SEO / SXO / AEO / GEO / AIO), the modern marketing taxonomy, the five board-level exec questions (cohort revenue, marginal CAC, payback period, contribution margin, channel concentration), a sequenced 15-day action plan for improving AI search visibility, and a 20-source ecosystem map with live connector check. Also covers the tactical page-level implementation that makes a site readable by AI assistants: semantic HTML, meta descriptions on every page, llms.txt AI guide, robots.txt, and an optional "Ask AI about me" block. Use whenever auditing search/AI visibility, building a marketing plan or content calendar, structuring a CEO/board marketing report, evaluating marketing KPIs, discussing AEO/GEO/AI citations, wanting a day-by-day plan to get cited by AI, or building/auditing any personal or business site where AI discoverability is a goal.
---

# AI Search Visibility

Consolidates: `ai-search-marketing-2026`, `ai-discoverable-site`.

## When to use which reference

- **Auditing or improving search/AI visibility** (SEO, AEO, GEO, SXO, AIO) → `references/seo-wheel-2026.md`
- **A concrete day-by-day plan to improve AI search visibility** → `references/15-day-ai-search-action-plan.md`
- **Building a marketing plan, content calendar, or explaining what modern marketing covers** → `references/marketing-taxonomy.md`
- **Building/reviewing a marketing dashboard, CEO/board report, or challenging vanity metrics** → `references/exec-ai-questions.md`
- **"Where" AI visibility work needs to happen, or which sources this account can monitor with a live connector** → `references/ai-search-visibility-ecosystem.md`

Read only the reference(s) relevant to the request — don't load all five for a narrow question.

---

## PART 1: STRATEGY & REPORTING FRAMEWORK

Source: five infographics synthesized into one operating framework (AI marketing analytics questions — D. Manela; Modern Marketing 2026 taxonomy — Searchable.com; SEO in 2026 wheel — E. Möller; 15-Day AI Search Action Plan — Searchable.com; AI Search Visibility Ecosystem — Searchable.com). This is a **planning and audit lens**, not raw data — always ground specific numbers/claims in the user's actual analytics.

### Core operating principle: the two-question test

Before applying any checklist below:

1. **Is the number about to be reported a blended average or a marginal/cohort truth?** Blended numbers (overall CAC, overall revenue trend) systematically hide decay and waste. If a report or dashboard only shows blended figures, flag it — that is the single most common marketing-reporting failure this framework exists to catch.
2. **Which of the five search-visibility disciplines does this task actually touch?** Most people conflate "SEO" with all five. Naming the discipline (SEO vs SXO vs AEO vs GEO vs AIO) changes what "ranking higher" even means.

### The five disciplines

| Code | Full name | What it optimizes |
|---|---|---|
| SEO | Search Engine Optimisation | Organic rankings on Google (keywords, links, site health) |
| SXO | Search Experience Optimisation | On-site conversion once a visitor arrives |
| AEO | Answer Engine Optimisation | Being the direct answer inside AI Overviews / AI Mode |
| GEO | Generative Engine Optimisation | Being cited/summarised by ChatGPT, Perplexity, Gemini, Claude |
| AIO | AI Optimisation | Being accurately represented in the data AI models train on (Wikipedia, structured docs) |

### The five exec questions

1. Cohort revenue, not blended revenue — is growth from new customers or old ones?
2. Marginal CAC, not blended CAC — what does the *next* customer cost?
3. Payback period, by channel — how long until each channel's spend returns?
4. Contribution margin trend — what's left of revenue after variable costs?
5. Channel concentration — what % of acquisition comes from the top 1–2 channels? (>60% is a red flag)

### Output conventions

- Structure findings by discipline/question, not as a flat list.
- When the user's own data contradicts the framework's illustrative examples, trust the user's data. This framework supplies structure and questions, not benchmarks.
- Greek-language deliverables: keep AEO, GEO, SXO, AIO, SEO, CAC, ROAS, LTV as untranslated English acronyms (per user's standing instruction to preserve original terms in Greek output). No punctuation in fully-capitalized Greek titles.

---

## PART 2: TACTICAL SITE IMPLEMENTATION

Source: a "Claude Code builds" screenshot carousel (@theromanknox) demonstrating AI discoverability on a personal portfolio/profile site. The deployment mechanics are environment-specific — the four essentials and the "Ask AI about me" pattern are the portable, reusable part.

### Four essentials for AI readability

1. **Semantic, well-structured HTML** — real `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, heading hierarchy that actually nests (h1 → h2 → h3), not div soup. AI crawlers parse structure, not just visible text.
2. **Meta descriptions on every page** — a concise, accurate `<meta name="description">` per page, not just the homepage.
3. **`llms.txt` as an AI guide** — a plain-text file at the site root summarizing what the site/person/company is, key pages, and how to characterize them accurately. Treat it as a short brief for an AI assistant, not SEO keyword stuffing.
4. **`robots.txt` at the root** — explicit, so AI crawlers (and everyone else) know what's allowed.

This site-level implementation is the tactical execution layer for the AEO/GEO/AIO disciplines in Part 1. Run Part 1's audit to identify which disciplines need attention; then use these four essentials to address the AEO/GEO/AIO findings at the page level.

### Optional: "Ask AI about me" block

A footer block with buttons for ChatGPT, Claude, Perplexity, and Gemini. Clicking one opens that provider in a new tab with a pre-populated prompt:

> "Tell me about [name] based on [domain]. Summarize who they are, what they do, and how to get in touch."

Implementation notes:
- Each provider's support for pre-filling a prompt via URL query parameters differs and changes over time — verify current behavior for each provider before shipping, rather than assuming a pattern from an older screenshot still works. Where a provider doesn't support URL pre-fill, fall back to opening the provider's homepage and copying the prompt to the clipboard with a "prompt copied — paste it in" toast.
- Populate `[name]` and `[domain]` from the site's actual identity/positioning (see `product-marketing-context`), not a placeholder.
- This block only pays off once the four essentials above are in place — an AI-prompt button on a page with no semantic structure, no meta description, and no llms.txt sends the visitor to an AI that still has nothing solid to say.

---

## Related skills in this repo

- **claude-seo**: Full technical SEO with 24 sub-skills, Python runtime (`claude-seo` command), and `/seo` slash commands — use for deep on-page/technical SEO work rather than the strategic/reporting layer here.
- **content-strategy**: Use the marketing taxonomy's "Content Strategy" branch and the AEO "lead with the answer" pattern to shape what gets written, not just how it's structured technically.
- **business-intelligence-report** / **ceo-reporting-skill**: Run the five exec questions (`exec-ai-questions.md`) against any marketing section of these reports before they go to a CEO or board.
- **quarterly-okr-architect**: The 15-day action plan's Day 15 "next 30-day plan" is a natural input to a quarterly goal cascade for marketing/growth.
- **growth-operating-framework**: That skill's Step 2 (North Star metric) and Step 3 (data foundation) overlap with this skill's exec-questions discipline.
- **product-marketing-context**: Source of the "who they are, what they do" summary that populates both `llms.txt` and the pre-filled "Ask AI about me" prompt.
- **frontend-design** / **web-artifacts-builder**: Implementation of the actual page structure and the AI-prompt block.
- **design-dev-resources**: Real provider logos (via SVGL) for the ChatGPT/Claude/Perplexity/Gemini buttons.
