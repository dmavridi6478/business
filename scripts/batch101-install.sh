#!/usr/bin/env bash
# Batch 101 - optional installs. RUN ON YOUR OWN MACHINE from the repo root. Every step asks first.
# Already done in the cloud session: the six humanlayer skills (npx skills add humanlayer/skills) and
# five MCP servers written to .mcp.json (exa, context7, sentry, supabase read-only, playwright).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }

echo "== 1. MCP servers: log in (OAuth) =="
echo "   Start Claude Code in this repo, approve the project servers from .mcp.json, then run /mcp to log in to Sentry and Supabase."
echo "   Supabase is registered READ-ONLY. Add &project_ref=<ref> to scope it to one project before you use it on real data."
ask "claude mcp add --transport http github https://api.githubcopilot.com/mcp/ (needs your GitHub login or token)?" \
  && claude mcp add --transport http github https://api.githubcopilot.com/mcp/

echo "== 2. OpenRig (Apache-2.0) - persistent agent teams =="
echo "   Needs Node 22 or 24 and tmux. 'rig setup --dry-run' previews what it will do before it changes anything."
ask "npm install -g @openrig/cli?" && npm install -g @openrig/cli

echo "== 3. Octop (MIT) - NOT automated =="
echo "   Its README installs with:  curl -fsSL <Tencent COS URL>/octop/install.sh | bash"
echo "   Download the script, read it, then run it yourself, ideally in a VM. See https://github.com/TencentCloud/Octop"

echo "== 4. Scanners from Batch 100 =="
echo "   scripts/batch100-install.sh (gitleaks, osv-scanner and others)."
echo "Done."
