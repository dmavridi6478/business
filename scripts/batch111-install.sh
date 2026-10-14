#!/usr/bin/env bash
# Batch 108 (file name batch111) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, a checker script and design templates were added to the repo; nothing was installed.
# Facts come from each repo's README and LICENSE, read on 13 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 0. Scan first. Every tool below should pass /skill-scan or 'skillspector scan <folder> --no-llm' before it is installed =="

echo "== 1. Clone for reading (shallow; nothing is run) =="
for r in alibaba/open-code-review cloudflare/security-audit-skill hypit-ai/hypit JustVugg/colibri abue-ammar/tinycast woodpecker-ci/woodpecker imgproxy/imgproxy authelia/authelia; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   NOTE: the tinycast owner is 'abue-ammar' (with an e). The carousel spells it 'abu-ammar'; do not use that spelling."

echo "== 2. Agent tools (each needs a model key or tokens you pay for) =="
ask "npm install -g @alibaba-group/open-code-review (Apache-2.0; needs Git 2.41+ per the slide, and a model endpoint you configure)?" && npm install -g @alibaba-group/open-code-review
echo "   Cloudflare security audit skill (MIT; a full run uses many tokens). Run in a project folder:"
echo "     npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit"
echo "   Hypit (modified Apache-2.0: no multi-tenant service, no resale, keep its logo; Node 22.15+; renders cost money):"
echo "     npx skills add hypit-ai/hypit -g"

echo "== 3. Tinycast (macOS 26 or newer; AGPL-3.0). README commands, copied exactly: =="
echo "     brew trust --tap abue-ammar/tinycast"
echo "     brew tap abue-ammar/tinycast"
echo "     brew install --cask tinycast"
ask "run the three Homebrew commands above?" && { brew trust --tap abue-ammar/tinycast && brew tap abue-ammar/tinycast && brew install --cask tinycast; }

echo "== 4. Pre-launch checker (no install: stdlib Python) =="
echo "     python3 -I scripts/prelaunch_check.py index.html"

echo "== 5. Read first, not automated =="
echo "   colibri: its reference model is 429 GB on disk and runs at 0.05 to 0.1 tokens/s on a 25 GB laptop. The slide's v1.11.0 file name is outdated (README shows v2.0.0). Load model files only from sources you trust."
echo "   Authelia is identity infrastructure; Seafile's server licence was not confirmed from its repo; Odoo Community is LGPL-3.0 and Enterprise is proprietary; AppFlowy is AGPL-3.0."
echo "Done. Restart Claude Code so the new commands appear: /prelaunch-audit /swap-savings /repo-week-pick /biz-sites-pick"
