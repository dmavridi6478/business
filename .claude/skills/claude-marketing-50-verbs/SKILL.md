---
name: claude-marketing-50-verbs
description: A 50-verb menu of single-purpose marketing jobs for Claude (RESEARCH, ANALYZE, SUMMARIZE ... SCHEDULE), each with its input-to-output shape and a ready prompt starter, plus rules that make any verb reliable (name the source data, the output format and a check). Use when someone asks "what can Claude do for my marketing", wants a prompt for one specific job (hook, headline, dedupe, cluster, disprove, mine reviews), or needs to pick the right verb for a task. Run via /marketing-verb. Source - "50 ways to use Claude for marketing" infographic (Emilia Moller).
---

# 50 ways to use Claude for marketing

Source: a one-page infographic listing 50 verbs, each with a one-line "input -> output". It is a menu, not a method. A verb alone produces generic output; every prompt below therefore follows the **verb contract**.

## The verb contract (apply to every job)

1. **Source** - name the data Claude must use (file, URL list, pasted text, connector). No source = no verb.
2. **Output** - name the exact format (table, brief, 5 options, XLSX formula) and length.
3. **Check** - ask for one self-check (assumptions listed, claims marked "not in the data", counts reconciled).
4. Anything that would be sent, published or spent stays a draft until a human approves it.

## The 50 verbs

