#!/usr/bin/env bash
# Batch 114 (report batch-118) - optional reading clones. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills and one command were added to the repo. Nothing below was installed or run there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Clone for reading (shallow; no install, no build) =="
for r in microsoft/markitdown cursor/plugins Flow-Launcher/Flow.Launcher; do ask "git clone $r into ~/src?" && clone "$r"; done
echo "== Read first, not automated =="
echo "   cursor/plugins has no root LICENSE file: read each plugin folder's manifest and licence."
echo "   rea (reverse engineering MCP): use only on software you own or are authorised to analyse."
echo "   RustDesk, scrcpy: remote-access and debugging tools; secure them and switch them off when unused."
echo "   Leaked system prompt collections: unverifiable; do not use them to bypass provider terms."
echo "Done."
