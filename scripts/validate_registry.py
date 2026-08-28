#!/usr/bin/env python3
"""Validate Awesome-MVOD registries, schemas, references, and internal links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
CURRENT_YEAR = 2026
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-[0-9]{4}$")
GITHUB_RE = re.compile(r"^https://github\.com/[^/]+/[^/]+/?$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
DOCUMENTED_PATH_RE = re.compile(
    r"`((?:docs|data|schemas|scripts)/[A-Za-z0-9_.\-/]+\.(?:md|yaml|py))`"
)
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", re.IGNORECASE)
REQUIRED = {
    "id", "title", "year", "venue", "venue_type", "venue_status", "track",
    "view_setting", "training_paradigm", "status", "tasks", "mechanisms",
    "anomaly_types", "evidence_levels", "partial_view", "datasets", "summary",
    "links", "code_status", "link_status", "verified_from", "reproducibility",
    "protocol",
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


def extract_doi(url: object) -> str | None:
    if not isinstance(url, str):
        return None
    match = DOI_RE.search(unquote(url))
    return match.group(0).rstrip(".,;)").casefold() if match else None


def schema_errors(schema_path: Path, entries: list[dict], label: str) -> list[str]:
    schema = load_yaml(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for index, entry in enumerate(entries, 1):
        entry_label = entry.get("id") or entry.get("name") or f"{label}-{index}"
        for error in sorted(validator.iter_errors(entry), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "<entry>"
            errors.append(f"{entry_label}: schema {location}: {error.message}")
    return errors


def document_schema_errors(schema_path: Path, document: object, label: str) -> list[str]:
    schema = load_yaml(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(document), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<document>"
        errors.append(f"{label}: schema {location}: {error.message}")
    return errors


def internal_link_errors() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>").split(" ", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken internal link {target!r}")
    return errors


def documented_path_errors() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for documented in DOCUMENTED_PATH_RE.findall(text):
            if not (ROOT / documented).exists():
                errors.append(f"{path.relative_to(ROOT)}: documented path does not exist: {documented!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    taxonomy = load_yaml(ROOT / "data" / "taxonomy.yaml")
    papers = load_yaml(ROOT / "data" / "papers.yaml") or []
    datasets = load_yaml(ROOT / "data" / "datasets.yaml") or []
    resources = load_yaml(ROOT / "data" / "resources.yaml") or []
    comparability = load_yaml(ROOT / "data" / "comparability.yaml") or {}
    variants = load_yaml(ROOT / "data" / "dataset_variants.yaml") or []
    protocols = load_yaml(ROOT / "data" / "protocols.yaml") or []

    errors.extend(schema_errors(ROOT / "schemas" / "paper.schema.yaml", papers, "paper"))
    errors.extend(schema_errors(ROOT / "schemas" / "dataset.schema.yaml", datasets, "dataset"))
    errors.extend(schema_errors(ROOT / "schemas" / "resource.schema.yaml", resources, "resource"))
    errors.extend(document_schema_errors(ROOT / "schemas" / "taxonomy.schema.yaml", taxonomy, "taxonomy"))
    errors.extend(document_schema_errors(ROOT / "schemas" / "comparability.schema.yaml", comparability, "comparability"))
    errors.extend(schema_errors(ROOT / "schemas" / "dataset_variant.schema.yaml", variants, "dataset variant"))
    errors.extend(schema_errors(ROOT / "schemas" / "protocol.schema.yaml", protocols, "protocol"))

    allowed = {
        "track": set(taxonomy["tracks"]),
        "status": set(taxonomy["statuses"]),
        "view_setting": set(taxonomy["view_settings"]),
        "training_paradigm": set(taxonomy["training_paradigms"]),
        "protocol_confidence": set(taxonomy["protocol_confidence"]),
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

    resource_titles: set[str] = set()
    resource_urls: set[str] = set()
    for resource in resources:
        title = normalize_title(resource.get("title", ""))
        url = resource.get("url")
        if title in resource_titles:
            errors.append(f"data/resources.yaml contains duplicate resource title: {resource.get('title')!r}")
        resource_titles.add(title)
        if url in resource_urls:
            errors.append(f"data/resources.yaml contains duplicate resource URL: {url!r}")
        resource_urls.add(url)

    seen_ids: set[str] = set()
    seen_title_year: set[tuple[str, int]] = set()
    seen_dois: dict[str, str] = {}
    track_view = {
        "core_mvod": "complete",
        "partial_mvod": "partial",
        "related_natural_multimodal": "industrial",
        "uncertain": "unknown",
    }
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
            ("track", "track"), ("status", "status"), ("view_setting", "view_setting"),
            ("training_paradigm", "training_paradigm"), ("venue_type", "venue_type"),
            ("venue_status", "venue_status"), ("code_status", "code_status"),
            ("link_status", "link_status"),
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

        expected_view = track_view.get(paper.get("track"))
        if expected_view and paper.get("view_setting") != expected_view:
            errors.append(f"{label}: track requires view_setting={expected_view!r}")
        protocol = paper.get("protocol") or {}
        protocol_view = (protocol.get("view_setting") or {}).get("type")
        if protocol_view != paper.get("view_setting"):
            errors.append(f"{label}: protocol view setting disagrees with top-level view_setting")
        if protocol.get("anomaly_types") != paper.get("anomaly_types"):
            errors.append(f"{label}: protocol anomaly_types must mirror the registry classification")
        confidence = (protocol.get("verification") or {}).get("confidence")
        if confidence not in allowed["protocol_confidence"]:
            errors.append(f"{label}: unknown protocol verification confidence {confidence!r}")
        if paper.get("partial_view") and paper.get("view_setting") not in {"partial", "industrial"}:
            warnings.append(f"{label}: partial_view is true outside the partial/industrial tracks")

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

        doi = extract_doi(paper_url)
        if doi:
            if doi in seen_dois:
                errors.append(f"{label}: duplicate DOI with {seen_dois[doi]}: {doi}")
            seen_dois[doi] = label

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

    paper_ids = {paper["id"] for paper in papers}
    variant_ids = {variant["id"] for variant in variants}
    if len(variant_ids) != len(variants):
        errors.append("data/dataset_variants.yaml contains duplicate ids")
    protocol_ids = {protocol["id"] for protocol in protocols}
    if len(protocol_ids) != len(protocols):
        errors.append("data/protocols.yaml contains duplicate ids")
    for variant in variants:
        dangling = set(variant["papers"]) - paper_ids
        if dangling:
            errors.append(f"{variant['id']}: dangling paper references: {sorted(dangling)}")
    protocol_papers: set[str] = set()
    for experiment in protocols:
        label = experiment["id"]
        protocol_papers.add(experiment["paper_id"])
        if experiment["paper_id"] not in paper_ids:
            errors.append(f"{label}: dangling paper_id {experiment['paper_id']!r}")
        dangling = set(experiment["dataset_variants"]) - variant_ids
        if dangling:
            errors.append(f"{label}: dangling dataset variants: {sorted(dangling)}")
        paper = next((item for item in papers if item["id"] == experiment["paper_id"]), None)
        if paper and experiment["track"] != paper["track"]:
            errors.append(f"{label}: experiment track disagrees with paper track")
        if paper and experiment["view_setting"] != paper["view_setting"]:
            errors.append(f"{label}: experiment view setting disagrees with paper")
        for anomaly_name, anomaly in experiment["anomaly_generation"].items():
            if anomaly["enabled"] is False and anomaly["ratio"] not in {0, 0.0, "unknown"}:
                errors.append(f"{label}: disabled {anomaly_name} anomaly has a non-zero ratio")
            ratio = anomaly["ratio"]
            values = ratio if isinstance(ratio, list) else [ratio]
            for value in values:
                if isinstance(value, (int, float)) and not 0 <= value <= 1:
                    errors.append(f"{label}: invalid {anomaly_name} ratio {value}")
    priority_ids = {
        "dmod-2015", "ldsr-2018", "moddis-2019", "ncmod-2021", "srlsp-2023",
        "iamod-2024", "modgd-2024", "lrtdm-2025", "scone-2026", "rnamod-2026",
        "rcpmod-2024",
    }
    missing_priority = priority_ids - protocol_papers
    if missing_priority:
        errors.append(f"priority papers lack protocol records: {sorted(missing_priority)}")
    for dataset in datasets:
        label = dataset["name"]
        declared = dataset.get("papers_using_dataset", [])
        unknown_ids = set(declared) - paper_ids
        if unknown_ids:
            errors.append(f"{label}: unknown papers_using_dataset ids: {sorted(unknown_ids)}")
        actual = sorted(paper["id"] for paper in papers if label in paper.get("datasets", []))
        if sorted(declared) != actual:
            errors.append(f"{label}: papers_using_dataset is stale; expected {actual}")

    expected_statuses = {"DIRECTLY_COMPARABLE", "CONDITIONALLY_COMPARABLE", "NOT_DIRECTLY_COMPARABLE", "UNKNOWN"}
    if set(comparability.get("statuses", [])) != expected_statuses:
        errors.append("data/comparability.yaml must define the four conservative statuses exactly")
    rule_ids = [rule.get("id") for rule in comparability.get("rules", [])]
    if len(rule_ids) != len(set(rule_ids)):
        errors.append("data/comparability.yaml contains duplicate rule ids")

    errors.extend(internal_link_errors())
    errors.extend(documented_path_errors())

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        f"PASS: {len(papers)} papers, {len(datasets)} datasets, {len(resources)} resources, "
        f"{len(seen_dois)} unique DOIs; schemas, registries, references, and documented paths are consistent"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
