#!/usr/bin/env bash
# Batch 110 (file name batch113) - optional steps. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, an agent and design templates were added to the repo; nothing was installed.
# Facts come from each repo's README and LICENSE, read on 14 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
scan() {
  # Standing rule: scan before install. Static mode only. Scan the skill or script folder you will install, not a whole large repository:
  # whole-repo scans of software over-score and may time out. Read the findings.
  if command -v skillspector >/dev/null 2>&1; then
    echo "   SkillSpector (static) on $1:"; timeout 300 skillspector scan "$1" --no-llm 2>&1 | sed -n '1,25p' || echo "   scan timed out or failed: treat $1 as unscanned"
  else
    echo "   SkillSpector not found. Install it first: uv tool install git+https://github.com/NVIDIA/skillspector.git"
    ask "   continue WITHOUT a scan?" || return 1
  fi
}

echo "== 1. Clone for reading (shallow; nothing is run) =="
for r in morluto/rea tashfeenahmed/freellmapi agent-substrate/substrate Automattic/harper LimeSurvey/LimeSurvey; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Harper (Apache-2.0): local English grammar checker. Follow its README for your editor =="
echo "   Not automated: install steps differ by editor. Scan first: skillspector scan ~/src/harper --no-llm (or the folder you install)."

echo "== 3. REA (MIT): reverse-engineering MCP server. Changes your agent's configuration =="
echo "   Only for software you own or are authorized to examine. Its own disclaimer rules out circumventing licence checks and copying protected code."
echo "   Safer than the shell installer: read the proposed changes, then run, pinned to a version you have reviewed:"
echo "     npx rea-agents@<version> setup"
echo "   Scan the skill folder first:  skillspector scan ~/src/rea/.agents/skills/reverse-engineer-anything --no-llm"
echo "   Not run here: this script never registers an MCP server for you."

echo "== 4. FreeLLMAPI (MIT): routes prompts to up to 34 free providers =="
echo "   Do not send customer data or secrets through it. Single-user only. Leave its automatic update off. Its README links the provider terms review: read it."
echo "   Not installed by this script."

echo "== 5. Agent Substrate (Apache-2.0): Kubernetes runtime, pre-1.0 =="
echo "   For teams that already run Kubernetes. Not installed by this script."

echo "== 6. Swaps (Part 9): nothing to install here. Read the licence column in oss-swap-savings-table-12-part9 first =="

echo "Done. Restart Claude Code so the new commands appear: /ml-algo-pick /b2b-sales-skill /swap-savings /briefing-oct13-pick"
