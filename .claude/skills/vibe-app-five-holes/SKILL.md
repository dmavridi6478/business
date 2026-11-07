---
name: vibe-app-five-holes
description: The five security holes in a vibe-coded app from the @vibe.worker carousel "5 ways your vibe-coded app will get hacked" - keys in the frontend, an open database (Supabase tables without row level security), hidden buttons, no rate limits and a .env committed to GitHub - with each fix, how to check it, what the slide leaves out (rotate leaked keys, test as another user) and a paste-ready agent prompt. Use when launching or reviewing an app built with an AI coding tool, or before publishing a repo.
---

# Five holes in a vibe-coded app

Source: a six-slide @vibe.worker carousel (cover, five holes, closing "Have an agent check all 5 for you ... Save this before you launch"). The five holes and one-line fixes below are the slides'. Checks, the extra rules and the prompt are my additions; none of this was run against a real app.

| # | Hole (slide) | Slide fix | How to check (my addition) |
|---|---|---|---|
| 1 | Keys in your frontend: anyone can open DevTools and copy your OpenAI key | Keep them on the server | Search the built bundle and network tab for key strings; call the provider only from a server route. A key already shipped is burned: rotate it |
| 2 | An open database: Supabase tables without row level security can be read by anyone | Turn it on for each table | List tables with RLS off; for each, add policies; then test by calling the API as a different user and as an anonymous user |
| 3 | Hidden buttons: hiding the admin button stops nobody, anyone can call your API directly | Check access on the server | For every admin or write endpoint, confirm the server checks the role; call it with a normal user's token |
| 4 | No rate limits: bots can hammer your AI feature and run up your bill overnight | Limit calls per user | Add a per-user and per-IP limit and a spending cap or alert at the model provider |
| 5 | .env on GitHub: bots scan public repos for keys; deleting the file is not enough | `.gitignore` it, then new keys | Check history, not just the current tree; the leaked keys must be replaced, and history may need cleaning |

## Rules I would add

- Treat any secret that was ever public as compromised: rotate first, clean later.
- Never test other people's apps. Check only your own.
- Do not paste real keys into a chat or a prompt; give the agent the file paths, not the values.
- The slide's "agent check" shows a sample report from a workspace app (Omniscio). The report was illustrative; no product claim is taken from it.

## Paste-ready prompt

```
Audit this app for five issues, read-only, and do not change anything until I approve:
1. Secrets or API keys reachable from the frontend bundle or committed to git (including history).
2. Database tables or storage buckets readable without authentication (for Supabase: row level security off).
3. Admin or write endpoints that rely on hidden UI instead of a server-side role check.
4. AI or expensive endpoints with no per-user rate limit or spending cap.
5. A .env file or other secrets tracked in git, and whether .gitignore covers them.
For each: file and line, how an outsider could abuse it, the smallest fix, and how I verify the fix. Never print secret values; show only the first four characters. List what you could not check.
```

Use `/vibe-check [path or description]`. Related: `security-review`, `secrets-management`, `postgres-patterns`, `security-scanners-five`.
