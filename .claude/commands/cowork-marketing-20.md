---
description: 20 Claude Cowork marketing tasks across Research, Content, Social, and Reporting teams
argument-hint: [task number, team name, or "all" to see full list]
---

You are a marketing operations specialist running Claude Cowork automation for "$ARGUMENTS". Execute the relevant task or list the full set of automatable marketing workflows.

*How it works: Type a task → Cowork runs it → File lands. Runs on schedule, even with your laptop asleep.*

---

## RESEARCH TEAM (Tasks 01–05)

### Task 01 — Rival Pricing Monitor
**Tool:** Browser
**Prompt:**
"Open 3 rival pricing pages and log what changed vs last week. Check [Competitor 1 URL], [Competitor 2 URL], [Competitor 3 URL]. For each page: (1) note current pricing tiers and prices, (2) flag any changes from the prior version — new tiers, price increases, feature moves, new offers. Output a change log doc with date, competitor, change description, and my recommended response."

**Output:** A change log doc

---

### Task 02 — Industry Newsletter Shifts
**Tool:** Browser
**Prompt:**
"Read 5 industry newsletters from this week and identify the 3 most important shifts in our market. Newsletters: [list 5 newsletter URLs or names]. For each shift, give: (1) what is changing, (2) why it matters for our business, (3) one action we should take in the next 30 days. Output as a structured brief."

**Output:** 3 shifts, with sources

---

### Task 03 — G2 Customer Quote Scraper
**Tool:** Browser
**Prompt:**
"Pull every customer review from our G2 page at [G2 URL]. For each review: extract the customer's role/company size if listed, the key benefit they name, any specific result or metric they mention, and any criticism. Organise into a spreadsheet with columns: Reviewer, Role, Company Size, Key Benefit, Result/Metric, Criticism, Verbatim Quote. Flag the 5 quotes most useful for marketing copy."

**Output:** Quotes in a sheet

---

### Task 04 — Keyword Rank Tracker
**Tool:** Browser
**Prompt:**
"Check the current Google search rank for these 10 keywords: [list 10 keywords]. For each keyword, note: current position, prior position from last check, page 1 / not page 1, and the URL currently ranking. Flag any keyword that dropped more than 3 positions. For flagged keywords, give me one specific on-page action to recover the position."

**Output:** Rank table, drops flagged

---

### Task 05 — Sales Call Objection Ranker
**Tool:** Files
**Prompt:**
"Read the 20 sales call notes in [folder/file]. For each call, identify every objection raised by the prospect — price, timing, authority, need, trust. Categorise and count objection frequency across all 20 calls. Rank objections from most to least common. For the top 5 objections, write a 2-sentence handling script. Output as a ranked objection sheet."

**Output:** Objections, ranked

---

## CONTENT TEAM (Tasks 06–10)

### Task 06 — Brief to Captions
**Tool:** Plugin (Brand Voice)
**Prompt:**
"Turn this campaign brief into 5 social media captions in our brand voice. Brief: [paste brief]. For each caption: write for a different platform angle (awareness, consideration, conversion, retention, community). Each caption must be under 280 characters for Twitter/X compatibility, include a clear hook in line 1, and end with a call to action. Use our brand voice: [describe voice — e.g., direct, confident, no fluff]."

**Output:** 5 on-brand captions

---

### Task 07 — Blog to LinkedIn Posts
**Tool:** Drive
**Prompt:**
"Rewrite our 3 best-performing blog posts as LinkedIn posts. Blog posts: [link 1], [link 2], [link 3]. For each LinkedIn post: open with a pattern-interrupt hook (not the blog title), tell the core insight as a short story or list, end with a question or call to action that invites comments. Keep each post under 1,300 characters for full visibility without 'see more'. Output as 3 ready-to-post LinkedIn drafts."

**Output:** 3 ready posts

---

### Task 08 — Weekly Newsletter Draft
**Tool:** Drive
**Prompt:**
"Draft this week's newsletter from our published posts and content. This week's posts: [list titles or URLs]. Newsletter structure: (1) subject line — curiosity or value-led, under 50 characters; (2) preview text — 90 characters, extends the subject line; (3) intro — 2 sentences, sets context for this week; (4) 3 content blocks — one insight, one resource, one action; (5) close — personal sign-off, one ask or question for the reader. Tone: [your tone]. Length: under 400 words."

**Output:** A newsletter draft

---

