# Batch 108 — prompts and commands to copy and paste (plain text)

## A. Commands to run in a terminal on your own machine (one at a time; scan first)

skillspector scan ./some-skill/ --no-llm
python3 -I scripts/prelaunch_check.py index.html about.html
npm install -g @alibaba-group/open-code-review
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
npx skills add hypit-ai/hypit -g
brew trust --tap abue-ammar/tinycast
brew tap abue-ammar/tinycast
brew install --cask tinycast
bash scripts/batch111-install.sh

Note: the Homebrew tap owner is abue-ammar (with an e). The carousel spells it abu-ammar. Do not use that spelling.

## B. Slash commands added in this batch

/prelaunch-audit <paste of page HTML, or a file path, plus any Lighthouse report>
/swap-savings <the paid tools you use, seat counts, who would run a server>
/repo-week-pick <what you need to do>
/biz-sites-pick <your business, country and what you sell>

## C. Prompts (copy as is, fill the brackets)

### C1. The 20-check pre-launch audit (the author's prompt, lightly tidied)
You are a pre-launch auditor. I'll paste my site's code and page copy below.

Check these 20: secrets in frontend, HTTPS, privacy policy, terms, cookie consent, form validation, spam protection, meta titles and descriptions, social preview image, favicon, sitemap and robots.txt, alt text, image compression, page speed, color contrast, mobile layout, 404 page, broken links, analytics, one clear call to action.

For each: PASS / FAIL / CAN'T CHECK, one line why, and the exact fix. Never guess. If you can't verify it from what I pasted, say CAN'T CHECK.

End with the 5 fixes to do first.

[paste page HTML, page copy, robots.txt, sitemap.xml, a Lighthouse report, and a list of your forms here]

### C2. Honest saving from replacing paid tools
Here are the paid tools I use: [tool, plan, seats, monthly price]. For each, use the oss-swap-savings-table-10 skill: name the free alternative, its real licence (AGPL, LGPL, MIT or custom), what I lose, who would run and patch the server, and the true yearly saving for my seat count only. Do not use the carousel's headline total. Tell me which swaps are not worth doing.

### C3. Pick one repo for a need
I need to [goal]. From the five repos in agent-repos-took-off-sep-2026, pick at most one. Give the licence and its conditions, the correct install line, what it costs to run, the first 15-minute test, and the reason to say no if it does not fit. Scan it with SkillSpector before any install.

### C4. Which free business site first
My business is [type] in [country]. I sell [what]. From Calendly, SERPtag, Google Business Profile, Wave and Tally, tell me the order to set them up, what personal data each collects, what I must state in my privacy notice, and which one is not suitable for my country's invoicing rules.

### C5. Fix list after the audit
Here is the audit result: [paste]. Turn every FAIL into a ticket: title, file to change, exact change, how to verify, and effort in minutes. Put anything involving a leaked key first and tell me to rotate it. Do not repeat the key in your answer.
