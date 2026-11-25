#!/usr/bin/env bash
# Batch 113 (README Batch 109) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, an agent, a workbook and design templates were added to the repo; nothing was installed.
# Licences were read from each repo's own file on 28 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; nothing is installed or run) =="
echo "   MIT: browser-use/browser-use, K-Dense-AI/scientific-agent-skills, cathrynlavery/diagram-design, cloudflare/security-audit-skill, stablyai/orca, anomalyco/opencode, morluto/rea"
echo "   Apache-2.0: rohitg00/agentmemory, mukul975/Anthropic-Cybersecurity-Skills (not made by Anthropic), Graphify-Labs/graphify"
echo "   AGPL-3.0: volcengine/OpenViking (running a modified copy as a network service requires offering its source)"
for r in browser-use/browser-use rohitg00/agentmemory K-Dense-AI/scientific-agent-skills cathrynlavery/diagram-design mukul975/Anthropic-Cybersecurity-Skills yenanjing/awesome-harness-engineering volcengine/OpenViking cloudflare/security-audit-skill Graphify-Labs/graphify stablyai/orca anomalyco/opencode; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. morluto/rea (reverse engineering with agents) =="
ask "clone morluto/rea into ~/src for reading?" && clone morluto/rea
echo "   Dual-use. Use it only on software you own, open source, or have permission to analyse."

echo "== 3. Read first, not automated =="
echo "   orca and opencode run coding agents with your credentials and subscriptions; check permissions and spend limits before installing."
echo "   Graphify indexes PDFs and configs: exclude anything holding secrets."
echo "   The 'HERMES' setup guide from the carousel is a lead magnet and is not included."
echo "   Vet any repo first with the /repo-vet command in Claude Code."
echo "Done. Restart Claude Code so the new commands appear."
