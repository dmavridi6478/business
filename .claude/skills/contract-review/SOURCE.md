Vendored from https://github.com/evolsb/claude-legal-skill (skill.md → SKILL.md), MIT License.
Cloned at commit:
bca0d2e9d5ec81298ddfbfde78fa4f38fb4589b0

The upstream repo is named `claude-legal-skill`, but the skill's own
frontmatter declares `name: contract-review` — this directory is named to
match that, since Claude Code resolves a skill by its declared name, not
its repo name. Vendored: `skill.md` (renamed `SKILL.md`) and the four
markdown worked examples (`examples/*.md`: NDA, SaaS agreement, M&A
agreement, balanced-agreement reviews). The repo's `examples/demo.png`
(a 438KB marketing screenshot, not referenced by SKILL.md) and
`CHANGELOG.md` were left out as non-functional to the skill itself.

Distinct from the already-installed `claude-for-legal` plugin (Anthropic's
12-plugin suite covering commercial/privacy/product/corporate/employment/
regulatory/AI-governance/litigation/IP/law-student/legal-clinic/CoCounsel) —
this is a single focused skill for contract review specifically, built on
the CUAD dataset (41 risk categories), ContractEval benchmarks, and
LegalBench, with market-standard-clause comparison and redline suggestions.
