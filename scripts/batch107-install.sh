#!/usr/bin/env bash
# Batch 107 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, scripts and design templates were added to the repo; nothing was installed.
# Commands come from each repo's own README or marketplace file, read on 5 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Run the two code-video scripts (numpy only, in a virtual environment) =="
if ask "create ~/np-venv, install numpy, and run both scripts?"; then
  python3 -m venv "$HOME/np-venv" && "$HOME/np-venv/bin/pip" install numpy
  "$HOME/np-venv/bin/python" scripts/bell_curve_from_scratch.py
  "$HOME/np-venv/bin/python" scripts/attention_from_scratch.py
fi

echo "== 2. Clone for reading (shallow; no install) =="
for r in DietrichGebert/ponytail thedotmack/claude-mem Panniantong/Agent-Reach tester-army/e2e addyosmani/agent-skills coreyhaines31/marketingskills browser-use/browser-use penpot/penpot; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 3. Claude Code plugins - type these INSIDE Claude Code, one at a time, after reading each plugin =="
echo "   /plugin install superpowers@claude-plugins-official"
echo "   /plugin install security-guidance@claude-plugins-official"
echo "   /plugin install code-review@claude-plugins-official"
echo "   context7 and sentry are already in this repo's .mcp.json; do not install both routes."
echo "   Sentry's MCP server is FSL-1.1-Apache-2.0 (source-available) and needs a Sentry account."

echo "== 4. Per-repo routes from their READMEs (run yourself) =="
echo "   claude-mem:      npx claude-mem install            (Apache-2.0; read what it stores first)"
echo "   e2e:             npx e2e init                      (Apache-2.0)"
echo "   agent-skills:    npx skills add addyosmani/agent-skills --list     (MIT; browse before installing)"
echo "   marketingskills: npx skills add coreyhaines31/marketingskills --list (MIT)"
echo "   Agent-Reach:     agent-reach install --dry-run     (MIT; default only checks; --system changes your machine)"
echo "   t3code:          brew install --cask t3-code       (its README also shows a curl-to-shell line; do not use it)"

echo "== 5. Read first, not automated =="
echo "   OpenMontage is AGPL-3.0: check before offering it as a service."
echo "   The calcom/cal.com repo is now Cal.diy (MIT, enterprise features removed, personal non-production use)."
echo "   Dify: no multi-tenant service and no logo removal without a commercial licence. n8n: Sustainable Use License."
echo "   Open WebUI: custom licence with a branding clause above 50 users."
echo "Done. Restart Claude Code so the new commands appear."
