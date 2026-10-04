---
name: ai-team-org-chart-10
description: The "I replaced myself with 10 AIs" org chart from an @aigenesis.official carousel (creator handle @charliehills): ten tools cast as heads of design, memory, illustration, cinematography, analytics, operations and community, with each tool's real status checked - which connectors this repo's sessions already have (Notion, Higgsfield), which have an MCP server (Apify), the Hermes Agent licence and installer, and which claims cannot be verified. Use when designing a small AI-assisted content team, mapping tools to roles, or deciding which connectors to add for a content workflow.
---

# The 10-AI org chart, checked

Source: @aigenesis.official, "I (actually) replaced myself with 10 AIs: the exact org chart behind 350k+ followers" (the creator's handle on the cover is @charliehills). Seven of the ten role slides were in the upload; the cover shows two more icons (an orange asterisk and a teal/green split icon) and a stacked-layers icon with no slide, so **three roles are unidentified**.

| Role on slide | Tool | What the slide says | Status found |
|---|---|---|---|
| Head of Design | Claude Code | Builds every graphic as raw HTML; "a cold QA agent scores it to 95" | Product exists. The "score to 95" loop is the creator's own workflow; no method was shown |
| Head of Memory | Notion | System of record: ideas, assets, queue, metrics | **Connector already available in this session** [Certain] |
| Head of Illustration | GPT Image 2 | Every thumbnail and illustration from a short prompt | Product claim only; not verified here |
| Head of Cinematography | Higgsfield | B-roll generated and matched to each scene | **Connector already available in this session** [Certain] |
| Head of Analytics | Apify | Pulls reach, saves and comments so data picks the next idea | Apify publishes an MCP server (`apify/apify-mcp-server`, MIT; hosted at mcp.apify.com, needs an Apify account) |
| Head of Operations | Hermes | Scores and ranks every idea against the data | `NousResearch/hermes-agent`, MIT; its README installs with `curl ... \| bash`. This repo already has `hermes-*` skills |
| Head of Community | ManyChat | Auto-DMs the free guide to everyone who comments the keyword | Product claim; no connector was available here |

## What cannot be verified

The "350k+ followers" figure, any result attributed to this team, and the claim that ten tools "replaced" a person. The slides show tools, not outcomes. A tool list is not an org chart: the hard part is the hand-offs between roles, which the carousel does not show. [Certain]

## How to use it

1. Pick the three roles that cost you the most hours; do not start with ten.
2. For each, name the input, the output and the human check. A role with no check is a risk.
3. Prefer a tool you already have connected (Notion and Higgsfield here) before adding a new one.
4. Keep the system of record single: one Notion database for ideas, assets, queue and metrics.
5. Automated DMs and comment-triggered messages are governed by each platform's rules; read them first. [Likely]
6. Do not install Hermes with a piped `curl | bash`; download and read the script first.

Connector changes were not made in the build session.
