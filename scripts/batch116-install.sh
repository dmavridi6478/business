#!/usr/bin/env bash
# Batch 116 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 2 skills, 2 references, 1 command, merges into 4 existing skills, 3 design templates, 3 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 23 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences =="
for r in duckdb/duckdb jesseduffield/lazygit dandavison/delta docling-project/docling louislam/uptime-kuma Kilo-Org/kilocode; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Copyleft or unusual licence: read LICENSE first =="
for r in CorentinTh/it-tools open-webui/open-webui ubicloud/ubicloud debpalash/VoiceStudio; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   SnailSploit/Claude-Red: dual-use offensive-security skills. Read it on GitHub; use only on systems you are authorised to test, in a throwaway VM."
echo "   paperclip, andrej-karpathy-skills, ECC: the cards describe them wrongly; read each README first."
echo "   BleachBit deletes files: preview every selection."
echo "   Faceless-channel tooling: check YouTube policy, footage licences and voice consent first."
echo "   Connectors (NexLev, HubSpot, n8n) are authorised in claude.ai settings, not by a script."
echo "Done. Restart Claude Code so the new commands appear."
