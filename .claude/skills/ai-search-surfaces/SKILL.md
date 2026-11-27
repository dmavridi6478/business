---
name: ai-search-surfaces
description: Explains how AI assistants find and cite a brand (the nine-step flow from user question through query parsing, retrieval agents, reasoning and memory to output) and compares the three Google surfaces - organic results, AI Overviews and AI Mode - on how each finds you, what visibility looks like, where it pulls from, how to earn it, what to track, what loses the spot and one power move. Use when planning content for AI visibility, explaining why a top-ranking page is not cited, or choosing what to measure per surface. Run via /ai-surface-plan. Sources - "How AI Search Finds Your Brand" and "How to get found in Google Organic vs AI Overviews vs AI Mode" (searchable.com) infographics.
---

# AI search surfaces

**Evidence warning.** The statistics below are copied from a vendor infographic (searchable.com) that cites no study in the image. Treat each as an unverified claim, re-check before putting any in front of a client, and do not use them as targets.

## 1. The nine-step flow (assistants such as ChatGPT, Perplexity, Claude)

1. User asks a question. 2. The LLM search console understands intent (system prompt + query parsing). 3. It produces a refined question. 4. The model finds sources through retrieval agents. 5. Agent A reads public web sources (blogs, news, social posts); Agent B uses search engines. 6. Data is delivered back to the model; for hard questions an extra-thinking reasoning model is chosen. 7. The final answer is built. 8. Memory (short-term, long-term) is used. 9. Output is shown.

Two implications drawn in the source: make content **crawlable and public**; optimise for **both Google SEO and AI retrieval**.

## 2. Three surfaces compared

| | Google Organic | AI Overviews | AI Mode |
|---|---|---|---|
| How it finds you | One query, one ranked list; Google crawls, indexes and ranks pages against the words typed | Grounded in the existing index; fans the query into sub-searches, then writes one short answer; citation is at **passage** level | Same index, more stages; one question triggers many parallel sub-searches; conversation keeps context across follow-ups |
| What visibility looks like | Blue link, title and description, a measurable position | Source chips beside the answer, linked to organic results | Inline links inside a conversational answer |
| Where it pulls from | Indexed pages, ranked against the literal query | Claimed split of cited pages: organic top 10 = 38%, rank 11-100 = 31%, outside top 100 = 31% | Claimed: same URLs as Overviews for the same query only 13.7% of the time; Wikipedia share of citations 28.9% vs 18.1%; leans encyclopaedic |
| How to earn it | Build the entity first (identity, topics, clusters); refresh before publishing new; audit schema, content decay, Core Web Vitals; cover the whole topic | Lead with the answer in 40-60 words; question-based headers; FAQ and HowTo schema on commercial pages; update quarterly | Connected topic clusters; map questions nobody typed and answer them; aim to rank across the fan-out not the head term; identical entity information everywhere |
| What to track | Rank, clicks, impressions in Search Console | Citation share on the queries that matter | The same buyer questions again, separately - an Overview citation does not mean an AI Mode citation |
| What loses the spot | Submitting the sitemap to Google alone when ChatGPT leans on Bing | Assuming a top-ten rank carries you | Single-page optimisation |
| Power move | Get cited in the Overview above your listing (source claims +120% organic clicks per impression for cited brands) | Study the real competition: the source claims ~60% of Overview responses name no brand | Win the Overview first (claimed 61% chance of appearing in AI Mode too), then check who joined you |

Other claims in the source, same warning: with an Overview present the top page loses 58% of clicks; position one 50.8% and position two 46.4% (as printed); Overview answers roughly four times shorter than AI Mode; AI Mode names 3.3 brands on average vs 1.3; 11% of Overviews cite nothing outside; about two thirds of citations come from outside the top ten.

## Action plan (feeds `/ai-surface-plan`)

1. List the 20 questions that matter commercially. 2. For each, record today's organic rank, whether an Overview appears, and who is cited. 3. Fix answer-first structure and schema on pages for questions where you rank but are not cited. 4. Build a cluster for questions where you do not rank. 5. Submit the sitemap to Bing Webmaster Tools as well as Google. 6. Re-measure monthly; report citations gained, not impressions.

## Repo mapping

`ai-search-visibility` (five-discipline wheel, 15-day plan), `aeo-diagnostic-metrics` / `aeo-score`, `ai-seo`, `seo-geo-tool-stack`. Ahrefs Brand Radar and Semrush are connected in this account and can supply citation data; Search Console is not.

## Keywords
AI Overviews, AI Mode, answer engine optimisation, GEO, citation share, retrieval agents, LLM search
