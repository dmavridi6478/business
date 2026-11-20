#!/usr/bin/env python3
"""Analyze a Chrome Bookmarks file: counts, folders, duplicates, top domains, loose items.

Usage: python3 analyze.py [path-to-Bookmarks]
"""
from __future__ import annotations
import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

from _common import (
    default_chrome_bookmarks_path,
    load,
    walk_urls,
    walk_urls_from_root,
)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", help="Path to Chrome Bookmarks file")
    p.add_argument("--top-domains", type=int, default=20)
    p.add_argument("--show-loose", action="store_true", help="List every loose URL at root level")
    args = p.parse_args()

    path = Path(args.path) if args.path else default_chrome_bookmarks_path()
    if not path.exists():
        print(f"ERROR: not found: {path}", file=sys.stderr)
        return 1

    data = load(path)
    roots = data.get("roots", {})

    print(f"=== File: {path} ===\n")

    domains: Counter[str] = Counter()
    by_url: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    region_totals: dict[str, int] = {}

    for region in ("bookmark_bar", "other", "synced"):
        if region not in roots:
            continue
        items = list(walk_urls_from_root(roots[region], region))
        region_totals[region] = len(items)
        for folder_path, node in items:
            url = node.get("url", "")
            if url:
                by_url[url].append((folder_path, node))
            try:
                host = (urlparse(url).hostname or "").lower()
            except ValueError:
                host = ""
            if host.startswith("www."):
                host = host[4:]
            if host:
                domains[host] += 1

    total = sum(region_totals.values())
    print(f"=== Totals ===")
    for r, n in region_totals.items():
        print(f"  {r}: {n}")
    print(f"  TOTAL: {total}\n")

    for region in ("bookmark_bar", "other"):
        if region not in roots:
            continue
        print(f"=== {region} top-level structure ===")
        loose_count = 0
        for child in roots[region].get("children", []):
            if child.get("type") == "folder":
                sub = sum(1 for _ in walk_urls(child))
                print(f"  📁 {child.get('name', '?'):30s} ({sub})")
            elif child.get("type") == "url":
                loose_count += 1
        print(f"  └── {loose_count} loose URLs at root\n")

    print(f"=== Top {args.top_domains} domains ===")
    for d, c in domains.most_common(args.top_domains):
        print(f"  {c:4d}  {d}")
    print()

    dups = {u: locs for u, locs in by_url.items() if len(locs) > 1}
    print(f"=== Duplicate URLs ({len(dups)} sets) ===")
    for url, locs in list(dups.items())[:30]:
        print(f"  [{len(locs)}x] {url[:80]}")
        for folder, node in locs:
            print(f"        in [{folder}] {node.get('name', '')[:50]}")
    if len(dups) > 30:
        print(f"  ... and {len(dups) - 30} more")
    print()

    if args.show_loose:
        for region in ("bookmark_bar", "other"):
            if region not in roots:
                continue
            loose = [c for c in roots[region].get("children", []) if c.get("type") == "url"]
            if not loose:
                continue
            print(f"=== {region} loose URLs ({len(loose)}) ===")
            for c in loose:
                print(f"  id={str(c.get('id', '?')):>5s}  {c.get('name', '')[:55]}")
                print(f"          {c.get('url', '')[:90]}")
            print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
