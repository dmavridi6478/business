#!/usr/bin/env bash
# Batch 112 (README Batch 108) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and a design template were added to the repo; nothing was installed.
# Facts come from each repo's own files, read on 26 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in ossu/computer-science imthenachoman/How-To-Secure-A-Linux-Server jqlang/jq FreshRSS/FreshRSS FreeCAD/FreeCAD; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   FreeCAD's repository is large; the shallow clone is still sizeable. Prefer the release download for using it."

echo "== 2. jq (MIT) =="
if command -v jq >/dev/null 2>&1; then echo "   jq already installed: $(jq --version)"
else
  echo "   Use your package manager, for example: sudo apt install jq   or   brew install jq"
  ask "run 'sudo apt install jq' now (Debian/Ubuntu only)?" && sudo apt install jq
fi

echo "== 3. FreshRSS (AGPL-3.0) =="
echo "   Its Docker README gives a 'docker run' example and a Docker Compose section. Read it first:"
echo "   https://github.com/FreshRSS/FreshRSS/blob/edge/Docker/README.md"
echo "   You become responsible for updates and backups of the server. Not started by this script."

echo "== 4. Read first, not automated =="
echo "   FreeCAD (LGPL-2.1): download the release for your OS from the FreeCAD website; no script is provided."
echo "   OSSU computer-science (MIT): a reading list, nothing to install; the README estimates about 2 years at about 20 hours a week."
echo "   How-To-Secure-A-Linux-Server (CC BY-SA 4.0): read it on a test machine before touching a real one. This script never edits a server."
echo "Done. Restart Claude Code so the new commands appear."
