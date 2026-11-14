"""Shared helpers: Chrome paths, JSON I/O, tree traversal."""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path
from typing import Iterator


def default_chrome_bookmarks_path() -> Path:
    """Return the platform-default Chrome Default profile Bookmarks path."""
    home = Path.home()
    if sys.platform == "darwin":
        return home / "Library/Application Support/Google/Chrome/Default/Bookmarks"
    if sys.platform == "win32":
        local = os.environ.get("LOCALAPPDATA", str(home / "AppData/Local"))
        return Path(local) / "Google/Chrome/User Data/Default/Bookmarks"
    return home / ".config/google-chrome/Default/Bookmarks"


def load(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_compact(path: Path, data: dict) -> None:
    """Write Chrome-compatible compact JSON. Strips checksum so Chrome regenerates it."""
    data.pop("checksum", None)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def walk_urls(node: dict, folder_path: str = "") -> Iterator[tuple[str, dict]]:
    """Yield (folder_path, url_node) for every URL bookmark under node."""
    if not isinstance(node, dict):
        return
    t = node.get("type")
    if t == "folder":
        name = node.get("name", "")
        new_path = f"{folder_path}/{name}" if folder_path else name
        for child in node.get("children", []):
            yield from walk_urls(child, new_path)
    elif t == "url":
        yield folder_path, node


def walk_urls_from_root(root: dict, root_key: str) -> Iterator[tuple[str, dict]]:
    """Like walk_urls, but paths start with the root *key* (bookmark_bar/other/synced)
    instead of the root's display name, so they are usable as plan `to_path` values."""
    for child in root.get("children", []) or []:
        yield from walk_urls(child, root_key)


def is_within(node: dict, ancestor: dict) -> bool:
    """True if node is ancestor itself or lives anywhere under it."""
    if node is ancestor:
        return True
    for c in ancestor.get("children", []) or []:
        if is_within(node, c):
            return True
    return False


def subtree_ids(node: dict) -> set[str]:
    """Every id at or below node."""
    out: set[str] = set()

    def _w(n: dict) -> None:
        if not isinstance(n, dict):
            return
        if n.get("id") is not None:
            out.add(str(n["id"]))
        for c in n.get("children", []) or []:
            _w(c)

    _w(node)
    return out


def detach(node: dict, parent_list: list) -> bool:
    """Remove node from parent_list by identity. False if it was already gone."""
    for i, c in enumerate(parent_list):
        if c is node:
            del parent_list[i]
            return True
    return False


def find_folder(parent: dict, name: str) -> dict | None:
    for c in parent.get("children", []):
        if c.get("type") == "folder" and c.get("name") == name:
            return c
    return None


def collect_max_id(node: dict, acc: list[int]) -> None:
    if isinstance(node, dict):
        v = node.get("id")
        if v is not None:
            try:
                acc.append(int(v))
            except (TypeError, ValueError):
                pass
        for c in node.get("children", []):
            collect_max_id(c, acc)


def index_by_id(data: dict) -> dict[str, tuple[dict, list]]:
    """Return {id: (node, parent_children_list)} for every node with an id."""
    out: dict[str, tuple[dict, list]] = {}

    def _walk(node: dict, parent_list: list | None) -> None:
        if not isinstance(node, dict):
            return
        nid = node.get("id")
        if nid is not None and parent_list is not None:
            out[str(nid)] = (node, parent_list)
        children = node.get("children")
        if isinstance(children, list):
            for c in children:
                _walk(c, children)

    for root_name in ("bookmark_bar", "other", "synced"):
        if root_name in data.get("roots", {}):
            _walk(data["roots"][root_name], None)
    return out
