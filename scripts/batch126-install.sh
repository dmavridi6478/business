#!/usr/bin/env bash
# Batch 126 - optional read-only looks. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 3 skills, 3 commands, 1 design template, 2 themes, a workflows page and a prompts file; nothing was installed.
# Facts read from GitHub on 1 November 2026. This script only clones for reading.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. MIT-licensed, read-only looks =="
for r in JohnHeibel/ClaudeAnimationBase pyang5166/gbro-collage-broll lemomo-ai/lemo-opuscar; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 2. Licence unclear for company use: read LICENSE before anything else =="
if ask "git clone feitangyuan/onetake into ~/src (look only; GitHub shows licence 'Other', a listing says noncommercial)?"; then clone feitangyuan/onetake; echo "   Read ~/src/onetake/LICENSE now."; fi
echo "== 3. Not offered =="
echo "   Running any of these: each runs scripts, installs packages and drives a browser. Use a throwaway folder or container and keep API keys out of shared repos."
echo "   Collage B-Roll bills your Gemini API per clip; Lemo-Opuscar uses many tokens per film (author says 30 to 60 minutes)."
echo "   HyperFrames is already in the library as the 'hyperframes' skill; install its runtime from the official repo if you need to render."
echo "   Packs offered by commenting a keyword (e.g. 'VIDEO'): read every file before installing."
echo "Done. Restart Claude Code so the new commands appear."
