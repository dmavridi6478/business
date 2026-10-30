---
name: oss-swap-part-18
description: Verified table of 12 paid developer tools and the free open-source alternatives a TikTok series (Part 18, @modelsignal) says to switch to - Travis CI to Concourse, Factory to OpenAI Codex CLI, incident.io to Keep, Portkey to LiteLLM, Kinde to Better Auth, Splunk to Prometheus, Read the Docs to Starlight, Intruder to Nuclei, Socket to OSV-Scanner, Scout APM to Pinpoint, Descope to Logto, Atlassian Compass to Backstage - with repo slug, stars and licence checked on 19 Oct 2026, the annual saving arithmetic, and an equivalence-gap column showing what each swap does NOT replace. Use when someone considers replacing a paid dev tool with a self-hosted one, or wants the real cost of "free". Run via /oss-swap-18; follows the free-vs-paid-tool decision procedure.
---

# Part 18 - "Save $8,621 a year. Use these free dev tools instead."

Source: 14 TikTok cards (@modelsignal; prices "read 15 Oct", repo stats "checked 15 Oct"). Slugs, stars and licences below were checked against GitHub on 19 Oct 2026. The authors' own caveat is printed on each card: "Our call, not theirs."

## Verified table

| Job | Paid (month / year) | Free alternative | Repo | Stars (card / verified) | Licence (verified) |
|---|---|---|---|---|---|
| CI pipelines | Travis CI $13.75 / $165 | Concourse | `concourse/concourse` | 7.9K / 7,919 | Apache-2.0 |
| Coding agent CLI | Factory $20 / $240 | OpenAI Codex CLI | `openai/codex` | 129K / 129,903 | Apache-2.0 |
| Incident response | incident.io $15 / $180 | Keep | `keephq/keep` | 12K / 12,413 | "Other" - read LICENSE first |
| LLM gateway | Portkey $49 / $588 | LiteLLM | `BerriAI/litellm` | 61K / 61,565 | "Other" - read LICENSE; check which features are enterprise-only |
| User login | Kinde $25 / $300 | Better Auth | `better-auth/better-auth` | 30K / 30,311 | MIT |
| Metrics | Splunk $6 / $72 | Prometheus | `prometheus/prometheus` | 67K / 66,619 | Apache-2.0 |
| Docs site | Read the Docs $50 / $600 | Starlight | `withastro/starlight` | 9.4K / 9,425 | MIT |
| Vulnerability scans | Intruder $239 / $2,868 | Nuclei | `projectdiscovery/nuclei` | 32K / 32,106 | MIT |
| Dependency checks | Socket $25 / $300 | OSV-Scanner | `google/osv-scanner` | 11K / 11,198 | Apache-2.0 |
| Tracing | Scout APM $19 / $228 | Pinpoint | `pinpoint-apm/pinpoint` | 14K / 13,867 | Apache-2.0 |
| Enterprise SSO | Descope $249 / $2,988 | Logto | `logto-io/logto` | 15K / 14,689 | MPL-2.0 |
| Developer portal | Atlassian Compass $7.67 / $92 | Backstage | `backstage/backstage` | 35K / 34,614 | Apache-2.0 |

**Arithmetic check.** The 12 annual figures sum to $8,621 (165+240+180+588+300+72+600+2,868+2,988+300+228+92), matching the cover. The "8 of 12" summary card lists the eight largest, which sum to $8,112; its "$8,621" headline refers to all twelve. Prices are the lowest plan the card quotes; the card says nothing about seats or usage.

## What "free" does not replace (equivalence gaps)

| Swap | Gap to check before switching |
|---|---|
| Travis CI -> Concourse | You run and patch it; pipelines use Concourse's own model, so `.travis.yml` is rewritten, not imported |
| Factory -> Codex CLI | Different product shape; the CLI is free software but model usage is billed by the model provider |
| incident.io -> Keep | Keep describes itself as an AIOps and alert-management platform; compare on-call, status pages and chat workflow with what you actually use |
| Portkey -> LiteLLM | You operate the gateway, keys and logs; verify licence terms for the features you need |
| Kinde -> Better Auth | A TypeScript library you embed, not a hosted service: you own sessions, database and security patches |
| Splunk -> Prometheus | Prometheus covers metrics and alerting; it is not a log-search replacement |
| Read the Docs -> Starlight | A docs framework, not hosting or versioned builds: you add a host and a CI step |
| Intruder -> Nuclei | A scanner and template engine, not a managed service with triage and reporting; scan only systems you own or are authorised to test |
| Socket -> OSV-Scanner | Matches dependencies to known vulnerabilities in the OSV database; it does not claim to judge unknown package behaviour |
| Scout APM -> Pinpoint | Check infrastructure and language-agent requirements in its README before assuming it is cheap to run |
| Descope -> Logto | Self-hosting makes uptime, upgrades and backups yours |
| Compass -> Backstage | A framework that normally needs a team; at $92 a year the paid tool is almost certainly cheaper than the engineer time |

## Decision rule (from `docs/procedures/free-vs-paid-tool-decision.md`)

Count real users; check sync and collaboration needs; weigh portability against missing support; flag compliance-sensitive data; re-run the decision when the business changes shape. Total cost = licence + hosting + hours x hourly cost. **Only swap where no new server has to be run** - in this list, OSV-Scanner, Nuclei (authorised targets), Starlight and Better Auth are the low-ops candidates; Backstage, Keep, Pinpoint and Concourse are not.

## Install (this repo does not install them)

`scripts/batch110-install.sh` offers shallow clones for reading only, one question per repo. Nothing is installed or exposed to the network by this skill.

## Keywords
open source alternatives, self-hosted, Concourse, Codex CLI, Keep, LiteLLM, Better Auth, Prometheus, Starlight, Nuclei, OSV-Scanner, Pinpoint, Logto, Backstage
