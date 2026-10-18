#!/usr/bin/env bash
# Batch 112 (report batch-116) - optional reading clones. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills and one command were added to the repo. Nothing below was installed or run there.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Clone for reading (shallow; no install, no build) =="
for r in JustVugg/colibri MadsLorentzen/ai-job-search debpalash/VoiceStudio anthropics/claude-plugins-official; do ask "git clone $r into ~/src?" && clone "$r"; done
echo "== Read first, not automated =="
echo "   colibri: read the README and build script before building; weights of this size need hundreds of GB of disk."
echo "   VoiceStudio: clone only your own voice or with written consent. AGPL-3.0 if you modify and host it."
echo "   ai-job-search: keep a human review before any application is sent."
echo "   SalesDaily custom connectors (lemlist, Prospeo, FullEnrich): verify each URL on the vendor's own documentation before adding."
echo "   Open WebUI: custom licence with a branding clause; read LICENSE before rebranding."
echo "Done."
