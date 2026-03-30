#!/usr/bin/env python3
"""Validate a PRD.md against the i2o PRD template and generate prd-validate.md."""

import argparse
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

AMBIGUITY_TERMS = ["TBD", "TBA", "TBC", "TBR", "TBI", "unknown", "to be decided"]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Audit a project/release PRD using the bundled template and produce prd-validate.md."
    )
    parser.add_argument("--project_id", required=True, help="projects/{project_id}")
    parser.add_argument("--release_version", required=True, help="projects/.../{release_version}")
    parser.add_argument(
        "--projects_root",
        default="projects",
        help="Root directory that contains all project folders (defaults to 'projects').",
    )
    parser.add_argument(
        "--report_name",
        default="prd-validate.md",
        help="File name for the generated report in the requirements folder.",
    )
    return parser.parse_args()


def load_template_titles(template_path: Path):
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found at {template_path}")

    titles = []
    for line in template_path.read_text().splitlines():
        stripped = line.strip()
        if not stripped.startswith("title:"):
            continue
        remainder = stripped[len("title:") :].strip()
        if remainder.startswith(("\"", "'")) and len(remainder) > 1:
            remainder = remainder[1:-1]
        remainder = remainder.strip()
        if remainder:
            titles.append(remainder)
    return titles


def uppercase_contains(text: str, substring: str) -> bool:
    return substring.upper() in text.upper()


def find_ambiguous_terms(text: str):
    upper = text.upper()
    hits = []
    for term in AMBIGUITY_TERMS:
        count = upper.count(term.upper())
        if count:
            hits.append((term, count))
    return hits


def write_report(report_path: Path, lines):
    report_path.write_text("\n".join(lines) + "\n")


def main():
    args = parse_args()
    projects_root = Path(args.projects_root)
    prd_path = (
        projects_root
        / args.project_id
        / args.release_version
        / "docs"
        / "requirements"
        / "prd.md"
    )

    if not prd_path.exists():
        print(f"ERROR: PRD not found at {prd_path}")
        sys.exit(1)

    template_path = Path(__file__).resolve().parents[1] / "references" / "i2o-prd-template.yaml"
    try:
        template_titles = load_template_titles(template_path)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)

    prd_text = prd_path.read_text(errors="ignore")
    search_text = re.sub(r"[*>]+", " ", prd_text)
    search_text = re.sub(r"\s+", " ", search_text).strip()

    expected_sections = [title for title in template_titles if title.upper().startswith("SECTION ")]
    b_subsections = [title for title in template_titles if title.startswith("B") and len(title) >= 2 and title[1].isdigit()]
    appendix_subsections = [title for title in template_titles if title.startswith("E")]

    coverage = []
    gaps = []
    for section in sorted(expected_sections):
        found = uppercase_contains(search_text, section)
        coverage.append((section, found))
        if not found:
            gaps.append(f"Missing top-level section '{section}'.")

    b_gaps = []
    for item in sorted(b_subsections):
        found = uppercase_contains(search_text, item)
        coverage.append((item, found))
        if not found:
            b_gaps.append(item)
    if b_gaps:
        gaps.append("Section B detail(s) missing: " + ", ".join(b_gaps))

    appendix_gaps = []
    for item in sorted(appendix_subsections):
        found = uppercase_contains(search_text, item)
        coverage.append((item, found))
        if not found:
            appendix_gaps.append(item)
    if appendix_gaps:
        gaps.append("Appendix entries missing: " + ", ".join(appendix_gaps))

    story_count = len(re.findall(r"Story ID", search_text, flags=re.IGNORECASE))
    acceptance_count = len(re.findall(r"Acceptance Criteria", search_text, flags=re.IGNORECASE))
    corner_count = len(re.findall(r"Corner Cases", search_text, flags=re.IGNORECASE))
    show_stopper_count = len(re.findall(r"Show Stoppers?", search_text, flags=re.IGNORECASE))
    success_metrics = uppercase_contains(search_text, "SUCCESS METRICS")
    metric_definitions = uppercase_contains(search_text, "METRIC DEFINITIONS")

    if story_count == 0:
        gaps.append("No user stories detected (look for 'Story ID' headers).")
    if acceptance_count == 0:
        gaps.append("Acceptance Criteria block(s) missing from Section C stories.")
    if corner_count == 0:
        gaps.append("Corner Cases & Error Handling is not fleshed out for the stories.")
    if show_stopper_count == 0:
        gaps.append("Release plan lacks a Show Stopper / blocking risk entry.")
    if not success_metrics:
        gaps.append("Success Metrics table (Section B4) was not found or is incomplete.")
    if not metric_definitions:
        gaps.append("Metric Definitions (Single Source of Truth) section is absent.")

    ambiguous_hits = find_ambiguous_terms(prd_text)

    report_lines = [
        "# PRD Validation Report",
        "",
        "## Source",
        f"- PRD: {prd_path.resolve()}",
        f"- Template: {template_path.resolve()}",
        f"- Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Section coverage",
    ]

    for title, found in coverage:
        marker = "✅" if found else "⚠️"
        report_lines.append(f"- {marker} {title}")

    report_lines.extend(
        [
            "",
            "## Counts & heuristics",
            f"- User stories detected: {story_count}",
            f"- Acceptance criteria blocks: {acceptance_count}",
            f"- Corner case references: {corner_count}",
            f"- Show stopper mentions: {show_stopper_count}",
            f"- Success metrics cluster found: {'Yes' if success_metrics else 'No'}",
            f"- Metric definitions mentioned: {'Yes' if metric_definitions else 'No'}",
        ]
    )

    report_lines.extend(["", "## Gaps"])

    if gaps:
        for idx, gap in enumerate(gaps, 1):
            report_lines.append(f"{idx}. {textwrap.fill(gap, width=100)}")
    else:
        report_lines.append("No structural gaps detected against the template checklist.")

    if ambiguous_hits:
        report_lines.extend(["", "## Ambiguities & placeholders"])
        for term, count in ambiguous_hits:
            report_lines.append(f"- {term} (found {count} times) – clarify or replace with concrete data.")

    if gaps:
        report_lines.extend(
            [
                "",
                "## Recommendations",
                "1. Fill each missing section (Section A/B/C/D/E) using the template prompts and re-run the validator.",
                "2. Tag every user story with metadata, acceptance criteria, and at least 10 corner cases in Section C.",
                "3. Add SMART success metrics plus a single metric definitions table so downstream teams have a single source of truth.",
                "4. Document release show stoppers and ensure the appendix lists glossary, references, FAQ, and change log.",
            ]
        )

    report_path = prd_path.parent / args.report_name
    write_report(report_path, report_lines)

    print(f"Validation completed. Report written to {report_path}")
    if gaps:
        print(f"Gaps detected: {len(gaps)}. See 'Gaps' section for details.")
    else:
        print("No structural gaps detected.")


if __name__ == "__main__":
    main()
