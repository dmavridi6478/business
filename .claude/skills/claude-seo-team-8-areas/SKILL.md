---
name: claude-seo-team-8-areas
description: Maps the "Complete Claude SEO Team - 20 AI SEO Agents" graphic (eight workflow areas around a hub) onto the SEO agents, skills and connectors that already exist in this workspace, so one request can be routed to the right specialist. Covers keyword research, technical SEO, content and on-page, internal linking, backlinks, AI search (GEO), competitor analysis, and tracking and reporting, with a run order and the data each area needs. Use when the user asks for an SEO team, a full SEO workflow, an SEO audit plan, or wants to know which agent handles which SEO task.
---

# Claude SEO team - eight areas

Source: infographic "The Complete Claude SEO Team: 20 AI SEO Agents" (image supplied in chat, 12 October 2026; call to action: comment "SEO").

**What the image actually shows:** eight labelled areas around a hub, not twenty named agents. The "20" is not itemised, and the comment-to-receive gate means the vendor's agent files were not available to me. This skill maps the eight visible areas to what is already installed here and does not pretend to reproduce the missing twelve.

## Routing table

| Area (as labelled) | What the graphic says | Agent or skill to use here | Data connector |
|---|---|---|---|
| Keyword research and strategy | Find opportunities, build a keyword plan | `seo-keyword-strategist`, `searchfit-seo:keyword-cluster`, `seo-content-planner` | Ahrefs, Semrush |
| Technical SEO and audits | Crawl issues, indexing, site health | `seo-specialist`, `searchfit-seo:seo-auditor`, `seo-audit` skill | Ahrefs site audit, Semrush site audit |
| Content and on-page | Create and optimise pages | `seo-content-writer`, `seo-content-auditor`, `seo-meta-optimizer`, `seo-snippet-hunter` | Ahrefs content helper |
| Internal linking and site structure | Stronger site architecture | `seo-structure-architect`, `searchfit-seo` internal-linking skill, `site-architecture` skill | Ahrefs pages by internal links |
| Backlinks and authority | Grow authority, link opportunities | `seo-authority-builder`, `seo-backlinks` skill | Ahrefs backlinks, Semrush backlinks |
| AI search (GEO) | Visibility in AI answers | `ai-search-visibility`, `aeo-diagnostic-metrics`, `answer-engine-gap-auditor` | Ahrefs Brand Radar |
| Competitor analysis | Find gaps and opportunities | `searchfit-seo:competitor-analyzer`, `competitor-profiling` | Ahrefs, Semrush organic competitors |
| Tracking and reporting | Measure results and next steps | `content-analyst`, `windsor-ai` reports | Ahrefs rank tracker, Google Search Console via Ahrefs, Supermetrics |

Cannibalisation and freshness are covered by `seo-cannibalization-detector` and `seo-content-refresher`.

## Run order (what to ask first)

1. **Tracking baseline** - rank tracker and Search Console data, so every later change can be measured.
2. **Technical** - fix crawl and index blockers before writing anything.
3. **Competitors** - find the gaps.
4. **Keywords** - choose targets from those gaps.
5. **Content and on-page**, then **Internal linking**.
6. **Backlinks** - only after pages worth linking to exist.
7. **GEO** - structure answers for AI citation; check citations monthly.
8. **Report** - what changed, what moved, next two actions.

## Rules

- An agent reads and recommends. Changes to a live site go through the owner.
- Numbers (volume, difficulty, rankings) come from the connector, with the date. Never from memory.
- GEO results are noisy; do not promise placement.

## Command and agent

`/seo-team <site or topic>` runs the routing. The orchestrator is `.claude/agents/seo-team-orchestrator.md`. The design template is `Artifacts/templates/hub-spoke-agent-team-radial.html`.
