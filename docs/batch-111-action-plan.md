# Batch 107 (files numbered 111) - action plan

Input: `LinkedIn_GTM_funnel_in_2026.zip` with 7 images (no PDFs): an animated GIF (181 frames, 11-module LinkedIn GTM funnel, Paolo Trivellato), "10 Claude Cowork Prompts That Save Sales Reps 5+ Hours/Week" (SalesDaily), "50 Claude Use Cases" (Jonathan Parsons), "How to Build a High-Performing AI Market Research Engine" (The Blueprint Weekly), "Turn YouTube Videos Into Learning App" (Cyberman AI), a PMP formulas cheat sheet (file named "Project Management Templates & Advanced Excel Dashboards"), and "Claude Code for Growth Marketing: 9 things" (IMG_8408).

## 1. Prompts to commands and skills (done, committed)
| Source | Skill | Command |
|---|---|---|
| 10 Cowork prompts | cowork-sales-prompts-10 | /cowork-sales-10 |
| 50 use cases | claude-50-use-cases-by-capability | /use-case-pick |
| Market research engine | ai-market-research-engine | /market-research-engine |
| YouTube learning app | youtube-to-learning-app | /youtube-learning-app |
| LinkedIn GTM funnel | linkedin-gtm-funnel-modules | /linkedin-gtm-funnel |
| PMP formulas | pmp-formulas-cheat-sheet | /pmp-formula |
| Growth marketing 9 | claude-code-growth-marketing-9 | /growth-build |
Plain-text prompts: `docs/batch-111-prompts.md`.

## 2. Tasks executed
- Built `Artifacts/business/pmp-project-dashboard.xlsx` (EVM, schedule and float, risk and PERT, benefits) with live formulas; recalculated in LibreOffice and checked against hand calculation (CPI 0.818, SPI 0.90, EAC 611,111, TCPI 1.051 for PV 100k, EV 90k, AC 110k, BAC 500k).
- The Cowork prompts contain tasks that need your files, folders and a schedule; none was run.

## 3. Workflows created (n8n, inactive drafts in your personal project)
- LinkedIn comment routing (GTM funnel 2026): https://dmavridi.app.n8n.cloud/workflow/WLDBoSf43k6GhXsa . Webhook, normalise, ICP gate, Slack alert or nurture. Needs a Slack credential and a sender for the webhook.
- Weekly market research engine (Perplexity to report): https://dmavridi.app.n8n.cloud/workflow/gQNaSzMRiGyAKo6D . Monday 08:00, Perplexity API, report to Slack. Needs a Perplexity API key (header credential) and edited brief fields.
Both validated by n8n before creation; neither has been run or published.

## 4. Design
Templates: infographic-bento-funnel-modules, infographic-hub-spoke-engine, cheatsheet-formula-grid, learning-app-shell. Themes: theme-sand-bento-orange, theme-blueprint-teal-grid. Rendered at 1280 and 390 px, no overflow; learning-app answer logic tested.

## 5. Agent
`.claude/agents/market-research-engine.md` built from the research-engine sheet (read and write-a-file only; no outward actions).

## 6. Connectors
Already connected: Gmail, Google Drive, Google Calendar, Notion, Slack, Calendly, Figma, Supermetrics, Motion Creative Analytics, Semrush, Ahrefs, Taplio LinkedIn, Typefully, HubSpot, n8n, TinyFish, Amplitude, Consensus, Exa, GitHub.
Installable but not installed (needs your sign-in at claude.ai > Connectors): Firecrawl, Webflow, PostHog, Adspirer (search and social), Windsor.ai.
Half-connected: Vercel (connect incomplete). BigQuery: failed to connect (auth server does not support dynamic registration).
Not in the registry: Perplexity, DataForSEO, Searchable, NotebookLM, Gemini.
No `.mcp.json` change was made: nothing was verified as a safe remote server, and earlier batches recorded that edits to connector config are blocked by the permission classifier.

## 7. Not done - needs you
| Item | Why | Step |
|---|---|---|
| Install Firecrawl, Webflow, PostHog, Adspirer, Windsor.ai, finish Vercel | OAuth sign-in cannot be done from this session | claude.ai > Connectors |
| Perplexity | No connector; API key is yours | Create key at Perplexity, add as credential in the n8n workflow |
| Publish or run the two n8n workflows | They send Slack messages and call a paid API | Open the links, add credentials, test, then publish |
| Schedule Cowork prompts 4 and 7 | Recurring, needs folders and the Cowork desktop app | Run `/cowork-sales-10 4` and `7` there |

## 8. Claims to treat as unverified
- "5+ hours a week saved" (SalesDaily title): no method shown.
- The LinkedIn funnel's "$10k/mo" qualifier and the 14-day and 7-day thresholds in the Cowork prompts are the authors' rules of thumb.
- No results or conversion data accompany any of the seven images.
- The "Claude Code for Growth Marketing" tool logos (Searchable, DataForSEO) were read from small icons; names may differ from the vendors' current ones.
