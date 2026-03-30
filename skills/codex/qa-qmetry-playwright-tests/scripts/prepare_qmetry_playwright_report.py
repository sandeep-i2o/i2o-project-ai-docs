#!/usr/bin/env python3
"""Validate QMetry report directory and generate a Playwright execution report."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys
from typing import Any


@dataclass
class Summary:
    total: int
    passed: int
    failed: int
    skipped: int


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be >= 0")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate qmetery report folder and write a markdown report."
    )
    parser.add_argument("--docs-root", required=True, help="Path to i2o-ai-project-docs root")
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--qmetry-link", required=True)
    parser.add_argument("--results-json", help="Playwright JSON report path")
    parser.add_argument("--total", type=positive_int)
    parser.add_argument("--passed", type=positive_int)
    parser.add_argument("--failed", type=positive_int)
    parser.add_argument("--skipped", type=positive_int)
    parser.add_argument("--test-url", default="", help="Execution test URL")
    parser.add_argument("--test-username", default="", help="Execution test username")
    parser.add_argument(
        "--credentials-file",
        default="",
        help="Path to .config/credentials.json used for execution",
    )
    parser.add_argument(
        "--test-file",
        action="append",
        default=[],
        help="Generated test file path (repeat flag for multiple files)",
    )
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        help="Execution artifact path (repeat flag for multiple paths)",
    )
    parser.add_argument("--command", default="", help="Executed Playwright command")
    parser.add_argument("--output-file", help="Optional explicit output report path")
    parser.add_argument("--dry-run", action="store_true", help="Validate only, do not write")
    return parser.parse_args()


def extract_summary_from_json(json_path: Path) -> Summary | None:
    if not json_path.exists():
        raise FileNotFoundError(f"results json not found: {json_path}")

    payload: Any = json.loads(json_path.read_text(encoding="utf-8"))
    stats = payload.get("stats", {}) if isinstance(payload, dict) else {}

    if not isinstance(stats, dict):
        return None

    passed = int(stats.get("expected", 0) or 0)
    failed = int(stats.get("unexpected", 0) or 0)
    failed += int(stats.get("flaky", 0) or 0)
    skipped = int(stats.get("skipped", 0) or 0)
    total = int(stats.get("total", 0) or 0)

    if total == 0:
        total = passed + failed + skipped

    return Summary(total=total, passed=passed, failed=failed, skipped=skipped)


def resolve_summary(args: argparse.Namespace) -> Summary:
    from_json: Summary | None = None
    if args.results_json:
        from_json = extract_summary_from_json(Path(args.results_json))

    total = args.total if args.total is not None else (from_json.total if from_json else 0)
    passed = args.passed if args.passed is not None else (from_json.passed if from_json else 0)
    failed = args.failed if args.failed is not None else (from_json.failed if from_json else 0)
    skipped = args.skipped if args.skipped is not None else (from_json.skipped if from_json else 0)

    if total < passed + failed + skipped:
        raise ValueError("total cannot be smaller than passed+failed+skipped")

    if total == 0 and (passed or failed or skipped):
        total = passed + failed + skipped

    return Summary(total=total, passed=passed, failed=failed, skipped=skipped)


def resolve_target_dir(docs_root: Path, project_id: str, release_id: str) -> Path:
    return docs_root / project_id / release_id / "tests" / "qmetery-test-reports"


def resolve_report_path(target_dir: Path, output_file: str | None) -> Path:
    if output_file:
        return Path(output_file)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return target_dir / f"qmetry-playwright-report_{timestamp}.md"


def build_report(
    project_id: str,
    release_id: str,
    qmetry_link: str,
    summary: Summary,
    command: str,
    test_files: list[str],
    artifacts: list[str],
    test_url: str,
    test_username: str,
    credentials_file: str,
) -> str:
    created_at = datetime.now().isoformat(timespec="seconds")
    test_rows = "\n".join(f"- `{path}`" for path in test_files) if test_files else "- None"
    artifact_rows = "\n".join(f"- `{path}`" for path in artifacts) if artifacts else "- None"
    command_value = f"`{command}`" if command else "Not provided"
    test_url_value = f"`{test_url}`" if test_url else "Not provided"
    test_username_value = f"`{test_username}`" if test_username else "Not provided"
    credentials_file_value = f"`{credentials_file}`" if credentials_file else "Not provided"

    return f"""# QMetry Playwright Execution Report

## Context
- Project ID: `{project_id}`
- Release ID: `{release_id}`
- Created At: `{created_at}`
- QMetry Link: {qmetry_link}

## Execution Environment
- Test URL: {test_url_value}
- Test Username: {test_username_value}
- Credentials File: {credentials_file_value}
- Login First Step: `Mandatory for every generated test case`

## Execution Summary
| Metric | Count |
|---|---:|
| Total | {summary.total} |
| Passed | {summary.passed} |
| Failed | {summary.failed} |
| Skipped | {summary.skipped} |

## Command
{command_value}

## Generated Test Files
{test_rows}

## Artifacts
{artifact_rows}
"""


def main() -> int:
    args = parse_args()

    docs_root = Path(args.docs_root).expanduser().resolve()
    target_dir = resolve_target_dir(docs_root, args.project_id, args.release_id)

    if not target_dir.exists() or not target_dir.is_dir():
        print(
            "ERROR: report directory not found. Expected: "
            f"{target_dir}",
            file=sys.stderr,
        )
        return 2

    summary = resolve_summary(args)
    report_path = resolve_report_path(target_dir, args.output_file)

    if args.dry_run:
        print(f"OK: report directory exists: {target_dir}")
        print(f"OK: report would be written to: {report_path}")
        return 0

    report_body = build_report(
        project_id=args.project_id,
        release_id=args.release_id,
        qmetry_link=args.qmetry_link,
        summary=summary,
        command=args.command,
        test_files=args.test_file,
        artifacts=args.artifact,
        test_url=args.test_url,
        test_username=args.test_username,
        credentials_file=args.credentials_file,
    )

    report_path.write_text(report_body, encoding="utf-8")
    print(report_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
