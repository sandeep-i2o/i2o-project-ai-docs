#!/usr/bin/env python3
"""Resolve and persist Playwright test environment credentials."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
import sys
from typing import Any

DEFAULT_TEST_URL = "https://qa.i2oretail.com"
DEFAULT_TEST_USERNAME = "agency.user@i2oretail.com"
DEFAULT_TEST_PASSWORD = "I2oretail@123"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or update repo-local .config/credentials.json for Playwright test runs."
    )
    parser.add_argument("--repo-root", required=True, help="Absolute repository root path")
    parser.add_argument("--test-url", help=f"Test URL endpoint (default: {DEFAULT_TEST_URL})")
    parser.add_argument(
        "--test-username",
        help=f"Test username (default: {DEFAULT_TEST_USERNAME})",
    )
    parser.add_argument(
        "--test-password",
        help=f"Test password (default: {DEFAULT_TEST_PASSWORD})",
    )
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Print resolved credentials JSON to stdout (includes password)",
    )
    return parser.parse_args()


def load_existing_credentials(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid json in credentials file: {path}") from exc

    if not isinstance(payload, dict):
        raise ValueError(f"credentials file must contain a JSON object: {path}")

    return payload


def resolve_value(
    cli_value: str | None,
    existing: dict[str, Any],
    key: str,
    default: str,
) -> str:
    if cli_value:
        return cli_value
    existing_value = existing.get(key)
    if isinstance(existing_value, str) and existing_value.strip():
        return existing_value
    return default


def main() -> int:
    args = parse_args()

    repo_root = Path(args.repo_root).expanduser().resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        print(f"ERROR: invalid repo root: {repo_root}", file=sys.stderr)
        return 2

    credentials_path = repo_root / ".config" / "credentials.json"
    existing = load_existing_credentials(credentials_path)

    resolved = {
        "test_url": resolve_value(args.test_url, existing, "test_url", DEFAULT_TEST_URL),
        "test_username": resolve_value(
            args.test_username,
            existing,
            "test_username",
            DEFAULT_TEST_USERNAME,
        ),
        "test_password": resolve_value(
            args.test_password,
            existing,
            "test_password",
            DEFAULT_TEST_PASSWORD,
        ),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }

    credentials_path.parent.mkdir(parents=True, exist_ok=True)
    credentials_path.write_text(
        json.dumps(resolved, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    if args.print_json:
        print(json.dumps(resolved, indent=2, ensure_ascii=True))
        return 0

    masked_password = "*" * len(resolved["test_password"])
    print(f"CREDENTIALS_FILE={credentials_path}")
    print(f"TEST_URL={resolved['test_url']}")
    print(f"TEST_USERNAME={resolved['test_username']}")
    print(f"TEST_PASSWORD_MASKED={masked_password}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
