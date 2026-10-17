#!/usr/bin/env bash
# Batch 111 (report batch-115) - optional reading clones. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, one command and one template were added to the repo. Nothing below was installed or run there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Clone for reading (shallow; no install) =="
for r in k-dense-ai/scientific-agent-skills ranxianglei/billion-context basecamp/kamal opentofu/opentofu; do ask "git clone $r into ~/src?" && clone "$r"; done
echo "== Read first, not automated =="
echo "   Part 16 swaps: AGPL-3.0 tools (Worklenz, MegaLinter, Uptrace, Unleash) carry network-use obligations if you modify and host them."
echo "   Vibe-Trading and Fincept: paper-trade only; trading tools can lose real money."
echo "   Omnisend connector: add it yourself in claude.ai connector settings, read-only if possible."
echo "   Higgsfield workflows (product shoot, UGC, ads) spend credits; set a budget first and do not reuse a real person's likeness."
echo "Done."
