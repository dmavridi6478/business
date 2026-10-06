#!/usr/bin/env bash
# Batch 104 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, agents, design templates, the Vercel MCP entry in .mcp.json and a runnable ML script were added
# to the repo. No repo was cloned or installed there (the container is thrown away; ~/src on your machine is not).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) - agent evaluation and observability =="
for r in comet-ml/opik confident-ai/deepeval Arize-ai/phoenix UKGovernmentBEIS/inspect_ai Giskard-AI/giskard-oss lmnr-ai/lmnr traceloop/openllmetry; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Clone for reading - infrastructure and apps from the carousels =="
for r in mem0ai/mem0 rivet-dev/rivet getpaseo/paseo better-auth/better-auth lukevella/rallly THU-MAIC/OpenMAIC HKUDS/Vibe-Trading bilawalsidhu/gods-eye-view paperclipai/paperclip magnitudedev/magnitude; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 3. Claude skills published by the repos themselves (npx skills add) =="
echo "   These fetch third-party skill files into your agent. Read them first: github.com/rivet-dev/skills and github.com/mem0ai/mem0."
ask "npx skills add rivet-dev/skills ?" && npx skills add rivet-dev/skills
ask "npx skills add https://github.com/mem0ai/mem0 --skill mem0 ?" && npx skills add https://github.com/mem0ai/mem0 --skill mem0

echo "== 4. Run the 16-line deep network from the video (needs numpy) =="
ask "python3 scripts/ml/deep_spirals.py ?" && python3 "$(dirname "$0")/ml/deep_spirals.py"

echo "== 5. NOT automated =="
echo "   VoiceStudio (AGPL-3.0): its installer is 'curl ... | sh'. Download it, read it, then run it yourself. Clone a real person's voice only with their consent."
echo "   open-seo needs a paid DataForSEO key. Vibe-Trading: backtests are not predictions; never connect it to a live account unattended."
echo "   AGPL-3.0 (paseo, rallly, VoiceStudio) and Elastic-2.0 (phoenix): read the licence before offering any as a service."

echo "== 6. Connectors - do these in claude.ai (sign-in cannot run in a cloud session) =="
echo "   Reconnect: Taplio MCP LinkedIn, Supabase, Sentry, Stripe, MailerLite, Proshort, monday.com."
echo "   Connect: Vercel (already registered in .mcp.json - run /mcp in Claude Code and sign in), Fathom, tl;dv, Outreach, Grain."
echo "   Already connected and used by the new skills: Ahrefs, Semrush, Clay, Vibe Prospecting, Common Room, Fireflies, Typefully, Canva, Figma, Consensus, Zapier."
echo "Done. Restart Claude Code so the new commands and agents appear."
