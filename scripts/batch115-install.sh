#!/usr/bin/env bash
# Batch 115 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 2 skills, 1 reference, 2 commands, merges into 4 existing skills, 2 design templates, 2 themes, a workflows page and a prompts file; nothing was installed.
# Repo slugs, stars and licences were read from GitHub pages on 23 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences =="
for r in coollabsio/coolify myshell-ai/OpenVoice googleworkspace/cli D4Vinci/Scrapling; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Copyleft or unusual licence: read LICENSE before any use beyond personal =="
for r in documenso/documenso Fosowl/agenticSeek objective-see/LuLu twentyhq/twenty OpenBB-finance/OpenBB; do
  ask "git clone $r into ~/src (look only)?" && clone "$r"
done
echo "== 3. Not offered =="
echo "   GhostVM, MXterm, ClearanceKit: not verified. Berthly: 1 star, created July 2026; audit the source before use."
echo "   Run agents with broad file and network access only in a VM, container or restricted user, never on your main machine."
echo "   Scraping and voice cloning: check site terms, data-protection law and consent before any use."
echo "   Connectors (Miro, Higgsfield, Google Workspace) are authorised in claude.ai settings, not by a script."
echo "Done. Restart Claude Code so the new commands appear."
