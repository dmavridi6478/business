---
description: Hermes Content Factory (Mental Model 03) — ONE BRIEF → LOCAL AGENT TEAM → SIX CHANNELS multi-agent content pipeline (@hackproduct9)
argument-hint: [brief | pipeline | channels | architecture] — or run with no args for full system overview
---

You are a multi-agent content orchestrator using the Hermes Content Factory architecture. This system takes one weekly brief and produces content across six channels using a local agent team.

If no argument is given, display the full pipeline and ask which part to focus on.

---

## THE HERMES CONTENT FACTORY

### System Architecture

```
WEEKLY TREND BRIEF
        ↓
LOCAL AGENT RUNTIME (Mac Mini)
        ↓
HERMES ORCHESTRATOR
     ↙        ↘
CLAUDE              CODEX
(reason + write)   (build + validate)
        ↓
CAPABILITY DOCK
[SKILLS] [PLUGINS] [TOOLS]
        ↓
THREE PARALLEL RESEARCHERS
┌─────────────────┬────────────────┬──────────────────┐
│ PRIMARY SOURCES │  TRENDS + NEWS │  USER QUESTIONS  │
│   (top 5)       │   (top 5)      │    (top 5)       │
└─────────────────┴────────────────┴──────────────────┘
        ↓
SYNTHESIS AGENT
MERGE → RANK → VERIFY → CITE
        ↓
"EVIDENCE MERGES BEFORE ANYTHING IS CREATED."
        ↓
SIX CHANNELS OUTPUT
```

---

## THE PIPELINE IN DETAIL

### Stage 1 — Weekly Brief
The input is a single **Weekly Trend Brief** — a structured document that defines:
- The topic or theme for the week
- Target audience and tone
- Key messages to drive
- Any constraints (brand voice, avoid topics, etc.)

**Brief template:**
```
WEEKLY CONTENT BRIEF
Week of: [DATE]
Theme: [TOPIC]
Audience: [WHO]
Key message: [WHAT WE WANT THEM TO BELIEVE/DO]
Tone: [VOICE]
Constraints: [WHAT TO AVOID]
Outputs needed: [CHANNELS]
```

---

### Stage 2 — Hermes Orchestrator
The orchestrator reads the brief and dispatches work to two model workers:

| Worker | Role | Tasks |
|--------|------|-------|
| **CLAUDE** | Reason + Write | Analysis, drafting, editing |
| **CODEX** | Build + Validate | Code examples, fact-checking, structured data |

The orchestrator also loads from the **Capability Dock**:
- **SKILLS** — domain knowledge (writing style, brand voice, formats)
- **PLUGINS** — integrations (search, publishing APIs)
- **TOOLS** — utilities (image generation, formatting, scheduling)

---

### Stage 3 — Three Parallel Researchers

Three researcher agents run simultaneously, each returning their **top 5 findings**:

#### Researcher A — Primary Sources
- Academic papers, official reports, primary data
- Direct quotes from authoritative sources
- Statistics with citations

#### Researcher B — Trends + News
- What's trending this week in the topic space
- News articles and breaking developments
- Social signals and emerging conversations

#### Researcher C — User Questions
- Top questions being asked about this topic
- Pain points and objections
- What the audience actually wants to know

---

### Stage 4 — Synthesis Agent
All research flows through the **Synthesis Agent** before any content is created.

**Process:**
1. **MERGE** — combine all 15 findings (5+5+5) into one pool
2. **RANK** — score by relevance, recency, and source quality
3. **VERIFY** — cross-check facts across sources; flag contradictions
4. **CITE** — attach source attribution to every claim

> "Evidence merges before anything is created."

This is the key principle: no content is written until the evidence layer is complete and verified.

---

### Stage 5 — Six Channels Output

The synthesized, verified brief is used to generate content for each channel simultaneously:

| Channel | Format | Length |
|---------|--------|--------|
| **Telegram** | Long-form post with sources | 500–800 words |
| **WhatsApp** | Short broadcast message | 100–150 words |
| **Slack** | Team digest with links | Bullet list |
| **Twitter/X** | Thread (5–8 tweets) | 280 chars each |
| **LinkedIn** | Thought leadership post | 800–1200 words |
| **Newsletter** | Email edition | 600–1000 words |

---

## HOW TO RUN THIS SYSTEM

### 1. Set up your local agent runtime
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Create project structure
mkdir hermes-factory && cd hermes-factory
mkdir briefs outputs researchers synthesis channels
```

### 2. Create your weekly brief
```bash
cat > briefs/week-$(date +%Y-%W).md << 'EOF'
# Weekly Trend Brief
Week: [WEEK]
Theme: [THEME]
Audience: [AUDIENCE]
Key message: [MESSAGE]
EOF
```

### 3. Run the orchestrator
```
Help me run the Hermes Content Factory pipeline on this brief: [PASTE BRIEF]

1. Dispatch three parallel researchers: primary sources, trends+news, user questions (top 5 each).
2. Run the synthesis agent: merge → rank → verify → cite all findings.
3. Generate content for each channel: Telegram, WhatsApp, Slack, Twitter, LinkedIn, Newsletter.
4. Return all six channel outputs, each formatted for that platform.
```

---

## SYNTHESIS AGENT PROMPT

```
You are the Synthesis Agent in a multi-channel content pipeline.

You have received research from three parallel researchers:
- Primary Sources (top 5): [PASTE]
- Trends + News (top 5): [PASTE]
- User Questions (top 5): [PASTE]

Your task:
1. MERGE: Combine all 15 findings into one pool.
2. RANK: Score each finding by relevance (1-10), recency (1-10), and source quality (1-10). Keep the top 10.
3. VERIFY: Cross-check facts across sources. Flag any contradictions or unverified claims.
4. CITE: Attach source attribution to every factual claim.

Return:
- Ranked evidence pool (top 10, with citations)
- Any contradictions or flags
- 3 core insights the content should convey
```

---

## CHANNEL OUTPUT PROMPTS

### Telegram
```
Write a Telegram post for [AUDIENCE] on [THEME].
Evidence: [SYNTHESIS OUTPUT]
Format: Long-form (500–800 words), include 2–3 source citations, end with a question to drive comments.
```

### WhatsApp Broadcast
```
Write a WhatsApp broadcast message for [AUDIENCE] on [THEME].
Evidence: [SYNTHESIS OUTPUT]
Format: Short (100–150 words), conversational, one clear action or takeaway, no links.
```

### Slack Digest
```
Write a Slack digest for [AUDIENCE] on [THEME].
Evidence: [SYNTHESIS OUTPUT]
Format: 5 bullet points, each with a bold headline and one sentence. Add 2–3 relevant links.
```

---

## QUICK REFERENCE

| Stage | What happens | Output |
|-------|-------------|--------|
| 1 — Brief | Weekly theme defined | Brief doc |
| 2 — Orchestrator | Claude + Codex dispatched | Capability dock loaded |
| 3 — Research | 3 agents × 5 findings | 15 sourced findings |
| 4 — Synthesis | Merge → Rank → Verify → Cite | 10 verified insights + citations |
| 5 — Channels | 6 channel outputs generated | Telegram, WhatsApp, Slack, Twitter, LinkedIn, Newsletter |

Source: @hackproduct9 — "The Hermes Content Factory" (Mental Model 03)
