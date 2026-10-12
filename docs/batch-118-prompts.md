# Batch 118 prompts (plain text; replace [brackets])

## Vet an installer before running it (`/installer-safety-check`)
Here is an install command: [COMMAND]. Tell me what it runs and as which user, whether it pipes a download into a shell, fetches anything else, edits my shell profile or system paths, or asks for sudo. List what to check (repo owner, release signature or checksum, pinned version, a read of the script) and give a safer path: download and read it, verify the checksum, build from source, or use a package manager, ideally in a container or VM. Do not run it.

## Explain my own software with evidence (`/reverse-engineer-own-app`)
I own [APP OR REPO] and want to understand how [FEATURE] works. Explain it from the source, and for every claim give the file and line as evidence. Restate the rule in plain language and offer a small working example. Mark anything inferred rather than seen. Read-only: do not modify or run anything.

## Choose a terminal for parallel agents (`/agent-terminal-pick`)
I run [AGENTS] on [OS], about [N] at a time. Compare staying on tmux with MXterm, Wave, Tabby, Vesta and Calyx against: sessions survive a quit, I can see which agent waits for approval, each pane has its own git worktree, I can review each diff, source and licence are clear, and switching cost. Recommend one and the first test to run on a throwaway repo. Install nothing.

## Local big-model fit (`/local-llm-fit`)
My machine: GPU [MODEL, VRAM], RAM [GB], free SSD [GB]. Task: [TASK]. Would a 125-billion-parameter model compressed and split across GPU, RAM and SSD run? Estimate memory, disk and tokens per second, and the quality loss. Compare with a smaller local model and a hosted API for this task, and recommend one test first. Bind any local API to 127.0.0.1.

## Swap a paid tool for open source
I pay for [TOOL] for [USE]. Suggest an open-source replacement from Excalidraw, Heyform, Maxun, Macshot, OpenChatCut or another, list what I would lose, what self-hosting needs (database, email, backups), the data I must export first, and a one-week trial with a rollback plan.

## Agent browser trial (Moli-style)
Write a Playwright script that connects to a headless browser at [ENDPOINT], fetches [URL], returns the main content as Markdown, and measures time and memory. Run the same script against headless Chrome and compare. Respect robots.txt and the site's terms; do not scrape personal data.
