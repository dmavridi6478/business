---
name: ai-automations-50-marketing
description: The 50-item "AI Automations Every Marketer Can Build This Weekend" list (10 categories x 5) turned into build specs - for each automation the trigger, inputs, output, the connectors that already exist in this Claude workspace, the human approval point, and a copy-paste build prompt. Also lists the carousel's own errors (a duplicated item, two mismatched descriptions) and the stack it recommends. Use when the user wants to build, pick or sequence a marketing, sales, SEO, email, social, research or reporting automation, or asks which automation to build first.
---

# 50 AI automations (marketing) - build specs

Source: @aigenesis.official carousel, 11 slides (cover, stack, 10 category slides). Read on 12 October 2026.

## Corrections to the carousel

- **49 distinct items, not 50.** "Content Quality Reviewer" appears twice on the Advanced AI Agents slide.
- On the Content slide the descriptions of three items do not match their titles: "Trending LinkedIn Post Finder" carries a blog-SEO description; "Blog SEO Optimiser" repeats the news-scanner description. Specs below use the **title's** meaning.
- It is a lead-magnet format. "Build this weekend" is optimistic for anything that touches live ads, email sends or customer data.

## The stack the carousel recommends, and what is connected here

| Carousel layer | Tool named | Available in this workspace |
|---|---|---|
| Thinking | ChatGPT / Claude | Claude |
| Automation | n8n | not connected; skills `n8n-*` exist for building flows; Zapier connector is connected |
| Connect apps | MCP servers | many connected (below) |
| Emails | Gmail | Gmail connector (drafts, search, labels) |
| Storage | Google Drive | Google Drive connector |
| Database | Sheets / Airtable | Google Sheets and Airtable connectors |
| Notifications | Slack / WhatsApp | Slack connector; WhatsApp not connected |
| Knowledge base | Notion | Notion connector |

