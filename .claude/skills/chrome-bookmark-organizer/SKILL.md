---
name: chrome-bookmark-organizer
description: Reorganize a user's Chrome (or any Chromium-based browser) bookmarks via AI categorization. Reads the local Bookmarks JSON file, proposes a category plan, applies it after confirmation. Handles duplicate detection, cross-region moves, and the Chrome Sync gotcha. Trigger when the user asks to "organize / clean up / categorize / 整理 my Chrome bookmarks", or any equivalent request that involves restructuring browser bookmarks at scale.
---

# Chrome Bookmark Organizer

You help the user reorganize their Chrome bookmarks by analyzing the local file, proposing a categorization, and applying it after review. The user keeps full control: every destructive action (delete, merge, cross-region move) requires explicit confirmation.

## Critical pre-flight

1. **Chrome must be closed.** Check with `pgrep -x "Google Chrome"`. If running, ask user to fully quit (⌘+Q on macOS, not just close window).
2. **Sync warning.** Read `~/Library/Application Support/Google/Chrome/Local State` and check `profile.info_cache.<profile>.user_name`. If non-empty, Chrome is signed in and likely syncing. Tell the user: changes to the local file will be **silently overwritten by cloud sync** when Chrome reopens. They MUST disable sync first via `chrome://settings/syncSetup` → "Turn off". After applying changes, they re-enable sync and pick "merge / keep local data" to push the new structure to cloud. Full guide in `docs/chrome-sync.md`.
3. **Backup.** Before any modification, copy the Bookmarks file with a timestamped suffix: `cp Bookmarks Bookmarks.backup-$(date +%Y%m%d-%H%M%S)`. Keep the backup; do not delete it without explicit user permission.

## Bookmark file paths

| OS | Path |
|---|---|
| macOS | `~/Library/Application Support/Google/Chrome/Default/Bookmarks` |
| Linux | `~/.config/google-chrome/Default/Bookmarks` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks` |

User may have multiple profiles (`Profile 1`, `Profile 2`, etc.). If `Default` looks empty (<1KB), ask which profile is the active one. For Edge/Brave, the path differs but the JSON schema is identical.

## Workflow

### 1. Analyze
Run `python3 analyze.py <path>` (no path → uses platform default). This dumps:
- Total counts per region (`bookmark_bar`, `other`, `synced`)
- Existing top-level folders with item counts
- Top domains
- Duplicate URL sets
- (with `--show-loose`) every loose URL at root with id and full URL

Skim the output to understand the user's existing structure. **Reuse their existing folder names** wherever sensible — don't impose a new taxonomy on top of their organization.

### 2. Propose a plan
Build a categorization proposal as a Markdown table for the user. Group by:
- **Duplicates to delete** (table: id / name / reason for picking the kept one)
- **Misplaced items to move** (currently in wrong folder)
- **Loose items → existing folders** (reuse user's structure)
- **Loose items → new folders** (create when no existing folder fits ≥3 items)
- **Cross-region moves** (e.g. `other` item that semantically belongs in a `bookmark_bar` folder)

Highlight uncertain items separately and ask before deciding. **Conservative bias**: when in doubt, leave it alone.

### 3. Confirm
Wait for user approval. Process amendments interactively. Do **not** generate the plan JSON or run apply.py until the user explicitly approves.

### 4. Build plan JSON
Format:
```json
{
  "delete_ids": ["1234", "5678"],
  "create_folders": [{"path": "other/AI Tools"}, {"path": "other/Reading"}],
  "moves": [
    {"id": "9012", "to_path": "other/AI Tools"},
    {"id": "3456", "to_path": "bookmark_bar/Work"}
  ]
}
```

`to_path` is slash-separated, starting with the root name (`bookmark_bar`, `other`, or `synced`). Folders in the path that don't exist are auto-created during `apply.py` execution, so you don't need a separate `create_folders` entry for paths that `moves` will create — but include them when you want to create empty folders for future use.

Save plan to a temp path. Show the user the plan before running apply.

### 5. Apply
Run `python3 apply.py <bookmarks-path> <plan-path> --in-place`. The `--in-place` flag creates an auto-backup and overwrites the file. Or omit `--in-place` and write to `Bookmarks.new`, then have user inspect before manual replacement.

**Check the exit code — it is the contract:**

| Code | Meaning | What to do |
|---|---|---|
| 0 | Everything applied | Proceed to verify |
| 2 | Some plan entries failed — **nothing was written** | Read the errors, fix the plan, re-run. Do not pass `--allow-partial` unless the user explicitly accepts a partial apply. |
| 3 | Internal safety check tripped (nodes would be lost) | Stop. Report it as a bug; the file is untouched. |

Common causes of exit 2: an id listed twice in `delete_ids`/`moves`; a `to_path` that doesn't start with a root key (`bookmark_bar`/`other`/`synced`); moving a folder into itself or its own descendant.

### 6. Verify
Re-run `analyze.py` on the modified file to confirm: counts add up, duplicates gone, new folders populated, no orphans. Show the user a one-screen summary.

### 7. Hand off
Tell the user:
1. Open Chrome and inspect the result.
2. If satisfied, re-enable sync and choose "merge / keep my local data" — **never** "use cloud version" or all the work gets reverted.
3. If unsatisfied, restore from backup: `cp <backup-file> Bookmarks` (Chrome must be closed first).

## Implementation notes (for the AI assistant)

- Always strip the `checksum` field — `apply.py` does this automatically. Chrome regenerates on next launch.
- Output JSON in compact form (no indent). `apply.py` does this automatically.
- IDs are stable across edits; **prefer id-based addressing** in the plan over URL or name (URLs duplicate, names collide).
- Never list the same id twice in `delete_ids` or `moves` — `apply.py` rejects the plan rather than guess the intent.
- `analyze.py` prints folder paths using root **keys** (`other/AI Tools`), the same form `to_path` expects, so paths can be copied straight from its output.
- Empty folders the user already has (e.g. `New folder`) — leave them alone unless asked.
- Folders with garbled-zero-width-character names (Feishu/Lark docs sometimes embed these) — preserve verbatim; renaming risks breaking deep links the user remembers by URL.
- For deduplication, prefer keeping the URL with the more specific path over the bare-domain version.
- The user's instructions (CLAUDE.md style) override defaults: if they say "don't merge X and Y", respect that even if the rule seems obvious.
