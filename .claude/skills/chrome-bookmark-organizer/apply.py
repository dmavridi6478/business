#!/usr/bin/env python3
"""Apply a categorization plan to a Chrome Bookmarks file.

Usage: python3 apply.py <bookmarks-path> <plan-path> [--out <output-path>]

Plan JSON schema:
  {
    "delete_ids": ["123", "456"],
    "create_folders": [{"path": "other/AI Tools"}],
    "moves": [{"id": "789", "to_path": "other/AI Tools"}]
  }

Order of operations: deletes -> create_folders -> moves.
"""
from __future__ import annotations
import argparse
import shutil
import sys
import time
import uuid
from pathlib import Path

from _common import (
    collect_max_id,
    detach,
    find_folder,
    index_by_id,
    is_within,
    load,
    save_compact,
    subtree_ids,
)


def make_folder(name: str, fid: str, ts: str) -> dict:
    return {
        "type": "folder",
        "name": name,
        "id": fid,
        "guid": str(uuid.uuid4()),
        "date_added": ts,
        "date_modified": ts,
        "children": [],
    }


def chrome_timestamp() -> str:
    """Chrome WebKit-style timestamp: microseconds since 1601-01-01."""
    epoch_diff = 11644473600
    return str(int((time.time() + epoch_diff) * 1_000_000))


def _deepest_existing(roots: dict, path: str) -> dict | None:
    """Walk `path` as far as it already exists; return the deepest existing folder.
    None if the root key is unknown. Used to validate a move before creating anything."""
    parts = [p for p in path.split("/") if p]
    if not parts or parts[0] not in roots:
        return None
    cur = roots[parts[0]]
    for part in parts[1:]:
        nxt = find_folder(cur, part)
        if nxt is None:
            break
        cur = nxt
    return cur


def ensure_folder(roots: dict, path: str, id_counter: list[int]) -> dict:
    """Resolve path; create missing folders along the way. Returns the leaf folder node."""
    parts = [p for p in path.split("/") if p]
    if not parts:
        raise ValueError(f"empty path: {path!r}")
    if parts[0] not in roots:
        raise ValueError(f"unknown root: {parts[0]!r} (must be bookmark_bar/other/synced)")
    cur = roots[parts[0]]
    ts = chrome_timestamp()
    for part in parts[1:]:
        nxt = find_folder(cur, part)
        if nxt is None:
            id_counter[0] += 1
            nxt = make_folder(part, str(id_counter[0]), ts)
            cur.setdefault("children", []).append(nxt)
        cur = nxt
    return cur


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("bookmarks", help="Path to Bookmarks file")
    p.add_argument("plan", help="Path to plan JSON")
    p.add_argument("--out", help="Output path (default: same as input + .new)")
    p.add_argument("--in-place", action="store_true", help="Overwrite input (auto-backup created)")
    p.add_argument("--allow-partial", action="store_true",
                   help="Write the result even if some plan entries failed (default: abort, write nothing)")
    args = p.parse_args()

    bm_path = Path(args.bookmarks)
    plan_path = Path(args.plan)
    if not bm_path.exists():
        print(f"ERROR: bookmarks not found: {bm_path}", file=sys.stderr)
        return 1
    if not plan_path.exists():
        print(f"ERROR: plan not found: {plan_path}", file=sys.stderr)
        return 1

    data = load(bm_path)
    plan = load(plan_path)
    roots = data["roots"]

    ids: list[int] = []
    for r in ("bookmark_bar", "other", "synced"):
        if r in roots:
            collect_max_id(roots[r], ids)
    id_counter = [max(ids) if ids else 0]

    by_id = index_by_id(data)
    before_ids = set(by_id)
    removed_ids: set[str] = set()

    deletes = list(plan.get("delete_ids", []))
    creates = list(plan.get("create_folders", []))
    moves = list(plan.get("moves", []))

    deleted, created, moved, errors = 0, 0, 0, []

    seen_deletes: set[str] = set()
    for nid in deletes:
        nid = str(nid)
        if nid in seen_deletes:
            errors.append(f"delete: id {nid} listed more than once")
            continue
        seen_deletes.add(nid)
        if nid not in by_id:
            errors.append(f"delete: id {nid} not found")
            continue
        node, parent_list = by_id[nid]
        if not detach(node, parent_list):
            errors.append(f"delete: id {nid} already removed (an ancestor was deleted too)")
            continue
        removed_ids |= subtree_ids(node)
        deleted += 1

    for entry in creates:
        path = entry.get("path") if isinstance(entry, dict) else entry
        if not path:
            errors.append(f"create_folders: missing path in {entry}")
            continue
        try:
            ensure_folder(roots, path, id_counter)
            created += 1
        except ValueError as e:
            errors.append(f"create_folders {path!r}: {e}")

    by_id = index_by_id(data)

    seen_moves: set[str] = set()
    for mv in moves:
        nid = str(mv.get("id", ""))
        to = mv.get("to_path", "")
        if not nid or not to:
            errors.append(f"move: missing id or to_path in {mv}")
            continue
        if nid in seen_moves:
            errors.append(f"move: id {nid} listed more than once")
            continue
        seen_moves.add(nid)
        if nid not in by_id:
            errors.append(f"move: id {nid} not found")
            continue
        node, parent_list = by_id[nid]
        # Reject before creating anything: moving a folder into itself or its own
        # descendant detaches the whole subtree, which json.dump would silently drop.
        existing = _deepest_existing(roots, to)
        if existing is not None and is_within(existing, node):
            errors.append(f"move: id {nid} cannot move into itself or its own descendant ({to!r})")
            continue
        try:
            target = ensure_folder(roots, to, id_counter)
        except ValueError as e:
            errors.append(f"move id={nid} to {to!r}: {e}")
            continue
        if not detach(node, parent_list):
            errors.append(f"move: id {nid} already removed (an ancestor was deleted or moved)")
            continue
        target.setdefault("children", []).append(node)
        by_id[nid] = (node, target["children"])
        moved += 1

    summary = f"{deleted} delete(s), {created} folder(s) created, {moved} move(s)"

    def dump_errors(header: str) -> None:
        print(f"\n{header}", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)

    # Hard invariant: nothing may vanish except what delete_ids removed. Not bypassable.
    lost = before_ids - removed_ids - set(index_by_id(data))
    if lost:
        print(f"ERROR: refusing to write — {len(lost)} node(s) would be lost: "
              f"{', '.join(sorted(lost)[:20])}", file=sys.stderr)
        if errors:
            dump_errors(f"{len(errors)} error(s) also recorded:")
        print("This is a bug in apply.py; the input file is untouched.", file=sys.stderr)
        return 3

    if errors and not args.allow_partial:
        print(f"Aborted: {len(errors)} error(s), nothing written "
              f"(would have applied {summary}).", file=sys.stderr)
        dump_errors("Errors:")
        print("Fix the plan, or pass --allow-partial to write anyway.", file=sys.stderr)
        return 2

    if args.in_place:
        backup = bm_path.with_name(bm_path.name + f".backup-{int(time.time())}")
        shutil.copy2(bm_path, backup)
        print(f"Backup: {backup}")
        out = bm_path
    else:
        out = Path(args.out) if args.out else bm_path.with_name(bm_path.name + ".new")

    save_compact(out, data)

    print(f"Applied: {summary}")
    if errors:
        dump_errors(f"{len(errors)} error(s), written anyway (--allow-partial):")
    print(f"Written: {out}")
    return 2 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
