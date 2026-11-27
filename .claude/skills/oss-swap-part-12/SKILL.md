---
name: oss-swap-part-12
description: Verified table of 10 paid developer tools and the free open-source alternatives a TikTok series (Part 12, @modelsignal, '10 free GitHub repos replacing $100M+ software companies') names - SolarWinds Loggly to Graylog, JetBrains IntelliJ IDEA to VSCodium, LangSmith to Arize Phoenix, SonarQube Cloud to Semgrep, JetBrains DataGrip to DBeaver, Supabase to PocketBase, Augment Code to OpenCode, Amazon Q Developer to Kilo Code, JetBrains TeamCity to Jenkins, Grafana Cloud to VictoriaMetrics - with repo, stars, licence checked 19 Oct 2026, the $4,174 arithmetic and licence warnings. Use when comparing paid developer tools with open-source ones. Run via /oss-swap-12.
---

# Part 12 - "10 free GitHub repos replacing $100M+ software companies"

Source: 12 TikTok cards (@modelsignal; prices read 15 Oct). Repo data read from GitHub on 19 Oct 2026. "$100M+" is the series' own claim; it is not evidenced on the cards and is not used here.

## Verified table

| Job | Paid (month / year) | Free alternative | Repo | Stars (card / verified) | Licence (verified) |
|---|---|---|---|---|---|
| Log search | SolarWinds Loggly $79 / $948 | Graylog | `Graylog2/graylog2-server` | 8.2K / 8,157 | "Other" - read LICENSE |
| Code editor | JetBrains IntelliJ IDEA $71.90 / $863 | VSCodium | `VSCodium/vscodium` | 34K / 33,636 | MIT |
| LLM tracing | LangSmith $39 / $468 | Arize Phoenix | `Arize-ai/phoenix` | 12K / 11,909 | "Other" - read LICENSE before commercial use |
| Code scanning | SonarQube Cloud $34 / $408 | Semgrep | `semgrep/semgrep` | 17K / 17,118 | LGPL-2.1 (rules have their own licence) |
| Database IDE | JetBrains DataGrip $25.90 / $311 | DBeaver | `dbeaver/dbeaver` | 52K / 52,121 | Apache-2.0 |
| Backend | Supabase $25 / $300 | PocketBase | `pocketbase/pocketbase` | 61K / 61,492 | MIT |
| Terminal AI agent | Augment Code $20 / $240 | OpenCode | `anomalyco/opencode` (GitHub redirects `sst/opencode`) | 214K / 216,384 | MIT |
| Editor AI agent | Amazon Q Developer $19 / $228 | Kilo Code | `Kilo-Org/kilocode` | 28K / 27,602 | MIT |
| CI server | JetBrains TeamCity $15 / $180 | Jenkins | `jenkinsci/jenkins` | 27K / 26,675 | MIT |
| Time series | Grafana Cloud $19 / $228 | VictoriaMetrics | `VictoriaMetrics/VictoriaMetrics` | 18K / 17,841 | Apache-2.0 |

**Arithmetic check.** The ten annual figures sum to $4,174 (948+863+468+408+311+300+240+228+180+228), matching the cover of the summary card. The "8 of 10" list shows the eight largest (sum $3,766); the $4,174 headline is all ten. Monthly x 12 reproduces each annual figure ($71.90 x 12 = $862.80, shown as $863; $25.90 x 12 = $310.80, shown as $311).

## What "free" does not replace

| Swap | Gap |
|---|---|
| Loggly -> Graylog | You run and size the cluster; licence is not a standard OSI one - read it |
| IntelliJ -> VSCodium | A different editor, not a Java IDE; refactoring and inspections differ |
| LangSmith -> Phoenix | Self-hosting makes retention and access yours; "Other" licence needs a legal read |
| SonarQube -> Semgrep | Different rule sets and quality gates; compare findings on your repo |
| DataGrip -> DBeaver | Compare completion and refactoring on your own schema before assuming parity |
| Supabase -> PocketBase | A single-binary SQLite backend: no Postgres, no managed scaling |
| Augment / Amazon Q -> OpenCode / Kilo | The agents are free software; model usage is billed by the provider you plug in |
| TeamCity -> Jenkins | You maintain plugins and security updates |
| Grafana Cloud -> VictoriaMetrics | Storage and query engine; dashboards and alerting live elsewhere |

Nothing is installed by this skill.
