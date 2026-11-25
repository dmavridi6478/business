---
name: security-scanners-five
description: Checked map of the five open-source security scanners in the @cyberwithjohann video "5 GitHub Repositories to Find Security Problems in Code" - Gitleaks (secrets in git), TruffleHog (secrets, with live validation), Trivy (containers, packages, configs), Semgrep (insecure code patterns) and Prowler (cloud misconfiguration) - with commands, licences read from each repo, the order to run them, and the cautions the video omits (TruffleHog validation calls real services, Trivy's March 2026 supply-chain compromise, Semgrep metrics, cloud credentials). Use when choosing a scanner for a target, setting up scanning, or reviewing what these tools send and need.
---

# Five scanners, one job each

Source: a 48-second video with five repo screens and a "save these repositories" list. The screens show illustrative output (for example "Leaks found 3", "12 known CVEs"), not a real scan. Checked 7 November 2026: repos exist; licences and commands read from each repo's own README or licence file. Scan only code, images and accounts you own or are authorised to test.

| # | Repo | Finds | Video command | Licence (read) |
|---|---|---|---|---|
| 1 | `gitleaks/gitleaks` | Secrets committed to git | `gitleaks git -v` | MIT |
| 2 | `trufflesecurity/trufflehog` | Secrets across git, chats, wikis, buckets and more; classifies 800+ types and can check if a secret is live | `trufflehog git file://.` | **AGPL-3.0** |
| 3 | `aquasecurity/trivy` | Known CVEs, misconfigurations, secrets and licences in images, filesystems, repos, VM images and Kubernetes | `trivy image app:latest` | Apache-2.0 |
| 4 | `semgrep/semgrep` | Insecure code patterns, with rules written like code | `semgrep scan` | **LGPL-2.1** |
| 5 | `prowler-cloud/prowler` | Cloud misconfiguration and compliance gaps | `prowler a...` (cut off in the video; the README form is `prowler <provider>`, so `prowler aws` is my reading) | Apache-2.0 |

## Which to run on what

| Target | First choice | Also |
|---|---|---|
| A git repo before you push | Gitleaks (`gitleaks git -v`; its README documents `--redact`, `--baseline-path` and a pre-commit hook) | TruffleHog on a repo you own |
| A repo's history for old leaks | TruffleHog | Gitleaks with a baseline for the known ones |
| A container image or project folder | Trivy (`trivy image ...`, or `trivy fs --scanners vuln,secret,misconfig <dir>`) | |
| Application source | Semgrep (`semgrep scan`) | `sast-configuration` for rule setup |
| A cloud account | Prowler (`prowler <provider>`, list checks with `--list-checks`) | Trivy for the images that run there |

Suggested order for a project: Gitleaks, then Trivy on the folder and image, then Semgrep, then Prowler on the cloud account, and TruffleHog on history when you need to know whether a leaked key is still live.

## Cautions the video leaves out

1. **TruffleHog's validation uses the secret.** Its README says that for every classified secret it can log in to confirm the secret is live, and the "verified" results come from that step. That sends the found credential to the real service. Run it only where you are entitled to test those credentials. The README's examples filter with `--results=verified` or `--results=verified,unknown`; check `trufflehog --help` for the switch that skips validation (not in the README I read). It is **AGPL-3.0**: running a modified copy as a network service means offering its source.
2. **Trivy had a supply-chain compromise in March 2026.** Reports from Aqua, Snyk and Wiz say attackers published a malicious Trivy binary (v0.69.4) and rewrote tags on the `trivy-action` and `setup-trivy` GitHub Actions with a credential stealer, tracked as CVE-2026-33634. The sources disagree on tag counts. Pin the binary and any Action to a full commit SHA or a verified release, and check workflow runs from 19 to 20 March 2026 if you used tags then. I did not check the current state of the releases.
3. **Semgrep reports metrics.** Its README says remote registry configs such as `--config=p/ci` send pseudonymous rule metrics to semgrep.dev, and `--metrics=off` disables that. Logging in (`semgrep login`) is optional. The engine is LGPL-2.1; the platform's 20,000+ rules are proprietary, and I did not check the licence of the community registry rules.
4. **Prowler needs cloud credentials.** Use a read-only role, and review the account before running. Prowler Cloud is a paid service; the CLI and the self-hosted app are Apache-2.0.
5. **Scanners find; they do not fix.** A clean run is not proof of safety, and a leaked key stays leaked until rotated.

## Already in this repo

`sast-configuration` (Semgrep setup), `secrets-management`, `security-scan`, `security-review`, `agent-output-scanners`, the commands `/security-sast` and `/security-hardening`, and a `.gitleaksignore` file. This skill adds the five-tool map and the cautions; it does not replace them.

## Use

`/scanner-pick [target]` chooses scanners for a target and lists the commands, credentials and approvals needed. It runs nothing.
