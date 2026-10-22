#!/usr/bin/env bash
# Batch 108 (report batch-112) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, an agent, templates and a practice workbook were added to the repo. Nothing below was installed or run there.
# Licences come from each repo's LICENSE file, read on 15 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; no install) =="
for r in openai/whisper upscayl/upscayl localsend/localsend immich-app/immich debpalash/VoiceStudio; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   boykopovar/AnyPS5 (GPL-2.0 only) is a PlayStation 5 compatibility layer. Its legal position is unclear to me; it is NOT in the loop above on purpose."
ask "clone boykopovar/AnyPS5 for reading anyway (no install, no run)?" && clone boykopovar/AnyPS5

echo "== 2. Whisper in its own virtual environment (MIT; command line only) =="
echo "   Needs ffmpeg on PATH. It is not a drop-in Otter replacement: no meeting bot, no speaker labels, no live notes."
if ask "create ~/venvs/whisper and run: pip install -U openai-whisper?"; then
  command -v ffmpeg >/dev/null || echo "   ffmpeg not found: install it with your package manager first."
  python3 -m venv "$HOME/venvs/whisper" && "$HOME/venvs/whisper/bin/pip" install -U openai-whisper
  echo "   Try: $HOME/venvs/whisper/bin/whisper your-recording.mp3 --model small"
fi

echo "== 3. Read first, not automated =="
echo "   Immich (AGPL-3.0): you run a Docker server and own the storage. It is not a backup by itself; keep a 3-2-1 plan (3 copies, 2 media, 1 off-site). Face recognition processes biometric data about other people."
echo "   Upscayl (AGPL-3.0): AI upscaling invents detail. Do not use it on evidence or documents where accuracy matters."
echo "   VoiceStudio (AGPL-3.0): clone a voice only with the speaker's written permission. Model weights and voices have separate terms; read them before commercial use."
echo "   Sentry (FSL, source-available, not open source) and PostHog (MIT core) appear in app-launch-6-tools-ella: read each licence before building on it."
echo "   LinkedIn: the MAPS and 10k-content skills draft text only. Keep posting, comments, invitations and messages manual."
echo "   Job-site list (job-seeker-75-websites): about 66 distinct services, India-skewed; check each site's terms before uploading a CV."
echo "Done. Restart Claude Code so the new commands appear."
