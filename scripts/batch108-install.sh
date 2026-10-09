#!/usr/bin/env bash
# Batch 108 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; nothing was installed.
# Facts come from each repo's own README and LICENSE, read on 5 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in NanoNets/Graft firecrawl/anydoc andrewyng/openworker trycompai/crm garrytan/gstack bilawalsidhu/gods-eye-view OpenHands/OpenHands antirez/ds4; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. gstack (MIT) =="
echo "   Its README installs by cloning into ~/.claude/skills/gstack and running ./setup (needs Bun 1.0+ and Node)."
echo "   Read ~/src/gstack/setup first. Team mode edits and commits to your repo; do not use it until you have read it."
echo "   This repo already has a 'gstack' skill; check it before adding a second copy."

echo "== 3. Read first, not automated =="
echo "   ds4: Metal target is Macs with 96 GB or more; DGX Spark and Strix Halo also listed. Uses its own GGUF files."
echo "   gods-eye-view: install with Pinokio or from a terminal per its README; use public data lawfully."
echo "   HydraDB and Open-kritt are AGPL-3.0; Remotion needs a company licence above 3 employees; RedInk is non-commercial (CC BY-NC-SA 4.0)."
echo "   PersonaLive animates faces in real time: only with the person's consent."
echo "   Echo-Music is an unofficial YouTube Music client; likely against YouTube's terms."
echo "   Open-kritt runs agents against code: authorised targets only. Openworker and Crm hold keys and personal data: read their permission modes."
echo "Done. Restart Claude Code so the new commands appear."
