# "Deloitte-style AI marketing team": 12 departments, 60 agents (Batch 129)

Source: an infographic by Daniel McPherson, "Deloitte.-Style AI Marketing Team: 12 departments, 60 AI agents, all inside Claude Code." A "CMO" Claude Code turns one brief into a full marketing plan; the graphic shows "All 60 agents done" and ends "Comment MARKETING for the full team. Claude Code plans it, 60 agents build it, you approve it." The names and one-line jobs below are as printed. **The graphic shows no prompts or files**, so nothing below describes what an agent actually does; "Deloitte-style" is the author's phrase and implies no connection to that firm. The status ticks are a mock-up, not evidence of a working system. Compare the 50-role team in `../SKILL.md`, `claude-marketing-jobs` and `claude-marketing-department-48`.

| Department | Agents (printed job) |
|---|---|
| Strategy Office | strategy-lead (writes the annual plan), okr-setter (goals and KPIs), budget-planner (allocates the budget), scenario-planner (best and worst cases), board-reporter (one-page exec briefs) |
| Market Insights | market-sizer (TAM, SAM, SOM), trend-scout (spots shifts early), survey-designer (smart surveys), data-analyst (signal in noise), insight-writer (so-what memos) |
| Customer Lab | persona-builder (buyer personas), segment-mapper (who to serve), jtbd-interviewer (jobs to be done), voc-miner (customer voice), journey-mapper (buyer journey) |
| Competitor Intel | rival-tracker (rival moves), pricing-watcher (benchmarks pricing), ad-spy (rival ads), battlecard-maker (win battlecards), benchmark-scorer (you versus the top 5) |
| Brand Studio | positioning-lead (where you win), message-house (the core story), tagline-writer (names and taglines), tone-keeper (guards brand voice), brand-auditor (checks every asset) |
| GTM Office | launch-planner (days 1 to 90), offer-designer (packages your offer), channel-picker (where to show up), pricing-lead (prices for margin), sales-enabler (decks and one-pagers) |
| Content Studio | editorial-lead (runs the calendar), copywriter (posts, emails, pages), thought-leader (POV articles), repurposer (1 idea, 10 formats), campaign-planner (campaign briefs) |
| Demand Engine | paid-media (runs paid campaigns), seo-strategist (search that converts), linkedin-lead (posts that book calls), lead-scorer (scores every lead), funnel-builder (landing funnels) |
| Lifecycle Desk | onboarding-flow (owns the first 30 days), email-nurturer (nurture flows), churn-predictor (flags churn risk), upsell-finder (expansion deals), referral-engine (turns fans into leads) |
| Analytics Lab | attribution-pro (what drove sales), dashboard-maker (one live scorecard), kpi-monitor (alerts on any drop), ab-tester (tests, learns, scales), forecaster (next quarter) |
| Growth Office | growth-modeler (growth levers), cro-specialist (conversion rates), pipeline-auditor (funnel leaks), margin-analyst (profit by segment), experiment-lead (growth sprints) |
| Marketing Ops | crm-architect (keeps the CRM clean), automation-ops (automates busywork), stack-curator (lean martech stack), sop-writer (SOPs for the team), qa-checker (nothing ships broken) |

## Use, carefully
- Treat it as a department map: 12 functions with five jobs each. Pick the jobs you need; most teams need five to ten, not 60.
- Sixty agents from one brief multiplies cost and review work. Run one department first and read every output.
- Agents that touch ad accounts, the CRM or customer data (paid-media, crm-architect, lead-scorer, churn-predictor) need read-only access first, a spend cap in the ad platform itself and human approval before any write. See `claude-marketing-department-48` for the same rule.
- Churn and lead scoring use customer data: check privacy rules and keep models explainable.
- "Comment MARKETING for the full team" is a lead-generation hook; read every file before installing a pack received this way.
