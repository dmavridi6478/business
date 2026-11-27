---
name: digital-marketing-claude-prompts-6
description: The six digital-marketing Claude prompts visible on an "11 Digital Marketing Claude Prompts" cheat sheet (SEO content brief, competitor content gap, blog to LinkedIn posts, newsletter outline, ICP pain points by awareness stage, personalised cold outreach) quoted verbatim, with the quality checks the sheet omits (sourced data, claims, outreach law) and a note that prompts 7 to 11 were not in the image. Use when drafting SEO, content and outreach with Claude.
---

# Digital marketing Claude prompts (6 of 11 visible)

Source: a cheat-sheet image (Batch 128) titled "11 Digital Marketing Claude Prompts". **Only prompts 1 to 6 appear in the image; 7 to 11 were not sent and are not recreated.** Quoted verbatim; replace the <angle brackets>.

| # | Prompt (verbatim) |
|---|---|
| 1 | You're a senior SEO strategist. Build a detailed content brief for the keyword: <INSERT KEYWORD>. Include H1, H2s, target word count, search intent, FAQs, internal linking ideas, and meta description. |
| 2 | Compare my website <INSERT URL> against <INSERT COMPETITOR URL>. List 10 SEO content topics they rank for that I don't. Prioritize by traffic potential. |
| 3 | Turn this blog post into 5 LinkedIn posts. Punchy hooks, actionable takeaways, no emojis or hashtags. |
| 4 | Write a Sunday newsletter outline on <INSERT TOPIC> for an audience of 7,000+ SEOs and marketers. Hook them in 2 lines, deliver 3 actionable insights, end with a CTA. |
| 5 | You're a B2B marketing strategist. List the top 10 pain points of <INSERT ICP>. Group by awareness, consideration, and decision stages. |
| 6 | Write 3 personalized cold outreach emails to <INSERT ROLE> at <INSERT COMPANY TYPE>. Reference their recent activity, lead with value, and end with a soft CTA. |

Margin notes on the sheet: "pain points drive content" (prompt 5) and "value first" (prompt 6).

## Checks the sheet leaves out
1. **Prompt 2 needs real data.** A model given two URLs cannot see rankings or traffic. Supply an export from a rank tracker (Ahrefs, Semrush) or Search Console, otherwise the "topics they rank for" are guesses. Ask it to label each topic as from-data or inferred.
2. **Prompt 1 invents intent and word counts.** Check search intent against the live results page and use real competitor word counts.
3. **Prompt 3 should not overstate the post.** Tell it to use only claims present in the source and to keep every figure and quote exact.
4. **Prompt 4 contains an audience claim.** "7,000+" is the sheet author's list; replace it with yours.
5. **Prompt 5 is hypothesis generation.** Pain points from a model are not research. Validate against five customer calls or support tickets before building content on them.
6. **Prompt 6 and outreach law.** "Reference their recent activity" means processing personal data. Use public professional sources, keep a source note, and check email and privacy rules for your regions (see `tam-mapping-6-steps`). Keep drafts for human review.
7. **Sourced facts.** Ask for a link and date for every factual claim, and spot-check three.

Related: `claude-marketing-jobs`, `seo-prompts-10` (command), `content-strategy`, `ai-search-visibility`, `cold-email`, `carousel-writer`, `newsletter-writer`, `claude-sales-prompts-20`. Run with `/dm-prompt <1-6> <keyword, URL, topic or ICP>`.
