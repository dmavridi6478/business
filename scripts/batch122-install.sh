#!/usr/bin/env bash
# Batch 122 - optional read-only looks. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 2 skills, 3 commands, a merge into oss-alternatives, 2 design templates, 2 themes, a workflows page and a prompts file; nothing was installed.
# Repo paths, stars and licences were read from GitHub pages on 28 October 2026. This script only clones for reading.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only looks, permissive licences (MIT or Apache-2.0) =="
for r in KnifeLemon/Filee ai-job-search-dev/ai-job-search lfnovo/open-notebook triggerdotdev/trigger.dev petergyang/no-ai-slop; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done
echo "== 2. Large or high-privilege: look only, do not install =="
for r in ruvnet/ruflo Anil-matcha/Open-Generative-AI; do
  ask "git clone $r into ~/src (look only; ruflo changes Claude Code settings if installed)?" && clone "$r"
done
echo "== 3. Copyleft: read LICENSE first =="
ask "git clone gitroomhq/postiz-app into ~/src (AGPL-3.0, look only)?" && clone gitroomhq/postiz-app
echo "== 4. Not offered =="
echo "   cleanyourtv: lets an AI agent control your TV over ADB and its licence is 'Other'. Read its prompt file and restore script on the web first, and trial it only on a TV you can reset."
echo "   MacNativeGames: needs a game and console keys you dump yourself; check the law and the game's terms where you live before you go near it."
echo "   OmniRoute and similar routers: they forward your prompts and code to other providers; read what each free tier does with the data."
echo "Done. Restart Claude Code so the new commands appear."