| # | Verb | Job (input -> output) | Prompt starter |
|---|---|---|---|
| 1 | RESEARCH | 30 sources -> one answer | "Using only these sources, answer [question]. Cite each claim to a source; list what the sources disagree on." |
| 2 | ANALYZE | raw CSV -> actual insights | "Analyse this CSV. State the 5 findings that would change a decision, with the numbers behind each." |
| 3 | SUMMARIZE | 100 pages -> what matters | "Summarise to one page: decisions needed, risks, numbers. Quote anything you are unsure of." |
| 4 | COMPARE | you vs 10 competitors | "Compare us with these 10 on [criteria] as a table. Mark every cell 'verified' or 'inferred'." |
| 5 | EXTRACT | 50 calls -> recurring patterns | "From these transcripts extract recurring pains, phrases and objections with call counts." |
| 6 | INTERVIEW | calls -> pains + objections | "Turn this call into: top 3 pains, top 3 objections, buying triggers, exact quotes." |
| 7 | BRAINSTORM | 5 directions, not 50 ideas | "Give 5 clearly different directions for [goal]; for each the bet, the risk and the cheapest test." |
| 8 | CHALLENGE | make the case against your strategy | "Argue against this strategy as its smartest critic. Then say which objection is strongest." |
| 9 | CRITIQUE | ask what is wrong, not what is good | "List what is wrong with this draft, ranked by damage. No praise." |
| 10 | VALIDATE | pressure-test before you build | "List the 5 assumptions this idea needs to be true and the fastest evidence for each." |
| 11 | SIMULATE | see it as your customer | "Act as [persona]. React to this page line by line: what you believe, doubt, skip." |
| 12 | POSITION | find what only you can say | "From our proof and the competitor claims, find the statement only we can make and can prove." |
| 13 | SEGMENT | find audiences hidden in your data | "Cluster these customers into 3-5 segments; name each by behaviour, size and value." |
| 14 | PERSONALIZE | one message -> every audience | "Rewrite this message for each of these audiences; keep the offer identical, change the angle." |
| 15 | MEETING | notes -> actions + owners | "From these notes list decisions, actions with owner and date, open questions." |
| 16 | EDIT | good -> actually worth reading | "Edit for clarity and cut 20%. Keep my voice. Show what you removed." |
| 17 | SURVEY | responses -> key findings | "Summarise these responses: top findings, the minority view, one surprising result." |
| 18 | REPURPOSE | 1 webinar -> 20 assets | "From this transcript produce: 5 posts, 3 emails, 1 article outline, 5 hooks, 3 quotes." |
| 19 | SCRIPT | idea -> short-form video | "Write a 30-45 second script: hook, 3 beats, CTA, on-screen text." |
| 20 | HOOK | generate + rank opening lines | "Give 15 opening lines across 5 hook types; rank the top 3 and say why." |
| 21 | HEADLINE | generate + score alternatives | "Give 10 headlines; score each 1-5 for clarity, specificity, curiosity." |
| 22 | DEDUPE | messy list -> clean data | "Deduplicate by email then company+name; show merge rules and the count removed." |
| 23 | BRIEF | idea -> execution-ready brief | "Turn this idea into a brief: goal, audience, message, deliverables, KPI, deadline, owner." |
| 24 | PLAN | goal -> tasks + deadlines | "Break this goal into tasks with owner, dependency and date; flag the critical path." |
| 25 | ORGANIZE | chaos -> structured system | "Propose a folder/tag/naming system for these assets and map every file into it." |
| 26 | CALCULATE | model CAC, ROI + scenarios | "Model CAC, payback and ROI for base/low/high; state every assumption in a table." |
| 27 | FORMULA | describe it -> Excel formula | "Write the Excel formula for [description]; explain it and give a test row." |
| 28 | CLEAN | messy spreadsheet -> usable data | "Normalise these columns (case, dates, currency); list every change you made." |
| 29 | CLUSTER | 1,000 responses -> themes | "Cluster these responses into themes; give count, share and 2 verbatim quotes per theme." |
| 30 | CLASSIFY | sort leads, feedback or content | "Classify each row into [labels]; add a confidence flag and list the unclear rows." |
| 31 | SCORE | rank ideas against your criteria | "Score these ideas on [criteria, weights]; show the maths; give the ranked list." |
| 32 | AUDIT | find gaps before you publish | "Audit this page against [checklist]; list gaps by severity with the fix." |
| 33 | VERIFY | check claims + assumptions | "List every factual claim in this draft and mark it supported, unsupported or wrong." |
| 34 | DISPROVE | find evidence you are wrong | "Find the strongest evidence that this claim is false. If none, say so." |
| 35 | SYNTHESIZE | 20 sources -> one POV | "Synthesise these 20 sources into one point of view; show where it rests on thin evidence." |
| 36 | DEBRIEF | transcript -> insights + actions | "Debrief this meeting: what we learned, what changed, next 3 actions." |
| 37 | MINE | reviews -> exact customer language | "Mine these reviews for exact phrases customers use for problem, outcome and objection." |
| 38 | FAQ | customer questions -> answers | "Group these questions, then write answers from the approved docs only; flag any gap." |
| 39 | DASHBOARD | data -> interactive dashboard | "Build a single-file HTML dashboard from this data with 5 KPIs, 2 charts and a filter." |
| 40 | SEO | find content gaps + opportunities | "From this keyword and competitor data list content gaps ranked by opportunity." |
| 41 | AEO | find questions your brand should answer | "List the questions buyers ask AI assistants in this category that our site does not answer." |
| 42 | PITCH | research -> sales deck | "Turn this research into a 10-slide outline: problem, proof, offer, next step." |
| 43 | VISUALIZE | data -> charts + interactive visuals | "Pick the right chart for each question in this data and build it; state what it shows." |
| 44 | BUILD | idea -> interactive tool | "Build a small calculator/checker for [job] as one HTML file; list inputs and formula." |
| 45 | CREATE | prompt -> finished PPT/XLSX/DOCX | "Create the finished file (pptx/xlsx/docx) from this brief using the repo's file skills." |
| 46 | CONNECT | stop copy-pasting your context | "Which of my connected tools hold this context? Pull it directly instead of asking me to paste." |
| 47 | REMEMBER | give ongoing work a Project | "Set up a Project: instructions, reference files, voice rules for [ongoing work]." |
| 48 | REUSE | turn repeat workflows into Skills | "I repeat this workflow weekly. Write it as a skill with trigger, steps, output format." |
| 49 | MONITOR | competitors -> meaningful changes | "Check these competitor pages and report only meaningful changes since last time." |
| 50 | SCHEDULE | recurring work -> runs itself | "Propose a schedule and the exact prompt for [recurring job]; I approve before it is created." |

## Pairing with this repo

Verbs 1-6, 29, 35-37 -> `research-synthesis`, `customer-research`. 7-12 -> `marketing-ideas`, `positioning`, `grill-me`. 13-21 -> `copywriting`, `hook-generator`, `headlines`. 26-31 -> `kpi-reference-handbook`, `saas-growth-efficiency-metrics`. 32-34 -> `seo-audit`, `hallucination-audit`. 40-41 -> `ai-seo`, `aeo-score`. 45-48 -> `pptx`/`docx`/`xlsx`, `skill-creator`. 49-50 -> `competitor-price-watchlist`, `scheduled-routine`.

## Rules

- If the user names a verb, use its row verbatim, then add the three contract parts they did not supply (ask once, in a batch).
- If no verb fits, say so rather than stretching one.
- Report counts (rows read, sources used). Never present a number that was not in the input.
- Connected sources in this account (as of 19 Oct 2026): Ahrefs, Semrush, HubSpot, Clay, Notion, ClickUp, Fireflies, Gamma, Canva, Slack, Google Drive/Docs/Sheets. Say "not connected" for anything else.

## Keywords
50 ways Claude marketing, marketing verbs, prompt menu, hook, headline, dedupe, cluster, mine reviews, disprove, repurpose
