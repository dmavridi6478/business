#!/usr/bin/env bash
# Batch 120 - optional read-only looks. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 4 skills, 3 commands, a reference, a merge into oss-alternatives, 2 design templates, 2 themes, a workflows page and a prompts file; nothing was installed.
# Repo paths, stars and licences were read from GitHub pages on 26 October 2026. This script only clones for reading.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences =="
for r in pgvector/pgvector healthchecks/healthchecks slopus/happy; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Copyleft or unusual licence: read LICENSE first =="
for r in openreplay/openreplay Foundry376/Mailspring; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   OpenMausBot: days-old project that can give agents a desktop, a VM or your own computer. Read the source and trial only in a virtual machine with a throwaway account."
echo "   Openreplay records user sessions: you need consent, a privacy notice and field masking before you deploy it."
echo "   Cowork prompts and the business prompts run inside Claude; use approved accounts and one folder at a time."
echo "Done. Restart Claude Code so the new commands appear."
