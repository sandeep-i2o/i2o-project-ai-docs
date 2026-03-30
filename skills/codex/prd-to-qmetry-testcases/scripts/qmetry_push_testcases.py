#!/usr/bin/env python3
"""Push approved manual test cases to QMetry (QTM4J Cloud)."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib import error, parse, request

EXIT_OK = 0
EXIT_INPUT_ERROR = 2
EXIT_AUTH_ERROR = 3
EXIT_API_ERROR = 4


class QmetryApiError(RuntimeError):
    """Raised when QMetry API call fails."""


def _clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _first_non_empty(data: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = _clean(data.get(key))
        if value:
            return value
    return ""


def _to_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _extract_error_message(raw: str) -> str:
    message = raw.strip()
    if not message:
        return "no response body"
    try:
        payload = json.loads(message)
    except json.JSONDecodeError:
        return message[:500]

    if isinstance(payload, dict):
        for key in ("message", "error", "details"):
            if key in payload and payload[key]:
                return str(payload[key])
    return message[:500]


def _parse_json_response(raw: str) -> Any:
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}


class QmetryClient:
    def __init__(self, base_url: str, api_key: str, basic_auth: str, timeout: int) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.basic_auth = basic_auth
        self.timeout = timeout

    def _build_url(self, path: str, query: dict[str, Any] | None = None) -> str:
        url = f"{self.base_url}{path}"
        if query:
            encoded = parse.urlencode(query, doseq=True)
            if encoded:
                url = f"{url}?{encoded}"
        return url

    def request_json(
        self,
        method: str,
        path: str,
        *,
        body: Any | None = None,
        query: dict[str, Any] | None = None,
        expected_status: tuple[int, ...] = (200,),
    ) -> Any:
        headers = {
            "Accept": "application/json",
            "Authorization": self.basic_auth,
            "apiKey": self.api_key,
        }

        data: bytes | None = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")

        req = request.Request(
            self._build_url(path, query),
            data=data,
            headers=headers,
            method=method.upper(),
        )

        try:
            with request.urlopen(req, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8", errors="replace")
                status = response.status
        except error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            detail = _extract_error_message(raw)
            raise QmetryApiError(f"{method} {path} failed with HTTP {exc.code}: {detail}") from exc
        except error.URLError as exc:
            raise QmetryApiError(f"{method} {path} failed: {exc.reason}") from exc

        if status not in expected_status:
            detail = _extract_error_message(raw)
            raise QmetryApiError(
                f"{method} {path} returned HTTP {status}, expected {expected_status}: {detail}"
            )

        return _parse_json_response(raw)


def _build_basic_auth(args: argparse.Namespace) -> str:
    explicit = _clean(args.basic_auth)
    if explicit:
        if explicit.lower().startswith("basic "):
            return explicit
        return f"Basic {explicit}"

    email = _clean(args.jira_email)
    token = _clean(args.jira_api_token)
    if not email or not token:
        raise ValueError(
            "Missing Jira auth. Set QMETRY_BASIC_AUTH or both QMETRY_JIRA_EMAIL and QMETRY_JIRA_API_TOKEN."
        )

    encoded = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("utf-8")
    return f"Basic {encoded}"


def _load_cases(input_path: Path) -> list[dict[str, Any]]:
    if not input_path.exists():
        raise ValueError(f"Input file does not exist: {input_path}")

    try:
        payload = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Input JSON is invalid: {exc}") from exc

    if isinstance(payload, list):
        cases = payload
    elif isinstance(payload, dict):
        cases = None
        for key in ("test_cases", "testcases", "cases", "data"):
            candidate = payload.get(key)
            if isinstance(candidate, list):
                cases = candidate
                break
        if cases is None:
            raise ValueError(
                "Input object must contain one of: test_cases, testcases, cases, data (as array)."
            )
    else:
        raise ValueError("Input JSON must be an array or object containing an array of test cases.")

    normalized: list[dict[str, Any]] = []
    for idx, item in enumerate(cases, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Test case #{idx} is not an object.")
        normalized.append(item)

    if not normalized:
        raise ValueError("No test cases found in input.")

    return normalized


def _extract_data_list(response_payload: Any) -> list[dict[str, Any]]:
    if isinstance(response_payload, list):
        return [item for item in response_payload if isinstance(item, dict)]
    if isinstance(response_payload, dict):
        data = response_payload.get("data")
        if isinstance(data, list):
            return [item for item in data if isinstance(item, dict)]
    return []


def _coerce_int(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _normalize_folder_path(path: str) -> list[str]:
    parts = [segment.strip() for segment in path.split("/") if segment.strip()]
    if not parts:
        raise ValueError("Folder path is empty.")
    for segment in parts:
        if segment in (".", ".."):
            raise ValueError("Folder path cannot contain '.' or '..'.")
    return parts


def _extract_folder_items(response_payload: Any) -> list[dict[str, Any]]:
    if isinstance(response_payload, list):
        return [item for item in response_payload if isinstance(item, dict)]
    if isinstance(response_payload, dict):
        for key in ("data", "results", "values", "folders", "items"):
            items = response_payload.get(key)
            if isinstance(items, list):
                return [item for item in items if isinstance(item, dict)]
    return []


def _get_parent_id(item: dict[str, Any]) -> int | None:
    parent_id = _coerce_int(item.get("parentId") or item.get("parent_id") or item.get("parentFolderId"))
    if parent_id is not None:
        return parent_id
    parent = item.get("parent")
    if isinstance(parent, dict):
        return _coerce_int(parent.get("id"))
    return _coerce_int(parent)


def _build_folder_index(items: list[dict[str, Any]]) -> dict[tuple[int | None, str], int]:
    index: dict[tuple[int | None, str], int] = {}
    for item in items:
        name = _clean(item.get("name"))
        if not name:
            continue
        folder_id = _coerce_int(item.get("id") or item.get("folderId") or item.get("folder_id"))
        if folder_id is None:
            continue
        parent_id = _get_parent_id(item)
        if parent_id == 0:
            parent_id = None
        index[(parent_id, name.lower())] = folder_id
    return index


def _create_folder(
    client: QmetryClient,
    *,
    project_id: int,
    name: str,
    parent_id: int | None,
) -> int:
    body: dict[str, Any] = {"name": name}
    if parent_id is not None:
        body["parentId"] = int(parent_id)

    try:
        created = client.request_json(
            "POST",
            f"/rest/api/latest/projects/{project_id}/testcase-folders",
            body=body,
            expected_status=(200, 201),
        )
    except QmetryApiError:
        if parent_id is not None:
            raise
        body["parentId"] = 0
        created = client.request_json(
            "POST",
            f"/rest/api/latest/projects/{project_id}/testcase-folders",
            body=body,
            expected_status=(200, 201),
        )

    if isinstance(created, dict):
        folder_id = _coerce_int(created.get("id") or created.get("folderId") or created.get("folder_id"))
        if folder_id is not None:
            return folder_id

    raise QmetryApiError(f"Folder create returned no id for '{name}'.")


def _resolve_folder_path(
    client: QmetryClient,
    *,
    project_id: int,
    folder_path: str,
    create_missing: bool,
) -> tuple[int | None, list[dict[str, Any]]]:
    payload = client.request_json(
        "GET",
        f"/rest/api/latest/projects/{project_id}/testcase-folders",
        expected_status=(200,),
    )
    items = _extract_folder_items(payload)
    index = _build_folder_index(items)
    created: list[dict[str, Any]] = []

    parent_id: int | None = None
    for segment in _normalize_folder_path(folder_path):
        key = (parent_id, segment.lower())
        if key in index:
            parent_id = index[key]
            continue

        if not create_missing:
            return None, created

        new_id = _create_folder(client, project_id=project_id, name=segment, parent_id=parent_id)
        index[(parent_id, segment.lower())] = new_id
        created.append({"name": segment, "id": new_id, "parentId": parent_id})
        parent_id = new_id

    return parent_id, created


def _resolve_project_id(client: QmetryClient, args: argparse.Namespace) -> int:
    if args.project_id is not None:
        return int(args.project_id)

    projects_payload = client.request_json(
        "POST",
        "/rest/api/latest/projects",
        query={"startAt": 0, "maxResults": 100, "fields": "key,name,qmetryEnabled"},
        body={"qmetryEnabled": True},
        expected_status=(200,),
    )
    projects = _extract_data_list(projects_payload)

    project_key = _clean(args.project_key).lower()
    project_name = _clean(args.qmetry_project_name).lower()

    if project_key:
        for project in projects:
            if _clean(project.get("key")).lower() == project_key:
                return int(project["id"])
        available = sorted({_clean(p.get("key")) for p in projects if p.get("key")})
        raise ValueError(f"QMetry project key not found: {args.project_key}. Available keys: {available}")

    if project_name:
        for project in projects:
            if _clean(project.get("name")).lower() == project_name:
                return int(project["id"])
        available = sorted({_clean(p.get("name")) for p in projects if p.get("name")})
        raise ValueError(
            f"QMetry project name not found: {args.qmetry_project_name}. Available names: {available}"
        )

    if len(projects) == 1:
        return int(projects[0]["id"])

    raise ValueError(
        "Provide --project-id or --project-key (or --qmetry-project-name) when multiple QMetry projects exist."
    )


def _fetch_named_catalog(
    client: QmetryClient,
    path: str,
    *,
    query: dict[str, Any] | None = None,
) -> dict[str, int]:
    payload = client.request_json("GET", path, query=query, expected_status=(200,))
    entries = _extract_data_list(payload)

    mapping: dict[str, int] = {}
    for entry in entries:
        name = _clean(entry.get("name")).lower()
        if not name:
            continue
        item_id = entry.get("id")
        if item_id is None:
            continue
        try:
            mapping[name] = int(item_id)
        except (TypeError, ValueError):
            continue
    return mapping


def _resolve_named_or_numeric(value: Any, mapping: dict[str, int], *, field: str) -> int | None:
    raw = _clean(value)
    if not raw:
        return None

    try:
        return int(raw)
    except ValueError:
        pass

    key = raw.lower()
    if key in mapping:
        return mapping[key]

    available = sorted(mapping.keys())
    raise ValueError(f"Unknown {field} '{raw}'. Available {field} names: {available}")


def _normalize_steps(raw_steps: Any, fallback_expected: str) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []

    if isinstance(raw_steps, str):
        raw_steps = [line.strip() for line in raw_steps.splitlines() if line.strip()]

    if raw_steps in (None, "", []):
        raw_steps = []

    if not isinstance(raw_steps, list):
        raise ValueError("steps must be a list or newline-delimited string.")

    for idx, step in enumerate(raw_steps, start=1):
        if isinstance(step, str):
            details = step.strip()
            if not details:
                continue
            payload_step: dict[str, str] = {"stepDetails": details}
            if fallback_expected and idx == len(raw_steps):
                payload_step["expectedResult"] = fallback_expected
            normalized.append(payload_step)
            continue

        if not isinstance(step, dict):
            raise ValueError(f"Step #{idx} must be string or object.")

        details = _first_non_empty(step, ["stepDetails", "step", "action", "instruction", "details"])
        if not details:
            raise ValueError(f"Step #{idx} is missing step details.")

        payload_step = {"stepDetails": details}
        test_data = _first_non_empty(step, ["testData", "test_data", "data"])
        expected = _first_non_empty(step, ["expectedResult", "expected_result", "expected"])
        if not expected and fallback_expected and idx == len(raw_steps):
            expected = fallback_expected

        if test_data:
            payload_step["testData"] = test_data
        if expected:
            payload_step["expectedResult"] = expected

        normalized.append(payload_step)

    if not normalized:
        if fallback_expected:
            return [
                {
                    "stepDetails": "Execute the scenario as described in objective.",
                    "expectedResult": fallback_expected,
                }
            ]
        raise ValueError("At least one test step is required.")

    return normalized


def _compose_description(testcase: dict[str, Any], module: str, release: str) -> str:
    lines: list[str] = []

    objective = _first_non_empty(testcase, ["objective", "Objective"])
    if objective:
        lines.append(f"Objective: {objective}")

    requirement = _first_non_empty(
        testcase,
        [
            "requirement_mapping",
            "requirementMapping",
            "requirement",
            "user_story",
            "userStory",
            "story",
        ],
    )
    if requirement:
        lines.append(f"Requirement Mapping: {requirement}")

    case_module = _first_non_empty(testcase, ["module", "Module"]) or module
    case_release = _first_non_empty(testcase, ["release", "Release"]) or release
    if case_module:
        lines.append(f"Module: {case_module}")
    if case_release:
        lines.append(f"Release: {case_release}")

    case_type = _first_non_empty(testcase, ["type", "Type"]) or "Manual"
    automation_status = _first_non_empty(testcase, ["automation_status", "automationStatus"]) or "Not Automated"
    lines.append(f"Type: {case_type}")
    lines.append(f"Automation Status: {automation_status}")

    tags = _to_list(testcase.get("tags"))
    tags = [str(tag).strip() for tag in tags if str(tag).strip()]
    if tags:
        lines.append(f"Tags: {', '.join(tags)}")

    return "\n".join(lines)[:65535]


def _normalize_case(
    testcase: dict[str, Any],
    *,
    index: int,
    module: str,
    release: str,
) -> dict[str, Any]:
    title = _first_non_empty(testcase, ["title", "summary", "name", "Title"])
    if not title:
        raise ValueError(f"Test case #{index} is missing title/summary.")

    precondition = _first_non_empty(testcase, ["preconditions", "precondition", "Preconditions"])
    fallback_expected = _first_non_empty(testcase, ["expected_result", "expectedResult", "Expected Result"])
    steps = _normalize_steps(testcase.get("steps"), fallback_expected)

    labels = _to_list(testcase.get("labels"))
    labels = [str(label).strip() for label in labels if str(label).strip()]

    return {
        "title": title[:255],
        "description": _compose_description(testcase, module=module, release=release),
        "precondition": precondition[:65535],
        "priority": _first_non_empty(testcase, ["priority", "Priority"]),
        "status": _first_non_empty(testcase, ["status", "Status"]),
        "labels": labels,
        "steps": steps,
    }


def _merge_label_names(
    *,
    default_labels: str,
    module_label: str,
    release_label: str,
    case_labels: list[str],
) -> list[str]:
    merged: list[str] = []

    defaults = [item.strip() for item in _clean(default_labels).split(",") if item.strip()]
    merged.extend(defaults)

    if _clean(module_label):
        merged.append(_clean(module_label))
    if _clean(release_label):
        merged.append(_clean(release_label))

    merged.extend(case_labels)

    unique: list[str] = []
    seen: set[str] = set()
    for label in merged:
        lowered = label.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        unique.append(label)
    return unique


def _resolve_label_ids(
    *,
    client: QmetryClient,
    project_id: int,
    known_labels: dict[str, int],
    label_names: list[str],
    create_missing: bool,
) -> tuple[list[int], list[str], dict[str, int]]:
    label_ids: list[int] = []
    warnings: list[str] = []

    for name in label_names:
        raw = _clean(name)
        if not raw:
            continue

        try:
            label_ids.append(int(raw))
            continue
        except ValueError:
            pass

        key = raw.lower()
        if key in known_labels:
            label_ids.append(known_labels[key])
            continue

        if create_missing:
            created = client.request_json(
                "POST",
                f"/rest/api/latest/projects/{project_id}/labels",
                body={"name": raw},
                expected_status=(201,),
            )
            created_id = created.get("id") if isinstance(created, dict) else None
            if created_id is None:
                warnings.append(f"Label '{raw}' creation returned no id; label not linked.")
                continue
            try:
                created_id_int = int(created_id)
            except (TypeError, ValueError):
                warnings.append(f"Label '{raw}' creation returned invalid id '{created_id}'.")
                continue
            known_labels[key] = created_id_int
            label_ids.append(created_id_int)
            continue

        warnings.append(f"Label '{raw}' not found in project and was skipped.")

    deduped = sorted(set(label_ids))
    return deduped, warnings, known_labels


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Push approved manual test cases to QMetry.")
    parser.add_argument("--input", required=True, help="Path to approved test cases JSON file.")

    parser.add_argument("--project-id", type=int, help="QMetry project id.")
    parser.add_argument("--project-key", help="QMetry project key. Used when project-id is not provided.")
    parser.add_argument(
        "--qmetry-project-name",
        help="QMetry project name. Used when project-id/project-key are not provided.",
    )

    parser.add_argument("--module", default="", help="Module name for metadata and default label.")
    parser.add_argument("--release", default="", help="Release version for metadata and default label.")
    parser.add_argument("--folder-id", type=int, help="Optional QMetry test case folder id.")
    parser.add_argument(
        "--folder-path",
        default="",
        help="Folder path for test cases (e.g. project_id/release_version).",
    )

    parser.add_argument("--default-priority", default="Medium", help="Default priority name or id.")
    parser.add_argument("--default-status", default="To Do", help="Default test case status name or id.")
    parser.add_argument(
        "--default-labels",
        default="",
        help="Comma-separated default labels (names or ids).",
    )
    parser.add_argument(
        "--create-missing-labels",
        action="store_true",
        help="Create missing labels in QMetry before linking them.",
    )

    parser.add_argument("--dry-run", action="store_true", help="Validate and print payloads without creating test cases.")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on first create failure.")
    parser.add_argument("--timeout", type=int, default=45, help="HTTP timeout in seconds.")

    parser.add_argument(
        "--base-url",
        default=os.environ.get("QMETRY_BASE_URL", "https://qtmcloud.qmetry.com"),
        help="QMetry base URL.",
    )
    parser.add_argument("--api-key", default=os.environ.get("QMETRY_API_KEY"), help="QMetry apiKey header value.")
    parser.add_argument(
        "--basic-auth",
        default=os.environ.get("QMETRY_BASIC_AUTH"),
        help="Basic auth value with or without 'Basic ' prefix.",
    )
    parser.add_argument("--jira-email", default=os.environ.get("QMETRY_JIRA_EMAIL"), help="Jira user email.")
    parser.add_argument(
        "--jira-api-token",
        default=os.environ.get("QMETRY_JIRA_API_TOKEN"),
        help="Jira API token for basic auth generation.",
    )

    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    api_key = _clean(args.api_key)
    if not api_key:
        print(
            json.dumps(
                {
                    "status": "error",
                    "message": "Missing QMetry API key. Set --api-key or QMETRY_API_KEY.",
                },
                indent=2,
            )
        )
        return EXIT_AUTH_ERROR

    try:
        basic_auth = _build_basic_auth(args)
    except ValueError as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
        return EXIT_AUTH_ERROR

    try:
        cases_raw = _load_cases(Path(args.input))
    except ValueError as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
        return EXIT_INPUT_ERROR

    module_raw = _clean(args.module)
    module_label = module_raw
    folder_path = _clean(args.folder_path)
    release_label = _clean(args.release)

    if args.folder_id is not None and folder_path:
        print(
            json.dumps(
                {"status": "error", "message": "Use either --folder-id or --folder-path, not both."},
                indent=2,
            )
        )
        return EXIT_INPUT_ERROR

    if not folder_path and args.folder_id is None and "/" in module_raw:
        folder_path = module_raw
        module_label = module_raw.split("/", 1)[0]

    client = QmetryClient(args.base_url, api_key, basic_auth, args.timeout)

    try:
        project_id = _resolve_project_id(client, args)

        priorities = _fetch_named_catalog(
            client,
            f"/rest/api/latest/projects/{project_id}/priorities",
            query={"status": ["active"]},
        )
        statuses = _fetch_named_catalog(
            client,
            f"/rest/api/latest/projects/{project_id}/testcase-statuses",
            query={"status": ["active"]},
        )
        labels = _fetch_named_catalog(client, f"/rest/api/latest/projects/{project_id}/labels")

        default_priority_id = _resolve_named_or_numeric(
            args.default_priority,
            priorities,
            field="priority",
        )
        default_status_id = _resolve_named_or_numeric(
            args.default_status,
            statuses,
            field="status",
        )

    except (ValueError, QmetryApiError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
        return EXIT_API_ERROR

    folder_id = args.folder_id
    created_folders: list[dict[str, Any]] = []
    folder_warnings: list[str] = []

    if folder_id is None and folder_path:
        try:
            folder_id, created_folders = _resolve_folder_path(
                client,
                project_id=project_id,
                folder_path=folder_path,
                create_missing=not args.dry_run,
            )
        except ValueError as exc:
            print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
            return EXIT_INPUT_ERROR
        except QmetryApiError as exc:
            print(json.dumps({"status": "error", "message": str(exc)}, indent=2))
            return EXIT_API_ERROR

        if folder_id is None:
            if args.dry_run:
                folder_warnings.append(
                    f"Folder path '{folder_path}' not found; dry-run will not set folderId."
                )
            else:
                print(
                    json.dumps(
                        {
                            "status": "error",
                            "message": f"Folder path '{folder_path}' could not be resolved.",
                        },
                        indent=2,
                    )
                )
                return EXIT_API_ERROR

    created: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    warnings: list[str] = []
    payload_preview: list[dict[str, Any]] = []

    for idx, raw_case in enumerate(cases_raw, start=1):
        try:
            normalized = _normalize_case(
                raw_case,
                index=idx,
                module=_clean(module_label),
                release=_clean(release_label),
            )

            case_priority = _resolve_named_or_numeric(
                normalized["priority"] or default_priority_id,
                priorities,
                field="priority",
            )
            case_status = _resolve_named_or_numeric(
                normalized["status"] or default_status_id,
                statuses,
                field="status",
            )

            label_names = _merge_label_names(
                default_labels=args.default_labels,
                module_label=module_label,
                release_label=release_label,
                case_labels=normalized["labels"],
            )
            label_ids, label_warnings, labels = _resolve_label_ids(
                client=client,
                project_id=project_id,
                known_labels=labels,
                label_names=label_names,
                create_missing=args.create_missing_labels,
            )
            warnings.extend([f"[{normalized['title']}] {item}" for item in label_warnings])

            payload: dict[str, Any] = {
                "projectId": project_id,
                "summary": normalized["title"],
                "isAutomated": False,
                "steps": normalized["steps"],
            }

            if normalized["description"]:
                payload["description"] = normalized["description"]
            if normalized["precondition"]:
                payload["precondition"] = normalized["precondition"]
            if case_priority is not None:
                payload["priority"] = case_priority
            if case_status is not None:
                payload["status"] = case_status
            if label_ids:
                payload["labels"] = label_ids
            if folder_id is not None:
                payload["folderId"] = int(folder_id)

            if args.dry_run:
                payload_preview.append(payload)
                continue

            response = client.request_json(
                "POST",
                "/rest/api/latest/testcases",
                body=payload,
                expected_status=(201,),
            )

            created_item = {
                "title": normalized["title"],
                "id": response.get("id") if isinstance(response, dict) else None,
                "key": response.get("key") if isinstance(response, dict) else None,
                "versionNo": response.get("versionNo") if isinstance(response, dict) else None,
            }

            if isinstance(response, dict) and response.get("warningMessage"):
                created_item["warningMessage"] = response["warningMessage"]

            created.append(created_item)

        except (ValueError, QmetryApiError) as exc:
            errors.append({"index": idx, "title": _clean(raw_case.get("title") or raw_case.get("summary")), "error": str(exc)})
            if args.fail_fast:
                break

    output: dict[str, Any] = {
        "status": "dry_run" if args.dry_run else ("ok" if not errors else "partial_failure"),
        "projectId": project_id,
        "folderPath": folder_path or None,
        "folderId": folder_id,
        "total": len(cases_raw),
        "createdCount": len(created),
        "errorCount": len(errors),
        "created": created,
        "errors": errors,
        "warnings": warnings + folder_warnings,
    }

    if args.dry_run:
        output["payloadPreview"] = payload_preview
    if created_folders:
        output["createdFolders"] = created_folders

    print(json.dumps(output, indent=2))
    if errors:
        return EXIT_API_ERROR
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