### Task 09 — Campaign Deck Builder
**Tool:** Files
**Prompt:**
"Build a 6-slide campaign presentation deck from this campaign document: [file or paste content]. Slide structure: Slide 1 — Campaign name and one-line objective; Slide 2 — Target audience and insight; Slide 3 — Campaign idea and creative direction; Slide 4 — Channel plan and budget split; Slide 5 — KPIs and success metrics; Slide 6 — Timeline and key milestones. Each slide: title, 3–5 bullet points, no full sentences. Output as a structured document I can paste into slides."

**Output:** A 6-slide deck file

---

### Task 10 — Webinar to Blog
**Tool:** Files
**Prompt:**
"Turn this 40-minute webinar transcript into a blog post. Transcript: [paste or link]. Blog structure: (1) headline — SEO-optimised, contains the primary keyword; (2) intro — 150 words, hook + promise + credibility; (3) 5 main sections — one for each key topic covered in the webinar, with subheadings; (4) conclusion — 100 words with key takeaway and CTA; (5) meta description — 155 characters. Remove filler, presenter asides, and Q&A. Tone: [brand tone]. Target keyword: [keyword]."

**Output:** A blog draft doc

---

## SOCIAL TEAM (Tasks 11–15)

### Task 11 — Weekly Posts Scheduler
**Tool:** Schedule (every Sunday)
**Prompt:**
"Every Sunday, draft next week's 5 social posts — one for each weekday Monday through Friday. For each post: choose a content type (Monday = insight, Tuesday = behind-the-scenes, Wednesday = social proof, Thursday = educational, Friday = engagement question). Use this week's content themes: [themes]. Write each post for LinkedIn and include a hook, body, and CTA. Output as 5 ready-to-schedule posts by Sunday evening."

**Output:** 5 drafts by Monday

**Schedule command:** `/schedule Every Sunday at 8pm, draft next week's 5 social posts`

---

### Task 12 — Launch Hooks Generator
**Tool:** Chat
**Prompt:**
"Write 10 hooks for our upcoming launch post, ranked from most likely to stop the scroll to least. The launch: [describe offer, product, or event]. Hook types to include: (1) bold statement, (2) surprising number, (3) contrarian take, (4) curiosity gap, (5) story opener, (6) direct address, (7) before/after, (8) warning, (9) question, (10) list. For each hook, note the psychological trigger it uses."

**Output:** 10 hooks, best first

---

### Task 13 — Multi-Channel Message Adapter
**Tool:** Chat
**Prompt:**
"Adapt this core message for 3 different channels — X/Twitter, LinkedIn, and email. Core message: [paste message]. For X: max 280 characters, punchy, hook-first. For LinkedIn: 150–300 words, professional, end with a question. For email: subject line (50 chars), preview text (90 chars), body (200 words), CTA button text. Keep the core idea identical but adapt the tone, length, and format to platform norms."

**Output:** 3 channel versions

---

### Task 14 — Video Script to Short Posts
**Tool:** Files
**Prompt:**
"Cut this video script into 5 short social posts. Script: [paste script]. For each post: (1) extract a single insight or story beat from the script, (2) rewrite it as a standalone post that works without watching the video, (3) add a hook that earns attention without context, (4) end with a CTA to watch the full video. Each post should be under 300 characters for maximum reach. Output as 5 ready-to-publish posts."

**Output:** 5 short posts

---

### Task 15 — 4-Week Content Calendar
**Tool:** Files
**Prompt:**
"Plan a 4-week content calendar in a spreadsheet format. Inputs: platforms [list], posting frequency [e.g., 3x/week per platform], content themes [list 3–5 themes], upcoming campaigns or launches [list]. For each post slot, fill in: Date, Platform, Content Type, Hook/Topic, Format (post/video/carousel/story), Status (draft/scheduled/live). Output as a table ready to paste into a spreadsheet."

**Output:** A calendar sheet

---

## REPORTING TEAM (Tasks 16–20)

### Task 16 — Weekly Numbers Summary
**Tool:** Schedule (every Monday 9am)
**Prompt:**
"Every Monday at 9am, summarise last week's campaign numbers into a one-page brief. Pull data from [connected sources]. Structure: (1) top-line — total spend, total revenue, overall ROAS; (2) by channel — spend, revenue, ROAS for each; (3) wins — what outperformed; (4) misses — what underperformed; (5) this week's priority — one thing to fix, one thing to scale. One page, no tables longer than 6 rows."

