---
name: codedex-5-repos
description: The H42 "CODEDEX" series of five open-source repos for building software - Polar (billing), Appwrite (backend), OpenShip (deployment), PocketBase (backend in one file) and DeepDiagram (turn ideas into diagrams) - with verification status for each. Use when choosing billing, backend, deployment or diagramming infrastructure and wanting open-source options.
---

# CODEDEX: 5 GitHub Repos Worth Catching

Source: @hash42labs "CODEDEX" seven-slide carousel (slides 01-07: intro, #001-#005, "Codedex complete").

| # | Repo | Type | Card tagline | GitHub check (7 Oct 2026) |
|---|---|---|---|---|
| 001 | Polar | Billing | Billing infrastructure for software: subscriptions, usage-metered billing, checkout, usage to billing to revenue | `polarsource/polar` exists |
| 002 | Appwrite | Backend | Backend for apps and agents: auth, database, storage, functions | `appwrite/appwrite` exists |
| 003 | OpenShip | Deployment | Deploy your apps, keep control: build, route, secure | Owner not shown on the card. Not verified. Search GitHub for "openship" and read the licence before use. |
| 004 | PocketBase | Backend | A backend in one file: SQLite, auth, realtime, files | `pocketbase/pocketbase` exists |
| 005 | DeepDiagram | Diagrams | Turn ideas into diagrams: mind maps, flowcharts, architecture | Owner not shown on the card. Not verified. |

## When to use which

- Need subscriptions or metered billing without building it: Polar.
- Need auth + database + storage as a service you can self-host: Appwrite (heavier) or PocketBase (single binary, lighter, good for prototypes).
- Need to self-host deployments: OpenShip (after verifying the repo).
- Need diagrams from a text idea: DeepDiagram (after verifying), or the existing `diagram`/mermaid skills.

Clone pattern (public repos only): `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/<owner>/<repo>`. Read the licence and security notes before running anything.
