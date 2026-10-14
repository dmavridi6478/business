# Batch 107 — prompts and commands to copy and paste (plain text)

## A. Commands to run inside Claude Code (one at a time; scan first)

/plugin install superpowers@claude-plugins-official
claude plugin install mattpocock-skills@claude-plugins-official
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc

## B. Commands to run in a terminal on your own machine

uv tool install git+https://github.com/NVIDIA/skillspector.git
skillspector scan ./some-skill/ --no-llm
npm install -g @playwright/cli@latest
npm install -g skillui
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
bash scripts/batch110-install.sh

## C. Slash commands added in this batch

/skill-scan <path, repo URL or zip>
/automation-pick <your business, goal and tools>
/brand-map
/seo-team <site and goal>
/addon-pick <what you are building>
/oss-pick-oct <what you need>
/lead-gen-map <your offer and target market>

## D. Prompts (copy as is, fill the brackets)

### D1. Scan before install
Scan [path or URL] with SkillSpector in static mode only. Show the score, every finding with file and line, and tell me in plain words whether each one is a real risk or a text that only quotes a command. Do not install anything. Recommend install, install after fixes, or do not install.

### D2. Build one of the 50 automations
Build automation #[number] "[name]" from the ai-automations-50-marketing skill. Trigger: [trigger]. Inputs: [inputs]. Output: [output]. Use only these connectors: [list]. Stop at a human approval before anything is sent, posted or written to a CRM. Give me the step list, the exact prompt for the AI step, the fields it needs, a 10-example test plan, what could go wrong, and a run log format. Do not run it; show the plan first.

### D3. Personal brand map
Interview me with the 14 questions of the personal-brand-strategy-map skill, one at a time, starting with Niche. Do not answer for me. Score each element 0 to 4, name my weakest "Who you are" element, then give me a one-page brand sheet and a 30-day plan.

### D4. SEO team
Act as the seo-team-orchestrator for [site URL]. Goal: [traffic, leads or sales]. Market: [country, language]. Route the work through the eight areas in the claude-seo-team-8-areas skill in the run order. Use Ahrefs or Semrush only for numbers and date every figure. Give me the plan and the first two actions this week.

### D5. Lead generation system
Using the lead-gen-skill-map-10x10 skill, plan lead generation for [offer] aimed at [market, country]. Walk the ten folders in order, name the existing skill or agent and the connector for each step, mark what a human must do, and make every outbound message a draft for my approval.

### D6. Multi-agent campaign planner
Use the campaign-planner-multi-agent agent. Brief: [goal, audience, budget range, deadline, channels]. Run research, write, review and launch-plan as separate passes, stop before anything is published or spent, and list the decisions you need from me.

### D7. Pick add-ons without stacking
Which Claude Code add-ons should I install for [what I am building]? Use the claude-code-addons-top5 and vibe-coding-plugin-layers-5 skills. Tell me what is already installed here, what overlaps, the exact commands, and what to scan first.

### D8. Superpowers sample (from the carousel)
build me a booking page

### D9. Grill me (from the carousel)
/grill-me [paste your plan here]

### D10. Pick an open-source tool
Which of the repos in oss-trending-picks-oct-2026 fit [my need]? Give me the licence consequence for [internal use / client work / offering it as a service] and the first command from its README. Do not install anything.

## E. Design prompts

Create a [repo card / automation list card / two-tier tree / hub-and-spoke team poster] from the matching template in Artifacts/templates, using the tokens of Artifacts/theme-github-vault-mono-starfield.html. Content: [paste your text]. Keep Aptos as the first font, state only figures I have checked, and show the result as a rendered screenshot.
