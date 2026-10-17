---
name: claude-seo-10-prompts
description: Ten fill-in-the-bracket Claude SEO prompts (keyword research, content brief, SERP analysis, internal linking, meta data, content upgrade, FAQ schema, competitor gap, repurposing, monthly report summary) from the "10 SEO Claude Prompts" graphic, with plain-text versions to copy. Use to run a lean SEO workflow in Claude. Complements the 10-prompt command seo-prompts-10, which covers different prompts.
---

# 10 SEO prompts for Claude (graphic, Batch 111)

Source: one graphic, "10 SEO Claude Prompts", with a title and a one-line brief per prompt. Only the briefs were printed, so the prompt text below is **my expansion of each printed brief**, with the printed wording kept in the first line. Replace every [bracket]. The graphic gave no data source or accuracy claim, so none is made here.

Claude has no access to live search volumes, rankings or SERPs unless a connector (Ahrefs, Semrush, Search Console) or web search is on. Treat "difficulty" and "volume" it invents as guesses and verify them in a tool.

## The ten prompts (plain text)

**01 Keyword Research**
Give me 20 long-tail keyword ideas for [main keyword]. For each, state the search intent, an estimated difficulty (low, medium or high, and say it is an estimate), and why it matters for a [ICP] audience.

**02 Content Brief**
Write a content brief for [keyword or topic] for [ICP]. Include the H1, H2 and H3 outline, a target word count, primary and secondary keywords, 5 FAQs, a meta description under 155 characters, and a call to action.

**03 SERP Analysis**
Here are the top 10 results for [keyword]: [paste titles, URLs and key headings]. Say what they cover, what they all miss, and give me 5 angles a new article could take to stand out.

**04 Internal Linking**
Here are 20 of my posts: [paste titles and URLs]. Propose an internal linking structure: which posts are pillars, which link to which, and the anchor text for each link. Flag orphan posts.

**05 Meta Data**
For this page [paste URL or text], write 5 title tag and meta description variations. Titles under 60 characters, descriptions under 155, each with the primary keyword [keyword] and a different angle.

**06 Content Upgrade**
Read this post [paste text]. Identify its 5 weakest sections and, for each, say why it is weak and how to upgrade it (data, example, structure or depth).

**07 FAQ Schema**
Write 8 question and answer pairs about [topic] suited to featured snippets (answers 40 to 60 words), then output them as valid FAQPage JSON-LD.

**08 Competitor Gap Analysis**
Here are 3 competitor posts on [topic]: [paste text or URLs]. List the subtopics they cover that my post [paste] does not, and the subtopics none of them cover.

**09 Content Repurposing**
Turn this post [paste] into 8 pieces of content for other channels (for example LinkedIn post, email, carousel, short video script). One line on the hook for each.

**10 Monthly SEO Report Summary**
Here is this month's data [paste clicks, impressions, rankings, conversions vs last month]. Summarise the wins, the concerns and 3 actions for next month. Do not invent numbers that are not in the data.

## Guardrails
- **[Certain]** Prompts 03, 04, 06 and 08 need the real text or URLs pasted; without them Claude will invent plausible competitor content.
- **[Likely]** Prompt 07 FAQ markup no longer gives rich results for most sites in Google; use it for structure and AI-search readability, not for a SERP feature.
- Run `/seo-claude-prompt <1-10> <inputs>` to execute one. Related skills here: `seo`, `claude-seo`, `ai-seo`, `programmatic-seo`, and the command `/seo-prompts-10` (a different ten).
