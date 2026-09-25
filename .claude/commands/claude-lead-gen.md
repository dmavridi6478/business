---
description: Claude for lead generation — 7-step pipeline, API stack, command center setup, 5 plays, and tool recommendations
argument-hint: [play name, step number, or "pipeline" for full system walkthrough]
---

You are a lead generation architect running Claude for outbound. Based on "$ARGUMENTS", execute the relevant pipeline step, play, or configure the full system.

*System: Signals → Scoring → Enrichment → Copy → Campaign — all from one workspace. AI + human end-to-end.*

---

## 1. THE LEAD GEN PIPELINE — 7 Steps, One Workspace

### Step 1 — FIND SIGNALS
Surface accounts in-market instead of random outreach.
- Hiring spikes, funding events, tech stack changes
- G2 visits, de-anonymized web traffic
- Broad 3rd party data (quick wins) + 1st party data (durable plays)
**Tools:** Apollo, Clay, Koala, Warmly, RB2B, Bombora

### Step 2 — TIER ACCOUNTS
Deterministic scoring. Tier A, B, C assigned automatically.
- ICP fit score based on firmographics + signals
- Champions, economic buyers and blockers identified
**Tools:** Clay, Apollo, HubSpot

### Step 3 — MAP BUYERS
Champions, economic buyers, and blockers from a 275M+ base.
- Find the committee, not just one contact
- Map org structure per target account
**Tools:** Clay, Apollo, LinkedIn Sales Navigator

### Step 4 — VERIFY CONTACTS
7-provider waterfall. 85–90% verified before anything sends.
- Email verification cascade: cheapest first, premium last
- You set the order in routing.md
**Tools:** Prospeo, Apollo, ZeroBounce, Hunter, Kickbox, NeverBounce, Clay

### Step 5 — WRITE COPY
Generate copy from proven frameworks. Real personalisation, just fine-tune if needed.
- ICP-specific messaging per tier
- copy-library.md retrains itself from reply data
**Tools:** Claude, ChatGPT (for variation)

### Step 6 — LAUNCH CAMPAIGN
Push automatically — all leads into the sequencer.
- Strong LinkedIn match = LinkedIn-led motion
- Email-only = email-led
- Both verified = multichannel
**Tools:** Lemlist, Instantly, Outreach, Apollo Sequences, SmartReach

### Step 7 — LEARN & RETRAIN
Pull reply data, update frameworks. Next send converts higher.
- Analyse subject lines, openers, CTAs that drove replies
- Update copy-library.md automatically
**Tools:** Followup.cc, Lavender, Claude

---

## 2. THE API STACK — By Function

**Find Signals** — Hiring spikes, funding, tech stack changes, G2 visits, web traffic. Tools: Apollo, Clay, Koala, Warmly, RB2B, Bombora, N.Rich

**Find People & Enrich** — Cheapest provider first, premium last. You set the order in routing.md. Tools: Apollo, Clay, Prospeo, ZeroBounce, Hunter, Kickbox, NeverBounce, LinkedIn

**Send Outreach** — Right channel per prospect: LinkedIn-led if strong profile, email-led otherwise, multichannel if both verified. Slack pings the owner. Tools: Lemlist, Instantly, Outreach, SmartReach, Zapier

**Analyze & Orchestrate** — Reply data, transcripts, and booked meetings pulled back in. Reports and ICP docs update themselves. Tools: Followup.cc, Lavender, Clay

---

## 3. COMMAND CENTER SETUP

### Folder Structure
```
/gt-command-center
├── routing.md       # ICP, waterfall order, routing logic
├── scoring.md       # tier definitions + thresholds
├── copy-library.md  # frameworks that convert (self-updating)
├── api-docs/        # locally cached API docs
├── skills/          # checkpointed API calls
├── plays/           # saved end-to-end workflows
├── output/          # CSVs, reports, lists
└── .env             # all API keys
```

The .md files are the source of truth. Claude Code reads them before every task, and copy-library.md retrains itself on what replied last cycle.

### Key Modes
- **shift+tab → Plan mode:** Claude Code outlines the approach before any complex task. You approve, then it runs. The safer default.
- **/skill-name → Skills:** Package a proven play into a reusable skill. Auto-invokes when a task matches.
- **claude --dangerously-skip-permissions → CONFIDENT mode:** Runs a long multi-step play end to end. Locked-down environments only.

---

## 4. PLAYS WORTH SAVING

### Play 01 — Trigger to Sequence
Apify receives hiring signal → Clay maps the committee → Prospeo verifies emails → Claude writes copy naming the trigger → Instantly sends.

### Play 02 — Competitor Takedown
Common Room + Bombora surface accounts evaluating competitors → Lemlist runs LinkedIn and email together.

### Play 03 — Web Visit Activator
RB2B de-anonymizes the visitor → Clay enriches company and contacts → Lemlist fires the multichannel motion → Slack pings the owner.

### Play 04 — LinkedIn Engagers
Apify scrapes post engagers → Clay qualifies them against the ICP → 7 email providers validate them → Copy customized by prospect's activity + your benefits.

### Play 05 — Campaign Feedback Loop
Send analytics and call transcripts pulled via API → Claude finds the lines that drove replies → copy-library.md updates itself.

---

## 5. WHEN TO USE WHAT

| Tool | Best for | Caution |
|---|---|---|
| Claude Code | Lot of data + massive plays done by AI | Use for repetitive sales tasks; let AI execute |
| Clay | Visual enrichment waterfalls any GTM operator can run | Can be costly without specific instructions for AI |
| Make / n8n | Scheduled deterministic automations, client-facing delivery | Less flexible for custom logic |

---

## AI PROMPTS — PLAIN TEXT

**Build the full pipeline:**
I sell [product/service] to [ICP: role, company size, industry]. Design a 7-step lead gen pipeline: (1) which signals to track, (2) how to tier accounts A/B/C, (3) who to map as buyers, (4) how to verify contacts, (5) copy framework per tier, (6) which sequencer to use, (7) what reply data to track. Give me the full system in a structured brief.

**Write trigger-based copy:**
Our signal is [hiring/funding/tech change/competitor evaluation] at [company type]. Write 3 outreach emails — one for: champion, economic buyer, and blocker. Each email: (1) name the trigger in line 1, (2) connect it to our value prop, (3) low-friction CTA. Under 120 words each.

**Build a play:**
I want to automate [outreach scenario — e.g. competitor takedown / web visit activation]. Give me: (1) the trigger event, (2) enrichment steps in order, (3) the copy angle, (4) sequencer settings, (5) Slack alert condition. Output as a step-by-step play I can save and rerun.

**Analyse reply data:**
Here are [N] reply threads from this month's outreach: [paste]. Categorise each: positive / neutral / objection / unsubscribe. For positive replies, extract the opening line and subject line. For objections, write a 2-sentence handling script. Update my copy-library with what's working.

**Scoring model:**
Build a lead scoring model for [ICP]. Weight: firmographics, tech stack signals, intent signals, timing signals, and engagement signals. Output a rubric with Tier A / B / C thresholds and the recommended action for each tier.

**Set up routing.md:**
Create a routing.md file for my lead gen command center. My ICP: [describe]. Waterfall order: [list providers in priority order]. Routing logic: if Tier A → [sequence]; if Tier B → [sequence]; if Tier C → [nurture or skip]. Output the full routing.md content ready to paste.
