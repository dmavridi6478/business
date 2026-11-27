# Archive Agent: install and test checklist

Source: the README of `shredEngineer/Archive-Agent`, read on 19 October 2026. Archive Agent is a command-line file indexer and RAG search tool. It is not the Agent Archive service (agentarchive.io). Licence: GNU GPL v3.0.

No secret belongs in this file. Never paste an API key into chat, a commit or a shared document.

## 1. Before you start

- [ ] Use your own machine. The README lists only Ubuntu 24.04 and 22.04 as tested; other systems are unconfirmed.
- [ ] Docker is installed (it runs the Qdrant database).
- [ ] Python 3.10 or newer is installed.
- [ ] Decide the provider: OpenAI, OpenRouter, Ollama or LM Studio. Local providers (Ollama, LM Studio) need no key and keep documents on the machine.
- [ ] Choose a small test folder (a few non-sensitive files). Do not start with your whole document library.

## 2. Secrets

- [ ] If an API key was ever pasted into a chat, revoke it at the provider and create a new one. Set a monthly spend limit.
- [ ] Set `LOCAL_AUTH_PASSWORD` in your shell. The GUI, MCP server and Qdrant refuse to start without it.
- [ ] Set the provider key (`OPENAI_API_KEY` or `OPENROUTER_API_KEY`) for the current session, or load it from a file with `chmod 600` that is not in git. The README suggests appending it to `~/.bashrc`, which stores it in plain text; prefer the safer options.
- [ ] To use Claude or Grok through the OpenAI-compatible route, change the URL setting and put that provider's key in `OPENAI_API_KEY` (per the README).

## 3. Install

- [ ] `git clone https://github.com/shredEngineer/Archive-Agent` and `cd Archive-Agent`.
- [ ] Read `install.sh` before running it. It downloads and installs `uv`, sets up a Python environment and the spaCy model, installs `pandoc`, starts Qdrant in Docker, and adds a global `archive-agent` command.
- [ ] Run `./install.sh`.

## 4. First test (small and cheap)

- [ ] Start Archive Agent and choose the provider when prompted. The provider cannot be changed for an existing profile; create a new profile instead.
- [ ] Create a profile for the test.
- [ ] Add one include pattern pointing at the test folder, then track and commit the files. Exact command names are in the README section "CLI command reference"; check it rather than guessing.
- [ ] Ask one question whose answer you already know. Confirm the answer cites the right file and page or line.
- [ ] Note the token usage the tool prints at the end and multiply for your real library before scaling up.

## 5. Settings worth checking

- [ ] PDF OCR strategy: `strict` is recommended (accurate, slower, costlier because each page goes through the vision model); `relaxed` is cheaper; `auto` is experimental.
- [ ] Models for chunk, rerank, query, vision and embed in the profile settings.
- [ ] `max_workers_*` if your provider rate-limits you.

## 6. Safety

- [ ] Index only files you may process with the chosen provider; remote providers receive document content.
- [ ] Keep the Qdrant port and the MCP server on localhost behind the password.
- [ ] Treat answers as retrieval with approximate references (the README says references are approximate).
- [ ] If you reuse any of its code in a distributed product, GPL v3.0 applies to that product. Reusing only ideas (retry with backoff, schema-validated retries, permutation repair) does not.

## 7. Limits of this checklist

- Written from the README only; I did not run the install, and the CLI reference section was not read in full.
- This cloud session cannot be assumed to have Docker, and nothing persists after it ends.
