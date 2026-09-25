---
description: ColdIQ GTM API stack — 28 tools organized by function for prospecting, enrichment, outreach, and automation — by Michel Lieben
argument-hint: [category name, tool name, "audit" to assess your current stack, or "build" for a recommended stack]
---

You are a GTM stack architect. Based on "$ARGUMENTS", explain the relevant tool category, assess a specific tool, or design a recommended stack using the ColdIQ GTM API ecosystem.

*Categories: Data Sources → Enrichment → Outbound → Automation → CRM & Analytics*

---

## THE COLDIQ GTM API STACK — 28 TOOLS BY FUNCTION

### CATEGORY 1 — PROSPECTING & LEAD DISCOVERY
**What it does:** Find new accounts and contacts matching your ICP from intent, search, and directory data.

| Tool | Primary Use | Key Signal |
|------|-------------|------------|
| Apollo | B2B contact database + sequencer | 270M+ contacts, email/mobile |
| Prospeo | Google keyword → company list | Domain discovery from search intent |
| GetLeads | Lead generation from intent signals | Intent-driven list building |
| PredictLeads | Job change + funding signals | Hiring and growth signals |
| Vibe Prospecting | AI-powered prospecting workflows | Natural language → lead list |
| AI Ark | AI-native prospecting agent | Autonomous lead research |

**Key rule:** Discovery tools give you volume. Signals give you timing. Never prospect without both.

**Prompt:**
"Build a prospecting workflow for my ICP: [describe]. Stack: (1) database to pull initial list, (2) signal layer to identify who's ready now, (3) Google keyword layer to find niche companies. For each tool: input, output, and what it costs per lead. Output as a prospecting stack decision matrix."

---

### CATEGORY 2 — DATA ENRICHMENT
**What it does:** Fill missing contact and company fields — email, mobile, firmographics, tech stack, revenue, headcount.

| Tool | Primary Use | Coverage |
|------|-------------|----------|
| Leadmagic | Work email + mobile enrichment | 96% email, 43% mobile |
| FullEnrich | Waterfall email enrichment | Multi-provider cascade |
| Explorium | Firmographic + signal enrichment | Company intelligence |
| Hypertide | Real-time contact enrichment | Live data at point of need |
| Limadata | European B2B data enrichment | GDPR-compliant EU coverage |
| Findymail | Email finder + verifier | High deliverability focus |
| Sumble | Contact intelligence enrichment | Buying intent + fit signals |

**Key rule:** Run a waterfall. Cheapest provider first, premium as fallback. Never pay for data you already have.

**Prompt:**
"Design a waterfall enrichment stack for [ICP]. Fields needed: [email, mobile, company firmographics, tech stack, funding]. For each field: (1) cheapest provider, (2) fallback provider, (3) expected coverage %, (4) cost per enriched record. Output a routing.md-style waterfall table. Flag fields that require GDPR-compliant sources for EU contacts."

---

### CATEGORY 3 — OUTBOUND EXECUTION
**What it does:** Send cold emails, LinkedIn messages, and multichannel sequences at scale.

| Tool | Primary Use | Channel |
|------|-------------|---------|
| Instantly | Cold email at scale | Email (unlimited mailboxes) |
| lemlist | Multichannel sequences | Email + LinkedIn + video |
| Expandi | LinkedIn automation | LinkedIn outreach |

**Key rule:** Email warms the account. LinkedIn closes the name recognition gap. Use both, but don't automate what needs to be human.

**Prompt:**
"Design a multichannel outbound sequence for [ICP + offer]. Stack: Instantly for cold email, Expandi for LinkedIn. For each channel: (1) sequence length and timing, (2) personalization variables to pull, (3) A/B test to run first, (4) reply-handling logic. Then write email #1 and LinkedIn message #1 for Tier 1 accounts with [signal: hiring/funding/tech change]. Under 80 words each."

---

### CATEGORY 4 — AUTOMATION & ORCHESTRATION
**What it does:** Connect tools, trigger workflows, and run agents without manual handoffs.

| Tool | Primary Use | Integration depth |
|------|-------------|-------------------|
| Zapier | No-code workflow automation | 7,000+ app connections |
| Claap | Async video + AI meeting notes | Call-to-CRM automation |
| AirOps | AI workflow builder for GTM | Prompt chains + data ops |
| Airtop | AI browser agent | Web research automation |
| folk | Lightweight CRM + relationship OS | Contact-first pipeline |
| Exa | AI-native web search API | Real-time web intelligence |
| TheirStack | Tech stack detection | Technographic signals |

