---
name: gtm-six-levels-strategy
description: A six-level go-to-market ladder (traffic generation, lead capture, lead nurture, conversion, qualification, retention and expansion) with the sub-channels and example tools at each level, and the "then versus now" shift from a CRM-plus-sequencer stack to a stack per job (AI and research, data, outreach, ops and CRM, channels). Use when mapping a GTM motion level by level, finding which level is the bottleneck, or choosing tools per job instead of per vendor. Run via /gtm-six-levels. Sources - "The 6 Levels of a GTM Strategy" (Jani Vrancsik, Growth Today) and "GTM in 2026 - Then / Now" (Monika Grycz) infographics.
---

# The six levels of a GTM strategy

Sources: two infographics; tools are the authors' examples. Use the structure, then choose tools with `free-vs-paid-tool-decision` rules and connector status.

## The ladder

| Level | Name | Sub-channels (tools shown) |
|---|---|---|
| 1 | Traffic generation | Content (LinkedIn, YouTube, X, Instagram, Reddit, podcasts); Outbound (Instantly, HeyReach, Smartlead, Nooks, Lemlist, Apollo); Ads (LinkedIn, Reddit, Google, YouTube, Meta, X); Partnerships (Crossbeam, PartnerStack, G2, Zapier, affiliates, events) |
| 2 | Lead capture | Lead magnets (Tally, Notion, Lovable); Webinars (Luma, Google Meet); Community (Skool, Slack); Newsletter (Beehiiv, Kit); Social engagement (Trigify, HeyReach) |
| 3 | Lead nurture | Email flows (ActiveCampaign, HubSpot, Instantly); Retargeting ads (LinkedIn, Meta, Google); SDRs (Nooks, Apollo, HeyReach); Website intent (RB2B, Koala, Trigify); Content (LinkedIn, YouTube, X) |
| 4 | Conversion | Website (Webflow, Lovable); Proof (G2, Trustpilot, case studies); Free tools (Replit, calculators, templates); Demo video (Loom, HeyGen, Synthesia); Booking (Calendly, Chili Piper, HubSpot) |
| 5 | Qualification | Enrich (Clay, FullEnrich, Prospeo); Score (HubSpot, MadKudu, Pocus); Route to CRM (Chili Piper, Salesforce, Attio); Tiered outreach (Tier 1 Nooks, Tier 2 HeyReach, Tier 3 Instantly) |
| 6 | Retention and expansion | Support (Intercom, Pylon, Slack); Champions (Champify, Common Room); Referrals (PartnerStack, Crossbeam); Offers (sprint projects, recurring services, courses) |

## Then versus now

| Then: "a CRM and a sequencer" | Now: "a stack per job" |
|---|---|
| Salesforce - CRM | **AI and research**: Claude (writing, strategy), ChatGPT (ideation), Perplexity (account research), Clay (enrichment, workflows) |
| ZoomInfo - contact data | **Data**: Apollo (B2B database), Prospeo (email finding), FullEnrich (phone finding), RB2B (website visitors) |
| Sales Navigator - prospecting | **Outreach**: Smartlead (cold email), HeyReach (LinkedIn outreach), Nooks (AI dialer) |
| Outreach - sequences | **Ops and CRM**: HubSpot (CRM), Claude Code (internal tools, scripts), n8n (automation), Fireflies (call insights) |
| Gmail - cold email; Excel - lead lists | **Channels**: LinkedIn (founder content), YouTube (video), X (short-form), Webinars (live education), Luma (in-person events), WhatsApp / Skool (community) |
| Gong - call recording | |

## Diagnose the bottleneck

For each level record one number: visits, captured leads, nurtured-to-meeting rate, conversion rate, qualified share, retention/expansion rate. The weakest ratio between adjacent levels is the bottleneck; spend only there. Do not buy a Level 5 tool to fix a Level 1 problem.

## Rules

- A stack per job is a trade-off: more integration and data-quality work. Cap the stack at one tool per sub-channel you actively run.
- Every outreach tool needs a lawful basis and an unsubscribe path (GDPR/ePrivacy); sends need human approval (`gtm-outbound-engine`).
- Name the owner of each level; an unowned level decays.
- Connector status: connected - HubSpot, Clay, Calendly, Canva, Slack, Notion, Fireflies, Common Room, Klaviyo; available not connected - Apollo.io, Intercom, Webflow, n8n; others have no connector.

Pairs with: `gtm-team-roles-revops-boundary`, `ai-gtm-maturity-levels`, `gtm-funnel-2026`, `gtm-strategy`, `linkedin-client-acquisition-16`.

## Keywords
GTM strategy, six levels, traffic, lead capture, nurture, conversion, qualification, retention, stack per job
