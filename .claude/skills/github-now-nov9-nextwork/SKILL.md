---
name: github-now-nov9-nextwork
description: Register of two sources from 9 November 2026 - the @githubnow daily briefing "The GitHub repos you wish you had found sooner" (boykopovar/AnyPS5 PS5 executable porter, storytold/artcraft creative IDE, google-deepmind/mujoco physics engine) and the @itsnextwork carousel "People found more insane new use cases for Claude" (pothole simulator, ad-free TV, 3D jaw scan viewer, anatomy figure, slow Wi-Fi fix) - with licences read, what is new, the legal and safety cautions the slides omit (console binaries, router access, medical scans), and what was not verified. Use before trying any of them or when comparing Claude Code project ideas.
---

# 9 November 2026: three repos and five Claude projects

Checked 9 November 2026: the three repos exist (`git ls-remote`, default branch `main`), licences read. Star gains on the slides (+43,690, +35,633, +26 "this month/today") are unchecked; the GitHub API is blocked from the cloud container.

## @githubnow: three repos

| Repo | Licence (read) | Slide claim | Caution |
|---|---|---|---|
| `boykopovar/AnyPS5` | GPL-2.0 only (`LICENSE`) | "No emulation, no runtime: native PS5 ports"; relinks PS5 executables into the native format of Linux and Windows, ships system library implementations and a shader recompiler | README disclaimer: for interoperability, research and preservation; includes no copyrighted software, firmware or keys; not affiliated with Sony; users are responsible for what they run. Only use files you are entitled to. The slide's "running in ten minutes" is not from the README and was not checked |
| `storytold/artcraft` | MIT OR Apache-2.0 (README; the separate licence files were not opened) | Rust creative IDE: composes 2D layers and 3D staged scenes for AI image and video, then you pick a model | Same author as Craft Anything (`five-repos-agent-tools-nov2026`). Generating media sends prompts to the model you choose: check each model's terms |
| `google-deepmind/mujoco` | Apache-2.0 | Fast, accurate contact physics for robots; C API, Python bindings (`pip install mujoco`), viewers | Mature project; the slide's "+26 stars today" is a daily gain, not a measure of quality |

The briefing's call to action ("star the ones that fit, fork the one you would have built yourself") is promotion for the account.

## @itsnextwork: five "new use cases for Claude"

Each slide pairs a striking claim with a link to a free NextWork guide; the closing slide says to comment "BUILD" to receive them, i.e. a lead-capture mechanic. I did not open the guides.

| Project | Claim | What I would check |
|---|---|---|
| Pothole simulator | Six photos of a pothole rebuilt in 3D, each crash priced at EUR 21,340, "the city filled it two days later" | The causal claim is the creator's; one anecdote is not evidence |
| TV with no ads | A custom TV system replaced ad areas with a live 3D model of an apartment | Modifying a TV launcher can void warranty or break the device |
| 3D jaw scan viewer | One prompt produced a viewer for 800 DICOM files | A viewer is not a diagnostic device. Medical images are special-category personal data: keep them local and anonymised |
| Anatomy figure | Free skill that draws machines in 3D with moving parts | This is `wheresryan22/anatomy`, already in `oss-finds-eight-creators-nov2026` |
| Slow Wi-Fi fixed | Claude Code logged into a router from a photo, found six settings and fixed them in 5 minutes | Giving an agent router admin access can lock you out or open the network; back up the config, change one setting at a time, and never share the password in a prompt |

## New to this repository

AnyPS5, artcraft (named only elsewhere), mujoco, and the NextWork projects as ideas. Use `/repo-vet owner/repo` before installing any of them.

## Not done

Nothing cloned, installed or run; the NextWork guides were not opened.
