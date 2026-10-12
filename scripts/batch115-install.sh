#!/usr/bin/env bash
# Batch 115 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 6 skills, 4 commands, 2 design templates, prompts. No plugin, connector or clone was added.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Repos (shallow clones; read README and LICENSE first) =="
for r in n8n-io/n8n coder/coder abue-ammar/tinycast Vrun-design/openflowkit ScrapeGraphAI/scrapecraft bridge-mind/bridgeclip knadh/listmonk figranium/figranium wheresryan22/anatomy; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "== Claude Code plugins (inside Claude Code, one at a time; marketplace here is anthropic-plugin-directory) =="
echo "   /plugin install modern-web-guidance@anthropic-plugin-directory   (Chrome team web guidance)"
echo "   /plugin install browser-use@anthropic-plugin-directory           (needs a browser; asks for access)"
echo "   /plugin install lovable@anthropic-plugin-directory               (uses your Lovable credits; authenticate via /mcp)"
echo "   /plugin install hyperframes@anthropic-plugin-directory           (HTML to video)"
echo "   /plugin install paypal@anthropic-plugin-directory                (payments: sandbox account first)"
echo "   If a name is not found, search with /plugin and check the publisher."
echo "== Token tools: measure first =="
echo "   npx codeburn   (reads local session files; read the source first)"
echo "   Skip pxpipe (local proxy sees all prompts) and OmniRoute (router sees all prompts) unless you have read the code."
echo "   anatomy skill: npx skills add wheresryan22/anatomy -g -a claude-code   (read its SKILL.md first)"
echo "Done."
