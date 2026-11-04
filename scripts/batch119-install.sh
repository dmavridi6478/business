#!/usr/bin/env bash
# Batch 119 - optional read-only looks. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 3 skills, a 40-item catalogue, 3 commands, 3 design templates, 3 themes, a workflows page and a prompts file; nothing was installed.
# Repo paths, stars and licences were read from GitHub pages on 25 October 2026. This script only clones for reading: install each tool by following its own README.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Short list worth reading (permissive licences) =="
for r in jarrodwatts/claude-hud rtk-ai/rtk upstash/context7 coleam00/Archon BloopAI/vibe-kanban; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Read the licence or terms first =="
for r in firecrawl/firecrawl oraios/serena multica-ai/multica; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   cc-switch: the repo warns that only ccswitch.io is official; download only from the repo or that site."
echo "   claude-code-router and codex-plugin-cc send your code to another provider: check privacy and terms first."
echo "   claude-mem, agentmemory, beads: memory systems; this environment already uses Cognee, so pick one."
echo "   x1xhlol/system-prompts-and-models-of-ai-tools: collected commercial prompts; read only, do not republish."
echo "   Installing all 40 is not recommended: see skills/claude-install-list-40."
echo "Done. Restart Claude Code if you installed anything so new commands appear."
