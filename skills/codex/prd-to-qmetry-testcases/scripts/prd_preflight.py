#!/usr/bin/env python3
"""Preflight checks for PRD-to-QMetry workflow.

Validates repo clone, branch existence, PRD location, and user story presence.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/sandeep-i2o/i2o-project-ai-docs/"
EXIT_OK = 0
EXIT_BRANCH_MISSING = 2
EXIT_PRD_MISSING = 3
EXIT_NO_USER_STORIES = 4
EXIT_TOOL_ERROR = 5


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
        check=False,
    )


def ensure_repo(repo_dir: Path) -> None:
    if repo_dir.exists():
        return
    clone = run(["git", "clone", REPO_URL, str(repo_dir)])
    if clone.returncode != 0:
        raise RuntimeError(f"git clone failed: {clone.stderr.strip()}")


def branch_exists(repo_dir: Path, branch: str) -> bool:
    remote = run(["git", "-C", str(repo_dir), "ls-remote", "--heads", "origin", branch])
    if remote.returncode != 0:
        raise RuntimeError(f"git ls-remote failed: {remote.stderr.strip()}")
    return bool(remote.stdout.strip())


def checkout_branch(repo_dir: Path, branch: str) -> None:
    fetch = run(["git", "-C", str(repo_dir), "fetch", "origin", branch])
    if fetch.returncode != 0:
        raise RuntimeError(f"git fetch failed: {fetch.stderr.strip()}")

    checkout = run(["git", "-C", str(repo_dir), "checkout", branch])
    if checkout.returncode != 0:
        create = run(["git", "-C", str(repo_dir), "checkout", "-b", branch, f"origin/{branch}"])
        if create.returncode != 0:
            raise RuntimeError(
                "git checkout failed: "
                f"{checkout.stderr.strip()} | create branch failed: {create.stderr.strip()}"
            )


def count_user_story_lines(prd_text: str) -> int:
    patterns = [
        r"(?im)^\s*#{1,6}\s*user\s*stor(?:y|ies)\b",
        r"(?im)^\s*(?:-|\*|\d+\.)\s*(?:us[-_\s]*\d+|user\s*story\b)",
        r"(?im)^\s*as\s+a[n]?\s+.+\bi\s+want\s+.+\bso\s+that\b",
    ]
    total = 0
    for pattern in patterns:
        total += len(re.findall(pattern, prd_text))
    return total


def build_prd_path(repo_dir: Path, project_name: str, release_version: str) -> Path:
    return (
        repo_dir
        / "projects"
        / project_name
        / release_version
        / "docs"
        / "requirements"
        / "prd.md"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run PRD preflight checks for QMetry test case generation.")
    parser.add_argument("--module", required=True, help="Module name. Expected to match branch name.")
    parser.add_argument("--project-name", required=True, help="Project name under projects/ directory.")
    parser.add_argument("--release-version", required=True, help="Release version folder.")
    parser.add_argument(
        "--repo-dir",
        default="i2o-project-ai-docs",
        help="Local repository path (default: ./i2o-project-ai-docs).",
    )
    return parser.parse_args()


def emit(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main() -> int:
    args = parse_args()
    repo_dir = Path(args.repo_dir).resolve()

    try:
        ensure_repo(repo_dir)
        if not branch_exists(repo_dir, args.module):
            emit(
                {
                    "status": "branch_missing",
                    "module": args.module,
                    "message": "Provided module branch is not present in origin. Ask user for branch name.",
                }
            )
            return EXIT_BRANCH_MISSING

        checkout_branch(repo_dir, args.module)
    except RuntimeError as err:
        emit({"status": "tool_error", "message": str(err)})
        return EXIT_TOOL_ERROR

    prd_path = build_prd_path(repo_dir, args.project_name, args.release_version)
    if not prd_path.exists():
        emit(
            {
                "status": "prd_missing",
                "prd_path": str(prd_path),
                "message": "PRD file not found at required path.",
            }
        )
        return EXIT_PRD_MISSING

    prd_text = prd_path.read_text(encoding="utf-8", errors="ignore")
    story_count = count_user_story_lines(prd_text)
    if story_count == 0:
        emit(
            {
                "status": "no_user_stories",
                "prd_path": str(prd_path),
                "message": "User stories are not present in the document.",
            }
        )
        return EXIT_NO_USER_STORIES

    emit(
        {
            "status": "ok",
            "module": args.module,
            "project_name": args.project_name,
            "release_version": args.release_version,
            "repo_dir": str(repo_dir),
            "prd_path": str(prd_path),
            "user_story_signals": story_count,
        }
    )
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
