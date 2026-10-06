---
name: ai-tools-50-map
description: 'The "50 AI tools that finish hours of work in minutes" list (5 slides of 10) with each tool''s job, cross-checked against the connectors available in this workspace on 6 Oct 2026 (connected, in registry but not connected, or none found). Use when picking tools for a task, or when asked whether Claude can drive a given tool directly.'
---

# 50 AI tools - and what Claude can reach

Source: @ai_slacker carousel. Reach column checked against the claude.ai connector list and registry for this account on 6 Oct 2026. "Connected" = tools load in a session. "Registry" = a listing exists, the owner must authorise it. "None found" = no listing found (not proof none exists; try Zapier `discover_zapier_actions`). Overlaps `ai-marketing-sales-tools-60`; this one is organised by job.

| # | Tool | Job | Reach |
|---|---|---|---|
| 1 | Claude | Writing and document drafting | This session |
| 2 | ChatGPT | Brainstorming, first drafts | none needed |
| 3 | Gemini | Research and analysis | none found |
| 4 | Perplexity | Real-time web research | none found |
| 5 | Canva | Graphic design, carousels | **Connected** |
| 6 | CapCut | Reel/video editing | none found |
| 7 | GitHub Copilot | Code autocomplete | n/a |
| 8 | Cursor | AI-assisted coding | n/a |
| 9 | Replit | Build and deploy apps | Registry |
| 10 | Notion AI | Notes and knowledge base | **Connected** (Notion) |
| 11 | Loom | Async video updates | via Atlassian (connected) |
| 12 | PostHog | Product usage analytics | none found (Amplitude connected) |
| 13 | Google Trends | Market/topic validation | web only |
| 14 | Search Console | SEO performance tracking | via Ahrefs/Semrush (connected) |
| 15 | HubSpot CRM | Sales pipeline | **Connected** |
| 16 | Grammarly | Grammar and tone | none found |
| 17 | Zapier | Workflow automation | **Connected** |
| 18 | Make | Visual automation builder | none found |
| 19 | n8n | Self-hosted automation | skills in repo (`n8n-*`) |
| 20 | Activepieces | Open-source automation | none found |
| 21 | Fireflies.ai | Meeting transcription | **Connected** |
| 22 | Front | Shared inbox and support | none found |
| 23 | Linear | Task/bug tracking | **Connected** |
| 24 | Vercel | Website hosting | **Registered in `.mcp.json`** (sign in via /mcp) |
| 25 | Figma AI | UI prototyping | **Connected** |
| 26 | Framer AI | Landing page builder | none found |
| 27 | Beautiful.ai | Auto-designed slides | none found |
| 28 | Gamma | AI presentations | **Connected** |
| 29 | Tome | Pitch deck storytelling | none found |
| 30 | Descript | Video/podcast editing | none found |
| 31 | ElevenLabs | AI voiceovers | Registry |
| 32 | Runway ML | AI video generation | none found (Higgsfield connected) |
| 33 | Pictory | Text-to-video | none found |
| 34 | Copy.ai | Marketing copywriting | none found |
| 35 | Otter.ai | Meeting notes | none found (Fireflies connected) |
| 36 | Clockify | Time tracking | none found |
| 37 | Trello (Butler) | Task automation | none found (ClickUp, Linear connected) |
| 38 | Slack AI | Thread summarising | **Connected** (Slack) |
| 39 | Zoom AI | Call summaries | none found |
| 40 | Mailchimp AI | Email campaign writing | none found (Klaviyo connected, MailerLite needs reconnect) |
| 41 | Apollo.io | Lead prospecting | none found (Clay, Vibe Prospecting connected) |
| 42 | Hunter.io | Email finder | none found |
| 43 | Crayon | Competitor tracking | none found |
| 44 | Ubersuggest | Keyword research | none found (Ahrefs, Semrush connected) |
| 45 | AnswerThePublic | Content idea generation | none found |
| 46 | Remove.bg | Background removal | via Canva `remove-background` (connected) |
| 47 | Ideogram | AI image generation | none found |
| 48 | Suno | AI music creation | none found |
| 49 | Krisp | Background noise removal | none found |
| 50 | Perplexity | Shareable research docs | duplicate of #4 in the source |

## Judgement
Fifty tools is a shopping list. A one-person business needs about one per job. Before adding a paid tool, apply `docs/procedures/free-vs-paid-tool-decision.md`. Never wire cold-email or prospecting tools to send automatically (consent and platform rules).
Rendering: `design-templates` > `tool-list-red-numbers.html`.

## Keywords
AI tools, productivity, tool stack, connectors, MCP, ai_slacker
