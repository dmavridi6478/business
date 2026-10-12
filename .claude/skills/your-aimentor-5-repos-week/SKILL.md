---
name: your-aimentor-5-repos-week
description: The @your.aimentor "5 GitHub repos that blew up this past week (Claude Code)" series - i-have-adhd (answer-first output skill), ECC (affaan-m agent harness, 68 agents / 291 skills), Recordly (free auto-zoom screen recorder), coreyhaines31/marketingskills (50 marketing skills; /cro and /emails) and microsoft/markitdown (any file to Markdown) - with slide stats, install commands as shown, which are already in this repo and a safe adoption order. Use when evaluating these repos or choosing how to turn documents into Markdown, record product demos, or add marketing skills.
---

# 5 repos from @your.aimentor

Stats are the slides' own ("this week" gains too). Not installed in the cloud session; commands are for your machine.

| # | Repo | What | Stats | Install as shown | Already here |
|---|---|---|---|---|---|
| 01 | `ayghri/i-have-adhd` | every reply: action first, numbered steps, one next move; a single 142-line file, MIT | 40.4k stars, +10.2k wk | `claude plugin marketplace add ayghri/i-have-adhd` then `claude plugin install i-have-adhd@i-have-adhd` | skill `i-have-adhd` (142 lines) |
| 02 | `affaan-m/ECC` | one person's Claude Code setup open-sourced after an Anthropic hackathon win: 68 agents, 291 skills, 61 hooks, a security scanner; plan first, test first, review from a fresh session, save what worked as a skill | 256k stars, +9.3k wk | `npx ecc-universal@2.2.1 setup` (pinned version on the slide) | many `ecc-*` skills; "start with one workflow, skip the catalog" |
| 03 | `webadderallorg/Recordly` | free screen recorder: auto-zoom on the cursor, smoothed mouse, click bounce, webcam bubble, wallpaper frame, MP4 or GIF; Mac, Windows, Linux; slide says no AI, one developer | 26.9k stars, +3.2k wk | download DMG, EXE or AppImage from the repo's releases page (macOS 14+) | no |
| 04 | `coreyhaines31/marketingskills` | 50 marketing skills from a growth operator (Baremetrics, SavvyCal): CRO, copy, cold email, SEO, pricing, welcome sequences; each reads one `product-marketing.md` first | 49.6k stars, +2.7k wk | `npx skills add coreyhaines31/marketingskills --skill cro emails` | skills `*-corey-haines`, `product-marketing-context` |
| 05 | `microsoft/markitdown` | Python tool: PDF, Word, Excel, PowerPoint, audio, HTML, EPUB, YouTube links to Markdown | 182.6k stars, +4.6k wk | `pip install 'markitdown[all]'` then `markitdown paper.pdf -o paper.md` (Python 3.10-3.13; scans need markitdown-ocr) | skill `pdf-to-markdown` (use it first for PDFs) |

The narrator's picks: markitdown (installed), marketing skills (cro + emails, installed), i-have-adhd (stealing two rules), Recordly and ECC (trying).

## Use
- **/cro**: type `/cro` plus your homepage URL; expect: is the value clear in 5 seconds, who it is for, does the button say more than "Get Started", a rewritten headline. `/emails` does the same for welcome emails. In this repo use `/headline`, `/value-proposition` or the Corey Haines skills.
- **Documents to Markdown:** run markitdown on a copy of the file; check tables and headings; for scanned PDFs add OCR. Never convert files you must keep private through an online service.
- **Demo video:** record with Recordly, then polish with `hyperframes` or `video-editing`.

## Cautions
1. ECC and any "install a whole catalogue" repo: start with one workflow, read hooks before enabling (hooks run commands).
2. 256k and 182k star counts are slide figures; confirm on GitHub.
3. `npx` and `pip` run third-party code on your machine; pin versions, use a venv.
Command: `/convert-to-markdown`.
