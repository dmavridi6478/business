---
name: replace-so-oss-swap-6-oct
description: The @replace.so "Stop paying for these, start using these 6 free tools" carousel (Oct 2026) - Excalidraw (whiteboard, versus Miro), OpenChatCut (AI video editor), Maxun (website to structured API), Heyform (Typeform alternative), Macshot (macOS screenshots and recording) and a sixth tool not in the upload - with slide stars, what each replaces, which are already covered by other skills, licence and data cautions, and a swap checklist. Use when replacing a paid whiteboard, form, screenshot, scraping or video-editing subscription with open source.
---

# Stop paying, start using (6 free tools)

Stars are the slides' own. The paid-tool icons are shown without names; identifications below are from the icons and are low confidence where marked.

| Tool | Replaces (icon) | What | Stars | Covered elsewhere |
|---|---|---|---|---|
| Excalidraw | Miro | open-source collaborative whiteboard for hand-drawn diagrams, wireframes, sketches on an infinite canvas | 133,615 | `dotdevs-app-and-dev-tools`, `dev-repos-to-clone`; a Miro connector exists here |
| OpenChatCut | a paid video editor (icon unclear) | local-first AI video editor: describe cuts, agent adds captions, music, transitions; multitrack timeline; reframing; editable exports; open source (v0.2.14) with a Pro tier | 2,257 | `replace-so-oss-repos-10`, `dev-repos-to-clone` |
| Maxun | a scraping SaaS (icon unclear) | no-code platform to scrape, crawl, search and extract websites into APIs and reusable outputs (Markdown, HTML, text, links) | 17,757 | `replace-so-dev-repos-6` |
| Heyform | Tally (asterisk icon, medium confidence) | open-source Typeform alternative: conversational forms, surveys, quizzes, polls; logic, customisation, integrations, analytics | 9,008 | `dev-repos-to-clone` |
| Macshot | a paid screenshot app (icon unclear) | native macOS screenshots and recording: annotate, blur and redact, OCR, scroll capture, audio, video editing, MP4/GIF; macOS 12.3+; v4.2.1 | 3,741 | `github-trending-oct8-repos` |
| (sixth) | | one icon pair is a database; not identifiable | | |

## Swap checklist
1. Export your data from the paid tool first; keep it until the swap is proven.
2. Check what the open-source version lacks (Excalidraw: no Miro-style templates and access controls unless self-hosted with extras; Heyform self-hosted needs a database and email).
3. Self-hosting means you own updates, backups and security (`self-hosted-docker-stack`).
4. Scraping (Maxun): respect robots.txt and each site's terms; do not collect personal data without a lawful basis.
5. Forms collect personal data: set retention, consent text and a processor agreement if you use a hosted plan.
Related: `open-source-swap-stack-8`, `oss-alternatives`, `/swap-stack-check`, `/self-host-swap`, `/oss-repo-vet`.
