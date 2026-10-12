#!/usr/bin/env bash
# Batch 116 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 6 skills, 5 commands, 2 design templates, prompts. No plugin, connector or clone was added.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Repos (shallow clones; read README and LICENSE first) =="
for r in santifer/career-ops amruthpillai/reactive-resume interviewstreet/hiring-agent Paramchoudhary/ResumeSkills webadderallorg/Recordly microsoft/markitdown coreyhaines31/marketingskills mobile-next/mobile-mcp; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   AIHawk (feder-cr/Jobs_Applier_AI_Agent_AIHawk) is deliberately NOT in this list: unattended mass auto-apply often breaks job-board terms."
echo "== Python tool (use a virtualenv) =="
ask "python3 -m venv ~/.venvs/markitdown && pip install 'markitdown[all]'?" && { python3 -m venv "$HOME/.venvs/markitdown" && "$HOME/.venvs/markitdown/bin/pip" install 'markitdown[all]'; echo "   run: ~/.venvs/markitdown/bin/markitdown file.pdf -o file.md"; }
echo "== Claude Code plugins (inside Claude Code, one at a time; read the files first) =="
echo "   /plugin marketplace add ayghri/i-have-adhd   (the skill already exists in this repo; only needed on another machine)"
echo "   /plugin marketplace add mobile-next/mobile-mcp  then  /plugin install mobile-mcp@mobile-mcp"
echo "   /plugin marketplace add devsemih/appstore-review-skill  then  /plugin install appstore-review-skill"
echo "   /plugin install expo@anthropic-plugin-directory ; /plugin install revenuecat@anthropic-plugin-directory   (search with /plugin if not found; check the publisher)"
echo "   npx skills add coreyhaines31/marketingskills --skill cro emails   (runs third-party code; pin and read first)"
echo "   brew install asc && asc install-skills   (needs an Apple developer account; use TestFlight first)"
echo "Done."
