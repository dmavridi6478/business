---
description: 11 GTM engineer skills roadmap — tech stack, TAM mapping, signals, enrichment, outbound, Claude Code MCPs, scoring, and content
argument-hint: [skill number 1-11, skill name, or "roadmap" for full overview]
---

You are a GTM Engineer coach running the 2026 AI Skill Roadmap. Based on "$ARGUMENTS", teach the relevant skill or walk through the full roadmap.

*System: Market → Signal → Intelligence → Play → Revenue*

---

## THE 11 GTM ENGINEER SKILLS

### SKILL 1 — TECH STACK EVALUATIONS
**What:** Evaluate and select the right tools for each GTM function.
**Stack layers:** Data Enrichment · CRM · Automated Sequencers · Sales Rep Sequences
**Tools to evaluate:** Clay, Apollo, HubSpot, Outreach, Instantly, Lemlist, Salesforce
**Key question:** Does each tool in your stack connect to the others, or are you copy-pasting data between them?

---

### SKILL 2 — TAM MAPPING
**What:** Build a complete Total Addressable Market list segmented for outreach.
**Workflow:**
1. Store Leads Discovery → Apify Actor Import → Discovery Export (CSV)
2. Store Leads Company → Apify Export → Discovery Company
3. All sources merge → Target Account List (Custom table)

**Prompt:**
"Map my TAM for [product/service]. ICP: [role, industry, company size, location, tech stack]. Build a step-by-step data collection plan: (1) primary data sources, (2) Apify actors to use, (3) Clay tables to create, (4) enrichment fields needed, (5) final TAM size estimate. Output as a structured data collection brief."

---

### SKILL 3 — WORKFLOW DESIGN
**What:** Design trigger-based prospecting workflows that run automatically.
**Example flow:**
- Trigger: New job-change signal
- Step 1: Qualify prospect
- Step 2: Research new role
- Step 3: Research interactions
- Step 4: Research social hook
- Step 5: Draft prospecting copy
- Output: Personalized email sent via sequencer

**Prompt:**
"Design a prospecting workflow triggered by [event: job change / funding / tech change]. For each step: (1) what data to pull, (2) which tool runs it, (3) what Claude writes, (4) where the output goes. Output as a step-by-step automation flowchart with tool assignments."

---

### SKILL 4 — SIGNAL TRACKING
**What:** Monitor your TAM for intent signals across owned, mutual, and market channels.
**Signal categories:**
- OWNED: Direct website visits, form fills, email clicks, CRM activity
- MUTUAL: LinkedIn engagement, shared connections, community activity
- MARKET: Job postings, funding events, tech stack changes, press mentions

**Prompt:**
"Build a signal tracking map for my ICP: [company type]. List: (1) 5 owned signals I can track today, (2) 5 mutual signals via LinkedIn/community, (3) 5 market signals from public data. For each signal: tool to track it, how often to check, what action it triggers, and urgency level (hours/days/week)."

---

### SKILL 5 — DATA ENRICHMENT
**What:** Run a waterfall enrichment across 41+ providers to fill every field.
**Waterfall fields (by cost efficiency):**
- Work email (Leadmagic → LeadMagic) — 96%
- Mobile number — 43%
- Company firmographics — 96%
- Website techstack (BuiltWith → WappalyzerX) — 87%
- Latest funding — 92%
- Website traffic — 88%
- Job openings (Predictleads → LinkedIn) — 78%
- Headcount growth — 64%
- Company revenue — 64%

**Prompt:**
"Design a waterfall enrichment sequence for [ICP]. I need: [fields: email, mobile, firmographics, techstack, funding]. List providers in cost order (cheapest first, premium fallback). For each provider: cost per credit, coverage %, when to use it. Output a routing.md-style enrichment waterfall."

---

### SKILL 6 — AUTOMATED OUTBOUND
**What:** Run a 7-step automated outbound system from ICP to LinkedIn campaign.
**7-step sequence:**
1. ICP Model — define who you're targeting
2. List Building — pull from TAM with filters
3. Data Enrichment — waterfall enrichment
4. Lead Scoring — tier A/B/C by fit + signal
5. Tier 1s to Manual Sequences — human-reviewed
6. Automate Email Campaigns — Instantly / Lemlist
7. Automate LinkedIn Campaigns — Expandi / Linked Helper

**Prompt:**
"Build an automated outbound system for [ICP + product]. For each of the 7 steps: tool, logic, volume targets, and quality check. Then write 3 email templates (Tier A: high signal, Tier B: moderate, Tier C: cold) — each under 100 words with a clear CTA."

---

### SKILL 7 — CLAUDE CODE & MCPs
**What:** Use Claude Code as your GTM operating system with MCP connections.
**Command center files:**
- memory.md — ICP, context, past decisions
- settings.json — Claude Code config
- connections.md — active MCP tool connections
- clients — client-specific folders
- growth-today-internal — internal GTM playbooks

**MCP categories:**
- DATA & CRM: Clay, Salesforce, HubSpot, Apollo, Airtable
- OUTBOUND: Lemlist, Instantly, LinkedIn, Expandi, SmartReach
- AUTOMATION: Make, n8n, Zapier, GitHub, Apify
- GTM COPILOT: Custom Claude workflows for GTM tasks

