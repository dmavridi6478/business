# Batch 115 prompts (plain text; replace [brackets])

## 1. Pick an automation tier (`/automation-tier`)
I need [TASK] to run [FREQUENCY]. It must survive [terminal closing / a restart / my laptop being off]. Pick Claude Code Tier 1 (/loop), Tier 2 (Desktop scheduled task) or Tier 3 (cloud routine) and say why. Name the trigger (schedule, GitHub event or API). Write the routine prompt so it is self-contained: repo, goal, definition of done, what not to touch, and what to post where. List the permissions it needs and mark anything that sends, spends or deletes as needing my approval. Do not schedule anything.

## 2. Loop with a goal
/loop 5m [TASK, for example process the support queue] /goal don't stop until [CHECKABLE CONDITION, for example the queue is empty]. Stop after [N] iterations or [BUDGET] and report what is left. Never disable a test or skip an item to meet the goal.

## 3. Three cloud routines that pay for themselves
Morning briefing: every weekday at 07:00, list issues opened overnight in [REPO], classify severity, post a summary to [SLACK CHANNEL].
PR review pass: when a pull request is opened in [REPO], leave a first-pass review comment flagging security and style issues; do not approve or merge.
Doc drift: every Monday, find docs not updated alongside code changes in [REPO] and open a draft PR with the fixes on a claude/ branch.

## 4. Permission rules
Always allow: reading files, running tests, git status. Never allow: force push, deleting everything, editing .env. Everything else: ask. Cheap to undo = allow; expensive to undo = never.

## 5. Token-saver claim check (`/token-saver-check`)
Evaluate [TOOL OR REPO] from its README and source. List what it changes in my prompts or tool results, what it sends to third parties, whether it sits in the network path, how compression could drop a needed detail, whether it breaks prompt caching, and one known-answer test on a throwaway repo. Verdict: adopt, trial, or skip. Install nothing.

## 6. Where do my tokens go (measure first)
Look at this session's context. List the five largest contributors (CLAUDE.md, MCP tool schemas, files re-read, long tool outputs, conversation history), estimate each as a share, and propose the three cheapest fixes that need no new software.

## 7. Operational excellence stage score (`/opex-stage`)
For [PROCESS OR TEAM] score Standardise, Measure, Improve, Automate and Innovate 0 (absent), 1 (partial), 2 (in place) with one line of evidence each; say "no evidence" instead of guessing. Name the binding constraint, the single artefact to produce next with an owner, and the "ready to move on" test.

## 8. Explain by building (anatomy-style)
Explain [CONCEPT] as one self-contained HTML page: an interactive diagram where each part is a labelled shape, hovering a part shows what it does, and a step button walks one request through the system. End with a three-sentence summary.

## 9. Vet an open-source repo (`/oss-repo-vet`)
For [OWNER/REPO] check from README, LICENSE and recent commits: what it does, licence and what it means if I host it for others, activity, install method (flag any piped installer), what data or credentials it touches, what it needs to run. Verdict: clone, trial in a container, or skip. Clone nothing.
