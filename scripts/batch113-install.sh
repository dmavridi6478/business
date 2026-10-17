#!/usr/bin/env bash
# Batch 109 (report batch-113) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, an agent, templates, a theme and a practice workbook were added to the repo. Nothing below was installed or run there.
# Licences come from each repo's LICENSE file, read on 16 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in NVIDIA/SkillSpector xerj-org/xerj max-sixty/worktrunk colbymchenry/codegraph storytold/artcraft storytold/photocraft storytold/pdfcraft morluto/rea; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Scan your own skills with SkillSpector (Apache-2.0) =="
echo "   Read its README for the install and scan commands first. Its optional LLM pass sends skill text to the model you configure; run the static pass first."
echo "   Suggested target: this repo's .claude/skills folder, because it holds many vendored third-party skills."

echo "== 3. Read first, not automated =="
echo "   REA (MIT): 'npx rea-agents@latest setup' edits your coding agent's config and needs a decompiler (Hopper, Ghidra or IDA). Reverse engineer only software you own or are authorised to analyse."
echo "   CodeGraph: the README installs with a curl | sh line. Read it. Measure token use with three runs before and after (see codegraph-hermes-token-savings)."
echo "   reclip (MIT): downloads video from many sites; use only content you own or may copy."
echo "   AutoHedge, Vibe-Trading, FinceptTerminal: can place or simulate trades. Not financial advice. Paper-trade only; never give an API key withdrawal rights."
echo "   Open-Generative-AI: advertises 'no content filters'. You carry the consent, likeness and copyright duty. Model calls usually go to paid providers."
echo "   VoiceStudio (AGPL-3.0): the slide shows a PowerShell one-liner that bypasses execution policy. Read the script or use a release. Clone a voice only with written permission."
echo "   Self-hosted swaps (modelsignal-free-swaps-part-10): AGPL-3.0 (EspoCRM, Logseq, Zitadel), GPL (Jellyfin, Flameshot), MPL-2.0 (Syncthing). Price the hosting and admin time first."
echo "   Comment, star, fork and follow requests on the source slides were not actioned."
echo "Done. Restart Claude Code so the new commands appear."
