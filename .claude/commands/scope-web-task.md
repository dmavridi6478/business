Scope a browser-automation/web-agent task before running it, using the `web-task-scoping` skill's Target/Limit/Run/Review discipline.

Given the task described in "$ARGUMENTS" (or, if empty, ask the user what web task they want automated):

1. **Target** — identify the single permitted site/domain (or fixed allowlist). If the request implies "the web" broadly, push back and ask for a specific site.
2. **Limit** — state the one measurable outcome the run should produce, and what's explicitly out of bounds (spend caps, no-send, no-delete, read-only unless stated otherwise).
3. **Run** — identify whether a test/sandbox account is available for this site. If not, flag that a first run should not use a production or personally-identifying account.
4. **Review** — define the approval checkpoint: what gets shown to the user before the agent is allowed to act with more autonomy (e.g. before any side-effecting submit).

Output the four elements as a short scoped brief, then:
- If the task is read-only (checking a page, extracting data, screenshotting), note that only Target and Limit are strictly required per the skill, and proceed once those two are clear.
- If the task has side effects (filling forms, submitting, purchasing, posting, deleting, changing settings), do not proceed until all four elements are explicit and the user has confirmed the Review checkpoint.
- If choosing a browser-automation framework is part of the ask, point to `claude-code-tooling`'s five-framework table (Playwright MCP, Stagehand, Skyvern, Magentic-UI, Steel Browser) and recommend one based on the job's shape (structured tools vs. natural-language flexibility vs. visual understanding vs. human-in-the-loop vs. durable remote sessions) — don't default to the same one every time.

Refuse to skip straight to execution on a side-effecting web task without stating the four elements first — that's the entire point of this command.
