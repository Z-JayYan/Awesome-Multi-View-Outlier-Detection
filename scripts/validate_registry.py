#!/usr/bin/env python3
"""Validate Awesome-MVOD registries without network access."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
CURRENT_YEAR = 2026
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-[0-9]{4}$")
GITHUB_RE = re.compile(r"^https://github\.com/[^/]+/[^/]+/?$")
REQUIRED = {
    "id", "title", "year", "venue", "venue_type", "venue_status", "track",
    "status", "tasks", "mechanisms", "anomaly_types", "evidence_levels",
    "partial_view", "datasets", "summary", "links", "code_status",
    "link_status", "verified_from", "reproducibility",
}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.casefold()).strip()


def valid_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    taxonomy = load_yaml(ROOT / "data" / "taxonomy.yaml")
    papers = load_yaml(ROOT / "data" / "papers.yaml") or []
    datasets = load_yaml(ROOT / "data" / "datasets.yaml") or []

    allowed = {
        "track": set(taxonomy["tracks"]),
        "status": set(taxonomy["statuses"]),
        "task": set(taxonomy["tasks"]),
        "mechanism": set(taxonomy["mechanisms"]),
        "anomaly": set(taxonomy["anomaly_types"]),
        "evidence": set(taxonomy["evidence_levels"]),
        "venue_type": set(taxonomy["venue_types"]),
        "venue_status": set(taxonomy["venue_statuses"]),
        "code_status": set(taxonomy["code_statuses"]),
        "link_status": set(taxonomy["link_statuses"]),
        "reproducibility": set(taxonomy["reproducibility_values"]),
    }
    dataset_names = {entry["name"] for entry in datasets}
    if len(dataset_names) != len(datasets):
        errors.append("data/datasets.yaml contains duplicate dataset names")

    seen_ids: set[str] = set()
    seen_title_year: set[tuple[str, int]] = set()
    for index, paper in enumerate(papers, 1):
        label = paper.get("id", f"entry-{index}")
        missing = REQUIRED - set(paper)
        if missing:
            errors.append(f"{label}: missing required fields: {sorted(missing)}")
        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or not ID_RE.fullmatch(paper_id):
            errors.append(f"{label}: invalid id format")
        elif paper_id in seen_ids:
            errors.append(f"{label}: duplicate id")
        seen_ids.add(paper_id)

        year = paper.get("year")
        if not isinstance(year, int) or not 2000 <= year <= CURRENT_YEAR + 1:
            errors.append(f"{label}: invalid year {year!r}")
        key = (normalize_title(str(paper.get("title", ""))), year)
        if key in seen_title_year:
            errors.append(f"{label}: duplicate normalized title + year")
        seen_title_year.add(key)

        for scalar_field, vocab_key in (
            ("track", "track"), ("status", "status"),
            ("venue_type", "venue_type"), ("venue_status", "venue_status"),
            ("code_status", "code_status"), ("link_status", "link_status"),
        ):
            value = paper.get(scalar_field)
            if value not in allowed[vocab_key]:
                errors.append(f"{label}: unknown {scalar_field} tag {value!r}")

        for list_field, vocab_key in (
            ("tasks", "task"), ("mechanisms", "mechanism"),
            ("anomaly_types", "anomaly"), ("evidence_levels", "evidence"),
        ):
            values = paper.get(list_field)
            if not isinstance(values, list) or not values:
                errors.append(f"{label}: {list_field} must be a non-empty list")
                continue
            unknown = set(values) - allowed[vocab_key]
            if unknown:
                errors.append(f"{label}: unknown {list_field}: {sorted(unknown)}")

        for dataset in paper.get("datasets", []):
            if dataset not in dataset_names:
                errors.append(f"{label}: unknown dataset reference {dataset!r}")

        links = paper.get("links") or {}
        paper_url = links.get("paper")
        if not valid_http_url(paper_url):
            errors.append(f"{label}: missing or malformed paper URL")
        code_url = links.get("code")
        if code_url is not None and not valid_http_url(code_url):
            errors.append(f"{label}: malformed code URL")
        if code_url is not None and urlparse(code_url).netloc.casefold() == "github.com" and not GITHUB_RE.fullmatch(code_url):
            errors.append(f"{label}: malformed GitHub repository URL")
        if paper.get("code_status") == "official" and code_url is None:
            errors.append(f"{label}: official code status requires a code URL")
        if paper.get("code_status") != "official" and code_url is not None:
            warnings.append(f"{label}: code URL exists but code status is not official")

        sources = paper.get("verified_from") or []
        if not sources:
            errors.append(f"{label}: verified_from must not be empty")
        for source in sources:
            if not valid_http_url(source.get("url")):
                errors.append(f"{label}: malformed evidence URL")

        summary = paper.get("summary", "")
        if not isinstance(summary, str) or len(summary.strip()) < 30:
            errors.append(f"{label}: mechanism summary is too short")

        repro = paper.get("reproducibility") or {}
        for field in ("official_code", "official_config", "dataset_instructions",
                      "pretrained_weights", "environment", "license"):
            if repro.get(field) not in allowed["reproducibility"]:
                errors.append(f"{label}: invalid reproducibility.{field}")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS: {len(papers)} papers, {len(datasets)} datasets; registries are internally consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
