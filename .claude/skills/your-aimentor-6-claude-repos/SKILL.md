---
name: your-aimentor-6-claude-repos
description: The @your.aimentor "6 repos blowing up on GitHub for Claude" terminal-card series (caveman, hyperframes, xerj, scientific-agent-skills, diagram-design, billion-context) with each slide claim, licences read from root LICENSE files on 17 October 2026, which are already vendored here, and the conflicting numbers across cards. Use to decide which repos to read before installing anything.
---

# 6 repos "blowing up on GitHub for Claude" (@your.aimentor)

Source: 7 dark terminal-style cards (cover and six repos). Star counts and claims are the author's and **unverified**. Licences were read from each repo's root LICENSE file on 17 October 2026.

| # | Repo | Slide claim | Licence | Here already |
|---|---|---|---|---|
| 01 | juliusbrussee/caveman | "cut token costs 65%", "100,000+ stars", #1 on GitHub Trending and Hacker News, "started as a joke", cited by Adobe Research | Apache-2.0 | skill `caveman` |
| 02 | heygen-com/hyperframes | "Write HTML, get video" | not rechecked | skill `hyperframes` |
| 03 | xerj-org/xerj | "40x fewer tokens than grep" | not rechecked | `githubnow-briefings-aug-sep-oct-2026` |
| 04 | k-dense-ai/scientific-agent-skills | "177 validated expert skills", "250,000+ scientists already use it" | MIT (LICENSE.md) | **new here** (not cloned) |
| 05 | cathrynlavery/diagram-design | "44 pro diagram types" | not checked | earlier cards said 29 types |
| 06 | ranxianglei/billion-context | "Compress AI context 5x", month-long sessions, "your AI bill just got 5x smaller" | MIT | **new here** (not cloned) |

## Read critically
- **[Certain]** Conflicting numbers across cards in this batch: diagram-design is 44 types here but 29 on an earlier card. At least one is stale or marketing.
- **[Certain]** "65% cheaper", "40x fewer tokens" and "5x smaller bill" are single-benchmark or best-case claims. Measure on your own workload before trusting any of them.
- **[Likely]** "250,000+ scientists" is an unverifiable adoption claim; check the repo's own stats.
- Compression and context tools change what the model sees; test accuracy, not only token counts.
- Read each repo's README and source before installing; nothing was cloned or run in this session. `scripts/batch115-install.sh` clones for reading only after you say yes.
