---
description: Audit a landing page against the 14-element AI-SEO anatomy (question H1, byline, answer block, FAQ, schema, proof, comparison table, CTA, last-updated) and propose fixes
argument-hint: [page URL, or paste the page HTML or copy]
---

Use the `ai-seo-landing-page-14` skill.

Input: $ARGUMENTS

1. Get the raw HTML of the page (fetch it, do not rely on a rendered view). If I pasted HTML or copy, use that and say what you could not check.
2. Score each of the 14 elements as present, partial or missing, with the evidence (quote the line or tag).
3. Check the answer block word count (40 to 60), that every H2 and H3 that should be a question is one, that key copy is visible without JavaScript, and that schema matches visible content.
4. Flag anything that would be deceptive or unsafe to publish: invented author or credentials, unpermitted logos, unsourced numbers, fake freshness, markup for content that is not visible.
5. Give the three highest-impact fixes with example copy, then a measurement plan (five target questions checked in AI search before and after, plus traffic and conversion). Do not promise citations.
