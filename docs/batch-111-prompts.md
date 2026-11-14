# Batch 107 prompts in plain text (file numbered 111)

Copy and paste. Fill each [bracket]. Each one is also installed as a command (see the action plan).

## A. Ten Claude Cowork prompts for sales (SalesDaily.co) - `/cowork-sales-10 [1-10]`

1. Account brief
```
Go through my Google Drive folder [folder name]. Pull every doc, email, and note related to [account name]. Build me a one-page account brief with: deal history, key stakeholders, open issues, and last 3 touchpoints.
```
2. CRM hit list
```
Here's my pipeline export [file]. Score every deal by likelihood to close this quarter based on last activity date, deal stage, and deal size. Flag anything that's been stuck in the same stage for 14+ days. Save as a spreadsheet sorted by priority.
```
3. Deals going dark
```
Check my Gmail for any prospect threads where I sent the last message and haven't gotten a reply in 7+ days. List them out with the contact name, company, what I last sent, and draft a follow-up for each one.
```
4. Weekly pipeline report (scheduled)
```
Schedule this: Every Friday at 4pm, pull my latest pipeline data from [CRM export folder], calculate week-over-week movement by stage, flag any deals that slipped or stalled, and save a one-page summary to my Desktop.
```
5. Prospect footprint
```
Use the browser to research [prospect name] at [company]. Check their LinkedIn activity, recent company press releases, job postings, and earnings calls. Save a one-page research brief to my Sales Prep folder.
```
6. Custom battle card
```
Go to [competitor website] and pull their pricing page, features page, and latest case studies. Compare against our positioning doc in [folder]. Build a battle card with: where we win, where they win, objection responses, and talk tracks.
```
7. Meeting prep (scheduled)
```
Schedule this: Each morning at 7am, check my calendar for today's external meetings. For each one, look up the attendee's company, pull any related files from my Drive, and drop a 5-bullet prep doc on my Desktop before I start work.
```
8. Call recordings to deal intelligence
```
Here are my call transcripts from this week [folder]. For each call, extract: buyer's stated priorities, objections raised, competitors mentioned, next steps promised, and any budget or timeline signals. Save as one summary doc.
```
9. Clean and enrich prospect list
```
Take this spreadsheet of leads [file]. Use the browser to verify each company's website, employee count, and industry. Remove any that are under 50 employees. Add a column with a personalized reason to reach out based on what you find. Save the updated file.
```
10. QBR deck
```
Open my [account name] folder. Read through every doc, email thread, and note from the last 90 days. Build a QBR presentation with: executive summary, key wins, usage highlights, open risks, and a proposed plan for next quarter. Save as a PPTX to my Desktop.
```

## B. YouTube to learning app (Cyberman AI) - `/youtube-learning-app`

```
Turn the attached notebook into an interactive learning app for [topic].
- explain concepts in plain English
- let me ask questions anytime
- break ideas into small steps
- quiz me after each section
- give real examples and use cases
- summarize what I've covered
- track what I've learned so far
```

## C. AI market research engine - `/market-research-engine`
Written from the six-step sheet; the sheet itself gives steps, not prompt text.

Claude Code, to run the loop:
```
Read my About Me file, target audience and content strategy. Then research [topic] for [audience]: 1) common questions, community problems and objections before buying; 2) recent industry reports, original research and surveys with dates and links, opening each source to confirm it; 3) what competitors publish and the gaps against my strategy; 4) repeated patterns, conflicting findings and topics worth exploring. Save a markdown report with: research topic, main findings, conflicts, content ideas, sources marked verified or unverified.
```
Perplexity, if you run the steps by hand:
```
Research the latest (last 90 days) on [topic]. Audience: [audience]. Return common questions, community problems, objections before buying, and industry reports and original research with dates and links.
```

## D. LinkedIn GTM funnel - `/linkedin-gtm-funnel`
```
Audit my LinkedIn funnel against the 11 modules: content stack, comment routing, idea sources, post jobs, post review, weekly setup, lead readiness, DM handling, posting calendar, booking handoff, funnel rules. My offer: [offer]. My ideal customer: [ICP]. Numbers: [posts per week, comments, opt-ins, bookings]. For each module say in place, partly or missing, then give the five highest-impact changes and the three numbers to track.
```

## E. Project controls - `/pmp-formula`
```
Compute earned value for my project: PV [x], EV [x], AC [x], BAC [x]. Give CV, SV, CPI, SPI, both EAC forms, ETC, VAC and TCPI, say what each means, and name the first action I should take.
```

## F. Growth marketing builds - `/growth-build [1-9]`
```
Brief me on build [number] from the nine growth-marketing systems: the question it answers each week, the data it reads, where it writes, which connectors I already have, and the first read-only version I can run today.
```

## G. 50 use cases - `/use-case-pick`
```
My goal is [goal / role]. Pick the three best items from the 50 Claude use cases, say which Claude surface to use for each, and give me a first prompt to paste.
```
