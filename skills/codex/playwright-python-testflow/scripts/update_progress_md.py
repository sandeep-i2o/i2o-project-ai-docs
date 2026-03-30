#!/usr/bin/env python3
"""Append a QA automation entry to progress.md without overwriting history."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

SECTION_HEADER = "## QA Automation Updates"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--progress-file", type=Path, required=True)
    parser.add_argument("--ticket-id", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--release", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--prd-path", required=True)
    parser.add_argument("--report-file", required=True)
    parser.add_argument("--tests-generated", type=int, required=True)
    parser.add_argument("--tests-passed", type=int, required=True)
    parser.add_argument("--tests-failed", type=int, required=True)
    parser.add_argument("--tests-skipped", type=int, required=True)
    parser.add_argument("--tests-errors", type=int, required=True)
    return parser.parse_args()


def build_entry(args: argparse.Namespace) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    status = "PASS" if (args.tests_failed == 0 and args.tests_errors == 0) else "FAIL"
    return (
        f"### {now} - {args.ticket_id} Playwright Automation\n"
        f"- Project/Release: `{args.project}/{args.release}`\n"
        f"- Branch: `{args.branch}`\n"
        f"- PRD: `{args.prd_path}`\n"
        f"- Report: `{args.report_file}`\n"
        f"- Generated Tests: {args.tests_generated}\n"
        f"- Execution: status={status}, passed={args.tests_passed}, "
        f"failed={args.tests_failed}, skipped={args.tests_skipped}, errors={args.tests_errors}\n\n"
    )


def main() -> int:
    args = parse_args()
    path = args.progress_file

    if not path.exists():
        raise SystemExit(f"progress.md not found: {path}")

    content = path.read_text(encoding="utf-8")
    entry = build_entry(args)

    if SECTION_HEADER not in content:
        if not content.endswith("\n"):
            content += "\n"
        content += f"\n{SECTION_HEADER}\n\n"

    updated = content
    if not updated.endswith("\n"):
        updated += "\n"
    updated += entry

    path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
