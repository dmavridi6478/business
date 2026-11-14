#!/usr/bin/env bash
# batch115-install.sh - USER-RUN ONLY. Run it yourself on your own machine.
# Shallow-clones a few repos from the November carousels so you can READ them, and optionally installs `rich` into a virtualenv.
# Every step asks first. Nothing is piped into a shell. Nothing is run from a cloned repo.
set -euo pipefail

DEST="${BATCH115_DIR:-$HOME/batch115-repos}"
ask() { local a; read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }

echo "Clone target: $DEST"
mkdir -p "$DEST"

repos=(
  "https://github.com/windirstat/windirstat.git"
  "https://github.com/Klocman/Bulk-Crap-Uninstaller.git"
  "https://github.com/sqlitebrowser/sqlitebrowser.git"
  "https://github.com/Textualize/rich.git"
  "https://github.com/mltframework/shotcut.git"
)
for url in "${repos[@]}"; do
  name="$(basename "$url" .git)"
  if [ -d "$DEST/$name" ]; then echo "skip $name (already there)"; continue; fi
  if ask "Shallow-clone $url for reading?"; then
    git clone --depth 1 "$url" "$DEST/$name"
    echo "Cloned. Read its README and licence before running anything."
  fi
done

if ask "Create a virtualenv at $DEST/venv and install rich from PyPI?"; then
  python3 -m venv "$DEST/venv"
  "$DEST/venv/bin/python" -m pip install rich
  echo "Try: $DEST/venv/bin/python -m rich"
fi

echo "Not done on purpose: Oh My Zsh (piped installer - download and read tools/install.sh yourself), ImageMagick, mpv, SearXNG, Shotcut binaries."
