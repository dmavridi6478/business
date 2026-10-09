#!/usr/bin/env bash
# Batch 106 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; nothing was installed.
# Commands come from each repo's own README, read on 4 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in NandhaKishorM/laya vectorize-io/hindsight paperclipai/paperclip google/ax browser-use/jev-ultrafast pocketbase/pocketbase getmaxun/maxun janhq/jan; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Laya (Apache-2.0; Python 3.10+) in a virtual environment =="
ask "create ~/laya-venv and pip install laya?" && { python3 -m venv "$HOME/laya-venv" && "$HOME/laya-venv/bin/pip" install laya; }
echo "   Measure it on 50 to 200 of your own labelled cases before trusting it (see the laya-jev-ultrafast skill)."

echo "== 3. Hindsight (MIT) - Docker route; needs an LLM provider key =="
echo "   Read the README's docker run command, set HINDSIGHT_API_LLM_API_KEY yourself, and keep real customer data out at first."

echo "== 4. Paperclip (MIT) - needs Node 24.11 or newer =="
ask "run 'pnpm install' in ~/src/paperclip?" && { [ -d "$HOME/src/paperclip" ] && (cd "$HOME/src/paperclip" && pnpm install) || echo "   clone it first"; }
echo "   Then 'pnpm dev' per its README. Read its adapters before pointing it at real agents."

echo "== 5. Read first, not automated =="
echo "   Google AX is alpha and needs a Kubernetes cluster with Agent Substrate installed first. Not for a laptop trial."
echo "   Jev Ultrafast needs a TypeSafe key and a text-model key and drives your real Chrome; use a separate profile."
echo "   Open WebUI uses a custom licence: no removing or replacing its branding above 50 users in 30 days without permission."
echo "   Maxun is AGPL-3.0. PocketBase is pre-1.0: pin versions."
echo "   Mods and third-party Claude Code plugins: read the source and run 'claude plugin validate' first (see claude-code-mods-guide)."
echo "   The 'LinkedIn Skills' pack for Hermes was promoted with no link; nothing to install."
echo "Done. Restart Claude Code so the new commands appear."