Also connected and relevant: Google Calendar, HubSpot, Ahrefs, Semrush, Supermetrics, Klaviyo, Taplio (LinkedIn), Typefully, Fireflies, Fathom, Canva, Clay, Vibe Prospecting, Zapier. **Not connected or needs your authorisation:** Meta Ads, Google Ads, Google Search Console, Reddit, Quora (use web search or a scraper, check each site's terms).

## Rules that apply to all 49

1. **Draft, never send.** Every outward action (email, post, reply, CRM write, ad change) stops at a human approval, matching this repo's `os-approval` rule.
2. **No personal data into a prompt without a basis** (GDPR). CRM, email and review text contain it.
3. **Log each run**: input, output, who approved, date.
4. **Test on 10 real examples** before it runs unattended.

## The list

Columns: # | automation | trigger | main inputs | output | connectors to use now.

### 1. Productivity
1. Meeting Notes Processor | transcript uploaded | Fireflies/Fathom transcript | summary + decisions | Fireflies, Fathom, Notion
2. Action Item Tracker | after a meeting | transcript | tasks with owner + date | Notion, Airtable, Slack
3. Daily Task Planner | every morning | tasks, calendar | ranked day plan | Google Calendar, Notion
4. Knowledge Base Search | a question | docs, notes | cited answer | Notion, Google Drive
5. Calendar Assistant | meeting request | calendars | proposed slots, conflicts | Google Calendar, Calendly

### 2. Sales & lead generation
6. Company Intelligence Report | a company name | web, CRM | one-page report | Clay, Vibe Prospecting, web search
7. CRM Auto Updater | after a call or email | transcript, thread | proposed field updates | HubSpot, Gmail
8. Meeting Brief Generator | before a meeting | attendees, history | one briefing | Calendar, HubSpot, Gmail
9. Proposal Generator | meeting notes | notes, price list | proposal draft | Drive, Notion
10. Lead Qualification Agent | new inbound lead | form, criteria | score + reason | HubSpot, Sheets

### 3. Content
11. Daily Industry News Scanner | every morning | web | curated briefing | web search, Slack
12. Trending LinkedIn Post Finder | weekly | niche | posts worth reacting to | Taplio
13. Blog SEO Optimiser | draft done | draft | optimised version | Ahrefs, Semrush
14. Headline A/B Generator | article or ad | text | 5-10 variants | none needed
15. Multi-Platform Caption Writer | one piece of content | content | captions per platform | Typefully, Taplio

### 4. SEO & research
16. Keyword Opportunity Finder | weekly | seed topics | clustered low-competition list | Ahrefs, Semrush
17. Competitor SEO Tracker | weekly | competitor domains | change report | Ahrefs, Semrush
18. Internal Linking Assistant | article published | sitemap | link suggestions | web fetch
19. Content Gap Analyser | monthly | your site, competitors | missing topics | Ahrefs
20. AI Overview Optimiser | page update | page | changes for AI answers | `ai-search-visibility` skill

### 5. Email marketing
21. Welcome Email Writer | new subscriber | source, interests | personalised welcome | Klaviyo
22. Cart Recovery Email Generator | abandoned cart | cart, customer | recovery sequence | Klaviyo, Shopify
23. Lead Nurture Sequence Builder | new segment | segment, journey | multi-email sequence | Klaviyo
24. Newsletter Personalizer | before send | behaviour segments | per-segment edition | Klaviyo
25. Follow-up Tracker | no reply after N days | sent mail | draft follow-up | Gmail

### 6. Advanced AI agents
26. Marketing Strategy Generator | goals described | goals, data | strategy with channels | Claude + context files
27. Content Quality Reviewer | before publishing | draft | grammar, facts, brand check | `brand-reviewer` agent
28. AI Marketing Consultant | continuous | marketing data | recommendations | Supermetrics
29. Multi-Agent Campaign Planner | brief | brief | research, write, review, launch plan | `campaign-planner-multi-agent` agent
(30 on the slide repeats #27.)

### 7. Social media
31. Comment Reply Assistant | new comment | comment, voice | draft reply | Taplio, Typefully
32. Reel Script Generator | a topic | topic | script with hook and CTA | none needed
33. Carousel Creator | blog or idea | text | slide copy | Canva
34. Headline A/B Generator (repeat of #14)
35. Viral Hook Generator | any new content | content | opening hooks | none needed

### 8. Performance marketing
36. Meta Ads Library Scanner | daily | competitor pages | categorised ad database | web scraper, Airtable
37. Landing Page Auditor | URL | page | conversion fixes | `landing-page-cro-expert`
38. Search Term Analyser | weekly | Google Ads terms | negatives to add | Supermetrics
39. Keyword Cluster Builder | seed keyword | keywords | clusters | Ahrefs, Semrush
40. A/B Test Generator | ad or page | creative | test plan with hypothesis | `ab-testing`

### 9. Market research
41. Reddit Research Agent | weekly | subreddits | problem themes | web search
42. Quora Insight Finder | daily | niche | question list | web search
43. Competitor Price Tracker | daily | pricing pages | change alerts | `competitor-price-watchlist`
44. Persona Generator | new research | reviews, surveys | personas | `ai-persona-builder`
45. Voice of Customer Collector | weekly | reviews, forums | customer language | web search

### 10. Analytics & reporting
46. Meta Ads Dashboard Summary | weekly | Meta data | plain-language summary | Supermetrics
47. Google Ads Performance Reporter | every Monday | Google Ads data | optimisation report | Supermetrics
48. KPI Alert System | continuous | KPIs | alerts on unusual change | Supermetrics, Slack
49. Monthly Marketing Review | monthly | all channels | presentation-ready report | Supermetrics, Gamma
50. Attribution Summary Generator | monthly | multi-platform data | which channels contributed | Supermetrics

(Numbering follows the slides; #30 and #34 are the two repeats.)

## Build order (value to effort)

1. #25 Follow-up Tracker, #1 Meeting Notes Processor, #3 Daily Task Planner (own data, low risk).
2. #16/#17 SEO pair, #47 Monday Google Ads report (read-only).
3. #13, #35, #32 content helpers (draft only).
4. Anything that writes to a CRM, sends email or posts: last, with approval and a test set.

## Build prompt (paste, then fill the brackets)

```
Build automation #[number] "[name]" from the ai-automations-50-marketing skill.
Trigger: [trigger]. Inputs: [inputs]. Output: [output].
Use only these connectors: [list]. Stop at a human approval before anything is sent, posted or written to a CRM.
Give me: 1) the step list, 2) the exact prompt for the AI step, 3) the fields it needs, 4) a 10-example test plan, 5) what could go wrong (privacy, cost, wrong data), 6) a run log format.
Do not run it; show the plan first.
```

## Commands

`/automation-pick <your business and goal>` returns the three to build first and the build prompt for each.
