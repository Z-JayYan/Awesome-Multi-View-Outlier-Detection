#!/usr/bin/env python3
"""Evidence-aware comparison of paper or experiment protocol fingerprints."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
UNKNOWN = {None, "unknown", "method_dependent", "protocol_defined"}


def is_unknown(value: Any) -> bool:
    if isinstance(value, list):
        return not value or any(is_unknown(item) for item in value)
    if isinstance(value, dict):
        return not value or any(is_unknown(item) for item in value.values())
    return value in UNKNOWN


def _load(name: str, key: str) -> dict[str, dict]:
    items = yaml.safe_load((ROOT / "data" / name).read_text(encoding="utf-8")) or []
    return {item[key]: item for item in items}


def load_papers() -> dict[str, dict]:
    return _load("papers.yaml", "id")


def load_protocols() -> dict[str, dict]:
    return _load("protocols.yaml", "paper_id")


def compare_experiments(a: dict, b: dict) -> dict[str, Any]:
    out = {"status": "INSUFFICIENT_INFORMATION", "matched": [], "mismatched": [], "unknown": [],
           "blocking": [], "warnings": [],
           "recommendation": "Do not merge reported numbers without protocol normalization."}
    if a["id"] == b["id"]:
        out.update(status="DIRECTLY_COMPARABLE", matched=["same experiment record"],
                   recommendation="This is the same registry experiment record.")
        return out
    if a["view_setting"] != b["view_setting"]:
        out["status"] = "NOT_DIRECTLY_COMPARABLE"
        out["blocking"].append(f"view setting: {a['view_setting']} vs {b['view_setting']}")
        out["warnings"].append("Scientific relevance is independent of direct experimental comparability.")
        return out
    fields = {
        "dataset variant": (a["dataset_variants"], b["dataset_variants"]),
        "feature construction": (a["preprocessing"]["feature_construction"], b["preprocessing"]["feature_construction"]),
        "normalization": (a["preprocessing"]["normalization"], b["preprocessing"]["normalization"]),
        "attribute operator": (a["anomaly_generation"]["attribute"]["operator"], b["anomaly_generation"]["attribute"]["operator"]),
        "class operator": (a["anomaly_generation"]["class"]["operator"], b["anomaly_generation"]["class"]["operator"]),
        "mixed operator": (a["anomaly_generation"]["mixed"]["operator"], b["anomaly_generation"]["mixed"]["operator"]),
        "contamination settings": (a["ratios"]["settings"], b["ratios"]["settings"]),
        "training contamination": (a["training"]["training_contamination"], b["training"]["training_contamination"]),
        "metrics": (a["evaluation"]["metrics"], b["evaluation"]["metrics"]),
        "aggregation": (a["evaluation"]["aggregation"], b["evaluation"]["aggregation"]),
        "repetitions": (a["evaluation"]["repetitions"], b["evaluation"]["repetitions"]),
        "endpoint": (a["evaluation"]["endpoint"], b["evaluation"]["endpoint"]),
    }
    for name, (left, right) in fields.items():
        if is_unknown(left) or is_unknown(right):
            out["unknown"].append(name)
        elif left == right:
            out["matched"].append(name)
        else:
            out["mismatched"].append(f"{name}: {left!r} vs {right!r}")
    if "dataset variant" in out["unknown"]:
        out["warnings"].append("A shared dataset name would not establish a shared feature variant.")
    if out["unknown"]:
        out["status"] = "INSUFFICIENT_INFORMATION"
    elif out["mismatched"]:
        out["status"] = "PARTIALLY_COMPARABLE"
    else:
        out.update(status="DIRECTLY_COMPARABLE",
                   recommendation="Captured fingerprints match; still cite the evidence and setting IDs.")
    return out


def _paper_compare(a: dict, b: dict) -> tuple[str, list[str]]:
    if a["id"] == b["id"]:
        return "DIRECTLY_COMPARABLE", ["same registry record"]
    if a["view_setting"] != b["view_setting"]:
        return "NOT_DIRECTLY_COMPARABLE", [f"view setting differs: {a['view_setting']} vs {b['view_setting']}"]
    a_end = set(a["protocol"]["evaluation"]["endpoint"]) - {"unknown"}
    b_end = set(b["protocol"]["evaluation"]["endpoint"]) - {"unknown"}
    if a_end and b_end and not a_end.intersection(b_end):
        return "NOT_DIRECTLY_COMPARABLE", ["evaluation endpoints do not overlap"]
    if a.get("datasets") and b.get("datasets") and not set(a["datasets"]).intersection(b["datasets"]):
        return "NOT_DIRECTLY_COMPARABLE", ["no shared dataset"]
    fields = [("dataset variants", a["protocol"]["data_setting"]["dataset_variants"], b["protocol"]["data_setting"]["dataset_variants"]),
              ("anomaly generation", a["protocol"]["anomaly_generation"], b["protocol"]["anomaly_generation"]),
              ("contamination", a["protocol"]["contamination"], b["protocol"]["contamination"]),
              ("preprocessing", a["protocol"]["preprocessing"], b["protocol"]["preprocessing"]),
              ("metrics", a["protocol"]["evaluation"]["metrics"], b["protocol"]["evaluation"]["metrics"]),
              ("train/test setting", a["protocol"]["data_setting"], b["protocol"]["data_setting"])]
    unknown = [name for name, left, right in fields if is_unknown(left) or is_unknown(right)]
    if unknown:
        return "INSUFFICIENT_INFORMATION", ["essential evidence is unknown: " + ", ".join(unknown)]
    different = [name for name, left, right in fields if left != right]
    return ("PARTIALLY_COMPARABLE", ["fingerprint differs: " + ", ".join(different)]) if different else ("DIRECTLY_COMPARABLE", ["all captured fields match"])


def compare(a: dict, b: dict) -> tuple[str, list[str]]:
    if a["id"] == b["id"]:
        return "DIRECTLY_COMPARABLE", ["same registry record"]
    protocols = load_protocols()
    if a["id"] in protocols and b["id"] in protocols:
        detail = compare_experiments(protocols[a["id"]], protocols[b["id"]])
        reasons = detail["blocking"] + detail["mismatched"]
        if detail["unknown"]:
            reasons.append("unknown: " + ", ".join(detail["unknown"]))
        return detail["status"], reasons or detail["matched"]
    return _paper_compare(a, b)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_a"); parser.add_argument("paper_b")
    args = parser.parse_args()
    papers, protocols = load_papers(), load_protocols()
    missing = [item for item in (args.paper_a, args.paper_b) if item not in papers]
    if missing:
        parser.error("unknown paper id(s): " + ", ".join(missing))
    if args.paper_a in protocols and args.paper_b in protocols:
        detail = compare_experiments(protocols[args.paper_a], protocols[args.paper_b])
        print(f"Status: {detail['status']}")
        for heading, key in (("Matched", "matched"), ("Mismatched", "mismatched"), ("Unknown", "unknown"), ("Blocking", "blocking"), ("Warnings", "warnings")):
            print(f"\n{heading}:")
            print("\n".join(f"- {value}" for value in detail[key]) or "- none")
        print(f"\nRecommendation:\n{detail['recommendation']}")
    else:
        status, reasons = _paper_compare(papers[args.paper_a], papers[args.paper_b])
        print(status)
        print("\n".join(f"- {reason}" for reason in reasons))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
