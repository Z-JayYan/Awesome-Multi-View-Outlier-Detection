#!/usr/bin/env python3
"""Conservatively compare two paper protocol fingerprints."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
UNKNOWN = {None, "unknown", "method_dependent", "protocol_defined"}


def is_unknown(value) -> bool:
    if isinstance(value, list):
        return not value or any(is_unknown(item) for item in value)
    if isinstance(value, dict):
        return not value or any(is_unknown(item) for item in value.values())
    return value in UNKNOWN


def compare(a: dict, b: dict) -> tuple[str, list[str]]:
    if a["id"] == b["id"]:
        return "DIRECTLY_COMPARABLE", ["same registry record"]

    reasons: list[str] = []
    if a["view_setting"] != b["view_setting"]:
        return "NOT_DIRECTLY_COMPARABLE", [f"view setting differs: {a['view_setting']} vs {b['view_setting']}"]

    a_endpoints = set(a["protocol"]["evaluation"]["endpoint"]) - {"unknown"}
    b_endpoints = set(b["protocol"]["evaluation"]["endpoint"]) - {"unknown"}
    if a_endpoints and b_endpoints and not (a_endpoints & b_endpoints):
        return "NOT_DIRECTLY_COMPARABLE", ["evaluation endpoints do not overlap"]

    shared_datasets = set(a.get("datasets", [])) & set(b.get("datasets", []))
    if a.get("datasets") and b.get("datasets") and not shared_datasets:
        return "NOT_DIRECTLY_COMPARABLE", ["no shared dataset"]

    fields = [
        ("dataset variants", a["protocol"]["data_setting"]["dataset_variants"], b["protocol"]["data_setting"]["dataset_variants"]),
        ("anomaly generation", a["protocol"]["anomaly_generation"], b["protocol"]["anomaly_generation"]),
        ("contamination", a["protocol"]["contamination"], b["protocol"]["contamination"]),
        ("preprocessing", a["protocol"]["preprocessing"], b["protocol"]["preprocessing"]),
        ("metrics", a["protocol"]["evaluation"]["metrics"], b["protocol"]["evaluation"]["metrics"]),
        ("endpoints", a["protocol"]["evaluation"]["endpoint"], b["protocol"]["evaluation"]["endpoint"]),
        ("train/test setting", a["protocol"]["data_setting"], b["protocol"]["data_setting"]),
    ]
    unknown_fields = [name for name, left, right in fields if is_unknown(left) or is_unknown(right)]
    if unknown_fields:
        return "UNKNOWN", ["essential evidence is unknown: " + ", ".join(unknown_fields)]

    different = [name for name, left, right in fields if left != right]
    if different:
        return "CONDITIONALLY_COMPARABLE", ["fingerprint differs: " + ", ".join(different)]
    return "DIRECTLY_COMPARABLE", ["all captured required fingerprint fields match"]


def load_papers() -> dict[str, dict]:
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8")) or []
    return {paper["id"]: paper for paper in papers}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_a")
    parser.add_argument("paper_b")
    args = parser.parse_args()
    papers = load_papers()
    missing = [paper_id for paper_id in (args.paper_a, args.paper_b) if paper_id not in papers]
    if missing:
        parser.error("unknown paper id(s): " + ", ".join(missing))
    status, reasons = compare(papers[args.paper_a], papers[args.paper_b])
    print(status)
    for reason in reasons:
        print(f"- {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
