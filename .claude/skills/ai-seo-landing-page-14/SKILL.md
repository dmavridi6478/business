---
name: ai-seo-landing-page-14
description: Fourteen-element anatomy of a landing page built to be quoted by AI search (question H1, named byline, outcome subheadline, question subheadings, 40 to 60 word answer block, crawlable build, problem block, FAQ block, solution block, schema, proof block, comparison table, one pricing CTA, last-updated stamp), with a pass or fail audit and the claims the graphic gets wrong or overstates. Use when writing or auditing a landing page for AI search visibility.
---

# The AI-SEO landing page: 14 elements

Source: a "The Million-Dollar Landing Page" infographic by Ankit Sharma (Batch 119). The title is hype: the graphic gives no evidence that this structure earns citations or revenue. [Guessing] It is a sound checklist because each element makes a page easier to read, to trust and to quote. Treat it as a hypothesis to test, with before and after tracking.

| # | Element | What the graphic says | Pass test (added) | Caution |
|---|---|---|---|---|
| 1 | The H1 | The question your buyer would type, answered in the same line | One H1 that matches a real query and states the answer | Do not keyword-stuff; use the words of search data or sales calls |
| 2 | The byline | A named author with photo, credentials and bio link | Real person, verifiable credentials, bio page | Never invent an author or credentials |
| 3 | The subheadline | One line naming the outcome they walk away with | One sentence, one outcome, no jargon | No outcome you cannot document |
| 4 | Question subheadings | Every H2 and H3 as a real question | Each heading is a question followed by a direct answer | Forced questions read badly; use where a question is natural |
| 5 | The answer block | A 40 to 60 word answer to the main question, up top, above the fold | Count the words; answer stands alone | The word range is the card's rule of thumb, not a documented requirement |
| 6 | The build | Raw HTML, copy as text, alt text on images, transcript under the video, nothing hidden from crawlers | Key copy visible with JavaScript off; alt text and transcript present | Several AI crawlers do not render JavaScript; check each one's documentation |
| 7 | The problem block | Name the problem in their words, then show what it costs them | Uses customer language from interviews; one quantified cost | Cite or label the number |
| 8 | The FAQ block | Real questions as headers, clean answers, marked up | Questions come from sales, support or search data | See the schema note below |
| 9 | The solution block | How you solve it, led by the outcome, closing on one clear next step | Outcome first, mechanism second, one next step | |
| 10 | Schema in the head | Organisation, FAQ, Product and Article schema | Valid JSON-LD that matches visible content | Schema must describe what is on the page; never add reviews, ratings or prices that are not visible |
| 11 | The proof block | Named case studies with real, checkable numbers, plus original data | Named customer, number, date, source | Get permission to name customers; no fabricated testimonials |
| 12 | The comparison table | Features and pricing versus the alternatives | Fair, dated, sourced; includes where a competitor wins | Check claims about competitors; ads and comparison rules differ by country |
| 13 | The pricing CTA | One action button in plain words | One primary action, plain verb | |
| 14 | The last-updated stamp | A visible last-updated date and fresh schema | Date changes only when content changes | Bumping the date without real changes is deceptive and search engines say not to do it |

The graphic also shows a "trusted by" logo strip under the subheadline. Use only logos you have permission to show.

## Schema notes (checked)
- [Certain] Since 2023 Google shows FAQ rich results only for well-known government and health sites, so FAQ markup on a commercial page will not get the rich result. It can still help machines parse the page, but "so AI pulls them straight in" is the card's claim, not something I could confirm.
- Put schema where the platform supports it (JSON-LD in the head or the body both parse). Validate with a structured-data testing tool before shipping.

## Audit procedure
1. Fetch the page as raw HTML (not rendered). List which of the 14 elements are present in that HTML.
2. For each missing element, say whether the page needs it (a pure product page may not need a long FAQ).
3. Check the answer block word count and that the answer is correct and sourced.
4. Check claims, logos, author and proof for permission and truth.
5. Output: a table of 14 rows (present, partial, missing), the three highest-impact fixes, and a measurement plan: AI-citation checks on five target questions before and after, plus organic traffic and conversion.

Run with `/ai-landing-audit <url or pasted HTML>`.

## Related
`ai-seo`, `schema`, `aeo-diagnostic-metrics`, `ai-search-visibility`, `llm-visibility-prompt-check`, `brand-landingpage`, `campaign-page-one-shot`, `cro`, `site-architecture`.
