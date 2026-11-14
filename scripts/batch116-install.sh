#!/usr/bin/env bash
# batch116-install.sh - USER-RUN ONLY. Shallow-clones a few repos so you can READ them. Every step asks first.
# Nothing is piped into a shell and nothing from a cloned repo is run. The anatomy skill install line is printed, not executed.
set -euo pipefail
DEST="${BATCH116_DIR:-$HOME/batch116-repos}"
ask() { local a; read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
mkdir -p "$DEST"; echo "Clone target: $DEST"
for url in https://github.com/wheresryan22/anatomy.git https://github.com/qarmin/czkawka.git https://github.com/espanso/espanso.git https://github.com/HKUDS/DeepTutor.git; do
  name="$(basename "$url" .git)"
  [ -d "$DEST/$name" ] && { echo "skip $name"; continue; }
  if ask "Shallow-clone $url for reading?"; then git clone --depth 1 "$url" "$DEST/$name"; echo "Read its README and licence first."; fi
done
echo "To install the anatomy skill yourself after reading it: npx skills add wheresryan22/anatomy -g -a claude-code"
