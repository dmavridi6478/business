---
name: ai-marketing-sales-tools-60
description: The "60 AI Marketing + Sales Tools" wheel - 12 categories x 5 tools (Copy, SEO, All-in-one, Enablement, Video, Social, Prospecting, AI Agent, Research, Image Gen, Meetings, Email) - cross-referenced against which tools already have a connected MCP connector in this workspace, which have a registry listing that needs the owner's OAuth, and which can only be reached through Zapier or not at all. Use when choosing a tool stack, or when asked "can Claude drive X directly?".
---

# 60 AI marketing + sales tools - and what Claude can actually reach

Checked 6 Oct 2026 against the claude.ai connector list and registry for this account. "Connected" = tools are loadable in a session now. "Registry, not connected" = exists as a connector; the **owner must authorise it in claude.ai** (OAuth cannot be done from a non-interactive session). "Via Zapier" = no dedicated connector found; Zapier is connected here and may expose actions - check with `discover_zapier_actions`. "None found" = no listing found in the registry search (absence of a hit is not proof there is none).

| Category | Tools on the wheel | Reach from Claude today |
|---|---|---|
| **Copy** | ChatGPT, Claude, Meta AI, Perplexity, Gemini | Claude native; others are other products - no connector needed |
| **SEO** | Ahrefs, Also Asked, SurferSEO, AIPRM, SEMrush | **Ahrefs connected; Semrush connected**; others none found |
| **All-in-one** | Crono, Outreach, ZELIQ, Salesloft, Amplemarket | Outreach: registry, not connected; others none found / via Zapier |
| **Enablement** | trumpet, Dock, Aligned, Allego, Flowla | none found |
| **Video** | Pika Labs, Synthesia, Runway, Luma, Veed.IO | Higgsfield and AgentOpus are connected video tools (not on the wheel); wheel tools none found |
| **Social** | EasyGen, AuthoredUp, Taplio, MagicPost, SuperGrow | Taplio MCP: **needs reconnect**; **Typefully connected** (LinkedIn/X drafting) |
| **Prospecting** | Sendler, Sendspark, Loom, HourOne, Hippovideo | Loom is reachable through the Atlassian connector (connected); others none found |
| **AI Agent** | 11x, Clay, Bardeen, AiSDR, Topo | **Clay connected**; Vibe Prospecting, Common Room, OpenFunnel also connected |
| **Research** | Glimpse, Humata, Perplexity, Consensus, AnswerThePublic | **Consensus connected**; others none found |
| **Image Gen** | Midjourney, ChatGPT Plus, Ideogram, Meta AI, Flux.1 | Canva, Figma, Adobe for creativity, Higgsfield connected (not on the wheel) |
| **Meetings** | Sybill, tl;dv, Substrata, Fathom, Winn | tl;dv and Fathom: registry, not connected; **Fireflies connected** (equivalent) |
| **Email** | Smartlead, Lemlist, Instantly, Reply, La Growth Machine | none found / via Zapier; Klaviyo and MailerLite (needs reconnect) are connected alternatives |

## Judgement
- Sixty logos is a shopping list for people selling tools. A one-person business needs roughly **one per category it actually uses**: usually research, one outreach channel, one meeting recorder, one scheduler. Start from `docs/procedures/free-vs-paid-tool-decision.md`.
- Cold-email tools (Smartlead, Lemlist, Instantly) carry real deliverability and consent risk (GDPR/PECR, LinkedIn's terms). This repo's `os_*` guards and `docs/ai-os/rules/compliance-rules.md` exist for that reason - do not wire them to send automatically.
- The most valuable gap-fillers already connected: Ahrefs/Semrush (SEO), Clay + Vibe Prospecting (prospect data), Fireflies (meetings), Typefully (social drafting).

## Keywords
tool stack, AI tools, marketing tools, sales tools, connectors, MCP, Ahrefs, Clay, Fireflies
