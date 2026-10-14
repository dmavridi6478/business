# Batch 110 — prompts and commands to copy and paste (plain text)

## A. Slash commands

/ml-algo-pick <problem, data size, labels or not, how much you must explain the result>
/b2b-sales-skill <stage or skill number and title, plus your deal facts>
/swap-savings <paid tools, seats, who would run a server>   (now covers Part 2 and Part 9)
/briefing-oct13-pick <what you need to do>                     (now covers both 13 October briefings)

## B. Terminal commands for your own machine (scan first; none are run for you)

skillspector scan <folder-you-will-install> --no-llm
npx rea-agents@<version-you-reviewed> setup
bash scripts/batch113-install.sh

Do not use: any installer fetched and piped straight into a shell, or `npx` without a version for tools that change your agent's configuration.

## C. Prompts (copy as is, fill the brackets)

### C1. Pick an algorithm
I have [describe the data: rows, columns, types, missing values] and I want to [predict X / group Y / detect Z]. Using the ml-algorithms-cheatsheet-16 skill, name the baseline I should try first, one stronger option, and one I should avoid, each with its assumption that my data might break. Say what test I should run to check each assumption. Do not recommend a deep network unless my data size justifies it.

### C2. Run one of the 50 B2B sales skills
Run B2B sales skill [number and title, e.g. "26 Pain Quantifier"] for this deal. Here is what I know: [paste notes, role, product, deal stage, numbers]. Give: (1) the output for this step, (2) for each claim, the line of my notes that supports it, or "assumption", (3) the three questions I still need to ask, (4) what could be wrong. Do not invent numbers or buyer statements. Do not draft anything to send.

### C3. Check a savings claim
Here are the paid tools I use: [tool, plan, seats, monthly price]. Using the oss-swap-savings-table-12-part9 and oss-swap-savings-table-10 skills, tell me for each: the free alternative, its real licence, who would run and patch it, what it costs me in hosting and time, and the true yearly saving for my seat count only. Flag any swap where the saving is smaller than the cost of running it. Do not use the carousel's headline total.

### C4. Check a "free" or "open source" claim
Here is a repository and the claim made about it: [URL and claim]. Read its LICENSE file and tell me the exact licence, whether it is approved as open source, what I may not do under it, and whether it matters for my use: [your use]. Quote the licence text you relied on.

### C5. Before routing prompts through a free-tier gateway
I am considering a gateway that routes my prompts to many free LLM providers. List every kind of data I must never send through it, what each provider might retain or train on, what their terms say about proxies and shared use, and what I would lose compared with a single paid provider under a contract. Ask me what data I intend to send before you answer.