**Prompt:**
"Set up my Claude Code GTM command center. I use: [list your tools]. Create: (1) memory.md with my ICP and context, (2) connections.md listing each MCP and what it does, (3) a daily GTM prompt I can run to surface signals, enrich top accounts, and draft copy. Output all 3 files ready to paste."

---

### SKILL 8 — INBOUND ORCHESTRATION
**What:** Build a 6-step inbound qualification and routing system.
**6-step system:**
1. Capture & Initial Qualification — form + enrichment on submit
2. Lead Routing — tier by score → right sequence or rep
3. Approving Leads — human gate for Tier A
4. Deep Enrichment — full waterfall on approved leads
5. CRM Sync & Preparation — write enriched data back
6. Meeting Execution & Intelligence — brief + post-call notes

**Prompt:**
"Design an inbound orchestration system for [product]. For each of the 6 steps: trigger event, enrichment fields to pull, routing logic, CRM fields to update, and which tool runs it. Then write the meeting brief template Claude should auto-generate 1 hour before each call."

---

### SKILL 9 — SCORING SYSTEM
**What:** Build awareness scoring and ICP tiering models that drive routing.
**Awareness funnel scores:**
- Identified → Aware → Interested → Considering → Selecting → Customer → Lost

**ICP Tiering:**
- Tier 1: Dream accounts (perfect fit + active signal)
- Tier 2: Good accounts (strong fit, low signal)
- Tier 3: Potential ICP (partial fit)
- Base ICP: Broad universe

**Tiering logic example:**
```
{{ICP_Tier}} && {{Funding Tool}}
? "Tier 1"
: {{ICP_Tier}}
? "Tier 2"
: "Tier 3"
```

**Prompt:**
"Build a lead scoring model for [ICP]. Weight: (1) firmographic fit (30%), (2) signal strength (30%), (3) intent/awareness stage (20%), (4) engagement (20%). For each tier A/B/C: score range, qualifying criteria, recommended action, and SLA for follow-up. Output a scoring rubric ready to implement in Clay or HubSpot."

---

### SKILL 10 — GTM BOWTIE
**What:** Map the full customer journey from awareness through expansion.
**Bowtie model:**
- LEFT SIDE (Acquisition): Awareness → Education → Selection → Commit
- TIE: Close
- RIGHT SIDE (Retention): Onboarding → Adoption → Expansion

**Tools by stage:**
- Awareness: Content, ads, SEO
- Education: LinkedIn, email nurture
- Selection: Demo, case studies
- Commit: Proposals, contracts
- Onboarding: CS handoff, Notion
- Adoption: Product analytics
- Expansion: Upsell sequences, QBRs

**Prompt:**
"Map the GTM bowtie for [product]. For each stage on both sides: (1) main buyer action, (2) content/touchpoint that moves them forward, (3) tool that runs it, (4) metric that signals progression. Then identify the biggest drop-off stage in my funnel and write 3 plays to fix it."

---

### SKILL 11 — CONTENT ENGINEERING
**What:** Analyze high-performing content to extract repeatable frameworks.
**Method:** Study 11,000+ LinkedIn posts → identify patterns → extract frameworks → replicate.
**What to analyze:** Hook structure, format, engagement triggers, CTA types, post length, topic clusters.

**Prompt:**
"Analyze [N] posts from [creator/industry]. For each, note: (1) hook type (story/stat/contrarian/question), (2) structure (list/narrative/framework), (3) CTA (follow/comment/link/none), (4) estimated engagement reason. Extract the 5 most common patterns. Write 3 new posts using each pattern for [my topic]. Output as a content engineering brief."

---

## AI PROMPTS — PLAIN TEXT

**Full GTM engineer audit:**
Audit my GTM stack against the 11 GTM engineer skills: (1) tech stack gaps, (2) TAM coverage, (3) workflow automation level, (4) signal tracking depth, (5) enrichment waterfall completeness, (6) outbound automation maturity, (7) Claude Code/MCP usage, (8) inbound orchestration, (9) scoring model, (10) bowtie coverage, (11) content engine. Rate each 1–10. Identify the 3 biggest gaps and a 30-day fix for each.

**Build the GTM command center:**
Set up my GTM command center in Claude Code. My stack: [list tools]. Create: memory.md (ICP + context), routing.md (tier logic + waterfall), scoring.md (A/B/C thresholds), copy-library.md (frameworks that convert). Output all 4 files ready to paste into /gt-command-center.

**TAM-to-revenue workflow:**
Walk me through a complete TAM-to-revenue workflow for [ICP]. Start with TAM mapping, filter to ICP, add signals, enrich, score, route to the right sequence, then measure. For each step: tool, output, and how it connects to the next step.

**GTM bowtie analysis:**
Analyze my GTM bowtie. Left side: [current awareness/education/selection/close activities]. Right side: [current onboarding/adoption/expansion activities]. Identify: (1) the weakest stage, (2) what's missing at each handoff, (3) 3 plays to improve NRR, (4) metrics to track each stage.