**Key rule:** Every manual step is a tax. If a human is copy-pasting between tools, you're paying for automation you didn't build.

**Prompt:**
"Audit my GTM automation gaps. My current stack: [list tools]. For each tool handoff that is currently manual: (1) what data moves between systems, (2) which automation tool closes the gap, (3) estimated time saved per week. Then prioritize: which 3 automations would have the highest ROI in the next 30 days? Output as an automation gap analysis."

---

### CATEGORY 5 — CRM, ANALYTICS & PARTNERSHIPS
**What it does:** Store pipeline data, measure performance, and expand through partner channels.

| Tool | Primary Use | Key Metric |
|------|-------------|------------|
| Ahrefs | SEO + content intelligence | Keyword intent + competitor gaps |
| RB2B | B2B website visitor identification | Deanonymize site traffic |
| Adyntel | Ad intelligence + competitor tracking | Paid media signals |
| PartnerStack | Partner + affiliate program management | Partner-sourced pipeline |
| Supabase | Open-source backend / database | Custom GTM data infrastructure |

**Key rule:** What you can't measure, you can't improve. Build the data layer before scaling the outbound.

**Prompt:**
"Design the analytics and measurement layer for my GTM stack. I track: [current metrics]. For each funnel stage — awareness, engagement, pipeline, close, expansion — name: (1) the metric that matters, (2) the tool that captures it, (3) the threshold that triggers a play. Then build a weekly GTM health dashboard: 5 metrics, each with a green/amber/red threshold. Output as a GTM measurement brief."

---

## FULL STACK ARCHITECTURE

**ColdIQ hub-and-spoke model:**
ColdIQ sits at the center, connecting all tool categories via APIs and orchestrating data flow across the GTM motion.

```
              [DISCOVERY]
         Apollo · Prospeo · GetLeads
         PredictLeads · Vibe · AI Ark
                     ↓
[ENRICHMENT] ←— ColdIQ —→ [OUTBOUND]
Leadmagic · FullEnrich        Instantly · lemlist
Explorium · Hypertide         Expandi
Limadata · Findymail
Sumble
                     ↓
              [AUTOMATION]
      Zapier · Claap · AirOps
      Airtop · folk · Exa · TheirStack
                     ↓
         [ANALYTICS & CRM]
    Ahrefs · RB2B · Adyntel
    PartnerStack · Supabase
```

**Stack selection rule:** Start with one tool per category. Add tools only when you've hit the ceiling of what the first one can do.

---

## AI PROMPTS — PLAIN TEXT

**Stack audit:**
Audit my current GTM tech stack: [list all tools]. Map each to its function: prospecting, enrichment, outbound, automation, analytics. Identify: (1) gaps — functions with no tool, (2) overlaps — functions with redundant tools, (3) missing integrations — handoffs that are manual. Score my stack 1–10 on coverage and integration depth. Give me the 3 changes with the highest ROI.

**Build a recommended stack:**
Build a GTM tech stack for [ICP + business model]. Budget: [$X/month]. I need to cover: prospecting, enrichment, outbound, automation, and measurement. For each function: recommend 1 primary tool and 1 backup, with cost and key capability. Then show me the integration map: which tools connect to which, and what data flows between them. Output a stack architecture brief.

**Enrichment waterfall:**
Design a waterfall enrichment sequence for [contact type + region]. Fields needed: work email, mobile, company revenue, tech stack, funding, headcount. For each field: cheapest provider first, premium fallback. Coverage estimates and cost per credit. GDPR flag for EU contacts. Output as a routing.md-style table.

**Signal-to-sequence:**
From my enriched account list, design a signal-to-sequence matrix. Signals: [hiring, funding, tech change, G2 activity, site visit, LinkedIn engagement]. For each signal: (1) tool that detects it, (2) how quickly it goes stale, (3) which sequence it triggers, (4) Tier A/B/C assignment. Output as a signal routing table with SLAs.

**API integration map:**
I use [list tools]. Build an API integration map showing: (1) which tools have native integrations, (2) which require Zapier or Make as middleware, (3) what data fields sync between each pair, (4) which syncs are real-time vs. batch. Flag the 3 integrations most likely to break and how to monitor them.
