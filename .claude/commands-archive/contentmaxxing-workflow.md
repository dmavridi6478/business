---
description: 5-stage AI content tool workflow (research → draft → edit → design → distribute) centered on Claude Cowork as the single brief
argument-hint: [topic or content piece to run through the workflow]
---

# How to Start CONTENTmaxxing

Source: an uploaded infographic, "How to start CONTENTmaxxing? Follow these 5 stages of research, drafting, editing, design and distribution." Maps a named tool stack to each stage, funneling into **Claude Cowork** as the single brief, then fanning out to production/distribution tools. No existing skill in this repo covers this specific tool combination (checked `claude-code-tooling` — no match on Ahrefs/Granola/Apify/AirOps/Framer as a workflow).

## The funnel

**Stage 1 — Research (funnels into the brief)**

| Tool | Job |
|---|---|
| Ahrefs | Surface the keyword gaps worth writing about |
| Perplexity | Pull an intelligent competitor + market research |
| Granola | Capture sales call transcripts, customer language |
| Apify | Scrape competitor posts before you write a word |

**Stage 2 — The brief (the funnel's neck)**

**Claude Cowork** turns scattered inputs from all 4 research tools into one brief — no tabs, no copy-pasting between tools. This is this repo's own `claude-cowork-setup` command territory: use it to configure the Cowork project that receives these 4 inputs.

**Stage 3 — Draft, edit, design, distribute (fans back out)**

| Tool | Job |
|---|---|
| Figma | Build a design system + ready templates |
| AirOps | One content piece splits into 5 pieces with AEO (answer-engine-optimization) content |
| Kit | The same research becomes a newsletter — no huge rewrite needed |
| Framer | Insights become a new landing page or blog post |
| LinkedIn | Start a personal branding growth engine from the same brief |

## How to run it in this repo (tool-agnostic version)

If you don't have all 5 named tools connected, the workflow still holds — substitute this repo's own skills for each stage:

1. **Research**: `content-researcher` agent (trend/competitor research) + `customer-research` skill (vendored) for the Granola-style "customer language" input
2. **Brief**: consolidate stage-1 outputs into one written brief before drafting anything — the point of this stage is *not* skipping it, whatever tool holds it
3. **Draft**: `content-script-writer` agent
4. **Design**: `content-designer` agent, or this repo's `design-templates` skill for a ready HTML template
5. **Distribute**: `newsletter-repurposer` (Kit-equivalent), `content-repurpose` (Framer/landing-page-equivalent), `content-manager` + `content-publisher` for scheduling

## Plain-text prompt to kick off one cycle

```
Run the CONTENTmaxxing workflow for [TOPIC]. Stage 1: research the
keyword gaps, competitor angles, and customer language for this topic.
Stage 2: consolidate that research into one single brief before drafting
anything. Stage 3: draft the core piece, then tell me what it should
become for (a) a newsletter, (b) a landing/blog post, (c) a LinkedIn
post — using the same research, not a rewrite from scratch.
```

## Not identified

The infographic names "AirOps" for the AEO content-splitting step; this repo has no existing AirOps integration or skill. Flagged here rather than assumed to already be covered.
