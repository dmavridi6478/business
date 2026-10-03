#!/usr/bin/env bash
# Batch 103 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; no repo was installed.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in louislam/uptime-kuma henrygd/beszel traefik/traefik FreshRSS/FreshRSS linkwarden/linkwarden; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Study repos (data and AI) =="
for r in DataTalksClub/data-engineering-zoomcamp DataTalksClub/mlops-zoomcamp DataTalksClub/llm-zoomcamp GokuMohandas/Made-With-ML; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 3. Read the licence first (not automated) =="
echo "   AGPL-3.0: comp, keila, tolaria, docmost, contentport, FreshRSS, linkwarden. Source-available: hexabot, directus. Commercial: screenpipe."

echo "== 4. wifit3 - NOT automated =="
echo "   A Wi-Fi attack toolkit. Use only on networks you own or have written permission to test. Not included in this script."
echo "Done. Restart Claude Code so the new commands appear."
