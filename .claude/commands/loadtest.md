---
description: Plan and (with confirmation) run a small, safe HTTP load test with rakyll/hey against a URL you own, then summarise latency percentiles and errors.
argument-hint: <url> [requests=200] [concurrency=10]
---

Load test target: $1 · requests: $2 (use 200 if empty) · concurrency: $3 (use 10 if empty)

Safety first — do these before anything else:
1. **Ownership gate.** Load-testing a site you do not own or have written permission to test is abuse. Ask me to confirm in one line that I own or am authorised to test `$1`. If I cannot confirm, stop.
2. Refuse if the target is a third-party SaaS, a government site, or a production system without a stated maintenance window. Prefer a staging URL.
3. Cap the first run at ≤ 200 requests and ≤ 10 workers. Only raise it step by step (×2) while error rate stays under 1% and I agree.

Then:
4. Check `hey` is installed (`command -v hey`). If not, tell me the install line from `scripts/batch98-install.sh` — do not install anything yourself.
5. Show me the exact command first, e.g. `hey -n 200 -c 10 -t 10 "$1"`, and wait for my "go".
6. Run it, then report: requests/sec, p50/p90/p99 latency, status-code distribution, error count, and one sentence on whether the numbers are healthy for this kind of page.
7. Add `-h2` only if I ask for HTTP/2. Never use `-z` (duration) above 30s without asking.
