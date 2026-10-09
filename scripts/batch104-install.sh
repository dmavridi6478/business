#!/usr/bin/env bash
# Batch 104 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, design templates and the ML script were added to the repo; no repo or app was installed.
# Every command below was taken from the repo's own README or a link in it, read on 4 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in HKUDS/nanobot Vrun-design/openflowkit busabase/busabase usenotra/notra lovasoa/whitebophir; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. OpenFlowKit MCP server for Claude Code (pinned; this edit was refused in the cloud session) =="
echo "   npm package checked: MIT, no install scripts, 3 dependencies. Runs locally over stdio, no API key."
ask "Add it to this project with 'claude mcp add'?" && claude mcp add --scope project openflowkit -- npx -y @vrun-design/openflowkit-mcp@0.1.2

echo "== 3. nanobot via PyPI (needs Python 3.11+) =="
ask "uv tool install nanobot-ai?" && uv tool install nanobot-ai

echo "== 4. Whitebophir shared whiteboard in Docker (AGPL-3.0) =="
ask "docker run lovasoa/wbo on port 5001?" && docker run -it --publish 5001:80 --volume "$(pwd)/wbo-boards:/opt/app/server-data" lovasoa/wbo:latest

echo "== 5. LocalSend on macOS (Homebrew cask linked from its README) =="
ask "brew install --cask localsend?" && brew install --cask localsend

echo "== 6. Read first, not automated =="
echo "   Open Interpreter and Goose install with 'curl | sh'. Download the script, read it, then run it yourself."
echo "   AutoGPT: the autogpt_platform folder is Polyform Shield (source-available), not open source."
echo "   AGPL-3.0: Whitebophir, DeepDiagram, Notra, Joplin. Keep your own modifications private or offer the source."
echo "   KeePassXC, Syncthing, Joplin, Krita: download from keepassxc.org, syncthing.net, joplinapp.org, krita.org."
echo "   Sync is not backup: keep a separate backup of your KeePassXC database and your demo files."
echo "Done. Restart Claude Code so the new commands appear."