**Output:** One-page summary

**Schedule command:** `/schedule Every Monday at 9am, summarise last week's campaign numbers`

---

### Task 17 — SEO Weekly Report
**Tool:** Schedule (every Friday)
**Prompt:**
"Every Friday, build the SEO performance report from our data export. Report sections: (1) organic traffic — week vs prior week vs prior year; (2) keyword rankings — top 20 terms, any moved up or down >3 positions; (3) top pages — 10 pages by organic sessions this week; (4) technical issues — any new crawl errors or Core Web Vitals flags; (5) action item — the single most important SEO task for next week."

**Output:** SEO report by Friday

**Schedule command:** `/schedule Every Friday at 4pm, build the weekly SEO report from our export`

---

### Task 18 — Friday Wins Email
**Tool:** Gmail
**Prompt:**
"Draft the Friday wins email to the team. This week's wins: [list key results — revenue, campaigns, content, client feedback]. Email structure: (1) subject line: 'Week [number] wins — [headline number or result]'; (2) intro: 2 sentences setting up the week; (3) 3 bullet wins with the number, what it means, and who did it; (4) next week preview: 2 bullets on what we're focused on; (5) closing line: motivating, not generic. Tone: direct, proud, brief. Under 200 words."

**Output:** Gmail draft, ready to send

---

### Task 19 — Ad Underspend Flagger
**Tool:** Files
**Prompt:**
"Review this month's ad budget spreadsheet: [file]. For each campaign, calculate: (1) expected spend to date (monthly budget × days elapsed / days in month); (2) actual spend to date; (3) underspend or overspend amount and percentage. Flag every campaign underspending by more than 15%. For each flagged campaign, identify whether the issue is budget cap, low bid, disapproved ads, low Quality Score, or audience size. Output as a flagged underspend list with root cause."

**Output:** An underspend list

---

### Task 20 — Lead List Cleaner
**Tool:** Files
**Prompt:**
"Clean, dedupe, and tag this lead list: [file]. Steps: (1) remove duplicates — same email or same name + company; (2) standardise formatting — capitalise names, lowercase emails, consistent phone format; (3) tag each lead by source if column exists; (4) flag leads with missing email, missing company, or obviously fake entries (test@test.com, etc.); (5) output a clean version and a separate 'removed' tab with reason for removal."

**Output:** A clean lead list

---

## AI PROMPTS — PLAIN TEXT (copy and paste)

**Rival pricing monitor:**
Open 3 rival pricing pages and log what changed vs last week. Note current pricing tiers, flag any changes, and output a change log with date, competitor, change description, and my recommended response.

**Industry shifts:**
Read 5 industry newsletters from this week. Identify the 3 most important market shifts. For each: what's changing, why it matters, one action to take in the next 30 days.

**Customer quotes:**
Pull every customer review from our G2 page. Extract: reviewer role, key benefit named, any result or metric, and any criticism. Flag the 5 quotes most useful for marketing copy.

**Keyword rank check:**
Check the current Google rank for these 10 keywords: [list]. Note current position, prior position, page 1 status. Flag drops >3 positions with one recovery action each.

**Objection ranker:**
Read 20 sales call notes. Identify every objection raised. Rank by frequency. For the top 5, write a 2-sentence handling script.

**Weekly posts:**
Every Sunday, draft next week's 5 social posts — one per weekday, rotating content types: insight, behind-the-scenes, social proof, educational, engagement question.

**Launch hooks:**
Write 10 hooks for the launch post, ranked by scroll-stop potential. Include: bold statement, surprising number, contrarian take, curiosity gap, story opener, direct address, before/after, warning, question, list.

**Multi-channel adapt:**
Adapt this core message for X/Twitter (280 chars), LinkedIn (150–300 words with question), and email (subject + preview + 200-word body + CTA). Keep the idea identical, adapt the format.

**Monday numbers brief:**
Summarise last week's campaign numbers: total spend, total revenue, overall ROAS; breakdown by channel; 3 wins; 3 misses; this week's single priority to fix and single priority to scale.

**Lead list clean:**
Clean, dedupe, and tag this lead list. Remove duplicates, standardise formatting, tag by source, flag missing data and fake entries. Output clean version and removed-items tab with reasons.

---

**Schedule this week:** `/schedule Every Monday at 9am, summarise last week's campaign numbers.`
