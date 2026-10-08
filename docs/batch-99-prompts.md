# Batch 99 — prompts in plain text (copy and paste)

Replace every [BRACKET] before sending. Slash commands live in `.claude/commands/`; skills in `.claude/skills/`.

## A. Executive presence (Dora Vanourek) — `/exec-presence`
A1. Rehearsal audit
Use the executive-presence-8 skill. Here is my talking-points draft for [MEETING] with [AUDIENCE]: [PASTE TEXT]. Score the 8 habits 0-2 with a quoted line as evidence, count undermining phrases (just, kind of, I think maybe), rewrite my three weakest lines, and give me one habit and one exact phrase to practise this week.

A2. Phrase drills (from the card)
- Strategic silence: ask "What are your thoughts?" and then hold the pause.
- Name the elephant: "Can we talk about what's really going on?"
- Make others look brilliant: "That was Sarah's idea." (then add your take)
- Own your authority: drop "just", "kind of", "I think maybe". Say "I recommend."
- Calibrate: ask "Will this matter in 6 months?" and pause before responding.
- Disagree without drama: "I see it differently. Here's why."

## B. CMO operating cadence — `/cmo-cadence` (prompts are the card's own wording)
01 Inbox drafts (scheduled task, 7am; needs Gmail): Draft replies in my voice to unread emails that need one. Never send.
02 Industry roundup (scheduled task, 7am): Find yesterday's top 5 industry news stories and give me one idea for each.
03 Daily priorities: Using my calendar and open tasks, pick my top 3 priorities today, and what I can delegate or drop.
04 Weekly report (dashboard + Monday 6am task): Build a dashboard of last week's results by channel. / then schedule: Refresh the data.
05 Delegation board: Build a tracker with task, owner, due date, and status. (Paste in team updates each week and ask what is late.)
06 Plan reviewer (skill `cmo-plan-reviewer`): Review this plan against our goals and budget. List risks, gaps, and three questions I should ask.
07 Monthly review (skill `cmo-monthly-review`): From this data, write wins, misses, lessons, and next month's changes. Plain English, one page.
08 Strategy reset: Based on last month's results, what are our three biggest gaps? Suggest 5 experiments ranked by impact and effort.
09 Budget vs actuals: (upload budget and actuals) Build a dashboard of spend vs plan by channel, with a forecast.
10 Brief writer (skill `cmo-brief-writer`): Turn these notes into a brief: goal, audience, message, deliverables, budget, and deadline.
11 Competitor scan: Search the web for [COMPETITOR]'s latest launches and ads. What changed, and what should we do about it?
12 Exec update: Summarise these updates in five lines for the CEO: progress, risks, and what I need from them.

## C. AEO diagnostic metrics (Gartner) — `/aeo-score`
C1. Page score
Use the aeo-diagnostic-metrics skill on [ENTITY] and these URLs: [URL1] [URL2]. Score answer extractability 0-5 per URL with quoted evidence, build the entity attribute list and report % coverage, and mark citation rate and citation quality NOT MEASURED unless I give you a prompt set and real citations. Finish with five prioritised fixes.

C2. Citation-rate prompt-set template (run by hand in each answer engine on the same day)
List 20-50 questions a buyer of [ENTITY] would ask, one per line. For each engine record: question, date, was my URL cited (yes/no), the URL that was cited instead. Citation rate = questions where my URL is cited / questions run.

## D. McKinsey 7S — `/7s-audit`
D1. Collect scores
Send each leader this: Score our organisation 1-10 on Strategy, Structure, Systems, Shared Values, Style, Staff and Skills, and add one sentence of evidence for each. Do this alone, before any discussion.

D2. Analyse
Use the mckinsey-7s-model skill. Here are the independent scores: [TABLE]. Build the matrix with mean and spread, flag spread of 3 or more, name the top three blind spots with their evidence, order the fixes (Shared Values, Structure, Systems, Style, Staff, Skills) and write a 30-minute quarterly review agenda.

## E. Token rules — `/token-audit`
E1. Run: /token-audit   (measures CLAUDE.md words and lines, lists enabled connectors and scheduled routines)
E2. Session openers from the card: "Ask me questions first." / "No web search." / "Only redo this section." / "Summarise this chat in 10 lines" (then start a new chat).

## F. Connectors — `/connector-stack`
F1. Life stack: /connector-stack life
F2. Content stack: /connector-stack content
F3. First read-only tests (run one at a time, one connector per week):
- Gmail: Find that invoice from last month. Do not draft or send anything.
- Calendar: Check my real availability next Tuesday and suggest three times. Do not create events.
- Notion: What's still open on my task list?
- Drive: Read [FILE] and summarise it in five lines.
F4. Content stack workflow: Using my Fathom transcripts, list the five most repeated client questions or objections and turn each into a post outline. Use Exa to find the original source behind any claim before I publish.

## G. Plugin test prompts (after installing; the card's examples)
- /plugin install paypal@claude-plugins-official  →  add a monthly plan with PayPal
- /plugin install modern-web-guidance@claude-plugins-official  →  (no prompt needed; guidance applies when writing web code)
- /plugin install browser-use@claude-plugins-official  →  sign up on my site like a new user
- /plugin install lovable@claude-plugins-official  →  /lovable:iterate bigger signup button
- /plugin install hyperframes@claude-plugins-official  →  make a promo video of my landing page
