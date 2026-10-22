---
name: dotdevs-3-tools-clean-messy-repo
description: The @dotdevs "3 tools for cleaning up a messy repo" carousel (lychee for dead links in Markdown, delta as a Git pager, Knip for unused files, exports and dependencies) with licences read on 21 October 2026 and how to use each safely. Use before releasing a repository.
---

# 3 tools for cleaning up a messy repo (@dotdevs)

Source: 5 slides (cover, three tools, a save slide). Licences read 21 October 2026.

| Tool | Slide says | Repo or site | Licence | Use it safely |
|---|---|---|---|---|
| lychee | Find dead links hiding in your README; run a link check on Markdown before release | lycheeverse/lychee | Apache-2.0 / MIT dual (Apache file read) | Rate-limit and exclude private URLs; a link checker makes real requests |
| delta | Make large code diffs easier to read: use as your Git pager, review a changed file | dandavison/delta | MIT | Set it as `core.pager` in git config; read-only display |
| Knip | Find unused files, exports and dependencies; run the report, review one finding before changing code | knip.dev, webpro-nl/knip | ISC | Never bulk-delete from its report; dynamic imports and config files can look unused |

Related: `plankton-code-quality`, `refactor-clean`, `orch-refine-code`. Nothing was installed.
