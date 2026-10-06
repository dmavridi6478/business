#!/usr/bin/env bash
# Batch 106 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, agents and design templates were added to the repo. No repo was cloned or installed there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) - self-hosted infrastructure from the cloud-bill carousel =="
for r in coollabsio/coolify ubicloud/ubicloud seaweedfs/seaweedfs SigNoz/signoz typesense/typesense imgproxy/imgproxy triggerdotdev/trigger.dev; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Clone for reading - agent tooling and observability =="
for r in langwatch/langwatch dagucloud/dagu stablyai/orca multica-ai/multica mvschwarz/openrig agent-substrate/substrate herdrdev/herdr deepseek-ai/deepseek-harness; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 3. Clone for reading - the ten free repos (read the licence and terms in the register first) =="
echo "   Not offered by default: cobalt, gallery-dl, ArchiveBox, Suwayomi-Server (they download third-party content; check the terms of each site)."
for r in searxng/searxng reactive-resume/reactive-resume dgtlmoon/changedetection.io localsend/localsend dani-garcia/vaultwarden LibreTranslate/LibreTranslate; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 4. Design and skill references =="
for r in cathrynlavery/diagram-design ComposioHQ/awesome-claude-skills; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   diagram-design also installs as a skill (/plugin marketplace add ... or npx skills add ...). That fetches third-party skill files into your agent: read them first."

echo "== 5. NOT automated =="
echo "   Claude Code mod: the infographic's '/plugin enable cc-plugin-you-should-know@builtin' is unverified and turns on usage-data sharing. Check /plugin in your own Claude Code first."
echo "   pullfrog: 'npx pullfrog init' installs a bot that comments on and edits pull requests with your own LLM key. Read its permissions before running it on any repo."
echo "   Installers that pipe curl into a shell (coolify, dagu, multica): download, read, then run yourself."
echo "   AGPL-3.0 (searxng, vaultwarden, LibreTranslate, ubicloud, fleetbase) and GPL (typesense, dagu): read the licence before offering any as a service or embedding it."
echo "   Vaultwarden holds passwords: you own backups and patching. Do not move a real vault without a tested restore."

echo "== 6. Connectors - do these in claude.ai (sign-in cannot run in a cloud session) =="
echo "   Reconnect or connect: Granola, Stripe, Taplio, Supabase, Sentry, MailerLite, Proshort, monday.com; Vercel via /mcp (already in .mcp.json)."
echo "   Already connected and used by the new skills: Notion, Clay, HubSpot, Zapier, Figma, Canva, Gamma, Ahrefs, Semrush."
echo "   No connector found for: Resend, n8n, Make, Apify, Instantly, Lemlist, Smartlead, Gong."
echo "Done. Restart Claude Code so the new commands and agents appear."
