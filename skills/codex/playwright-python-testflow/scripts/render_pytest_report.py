#!/usr/bin/env python3
"""Render a concise Markdown execution report from a pytest JUnit XML artifact."""

from __future__ import annotations

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


def _iter_suites(root: ET.Element):
    if root.tag == "testsuite":
        yield root
    elif root.tag == "testsuites":
        for child in root:
            if child.tag == "testsuite":
                yield child


def parse_junit(junit_xml: Path) -> dict:
    root = ET.parse(junit_xml).getroot()

    total = failures = errors = skipped = 0
    duration = 0.0
    failed_cases: list[tuple[str, str, str]] = []

    for suite in _iter_suites(root):
        total += int(suite.attrib.get("tests", 0))
        failures += int(suite.attrib.get("failures", 0))
        errors += int(suite.attrib.get("errors", 0))
        skipped += int(suite.attrib.get("skipped", 0))
        duration += float(suite.attrib.get("time", 0.0))

        for case in suite.findall("testcase"):
            case_name = case.attrib.get("name", "unknown")
            class_name = case.attrib.get("classname", "")
            label = f"{class_name}::{case_name}" if class_name else case_name

            failure = case.find("failure")
            error = case.find("error")
            if failure is not None:
                message = (failure.attrib.get("message") or failure.text or "failure").strip()
                failed_cases.append((label, "failure", message.replace("\n", " ")[:400]))
            elif error is not None:
                message = (error.attrib.get("message") or error.text or "error").strip()
                failed_cases.append((label, "error", message.replace("\n", " ")[:400]))

    passed = max(total - failures - errors - skipped, 0)
    status = "PASS" if failures == 0 and errors == 0 else "FAIL"

    return {
        "total": total,
        "passed": passed,
        "failures": failures,
        "errors": errors,
        "skipped": skipped,
        "duration": round(duration, 3),
        "status": status,
        "failed_cases": failed_cases,
    }


def write_report(args: argparse.Namespace, summary: dict) -> None:
    test_files = args.test_file or []
    tf_lines = [f"- `{p}`" for p in test_files] or ["- (not supplied)"]

    failure_lines = [
        f"- `{name}` ({kind}): {msg}"
        for name, kind, msg in summary["failed_cases"]
    ] or ["- None"]

    lines = [
        "# Playwright Execution Report",
        "",
        "## Context",
        f"- Ticket: `{args.ticket_id}`",
        f"- Project: `{args.project}`",
        f"- Release: `{args.release}`",
        f"- Branch: `{args.branch}`",
        f"- PRD: `{args.prd_path}`",
        f"- JUnit XML: `{args.junit_xml}`",
        "",
        "## Generated Test Files",
        *tf_lines,
        "",
        "## Summary",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Status | {summary['status']} |",
        f"| Total | {summary['total']} |",
        f"| Passed | {summary['passed']} |",
        f"| Failed | {summary['failures']} |",
        f"| Errors | {summary['errors']} |",
        f"| Skipped | {summary['skipped']} |",
        f"| Duration (s) | {summary['duration']} |",
        "",
        "## Failures And Errors",
        *failure_lines,
        "",
    ]

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--junit-xml", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    parser.add_argument("--ticket-id", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--release", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--prd-path", required=True)
    parser.add_argument("--test-file", action="append", default=[])
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.junit_xml.exists():
        parser.error(f"JUnit XML not found: {args.junit_xml}")

    summary = parse_junit(args.junit_xml)
    write_report(args, summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
