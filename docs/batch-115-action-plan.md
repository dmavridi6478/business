# Batch 111 action plan (files numbered 115)

## Do first (about 15 minutes)

1. Run the sell-listing prompt on one real item and see whether the sold-listing evidence is strong enough to set a price. If it rests on two or three sales, say so in the listing decision.
2. Write your positioning line with `/positioning-triangle`. The test is whether a stranger in your audience recognises themselves in five seconds.
3. Run `/gtm-model-pick` with your real situation. If the answer is "too many segments", start with the minimum viable segment and the beachhead, not the price meter.

## Install only what you need (your machine, your decision)

- `scripts/batch115-install.sh` clones up to five repos for reading and, if you answer yes, creates a virtualenv and installs `rich`. Each step asks first. It contains no piped installers.
- Oh My Zsh: its README install is a piped `curl | sh`. Download `tools/install.sh`, read it, then run it. It renames your existing `.zshrc`.
- BCUninstaller: its README says "Looking for maintainers". Make a restore point and read the leftover list before bulk removal.
- WinDirStat: Windows only. It can delete files and run cleanup tools, so inspect before removing.
- DB Browser for SQLite: edit a copy, not your only file.
- ImageMagick: keep it updated and restrict what it processes when files are untrusted.
- AGPL-3.0 (Whitebophir, DeepDiagram, SearXNG): if you run a modified copy as a network service, you must offer the source.

## Connectors

None installed. Figma, Lucid, Typefully, Taplio and Vibe Prospecting are already connected. Mermaid Chart, tldraw and Whimsical are installable but need your sign-in. The n8n connector needs re-authentication, so no workflow was built; there was nothing workflow-shaped in the files anyway.

## Not changed

`.mcp.json` is unchanged.
