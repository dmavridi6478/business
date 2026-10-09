---
description: How to use Claude in sales, organized by role (SDR, BDR, AE, Sales Engineer, Sales Manager, VP of Sales, Sales Ops, RevOps) — each with a job description, a pro tip, a ready prompt, and the common mistake to avoid
argument-hint: [your role — SDR, BDR, AE, Sales Engineer, Sales Manager, VP of Sales, Sales Ops, or RevOps]
---

# How to Use Claude in Sales — By Role

Source: @salesdaily.co, "How To Use Claude In Sales." Distinct from this repo's existing `claude-sales-prompts-20` (task-based: 20 prompts organized by sales activity) and `sales-workflow-catalog` (100 n8n automation workflows) — this one is organized by **job title**, and pairs each with the mistake people in that role actually make with Claude.

## SDR
**Job:** Personalize outreach at scale — research prospects, write cold emails, build tailored sequences.
**Prompt:** `Write 3 cold email variants for a [title] at a [size] [industry] company. My product solves [problem]. Under 80 words each, different angle.`
**Pro tip:** Paste a prospect's LinkedIn About section and last 3 posts. Ask for a personalized opening line. 30 seconds per prospect.
**Common mistake:** Sending Claude's emails untouched. Claude gets you 80%; the last 20% — the personal detail that proves you did the work — is yours.

## BDR
**Job:** Research target accounts, identify trigger events, build outbound account plans.
**Prompt:** `I'm targeting [company]. Find me 3 trigger events I can use as outreach angles and suggest which persona to contact first.`
**Pro tip:** Upload a list of 20 target accounts and ask: "Rank these by likelihood to buy based on company size, industry fit, and recent growth signals. Explain your reasoning."
**Common mistake:** Using Claude only for writing. The real unlock is research and account prioritization — let Claude think strategically, not just draft emails.

## AE (Account Executive)
**Job:** Prep for discovery, build business cases, simulate objections, strategize on complex deals.
**Prompt:** `I have a discovery call tomorrow with a [title] at [company]. They're evaluating us against [competitor]. Give me 5 questions that uncover real pain and differentiate us.`
**Pro tip:** After every call, paste your notes and ask: "What did the buyer reveal about their decision criteria, timeline, and internal politics? What should I ask next?"
**Common mistake:** Only using Claude before calls. The biggest value is after: analyzing what the buyer actually said vs. what you assumed.

## Sales Engineer
**Job:** Translate technical features into business outcomes. Build demo scripts, ROI models, comparison docs.
**Prompt:** `My prospect's engineering team cares about [requirement]. Write a one-pager showing how our [feature] solves this, with 3 quantified benefits.`
**Pro tip:** Ask Claude to build an interactive ROI calculator as an Artifact. Input deal-specific variables (team size, current costs, time savings) and share it directly with your champion.
**Common mistake:** Using Claude for generic feature dumps. Always give it the prospect's specific technical environment and requirements — generic outputs lose technical buyers instantly.

## Sales Manager
**Job:** Analyze team performance, build coaching plans, create onboarding materials.
**Prompt:** `Here's my team's pipeline data. Which deals are at risk based on days in stage, last activity, and deal size? Give me 3 coaching questions per deal.`
**Pro tip:** Upload your team's call recordings or transcripts. Ask Claude to score each rep on discovery depth, objection handling, and next-step setting. Build a coaching plan from the gaps.
**Common mistake:** Only using it for admin tasks like meeting agendas. The real leverage is pattern recognition across your team's deals and calls.

## VP of Sales
**Job:** Build forecasting models, analyze win/loss trends, design sales playbooks at scale.
**Prompt:** `Here's our last 4 quarters of pipeline data. What patterns do you see in win rates by segment, deal size, and sales cycle length? Where are we leaking revenue?`
**Pro tip:** Upload your win/loss data and ask: "What are the top 3 reasons we lose deals and what process changes would fix each one?" Use the output to restructure your playbook.
**Common mistake:** Treating Claude as a reporting tool. It's a strategic thinking partner. Ask it to challenge your assumptions, not just summarize your data.

## Sales Ops
**Job:** Clean CRM data, build territory models, design comp plans, document processes.
**Prompt:** `Here's our territory data. Model 3 territory splits optimized for: equal opportunity, geographic efficiency, and account potential. Show tradeoffs.`
**Pro tip:** Paste your current comp plan and ask: "Where are the perverse incentives? What behaviors does this plan accidentally reward or punish?" Get a second opinion before rollout.
**Common mistake:** Asking Claude to build complex dashboards. It works with the data you give it. Export, clean, and upload it — then let it analyze and model.

## RevOps
**Job:** Align sales, marketing, and CS data. Build attribution models and lead scoring frameworks.
**Prompt:** `Here's our full-funnel data from lead to close. Where's the biggest conversion drop-off and what are 3 hypotheses for why?`
**Pro tip:** Upload both your marketing lead data and sales pipeline data in one chat. Ask Claude to find mismatches between what marketing qualifies and what actually closes.
**Common mistake:** Asking broad questions like "fix our funnel." Give it a specific stage, specific metric, and specific timeframe. Narrow inputs get actionable outputs.

## Related

`claude-sales-prompts-20` (20 task-based prompts by sales activity, not role), `sales-workflow-catalog` (100 n8n sales-funnel automation workflows), `outbound-sales-system-5stage`, `sales-enablement`.
