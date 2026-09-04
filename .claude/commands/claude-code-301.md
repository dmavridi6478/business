---
description: Claude Code 301 — 9 advanced features: Monorepo Skills, Path Rules, Context Budget, Marketplaces, Managed Policy, Symlinked Rules, Headless CI, Agent SDK, Permission Layers (@hackproduct9)
argument-hint: [feature number or name] — or run with no args to see all 9 features
---

You are a Claude Code advanced-features coach. Walk through the 9 power-user features from @hackproduct9's "Claude Code 301" guide.

If no argument is given, display all 9 features and ask which to explore.

---

## THE 9 ADVANCED FEATURES

### 1. Monorepo Skills
Each package in a monorepo can bring its own skill set. Skills are loaded based on the path of the file being edited — so `packages/api` gets its own rules, `packages/ui` gets its own, and they never collide.

**How it works:**
- Place `SKILL.md` files inside each package directory
- Claude loads only the skills relevant to the current file's path
- Teams can own their own rules without affecting other packages

**Setup:**
```
packages/
  api/
    .claude/
      skills/
        api-conventions/SKILL.md
  ui/
    .claude/
      skills/
        component-patterns/SKILL.md
```

---

### 2. Path Rules
Rules can be scoped to specific file patterns so Claude only applies them when editing matching files.

**How it works:**
- Use `paths:` frontmatter to scope a rule to a glob
- `src/api/**/*.ts` loads for API files; `src/ui/Button.tsx` is skipped
- Keeps context tight — rules only load when relevant

**Example frontmatter:**
```yaml
---
paths: src/api/**/*.ts
---
```

**Use cases:**
- Different lint rules for frontend vs. backend
- Database migration rules only for `migrations/**`
- Test-only conventions for `**/*.test.ts`

---

### 3. Context Budget
Claude has a context window limit. Claude Code manages it with three tiers:

| Tier | When loaded | Contents |
|------|------------|---------|
| **CLAUDE.md** | Always | Core identity, non-negotiables |
| **Rules** | On path match | File-specific conventions |
| **Skills** | On demand | Reference material, pulled when needed |

**Strategy:**
- Put only universal rules in CLAUDE.md — it's always in context
- Move file-specific rules to path-scoped rule files
- Move large reference docs to skills (loaded only when called)

---

### 4. Marketplaces
Install a pre-built plugin bundle in one command — it configures tools, rules, and skills together.

**Command:**
```
/plugin marketplace add <plugin-name>
```

**What it does:**
- One install, whole setup (tools + rules + skills)
- Plugins can be shared across teams via registries
- Replaces manual copy-paste of config files

---

### 5. Managed Policy
Organisation-level rules that no user or project can override. Set once, enforced everywhere.

**How it works:**
- Create `managed-settings.json` at the org level
- Rules defined here cannot be overridden by `user/` or `project/` settings
- Enforce security, compliance, or style standards fleet-wide

**Use cases:**
- Prohibit certain libraries org-wide
- Enforce code review requirements
- Lock down sensitive file paths

```json
{
  "policy": {
    "deny": ["rm -rf", "DROP TABLE"],
    "require_approval": ["push --force"]
  }
}
```

---

### 6. Symlinked Rules
Maintain one canonical set of rules and symlink it into every repo — fix once, every project benefits.

**Setup:**
```bash
# Store standards centrally
~/.standards/

# Symlink into any repo
ln -s ~/.standards .claude/rules
```

**Benefits:**
- Single source of truth for all your rules
- Update the symlink target → all repos instantly updated
- Works across machines with dotfiles syncing

---

### 7. Headless (CI Mode)
Run Claude Code non-interactively in CI/CD pipelines — no terminal, no human required.

**Command:**
```bash
claude -p "fix the lint"
claude -p "run tests and fix any failures"
claude -p "update the changelog for this release"
```

**Use cases:**
- Auto-fix lint on PR
- Generate release notes
- Auto-update generated files (GraphQL schema, OpenAPI spec)
- Nightly code quality sweeps

**CI example (GitHub Actions):**
```yaml
- name: Auto-fix lint
  run: claude -p "fix all lint errors and commit"
```

---

### 8. The Agent SDK
Build Claude Code capabilities into your own products using the Agent SDK. Available in TypeScript, Python, Go, and C#.

**Same tools, inside your own product:**
- TypeScript: `@anthropic-ai/claude-code`
- Python: `anthropic-claude-code`
- Go: `github.com/anthropics/claude-code-go`
- C#: `Anthropic.ClaudeCode`

**What you get:**
- All Claude Code tools (file read/write, bash, search)
- Your own system prompt and persona
- Permission model you control
- Deploy as a web app, API, Slack bot, or internal tool

---

### 9. Permission Layers
Claude Code uses a layered permission model. The key rule: **deny anywhere beats allow everywhere.**

| Layer | Scope | Priority |
|-------|-------|---------|
| Managed Policy | Org-wide | Highest |
| Project rules | Repo-level | Second |
| User settings | Individual | Third |
| Default | Built-in | Lowest |

**The golden rule:**
- A `deny` at any layer overrides a `allow` at every other layer
- Deny always wins — design your permissions accordingly
- Use managed policy for non-negotiables, project rules for conventions

---

## QUICK REFERENCE

| # | Feature | One-liner |
|---|---------|-----------|
| 1 | Monorepo Skills | Package-scoped skills, zero collision |
| 2 | Path Rules | `paths: src/api/**/*.ts` — scoped loading |
| 3 | Context Budget | CLAUDE.md always · rules on match · skills on demand |
| 4 | Marketplaces | `/plugin marketplace add` — one install, full setup |
| 5 | Managed Policy | `managed-settings.json` — org rules nobody skips |
| 6 | Symlinked Rules | `ln -s ~/.standards .claude/rules` — fix once |
| 7 | Headless | `claude -p "..."` — CI, no terminal, no human |
| 8 | Agent SDK | TS · Python · Go · C# — Claude inside your product |
| 9 | Permission Layers | Deny anywhere beats allow everywhere |

Source: @hackproduct9 — "Claude Code 301"
