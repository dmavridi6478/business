#!/usr/bin/env bash
# Batch 113 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 3 skills, 3 commands, merges into existing skills, 4 design templates, 4 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 20 October 2026 (see .claude/skills/github-trending-top10-oct5, "Batch 113 finds").
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks (MIT / Apache-2.0) =="
for r in mattpocock/skills cathrynlavery/diagram-design anthropics/financial-services earthtojake/text-to-cad; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 2. Licence or dual-use care =="
ask "git clone DuarteSantos8/openGym (AGPL-3.0, network-use copyleft) into ~/src?" && clone "DuarteSantos8/openGym"
ask "git clone morluto/rea (reverse-engineering tool, MIT; use only on software you own or are authorised to test) into ~/src?" && clone "morluto/rea"

echo "== 3. Already covered in this repo, so no clone offered =="
echo "   affaan-m/ECC (ecc-* skills), stablyai/orca (orca-* skills), heygen-com/hyperframes (hyperframes skill)."

echo "== 4. MCP servers: commands only, not run =="
echo "   Review each vendor's docs, then run yourself, e.g.:"
echo "   claude mcp add chrome-devtools --scope user -- npx chrome-devtools-mcp@latest"
echo "   claude mcp add --transport http notion https://mcp.notion.com/mcp"
echo "   Stripe: use test mode or a restricted read-only key; do not put it in a shared .mcp.json."
echo "   Never paste a real token into a command you share."
echo "   Connectors cannot be installed from a script. Sentry and Stripe are installed in claude.ai but need reconnecting; Firecrawl and ElevenLabs exist but are not installed."
echo "Done. Restart Claude Code so the new commands appear."
