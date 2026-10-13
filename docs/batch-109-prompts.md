# Batch 109 — prompts and commands to copy and paste (plain text)

## A. Commands to run in a terminal on your own machine (one at a time; scan first)

skillspector scan ./some-skill/ --no-llm
python -m pip install aider-install
aider-install
npm install -g @alibaba-group/open-code-review
npx skills add <owner/repo> --list
npx skills use <owner/repo> --skill <name>
bash scripts/batch112-install.sh

Note: `npx skills add ... --all` installs every skill into every agent with no prompts. Do not use it on a source you have not read.

## B. Slash commands added in this batch

/coding-tool-pick <what you build, your editor or terminal habit, budget, who reviews the code>
/briefing-oct13-pick <what you need to do>
/linkedin-landing-page <paste your headline, About, Featured titles, Services text, top skills>

## C. Prompts (copy as is, fill the brackets)

### C1. Build the Replit slide's app, with the safety rules added
Build a task tracker for a small startup team. Postgres for data, email-and-password login with hashed passwords, each user sees only their own team's tasks. Do not hard-code secrets; put them in environment variables. List every table, route and auth rule you created so I can review them before deploying.

### C2. Pick a coding tool
I build [what]. I work in [VS Code / terminal / Android Studio / no editor]. My budget is [amount per month]. Code is reviewed by [who]. Using the ai-coding-tools-7-ranking-2026 skill, recommend at most two of the seven tools, say which slide claims I should not rely on, and list what I must check on each tool's current pricing and terms page. Do not quote a price from memory.

### C3. Audit my LinkedIn profile against the landing-page checklist
Act as a LinkedIn strategist. I will paste my current headline, About section, Featured item titles, Services text, the last two Experience entries and my top skills. Check each section against this list: headline says what I do in plain words; About tells a short story, includes at least one quantified result that I supplied, and ends with a contact call to action; Featured and Services point to one clear offer; Experience has a call to action and no irrelevant roles; top three skills match my offer. For each section give PASS, FAIL or CAN'T CHECK with one line of why, then a rewrite that uses only facts I gave you. Never invent results or numbers. If a number is missing, ask me.

[paste your sections here]

### C4. Read an AI review tool's benchmark honestly
Here is a benchmark table from a tool's own repository: [paste]. Tell me what precision, recall and F1 mean in plain words, what share of real issues the best row misses, how many of its comments are wrong, whether the vendor ran the comparison itself, and whether I should use the tool as a gate or as a second pair of eyes.

### C5. Scan before installing a skill source
Scan [folder or repo URL] with SkillSpector in static mode only. Show the score, the coverage, and every finding with file and line. For each high finding, open the file at that line and tell me whether it is a real risk or text that only quotes a phrase or a build command. Do not install anything. Recommend install, install after fixes, or do not install.
