#!/usr/bin/env bash
# Batch 117 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 3 skills, 3 references, 3 commands, merges into 3 existing skills, 3 design templates, 3 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 24 October 2026 (Steg Cloak could not be located).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences =="
for r in GyulyVGC/sniffnet localsend/localsend; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Copyleft or unusual licence: read LICENSE first =="
for r in LizardByte/Sunshine hluk/CopyQ ShareX/ShareX kando-menu/kando imputnet/cobalt rustdesk/rustdesk mifi/lossless-cut; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   Steg Cloak: repo not located, dual-use. Read the source before use."
echo "   Cobalt: downloading from platforms can breach their terms and copyright."
echo "   RustDesk and Sunshine expose remote-control surfaces: strong passwords, trusted network only."
echo "   CopyQ stores everything you copy: exclude password managers."
echo "   n8n connector: authorise it yourself in claude.ai settings; Make blueprints and n8n JSON carry no credentials."
echo "Done. Restart Claude Code so the new commands appear."
