#!/usr/bin/env bash
# Install the full gstack suite (garrytan/gstack, MIT). RUN ON YOUR OWN MACHINE, not in a cloud session.
# Why: the repo vendors only gstack's router SKILL.md (see .claude/skills/gstack/SOURCE.md). The ~70 sub-skills it routes to
# (/spec, /office-hours, /plan-ceo-review, ...) and the browse binary exist only after the upstream installer runs.
# What the upstream ./setup does (from the repo page, not read line by line by me): symlinks skills into your tool configs,
# downloads Chromium, writes config files, registers Claude Code hooks. It needs Git and Bun >= 1.4.2.
# Every step asks first. Nothing here pipes a download into a shell. Nothing here touches this repo's files.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
DEST="$HOME/.claude/skills/gstack"

echo "== 0. Checks =="
command -v git >/dev/null || { echo "git is required"; exit 1; }
if command -v bun >/dev/null; then echo "   bun $(bun --version)  (need 1.4.2 or newer)"; else echo "   bun not found. Install it from bun.sh by your own method, then re-run."; exit 1; fi

echo "== 1. Name clashes =="
echo "   gstack's router also routes to: benchmark, context-save, context-restore, design-review, learn, qa, review, ship."
echo "   This repo already has local skills or commands with those names (.claude/commands/{qa,review,ship,learn,context-save,context-restore,design-review}.md, .claude/skills/benchmark)."
echo "   After install, 'invoke /review' may reach either one. Decide which you want before relying on the router."
echo "   The router is proactive by default; to stop that, set PROACTIVE=false with gstack-config after install."
ask "Continue?" || exit 0

echo "== 2. Clone (documented command, shallow, single branch) =="
if [ -e "$DEST" ]; then
  echo "   $DEST already exists. Back it up or remove it yourself first, then re-run:"
  echo "   mv \"$DEST\" \"$DEST.bak\""
  exit 1
fi
ask "git clone garrytan/gstack into $DEST ?" || exit 0
mkdir -p "$HOME/.claude/skills"
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git "$DEST"

echo "== 3. Read before you run =="
echo "   Commit: $(git -C "$DEST" rev-parse HEAD)"
echo "   Read these first:  less \"$DEST/setup\"   and the README."
echo "   Check for: network downloads, writes outside $DEST, and which hooks it registers in ~/.claude/settings.json."
ask "I have read ./setup and want to run it now?" || { echo "Stopped after the clone. Run: cd $DEST && ./setup"; exit 0; }
(cd "$DEST" && ./setup)

echo "== 4. After setup =="
echo "   Restart Claude Code. Check that /spec, /office-hours and /plan-ceo-review now appear in the skills list."
echo "   Review ~/.claude/settings.json for the hooks it added, and keep a copy of what you removed or kept."
echo "   Team mode (./setup --team, gstack-team-init) commits files into a repo. It is NOT run here; do it per project, on purpose."
