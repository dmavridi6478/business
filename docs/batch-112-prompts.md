# Batch 112 - prompts in plain text

Copy and paste. Replace every [BRACKET] and read the output before using it.

## A. Source prompts (verbatim from the @earchoe carousel)

### Prompt 01 - open ChatGPT or Claude, start a new chat

```
I want to create a paid service around [TASK] for [CUSTOMER TYPE].

Design a beginner-friendly AI-assisted workflow. Show: inputs, AI steps, tools, human review points, final deliverable, quality checks, turnaround time, and what I should never automate. Keep the offer narrow enough to test with one customer.
```

### Prompt 02 - same chat, after reviewing the first workflow

```
Turn the workflow above into a simple paid pilot for [CUSTOMER TYPE].

Give me:
1. The exact deliverable.
2. A 3-step client process.
3. What I need from the client.
4. A quality-control checklist.
5. A short offer description.
6. Three sensible pricing structures without pretending any price is guaranteed.
```

## B. Command prompts (the instruction each new slash command runs)

### /oss-swap-17

```
Use the `oss-swap-part-17` skill. Input: "$ARGUMENTS"

1. Find the row; if absent say so and apply the free-vs-paid procedure generically.
2. Show verified repo, stars, licence (check date 19 Oct 2026) and the gap.
3. Total cost = licence + hosting + hours x hourly cost, using numbers the user supplies; never guess hours.
4. Verdict: switch / do not switch / pilot, with the one condition that would change it. Install nothing.
```

### /oss-swap-12

```
Use the `oss-swap-part-12` skill. Input: "$ARGUMENTS"

1. Find the row; if absent say so and apply the free-vs-paid procedure generically.
2. Show repo, stars, licence (19 Oct 2026). Where the licence reads "Other", tell the user to read LICENSE before any commercial use.
3. Total cost = licence + hosting + hours x hourly cost, from numbers the user supplies.
4. Verdict: switch / do not switch / pilot. Install nothing.
```

### /ui-polish

```
Use the `ui-polish-6-checks` skill on: "$ARGUMENTS"

Pass/fail each of the six checks with counted evidence, then a fix list ordered by effort. Do not edit files unless asked.
```

### /side-hustle-pilot

```
Use the `ai-side-hustle-pilot` skill on: "$ARGUMENTS"

1. Ask for task and customer type if missing (one question).
2. Score the five questions yes/no with a one-line reason each; any "no" stops at "not ready" plus the cheapest test that would flip it.
3. If ready, fill Prompt 01 then Prompt 02 and show the pilot offer. Mark every price as a structure, not a promise.
```

### /research-stack

```
Use the `customer-research-stack` skill for: "$ARGUMENTS"

1. One customer group, one problem keyword, one question for Tally ("what did you try before, and why did it fail?").
2. A 7-day plan: day 1 F5Bot keyword + SparkToro report, day 2-3 Tally form, day 4 first conversations, day 5 log in Twenty, day 6 Fider post, day 7 review.
3. Draft only; the user sends every message. Do not auto-post or bulk-scrape.
```

### /oss-25

```
Use the `oss-free-replacements-25` skill. Input: "$ARGUMENTS"

Return the row, the job, the hidden costs (hosting, backups, patching, hours) and a verdict: switch now / pilot / keep paying. Install nothing; if the tool holds sensitive data, require a tested restore first.
```

### /github-finds

```
Use the `github-finds-oct-19` skill. Input: "$ARGUMENTS"

Give: what it does in one sentence, verified stars and licence with date, one reason to try it, one reason not to, and the first safe command to read (README, not install). Say plainly if the repo is not in the skill.
```

### /docker-agent

```
Use the `docker-agent-yaml` skill for: "$ARGUMENTS"

Write a starter agent.yaml (lead + at most two specialists), mark every key that is not confirmed on screen in the video as "verify", list the permissions it needs, and say what it must never do. Do not run anything.
```

### /setup-recommend

```
Use the `claude-code-setup-recommender` skill on: "$ARGUMENTS"

1. Inventory existing skills, commands, agents, hooks and MCP servers for this repo (counts only, plus the closest existing match per category).
2. Recommend at most one addition per category, and say "nothing needed" where the existing set already covers it.
3. Read-only; install nothing.
```

## C. Ready-to-paste task prompts

**UI audit:** "Audit [URL or screenshot] with the six UI polish checks (cue overload, font sizes, spacing, shadows, icon set, alignment). Count the evidence for each, give pass or fail, then a fix list ordered by effort."

**Customer research kickoff:** "My product is [PRODUCT] for [CUSTOMER GROUP]. Write one Tally question asking what they tried before and why it failed, one F5Bot keyword for the problem, and a seven-day plan to hold five conversations. Drafts only; I will contact people myself."

**Tool swap:** "I pay [AMOUNT] a year for [PAID TOOL]. Use the oss-swap skills: show the verified free alternative, what it does not replace, and total cost with [HOURS] hours at [HOURLY COST]. Verdict: switch, pilot or keep."
