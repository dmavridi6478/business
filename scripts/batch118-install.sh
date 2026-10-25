#!/usr/bin/env bash
# Batch 118 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 3 skills, 3 commands, a merge into oss-alternatives, 2 design templates, 2 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 25 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences =="
for r in unslothai/unsloth charmbracelet/vhs getopenscreen/openscreen; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Copyleft or unusual licence: read LICENSE first =="
for r in CapSoftware/Cap alyssaxuu/screenity; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   Unsloth: install from the current docs page for your GPU and OS, inside a virtual environment; check each base model's licence."
echo "   Interactive-demo repos (runthru, showkit, demoscript): tiny and very new; trial in a sandbox only."
echo "   Excel and PowerPoint prompts run inside Copilot or Claude; work on a copy and keep a tie-out check."
echo "   n8n is already connected; nothing to install."
echo "Done. Restart Claude Code so the new commands appear."
