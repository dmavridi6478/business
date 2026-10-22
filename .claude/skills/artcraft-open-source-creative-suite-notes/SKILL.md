---
name: artcraft-open-source-creative-suite-notes
description: Notes from a TikTok clip "3 free open-source repos" about the ArtCraft creative apps (EffectCraft, an After Effects style compositor in Rust, and a Photoshop style PhotoCraft) plus hyperframes, with the on-screen stats, the unverified upstream repo, and cautions. Use before trying them. Upstream repository owner could not be confirmed; nothing was cloned or installed.
---

# ArtCraft open-source creative suite (3-repo TikTok clip)

Source: one 21-second clip, "Open-source repos. 3 free repos to explore this week". Frames were read; there is no transcript.

| Item | On screen | Verified |
|---|---|---|
| EffectCraft | "After Effects, rebuilt in pure Rust"; compositions, layers, keyframes, 306 effects, layer styles, expressions, 3D cameras and lights, render queue; macOS, Windows, Linux and browser; badges "young and moving fast", Rust 1.95+, licence "MIT / Apache-2.0"; 1,802 GitHub stars; site getartcraft.com | Site answers (HTTP 200) on 17 October 2026. **The upstream GitHub owner/repo was not found**; the search showed only third-party wrappers and ports (not reviewed) |
| PhotoCraft | A Photoshop-style app with layers, Curves editor, GPU compositor on wgpu; shown at **0 stars** | Not found as a separate repo |
| hyperframes | 64,474 stars | Skill `hyperframes` already here |

## Read critically
- **[Certain]** The slide's own badge says "young and moving fast"; treat it as early software.
- **[Certain]** The licence badge was read off a video frame, not a LICENSE file; read the file in the real repo before using the code commercially.
- **[Likely]** Third-party "ports" and "hosted builds" of a new project can contain unreviewed changes; use the official site and source only.
- Relevant to this repo: it feeds `design-templates` ideas (timeline, panels) only; no code was copied.
