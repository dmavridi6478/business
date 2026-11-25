---
description: Vet a GitHub repo before adopting it - does it exist, who owns it, what licence, how active, what it can do on your machine - without cloning or running it
argument-hint: [owner/repo]
---

Input: "$ARGUMENTS".

1. Check existence and the default branch: `git ls-remote --symref https://github.com/<owner>/<repo>.git HEAD`. If it fails, say the repo could not be confirmed; do not guess a similar name.
2. Read the licence from the repo's own file (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`) with `curl -sS https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<file> | head`. Report the licence, or that none was found. Flag AGPL and GPL (network or copyleft obligations), non-commercial and "source-available" terms.
3. Report the owner as an individual or an organisation, and say if the name suggests a vendor (for example "Anthropic" or "Cloudflare") that the owner is or is not.
4. Check `.claude/skills` and `docs/` for an existing skill covering the same job and name it.
5. Say what installing it would let it do (run commands, edit files, use credentials, reach the network). Star counts from a card or screenshot are unverified; say so.
6. Do not clone, install or run the repo.
