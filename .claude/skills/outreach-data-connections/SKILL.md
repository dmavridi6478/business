---
name: outreach-data-connections
description: Map which outbound-tooling integrations (Apollo, Clay, lemlist, Sales Navigator/LinkedIn, G2, Product Hunt, n8n, Tavus/HeyGen) this environment actually has connected versus needs setup for, before any other outreach skill assumes a tool is reachable. Use at the start of a new outreach campaign, or when an outreach skill's step turns out to need a data source that hasn't been verified yet.
---

# Outreach Data Connections

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`connections.md — all integrations`, `raw/ — cached CSV outputs`); no external repo existed to vendor, so this is written fresh for this repo, covering the same concern.

The other seven outreach skills all assume specific external tools are reachable — this skill is the check that assumption before relying on it, rather than each skill silently guessing.

## What to check

For each tool referenced across the outreach skill set, confirm actual status rather than assuming from the tool's popularity:

| Tool | Used by | How to check |
|---|---|---|
| Apollo / Clay / lemlist | `outreach-list-building` (company sourcing) | MCP connector, or manual export/CSV import if unconnected |
| Sales Navigator / LinkedIn | `outreach-list-building` (people sourcing), `outreach-channels` (LinkedIn sequence) | MCP connector or manual; note LinkedIn automation risk if not using an approved tool |
| G2 / Product Hunt | `outreach-list-building` (niche/intent data) | Usually manual/API export, rarely a direct MCP connector |
| n8n | `outreach-automation` | Self-hosted or cloud instance + API credentials |
| Tavus / HeyGen | `outreach-channels` (video outreach) | API key required; paid account |
| Email sending infra | `outreach-copywriting` → send step | Separate from the above — verify deliverability/domain warmup status, not just API access |

Use the `mcp-integration-scout` agent (this repo's `.claude/agents/`) to do the live check — it's built exactly for this: survey what's connected before any skill reaches for a manual workaround.

## Cached outputs

Treat intermediate outputs (built lists, scraped enrichment data, campaign performance pulls) as worth caching locally during a working session rather than re-fetching from source on every step — outbound data sources often rate-limit or charge per lookup. Don't let a stale cache silently override a fresh signal, though: re-verify trigger data (funding, hiring, tech changes) close to send time, since triggers are time-sensitive by definition.

## Related skills in this repo

- **mcp-integration-scout** (agent): does the actual live connector survey this skill describes.
- **outreach-list-building**, **outreach-channels**, **outreach-automation**: each depends on a subset of the tools mapped here — check this first rather than discovering a missing connector mid-task.
- **capability-scout** (agent): broader version of the same check, across this repo's full skill/plugin library rather than just the outreach tool list.
