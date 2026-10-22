#!/usr/bin/env bash
# Batch 111 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, agents and templates were added to the repo; mattpocock/skills 'grilling' and
# 'domain-modeling' were vendored (MIT). Nothing below was installed or run there.
# Facts come from each repo's LICENSE and README, read on 15 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in alibaba/open-code-review google/artemis mattpocock/skills vectorize-io/hindsight paperclipai/paperclip HKUDS/CLI-Anything; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Matt Pocock skills as a plugin (MIT; the two core skills are already vendored in this repo) =="
echo "   README: claude plugin install mattpocock-skills@claude-plugins-official"
ask "run that command now?" && claude plugin install mattpocock-skills@claude-plugins-official

echo "== 3. Open Code Review (Apache-2.0; npm package per its README) =="
echo "   It sends your git diff to the LLM you configure. Try it on a repo with nothing secret in it first."
ask "npm install -g @alibaba-group/open-code-review?" && npm install -g @alibaba-group/open-code-review

echo "== 4. Read first, not automated =="
echo "   google/artemis: needs an Android phone with USB debugging or an emulator. Its start.sh installs ADB, scrcpy, FFmpeg and uv, and offers to write a global MCP config and rules into your AI IDEs. Read start.sh before running it."
echo "   ntdevlabs/tiny11builder: NO licence file; its NOTICE says redistribution rights are not granted. Core builds cannot be updated and disable Defender. Use only on a test VM with your own Windows licence."
echo "   Self-hosted swaps (modelsignal-free-swaps-22): licences are AGPL (RustDesk, Passbolt, PhotoPrism, LinkStack), GPL (Weblate, Frappe HR), OSL (UVdesk), Elastic License (Invoice Ninja). Read each LICENSE before commercial use; price the hosting and admin time first."
echo "   LinkedIn automation (strategies 2 and 5): third-party sources say LinkedIn's terms prohibit automated tools. Keep invitations and messages manual."
echo "Done. Restart Claude Code so the new commands appear."
