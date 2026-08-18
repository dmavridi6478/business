---
name: outreach-automation
description: Automate outbound-campaign workflows with n8n — building import-ready n8n workflow JSON, debugging common n8n errors, and scraping websites (Playwright/BeautifulSoup-style) to supplement list enrichment where standard data sources fall short. Use when a validated manual outbound process needs to run on autopilot, or when an n8n workflow for outreach is erroring.
---

# Outreach Automation

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`n8n-workflow-builder.md`, `n8n-debugger.md`, `website-scraper.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same three concerns as one skill.

Automate a step only after it's been run manually enough times to know it's worth automating — automating a broken or unvalidated process just fails faster and at higher volume.

## 1. n8n workflow builder

Structure outbound workflows around the pipeline stages already defined elsewhere in this skill set: a trigger (new row in the list from `outreach-list-building`, or a scheduled poll), an enrichment/dedup step, a send step per channel, a wait/branch step keyed to reply detection (feeding `outreach-replies-pipeline`'s classification), and an exit condition matching `outreach-campaign-design`'s architecture. Build workflows as JSON exports that can be imported directly rather than describing steps in prose — n8n's own format is the actual deliverable here, not a summary of it. Keep credentials and API keys out of the exported JSON; reference them via n8n's credential store instead of hardcoding.

## 2. n8n debugger

Common failure patterns worth checking first, before deep-diving a specific node: rate-limit errors from sending too fast on a channel with volume caps (LinkedIn especially), auth/credential expiry on a connected service, malformed data reaching a node because an upstream step's output schema changed, and infinite-loop risk in reply-triggered branches that don't have a clear exit condition. Reproduce the specific failing execution before proposing a fix — n8n's execution history shows the actual data at each node, which is more reliable than guessing from the workflow diagram alone.

## 3. Website scraper for enrichment

When a target isn't covered by `outreach-list-building`'s standard sourcing tools (a niche site, a company's own team/about page for contact discovery, a job board for hiring-trigger detection), scrape directly — respecting robots.txt and rate limits, and preferring a site's own structured data (JSON-LD, sitemaps) over brittle HTML parsing where available. This supplements the standard sourcing pipeline; it's not a replacement for it, since scraped data typically needs more verification before trusting it as a trigger signal.

## Related skills in this repo

- **outreach-list-building**: the scraper here extends that skill's sourcing when standard tools don't cover a target.
- **outreach-replies-pipeline**: reply-triggered n8n branches feed that skill's classification and pipeline tracking.
- **outreach-data-connections**: check there first for which services already have credentials/connectors set up before building a new n8n integration node from scratch.
- **web-task-scoping**: apply that skill's Target/Limit/Run/Review discipline before granting any scraper or automation broader autonomy on a live site.
