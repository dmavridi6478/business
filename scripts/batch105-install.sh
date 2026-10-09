#!/usr/bin/env bash
# Batch 105 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; nothing was installed.
# Commands come from each repo's own README, read on 4 October 2026. Slash commands (/plugin ...) run inside Claude Code, not here.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in Leonxlnx/taste-skill pbakaus/impeccable nextlevelbuilder/ui-ux-pro-max-skill anthropics/skills TencentCloud/Octop Kanaries/graphic-walker DataAnts-AI/CutScript Zackriya-Solutions/meeting-minutes OpenWhispr/openwhispr; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Design skills for Claude Code (read each SKILL.md first; a skill is instructions your agent obeys) =="
ask "npx skills add Leonxlnx/taste-skill (MIT)?" && npx skills add https://github.com/Leonxlnx/taste-skill
ask "npx impeccable install (Apache-2.0; its launcher runs an engine binary - read it first)?" && npx impeccable install
echo "   Inside Claude Code, run these yourself:"
echo "     /plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill   then   /plugin install ui-ux-pro-max@ui-ux-pro-max-skill"
echo "     /plugin marketplace add anthropics/skills                      then   /plugin install example-skills@anthropic-agent-skills"
echo "   frontend-design, canvas-design, theme-factory, slack-gif-creator and algorithmic-art are already skills in this repo."

echo "== 3. Octop (MIT; Python 3.12+) - PyPI route, in a virtual environment =="
ask "create ~/octop-venv and pip install octop?" && { python3 -m venv "$HOME/octop-venv" && "$HOME/octop-venv/bin/pip" install octop; }
echo "   Or Docker: docker compose -f docker/docker-compose.yml up -d (from a clone of TencentCloud/Octop)."

echo "== 4. Read first, not automated =="
echo "   Octop, Hermes Agent: their README installers are 'curl | bash'. Download the script, read it, then run it yourself."
echo "   Jaaz is NOT open source: free for individuals; team use, modification and redistribution need its paid licence."
echo "   AGPL-3.0: OmniVoice Studio. Keep your own modifications private or offer the source to network users."
echo "   InteraOne: repo not found; do not install anything from a slide alone."
echo "   Connectors (Apify at mcp.apify.com, Notion, Higgsfield) are added in your Claude settings, not by this script."
echo "Done. Restart Claude Code so the new commands appear."
