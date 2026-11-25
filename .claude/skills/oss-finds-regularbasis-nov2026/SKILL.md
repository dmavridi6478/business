---
name: oss-finds-regularbasis-nov2026
description: Checked register of the @regularbasis.studio carousel "5 More GitHub Repos That Feel Illegal To Use For Free" (Floci, Craft Anything, Agent Desktop, Worktrunk, Kimi K3 in C) - what is new (Floci, Worktrunk, kimi-k3-in-c), what is already registered (Craft Anything, Agent Desktop), licences read from each repo, install lines, and what the slides omit (the 1.56 TB disk behind the "8 GB RAM" claim, the clickbait title, the "instead of" framing). Use before trying any of them, when you want a free local AWS emulator, a git-worktree workflow for parallel agents, or an honest read of the 2.78-trillion-parameter-on-one-CPU claim.
---

# Five repos "that feel illegal to use for free" (@regularbasis.studio)

Checked 8 November 2026: all five repos exist (`git ls-remote`, default branch `main`), licences read from each repo's own file, claims compared with READMEs. Star counts (30.6K, 16.1K, 17.4K, 11.7K, 10.8K) are slide snapshots and could not be checked. Seven slides: cover, five repo cards, closing "Send This To A Founder Who Still Pays For LocalStack Or A Computer-Use API". The title is clickbait: nothing here is illegal, and "free" is open source, not "no cost to run".

| # | Repo | Licence (read) | Slide claim | Check against the README | Status |
|---|---|---|---|---|---|
| 01 | `floci-io/floci` (local AWS emulator) | MIT (`LICENSE`) | AWS-shaped services on your laptop with Docker; no account, token or paywall; "instead of LocalStack Pro" | README: "No account. No auth token. No feature gates. Just `docker compose up`"; point the AWS SDK, CLI, Terraform or CDK at `http://localhost:4566`. Service coverage is a list in the README: check yours is on it. It is an emulator, so behaviour can differ from real AWS | New |
| 02 | `storytold/craft-anything` | Apache-2.0 on the slide; MIT OR Apache-2.0 per its README badge | Inspects any site, app or game and has an agent craft your own | Already in `five-repos-agent-tools-nov2026`: early alpha, a reverse-engineering engine, "clean room" is a rule not a sandbox | Registered |
| 03 | `vercel-labs/agent-desktop` | Apache-2.0 | Lets an agent operate desktop apps through the OS accessibility tree, not screenshots | Already registered: it can operate any app you grant, and snapshots can hold private content | Registered |
| 04 | `max-sixty/worktrunk` | Dual MIT and Apache-2.0 (`LICENSE`) | Makes git worktrees as easy as branches for parallel AI agents; `wt switch -c -x claude` | Install: `brew install worktrunk && wt config shell install` (README). It changes your shell config: read what the shell install adds first | New |
| 05 | `FareedKhan-dev/kimi-k3-in-c` | Apache-2.0 | A 2.78-trillion-parameter Kimi K3 that "runs on a single CPU in 8.24 GB of RAM" | README agrees on 8.24 GB peak RSS, but the checkpoint is 1.56 TB on disk and, at small RAM sizes, the whole model streams off the disk on every step. README says "slow, and answering correctly"; more memory only buys speed. The slide's "instead of cloud GPUs" is not an equivalent: you trade GPU cost for a 1.56 TB drive and long waits | New |

## Reading the "Instead of" strips

Each slide pairs a repo with a paid thing it "replaces". Treat these as the creator's framing: Floci is not LocalStack Pro (different coverage), Agent Desktop is not a hosted computer-use API, Worktrunk is a convenience layer over git, and K3 in C is a research demonstration, not a GPU substitute.

## Use

`/free-app-pick` for desktop jobs; `/repo-vet owner/repo` before installing any of these. Floci is a good first try only if you already run Docker and your tests target AWS.

## Not done

Nothing cloned or run. The Floci service list, Worktrunk behaviour and K3 speed were not tested.
