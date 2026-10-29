---
name: sitetusk-free-tools-5
description: Five free open-source projects from a @sitetusk repo carousel - FreeCAD (3D parametric modeler), OSSU computer-science (self-taught CS curriculum), jq (command-line JSON processor), How-To-Secure-A-Linux-Server (hardening guide) and FreshRSS (self-hosted feed reader) - with what each is for, the licence read from its own repository, how to start, and the catch. Use when someone needs a free tool for 3D design, learning computer science, processing JSON, securing a Linux server or reading feeds in one place.
---

# Five free tools from a @sitetusk carousel

Source: five repo cards by @sitetusk (Site Tusk). The one-line descriptions are the cards'; the licences below were read from each repository's own licence file on 26 October 2026.

| Repo | What the card says | Licence | Start | The catch |
|---|---|---|---|---|
| `FreeCAD/FreeCAD` | Free parametric 3D modeler for mechanical parts, architecture and products with fully editable, parameter-driven models (card shows release v1.1.4) | LGPL-2.1 | Download the release for your OS from the FreeCAD website; start in the Part Design workbench | Steep learning curve; parametric models break if you edit early sketches carelessly |
| `ossu/computer-science` | Free curriculum that guides self-taught learners through a full computer science education using top university courses online | MIT (repo); each linked course has its own terms | Read the README, follow Core CS in order | README estimates about 2 years at roughly 20 hours a week; courses are third-party and some content moves or goes paid for certificates |
| `jqlang/jq` | Command-line JSON processor, "like sed, awk, grep for JSON", C, zero runtime dependencies | MIT (see the COPYING file) | Prebuilt binary from the GitHub releases, a package manager, or Docker | Version differences change behaviour; use `jq --version` before copying snippets (see `jq-json-cookbook`) |
| `imthenachoman/How-To-Secure-A-Linux-Server` | Evolving step-by-step guide to firewalls, SSH hardening, intrusion detection and other measures | CC BY-SA 4.0 (guide text) | Read "Before You Start", then work through it on a test machine | Easy to lock yourself out; the author states it is an evolving guide for the author's own use case (see `linux-server-hardening-guide`) |
| `FreshRSS/FreshRSS` | Self-hosted RSS and Atom aggregator; multi-user, anonymous reading mode, API for mobile clients, CLI, web scraping with XPath, extensions | AGPL-3.0 | Official Docker image, see the repo's Docker README | AGPL: offering a modified copy over a network requires offering its source; you run and update the server |

## Pick by need

- Design a physical part or building: FreeCAD.
- Learn computer science without a degree: OSSU.
- Slice or reshape JSON from an API or log: jq.
- Lock down a VPS or home server: the Linux guide.
- Replace a social feed with sources you choose: FreshRSS (also covered in `dev-repos-to-clone`, batch 103).

## Reading it critically

- The cards give one sentence each; popularity figures, maintenance status and security posture are not shown. Check the repository's recent commits and open issues before depending on it.
- Four of the five are "learn and run" tools; only FreshRSS is a server you must keep patched.
- Run `/free-tool-pick [need]` to choose, `scripts/batch112-install.sh` (on your own machine) to clone or install with a prompt at every step.
