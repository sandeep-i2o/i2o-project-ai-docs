#!/usr/bin/env python3
"""Discover Spring controller endpoints from Java sources."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MAPPING_RE = re.compile(
    r"@(?P<kind>RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping)\s*(?:\((?P<args>.*)\))?"
)
CLASS_RE = re.compile(r"\bclass\s+\w+")
METHOD_RE = re.compile(r"RequestMethod\.([A-Z]+)")
VALUE_PATH_RE = re.compile(r'(?:value|path)\s*=\s*"([^"]*)"')
QUOTED_RE = re.compile(r'"([^"]*)"')

FIXED_METHODS = {
    "GetMapping": ["GET"],
    "PostMapping": ["POST"],
    "PutMapping": ["PUT"],
    "DeleteMapping": ["DELETE"],
    "PatchMapping": ["PATCH"],
}


def normalize_path(path: str) -> str:
    value = (path or "").strip()
    if not value:
        return "/"
    if not value.startswith("/"):
        value = f"/{value}"
    value = re.sub(r"/{2,}", "/", value)
    return value or "/"


def join_paths(base: str, child: str) -> str:
    base_n = normalize_path(base)
    child_n = normalize_path(child)
    if base_n == "/":
        return child_n
    if child_n == "/":
        return base_n
    return normalize_path(base_n.rstrip("/") + child_n)


def extract_path(args: str | None) -> str:
    if args is None:
        return "/"
    compact = " ".join(args.split())
    match = VALUE_PATH_RE.search(compact)
    if match:
        return match.group(1)
    match = QUOTED_RE.search(compact)
    if match:
        return match.group(1)
    return "/"


def extract_methods(kind: str, args: str | None) -> list[str]:
    if kind in FIXED_METHODS:
        return FIXED_METHODS[kind]
    if not args:
        return ["GET"]
    found = METHOD_RE.findall(args)
    return found or ["GET"]


def discover_from_file(root: Path, source_file: Path) -> list[dict[str, str]]:
    rel = source_file.resolve().relative_to(root.resolve()).as_posix()
    lines = source_file.read_text(encoding="utf-8", errors="ignore").splitlines()

    class_line = len(lines)
    for idx, line in enumerate(lines):
        if CLASS_RE.search(line):
            class_line = idx
            break

    base_path = "/"
    for idx in range(class_line):
        match = MAPPING_RE.search(lines[idx].strip())
        if match and match.group("kind") == "RequestMapping":
            base_path = extract_path(match.group("args"))

    endpoints: list[dict[str, str]] = []
    for idx in range(class_line + 1, len(lines)):
        match = MAPPING_RE.search(lines[idx].strip())
        if not match:
            continue

        kind = match.group("kind")
        args = match.group("args")
        sub_path = extract_path(args)
        methods = extract_methods(kind, args)

        for method in methods:
            endpoints.append(
                {
                    "method": method,
                    "path": join_paths(base_path, sub_path),
                    "source": rel,
                }
            )

    return endpoints


def resolve_sources(root: Path, includes: list[str]) -> list[Path]:
    if includes:
        files = []
        for item in includes:
            candidate = Path(item)
            if not candidate.is_absolute():
                candidate = root / item
            if candidate.exists() and candidate.is_file():
                files.append(candidate)
        return sorted(set(files))

    return sorted(root.glob("src/main/java/**/*Controller.java"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover Spring controller endpoints")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--file",
        action="append",
        default=[],
        help="Specific controller file to parse (repeatable)",
    )
    parser.add_argument(
        "--format",
        choices=("json", "table"),
        default="json",
        help="Output format",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    sources = resolve_sources(root, args.file)

    all_endpoints: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()

    for source in sources:
        for endpoint in discover_from_file(root, source):
            key = (endpoint["method"], endpoint["path"], endpoint["source"])
            if key in seen:
                continue
            seen.add(key)
            all_endpoints.append(endpoint)

    all_endpoints.sort(key=lambda item: (item["path"], item["method"], item["source"]))

    if args.format == "json":
        print(json.dumps(all_endpoints))
    else:
        for item in all_endpoints:
            print(f"{item['method']:<6} {item['path']:<50} {item['source']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
