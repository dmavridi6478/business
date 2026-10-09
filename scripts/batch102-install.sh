#!/usr/bin/env bash
# Batch 102 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; no repo was installed.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { # owner/repo
  [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }
  mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"
}

echo "== 1. Clone for reading (shallow, no install) =="
for r in NousResearch/hermes-agent CopilotKit/OpenBot busabase/busabase svix/svix-webhooks; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. llama.cpp (MIT) - use a package manager, not the pipe-to-shell installer on the card =="
echo "   macOS/Linux: brew install llama.cpp      Windows: winget install llama.cpp   (check the name with 'winget search')"
ask "brew install llama.cpp?" && brew install llama.cpp

echo "== 3. Read the licence first (not automated) =="
echo "   ChatbotX (custom licence), cmux (custom), unsloth (AGPL-3.0), athas and uptimepage (AGPL-3.0): read LICENSE before you self-host or resell."

echo "== 4. capd (MIT, macOS 26+) and alphai-tui (MIT) =="
ask "git clone jamiedavenport/capd and makeev/alphai-tui into ~/src?" && { clone jamiedavenport/capd; clone makeev/alphai-tui; }
echo "   alphai-tui needs Rust (cargo) to build; its news features need a free AlphAI key."
echo "Done. After pulling this branch, restart Claude Code so the new commands appear."
