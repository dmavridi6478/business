#!/usr/bin/env bash
# Batch 110 (report batch-114) - optional reading clones. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and a template and theme were added to the repo. Nothing below was installed or run there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Clone for reading (shallow; no install) =="
for r in omnara-ai/omnara actualbudget/actual; do ask "git clone $r into ~/src?" && clone "$r"; done
echo "== Read first, not automated =="
echo "   Omnara (Apache-2.0): the site says 'Read omnara.com/SKILL.md to set up my agent'. Open that file yourself and read every step before letting an agent follow it."
echo "   Actual Budget (MIT): holds financial data. Use end-to-end encryption if you sync, and keep a backup."
echo "   'Claude for Sales' course: no provider or link was given and none could be found; do not comment on a post to unlock it. Use /sales-lesson instead."
echo "Done."
