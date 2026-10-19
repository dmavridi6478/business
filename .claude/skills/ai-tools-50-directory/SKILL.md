---
name: ai-tools-50-directory
description: Categorised directory of 55 AI tools across seven groups - productivity and automation, image and video, audio and voice, writing and content, coding and development, SEO and marketing, design and presentation - with each tool's one-line job as printed, the connector status in this account, and a selection method that picks by job before brand. Use when someone asks "which AI tool for X", wants a lean tool stack, or needs to know whether Claude can use a tool directly. Run via /ai-tools-50. Source - "50+ Must-Have AI Tools" cheat sheet (Matic Pogladic); names and descriptions are as printed, prices are not given.
---

# 50+ must-have AI tools

Source: one cheat sheet. Product names change, merge or disappear quickly; **verify a tool still exists and check its current pricing and data terms before recommending it.** The list is a starting point for a shortlist, not a ranking.

## Directory

| Group | Tools (job as printed) |
|---|---|
| Productivity and automation | Zapier (connects apps, no coding); ClickUp (connects projects, docs, people, company knowledge); Calendly (AI-powered scheduling); Notion AI (generates, analyses, automates tasks in the workspace); Otter AI (real-time transcription, audio recording, action items); Reclaim AI (auto-schedules tasks, meetings, habits); Grammarly (writing assistant and text generation) |
| Image and video generation | Leonardo AI (production-quality visual assets); Synthesia (AI video generation); Midjourney (independent image lab); Stable Diffusion (generative model for images, music, sound); Pictory AI (videos from text, no editing); Veed GPT (video from text prompts); DALL-E (realistic images and art from a description) |
| Audio and voice | Fireflies AI (transcribes, summarises, analyses conversations); AIVA (AI music in 250+ styles); Murf AI (voice generation); Krisp (noise and meeting assistant); Descript (content analysis, topic clusters); Cleanvoice (audio clean-up); Podcastle (podcast production) |
| AI writing and content creation | Jasper AI (marketing content for teams); Hypotenuse AI (eCommerce, SEO-optimised copy); CopySmith (content tools); Writesonic (SEO-optimised on-brand content, chatbots); MarketMuse (content analysis, topic clusters); Anyword (scale on-brand content); Headlime (templates for marketing copy) |
| Coding and development | Codey (Google AI coding support); Data Analyst GPT (analyses and visualises uploaded data); Replit Ghost Writer (automates repetitive coding); GitHub Copilot (coding assistant); Tabnine (code completion, privacy); Code WP (WordPress code); Grimoire (GPT coding wizard for websites) |
| SEO and marketing | SurferSEO (research, audit, optimise articles); Yoast SEO (WordPress optimisation); Semrush (online marketing automation); INK (content creation and SEO performance); SEO Robot (SEO and ad campaigns in real time); Ahrefs (SEO tools); SEO.AI (gap finding for agencies); Tidio (chatbot and support); HubSpot (marketing, sales, customer service platform); Alli AI (rapid code and content changes for SEO) |
| Design and presentation | Slidesgo (text-to-presentation); SlidesAI (summarises and creates presentations); DesignsAI (image, video, design maker, logo maker); Prezi (impactful presentations); Vizcom (creative design tool); Visme (stunning presentations in minutes); Gamma (new medium for presenting ideas); BeautifulAI (pitches and slide decks); Canva (social posts, presentations, posters, videos); BoothAI (no-code AI workflow builder) |

## Connector status in this account (checked 19 Oct 2026)

Connected, so Claude can use them directly: **Zapier, ClickUp, Calendly, Notion, Fireflies, Gamma, Canva, Semrush, Ahrefs, HubSpot.** Available in the registry but not connected: **Otter.ai** (needs your authorisation in claude.ai connector settings). The other tools above were not individually searched; run `ListConnectors`/`SearchMcpRegistry` before saying "no connector".

## Selection method

1. Write the job in one line (e.g. "turn call recordings into action items").
2. Check the repo first: an existing skill or a connected tool may already do it (`ai-tool-finder`, `ai-tool-map`, `connector-stack`).
3. Shortlist at most 3 tools from one group; prefer connected ones.
4. Check, from the vendor's page on the day: price, free tier, export format, where data is stored, whether inputs train models.
5. Trial on one real task for a week and record time saved; keep only tools that save measurable time.
6. For customer or patient data, apply `gdpr-data-handling` and the `free-vs-paid-tool-decision` procedure before any upload.

## Rules

- Never recommend a tool solely because it appears on a list.
- Overlaps are normal (Semrush and Ahrefs, Canva and Gamma); pick one per job.
- Pairs with: `ai-tool-finder`, `ai-tool-links-index`, `seo-geo-tool-stack`, `business-growth-automation-tools`.

## Keywords
AI tools directory, productivity, image video, audio, writing, coding, SEO, design, presentation, connectors
