---
name: oss-animation-vfx-ten-nov2026
description: Checked register of ten open-source animation, VFX and motion tools from two @martiendejong_dev carousels ("GitHub is hiding THESE INSANE animation tools", slides x/8 and x/13) - OpenToonz, Friction, FreeMoCap, Synfig Studio, Effekseer, Theatre.js, Pencil2D, OpenVDB, SVG.js, Natron - with licences read from each repo, which are libraries rather than apps, platform notes, and the warning that the interface pictures on the cards are illustrations. Use when choosing a free 2D animation, compositing, particle, motion-capture or web-animation tool, or before installing any of them.
---

# Ten free animation and VFX tools (carousels read 15 November 2026)

Checked 15 November 2026: all ten repos exist (`git ls-remote`), default branches and licences read from the repo files, claims compared with the READMEs. Star counts were not on these cards. Nothing was installed or run.

**Read this first.** The "hiding" in the title is a hook: these are long-established projects. The interface pictures are AI-style illustrations, not screenshots: OpenVDB's card says "Illustrative Workflow - Not an Official OpenVDB UI", Natron's says "Illustrative UI - not an official screenshot", SVG.js's says "Illustrative SVG.js Code Playground - not an official app UI". Treat every picture on all ten cards as a mock-up. Two of the ten are libraries (OpenVDB, SVG.js), not apps, and Theatre.js is a library plus an editor.

Slide numbers: seven tools come from an 8-slide set (cover plus 02 to 08), three (09 OpenVDB, 10 SVG.js, 11 Natron) from a 13-slide set whose other ten slides were not supplied.

| Tool | Repo (default branch) | Licence (read) | What it is | Notes the card omits |
|---|---|---|---|---|
| OpenToonz | `opentoonz/opentoonz` (master) | Modified BSD (`LICENSE.txt`); `thirdparty` and brush folders carry their own licences | 2D frame-by-frame animation studio with Xsheet and timeline | Check third-party licences before shipping assets or builds |
| Friction | `friction2d/friction` (main) | GPL-3.0-only | 2D motion graphics: vector and raster, keyframes, SVG export, expressions | Third-party licences listed under Help > About > Licenses |
| FreeMoCap | `freemocap/freemocap` (main) | AGPL-3.0 | Markerless 3D motion capture, multi-camera, Blender export | README build steps use the `development` branch and `uv`; set-up is technical; recording people raises consent and privacy duties |
| Synfig Studio | `synfig/synfig` (master) | GPL-3.0 | 2D vector animation with tweening and bone rigging | |
| Effekseer | `effekseer/Effekseer` (master) | MIT | Particle effect tool for 2D and 3D | Unity and Unreal plugins live in separate repos |
| Theatre.js | `theatre-js/theatre` (main) | Core Apache-2.0; Studio AGPL-3.0 | Motion design for the web: keyframes, graph editor, Three.js and HTML/SVG | README says development moved temporarily to a private repo and 1.0 is coming; the editor you use is the AGPL part, only `@theatre/core` ships in your bundle |
| Pencil2D | `pencil2d/pencil` (master) | GPL-2.0 (`LICENSE.TXT`) | Bitmap and vector 2D animation, onion skin | Nightly builds are less stable than releases (README) |
| OpenVDB | `AcademySoftwareFoundation/openvdb` (master) | Apache-2.0 | C++ library for sparse volumetric data, from DreamWorks Animation | Library, not an app; trunk is "generally less stable" than release tags |
| SVG.js | `svgdotjs/svg.js` (master) | MIT | Lightweight JavaScript library for SVG, no dependencies | Library; the pictured "playground" is an illustration |
| Natron | `NatronGitHub/Natron` (RB-2.6) | GPL-2.0 | Node-based compositor like After Effects, Nuke or Fusion; OpenFX plugins, Python scripting | Default branch is `RB-2.6`, not master; some bundled plugins carry other licences |

## Which to look at for which job

| Job | Start with | Why |
|---|---|---|
| Hand-drawn 2D frames | Pencil2D (simple), OpenToonz (production style) | Both frame-by-frame, both free |
| Vector character animation | Synfig Studio | Bones and tweening |
| Motion graphics and web animation | Friction, Theatre.js, SVG.js | Friction for files, the other two for code on the web |
| Compositing and VFX | Natron | Node graph like commercial compositors |
| Game particle effects | Effekseer | Engine plugins exist |
| Body motion data | FreeMoCap | Needs cameras and set-up time |
| Volumetric data in a pipeline | OpenVDB | Developer library |

## Licence flags

GPL and AGPL (Friction, FreeMoCap, Synfig, Pencil2D, Natron, Theatre.js Studio): copyleft applies if you distribute changes, and AGPL extends that to network use. Output you make with these tools (a film, an image) is generally yours, but confirm each tool's terms and any bundled assets. MIT, BSD and Apache (Effekseer, SVG.js, OpenVDB, OpenToonz core) are permissive.

## Not done

Nothing cloned, installed or run; no version claim on any card checked (Pencil2D "v0.6.6" is in an illustration); platform lists on the cards not reproduced as fact (check each README). Use `/free-app-pick`, `/repo-vet owner/repo` and `/repo-licence-check` first.
