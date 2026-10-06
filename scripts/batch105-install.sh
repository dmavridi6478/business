#!/usr/bin/env bash
# Batch 105 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, agents and design templates were added to the repo. No repo was cloned or installed there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in msitarzewski/agency-agents DozenTwelve/Papermorph JustVugg/colibri reality-opened/openreality Chuloo/mural; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Agency Agents: install ONE division into Claude Code (read the files first) =="
echo "   The repo has 230+ personas. Installing all of them dilutes agent routing. Open ~/src/agency-agents, read scripts/install.sh, then choose."
ask "run ~/src/agency-agents/scripts/install.sh --tool claude-code now?" && (cd "$HOME/src/agency-agents" && ./scripts/install.sh --tool claude-code)

echo "== 3. Papermorph skill (fetches third-party skill files; README says it needs Opus 5.5) =="
ask "npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code ?" && npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code

echo "== 4. Open Reality (needs browser sign-in or self-hosting; uploads video to their service unless self-hosted) =="
echo "   Read the repo first. Not added to .mcp.json because it runs a third-party npm package at every session start."
ask "claude plugin marketplace add reality-opened/openreality ?" && claude plugin marketplace add reality-opened/openreality
echo "   then: claude plugin install openreality@openreality   and   npx -y openreality-mcp login"

echo "== 5. Colibri: NOT automated =="
echo "   Needs 16 GB RAM and about 372 GB of disk for GLM-5.2. Build per its README: cd colibri/c && ./setup.sh"

echo "== 6. Vercel connector (already registered in .mcp.json) =="
echo "   Run /mcp in Claude Code and sign in. Also reconnect in claude.ai: Taplio, Supabase, Sentry, Stripe, MailerLite, Proshort, monday.com."
echo "Done. Restart Claude Code so the new skills, commands and agents appear."
