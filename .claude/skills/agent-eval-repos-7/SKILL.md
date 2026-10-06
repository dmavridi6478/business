---
name: agent-eval-repos-7
description: Seven open-source repos for tracing, evaluating and red-teaming an LLM agent before users do - opik, deepeval, phoenix, inspect_ai, giskard-oss, laminar and openllmetry - verified against their GitHub pages on 6 Oct 2026 (owner, licence, stars, install command), with a decision guide, a minimal first test for each, and a scorecard procedure. Use when shipping or auditing an agent and you need observability and evals; complements agent-eval, eval-harness and agent-introspection-debugging.
---

# 7 repos that grade your agent

Source: @joshualevi.ai TikTok carousel "Save this and score the agent you shipped last" (7 slides, all legible). Facts below were re-checked on the repos' GitHub pages, not taken from the carousel; star counts move daily.

| # | Repo | What it is | Licence | Stars (Oct 2026) | Install | Pick it when |
|---|---|---|---|---|---|---|
| 1 | `comet-ml/opik` | Tracing for multi-step agents incl. every tool call + LLM-as-judge scoring, dev to production monitoring | Apache-2.0 | ~22.4k | `pip install opik` then `opik configure`; self-host: clone, `./opik.sh` | You want one tool for traces + evals + prompt management |
| 2 | `confident-ai/deepeval` | Evals that read like pytest unit tests; ready metrics for hallucination and custom criteria; works with local models | Apache-2.0 | ~18.7k | `pip install -U deepeval`; run `deepeval test run test_x.py` | You want evals in CI, cheapest path to a first test |
| 3 | `Arize-ai/phoenix` | OpenTelemetry tracing, versioned datasets, experiments, a playground to replay a call against another prompt/model | **Elastic License 2.0** (source-available, not OSI open source) | ~11.7k | `pip install arize-phoenix` then `phoenix serve` (or `uvx arize-phoenix serve`) | You want to replay and compare prompts/models on real traces |
| 4 | `UKGovernmentBEIS/inspect_ai` | Evaluation framework from the UK AI Security Institute; 200+ pre-built evals; solvers, tools, multi-turn, model-graded scoring | MIT | ~2.9k | `pip install inspect-ai` | You need rigorous, reproducible model/agent evals |
| 5 | `Giskard-AI/giskard-oss` | Testing, evaluation and red-teaming for agentic systems; multi-turn; async-first | Apache-2.0 | ~5.9k | `pip install giskard` | You need adversarial tests for failure modes you did not think of |
| 6 | `lmnr-ai/lmnr` | Observability built for agents (YC S24), OpenTelemetry-native, plain-English "signals" (e.g. agent stuck in a loop) that can notify Slack | Apache-2.0 | ~3.3k | self-host: clone, `docker compose up -d` (UI on :5667); SDK `pip install lmnr` | You want to describe a behaviour in English and be pinged when it happens |
| 7 | `traceloop/openllmetry` | Standard OpenTelemetry instrumentation for LLM apps; traces land in the backend you already run | Apache-2.0 | ~7.5k | `pip install traceloop-sdk` | You already have an observability backend |

## Minimal first test for each (verified against repo READMEs unless marked)
- **opik / phoenix / openllmetry / laminar (tracing):** install, point at a project, call your agent once, open the trace. Laminar: `from lmnr import Laminar; Laminar.initialize(project_api_key="<KEY>")`. OpenLLMetry: `from traceloop.sdk import Traceloop; Traceloop.init()`.
- **deepeval:** `GEval(name="Correctness", criteria="...", evaluation_params=[SingleTurnParams.ACTUAL_OUTPUT, SingleTurnParams.EXPECTED_OUTPUT], threshold=0.5)` on an `LLMTestCase(input=..., actual_output=..., expected_output=..., retrieval_context=[...])`, then `assert_test(test_case, [metric])`. Metrics call an LLM judge, so they cost tokens and need a key (or a local model).
- **inspect_ai:** define a `Task(dataset=[Sample(input=..., target=...)], solver=generate(), scorer=match())` and run `inspect eval file.py --model <provider/model>`. [Likely - from the library's documented pattern; confirm against inspect.aisi.org.uk before relying on it.]
- **giskard-oss:** install, then follow its README for the scan/red-team entry point [not verified here].

## Decision guide
1. No tracing yet? Pick **one** tracer: openllmetry if you have a backend, opik or laminar if you want a ready UI, phoenix if replay matters and the Elastic licence is acceptable.
2. Add **deepeval** for regression tests in CI (hallucination, correctness, retrieval).
3. Add **giskard** or **inspect_ai** when you need adversarial or benchmark-grade evaluation.
4. Do not stack all seven. Each judge model call costs money and an LLM judge is itself unreliable - calibrate it against 20+ human-labelled examples before trusting a score.

## Scorecard procedure (`/agent-scorecard`)
For the last agent shipped, score 0-3 on each: traces captured for every tool call; a golden set of 20+ cases; automated hallucination/groundedness check; adversarial/red-team pass; production alert on a named bad behaviour; cost and latency tracked; human review of a weekly sample. Total /21 -> the lowest two lines become the next two tasks. Never report a score without saying what evidence you saw.

## Keywords
LLM evaluation, observability, tracing, red teaming, agent testing, OpenTelemetry, deepeval, opik, phoenix, laminar
