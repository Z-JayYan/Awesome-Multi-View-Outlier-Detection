#!/usr/bin/env python3
"""Generate human-readable tables from the YAML registries."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- AUTO-GENERATED: {name} START -->"
END = "<!-- AUTO-GENERATED: {name} END -->"


def load_yaml(name: str):
    with (ROOT / "data" / name).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or []


def replace_region(path: Path, name: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    start, end = START.format(name=name), END.format(name=name)
    if start not in text or end not in text:
        raise RuntimeError(f"Missing generated markers {name!r} in {path}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    path.write_text(f"{before}{start}\n{body.rstrip()}\n{end}{after}", encoding="utf-8")


def paper_link(paper: dict) -> str:
    label = paper.get("acronym") or paper["title"]
    return f"[{label}]({paper['links']['paper']})"


def code_link(paper: dict) -> str:
    url = paper["links"].get("code")
    return f"[official]({url})" if url else "—"


def compact_papers(papers: list[dict]) -> str:
    lines = ["| Year | Method | Track | Venue | Mechanism | Anomaly | Code |",
             "|---:|---|---|---|---|---|---|"]
    for paper in sorted(papers, key=lambda item: (-item["year"], item["title"].casefold())):
        anomaly = "/".join(tag[0].upper() for tag in paper["anomaly_types"])
        mechanisms = ", ".join(tag.replace("_", " ") for tag in paper["mechanisms"][:2])
        track = {
            "core_mvod": "CORE",
            "partial_mvod": "PARTIAL",
            "related_natural_multimodal": "INDUSTRIAL / NATURAL",
            "uncertain": "UNCERTAIN",
        }[paper["track"]]
        lines.append(f"| {paper['year']} | {paper_link(paper)} | {track} | {paper['venue']} | {mechanisms} | {anomaly} | {code_link(paper)} |")
    return "\n".join(lines)


def recent_research(papers: list[dict]) -> str:
    tracks = [
        ("Recent Classical Multi-View Outlier Detection", "core_mvod"),
        ("Recent Partial / Incomplete Multi-View Outlier Detection", "partial_mvod"),
        ("Recent Industrial / Natural Multi-View Anomaly Detection", "related_natural_multimodal"),
    ]
    lines: list[str] = []
    for track_heading, track in tracks:
        lines.append(f"### {track_heading}\n")
        grouped: dict[int, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
        for paper in papers:
            if paper["track"] == track and paper["year"] >= 2024:
                grouped[paper["year"]][paper["venue"]].append(paper)
        if not grouped:
            lines.extend(["_No verified entries in this release._", ""])
            continue
        for year in sorted(grouped, reverse=True):
            lines.append(f"#### {year}\n")
            for venue in sorted(grouped[year]):
                lines.append(f"**{venue}**")
                for paper in sorted(grouped[year][venue], key=lambda item: item["title"]):
                    status = {
                        "preprint": " (preprint)",
                        "accepted": " (accepted; publisher record/DOI may still be pending)",
                    }.get(paper["venue_status"], "")
                    code = f" [[code]]({paper['links']['code']})" if paper["links"].get("code") else ""
                    lines.append(f"- **{paper['title']}**{status} [[paper]]({paper['links']['paper']}){code}")
                lines.append("")
    return "\n".join(lines).rstrip()


def dataset_table(datasets: list[dict]) -> str:
    lines = ["| Dataset | Track | Samples | Views | Feature / modality | Variants |",
             "|---|---|---:|---:|---|---|"]
    for dataset in sorted(datasets, key=lambda item: item["name"].casefold()):
        source = dataset["official_source"]
        name = f"[{dataset['name']}]({source})"
        dims = dataset.get("view_dimensions") or "unknown"
        n = dataset.get("num_samples", "unknown")
        views = dataset.get("num_views", "unknown")
        variants = ", ".join(dataset.get("known_variants", ["unknown"]))
        track = dataset["task_track"].replace("related_natural_multimodal", "industrial / natural").replace("core_mvod", "CORE")
        lines.append(f"| {name} | {track} | {n} | {views} | {dims} | {variants} |")
    return "\n".join(lines)


def baseline_cards(papers: list[dict], protocols: list[dict] | None = None) -> str:
    protocol_by_paper = {item["paper_id"]: item for item in (protocols or [])}
    tracks = [
        ("CORE / complete-view baselines", "core_mvod"),
        ("Partial / incomplete methodological baselines", "partial_mvod"),
        ("Industrial / natural multi-view baselines", "related_natural_multimodal"),
    ]
    sections = [
        "# Method-Level Baseline Evidence Map",
        "",
        "Generated from the `baseline` blocks in `data/papers.yaml`. A card explains why a method is a defensible comparison; it does not create a leaderboard.",
        "",
    ]
    for heading, track in tracks:
        selected = [paper for paper in papers if paper["track"] == track and paper.get("baseline")]
        sections.extend([f"## {heading}", ""])
        for paper in sorted(selected, key=lambda item: (-item["year"], item["title"].casefold())):
            card = paper["baseline"]
            experiment = protocol_by_paper.get(paper["id"])
            reconstructed_datasets = experiment["dataset_variants"] if experiment else card["main_datasets"]
            reconstructed_metrics = experiment["evaluation"]["metrics"] if experiment else card["metrics"]
            code = f"[official code]({paper['links']['code']})" if paper["links"].get("code") else f"{paper['code_status']}"
            sources = ", ".join(f"[source {i + 1}]({url})" for i, url in enumerate(card["sources"]))
            sections.extend([
                f"### {paper.get('acronym') or paper['title']} — {paper['title']}",
                "",
                f"- **Year / venue:** {paper['year']} / {paper['venue']}",
                f"- **Track / view setting:** `{paper['track']}` / `{paper['view_setting']}`",
                f"- **Core mechanism:** {card['core_mechanism']}",
                f"- **Artifact status:** {code}; registry status `{paper['status']}`",
                f"- **Main dataset variants / metrics:** {', '.join(reconstructed_datasets)} / {', '.join(reconstructed_metrics)}",
                f"- **Protocol reconstruction:** {experiment['id'] if experiment else 'not in v0.3 priority set'}",
                f"- **Baseline roles:** {', '.join(role.replace('_', ' ') for role in card['roles'])}",
                f"- **Closest counterfactual:** {card['closest_counterfactual']}",
                f"- **Why compare:** {card['why_compare']}",
                f"- **Why not automatically directly comparable:** {card['why_not_directly_comparable']}",
                f"- **Scalability candidate:** {'yes' if card['scalability_candidate'] else 'no'}",
                f"- **Evidence:** {sources}",
                "",
            ])
    return "\n".join(sections).rstrip() + "\n"


def contains_unknown(value) -> bool:
    if isinstance(value, dict):
        return any(contains_unknown(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_unknown(item) for item in value)
    return value in {None, "unknown"}


COMPLETENESS_SECTIONS = ("dataset_variants", "preprocessing", "anomaly_generation", "ratios", "training", "evaluation", "code_evidence")


def completeness(protocol: dict) -> tuple[int, dict[str, int]]:
    def leaves(value):
        if isinstance(value, dict):
            return [item for child in value.values() for item in leaves(child)]
        if isinstance(value, list):
            return [item for child in value for item in leaves(child)] or ["unknown"]
        return [value]
    scores = {}
    for name in COMPLETENESS_SECTIONS:
        values = leaves(protocol[name])
        scores[name] = round(100 * sum(not contains_unknown(value) for value in values) / len(values))
    return round(sum(scores.values()) / len(scores)), scores


def write_protocol_docs(protocols: list[dict], papers: list[dict]) -> None:
    by_id = {paper["id"]: paper for paper in papers}
    lines = ["# Experiment-Level Protocol Reconstructions", "",
             "Generated from `data/protocols.yaml`. Completeness is a maintenance signal, not a paper-quality score. Unknown primary-source facts remain unknown.", ""]
    for protocol in protocols:
        paper = by_id[protocol["paper_id"]]
        score, sections = completeness(protocol)
        lines.extend([f"## {paper.get('acronym') or paper['title']} — {paper['title']}", "",
                      f"- **Record / track:** `{protocol['id']}` / `{protocol['track']}`",
                      f"- **Dataset variants:** {', '.join(f'`{item}`' for item in protocol['dataset_variants'])}",
                      f"- **View / training:** `{protocol['view_setting']}` / `{protocol['training']['paradigm']}`",
                      f"- **Anomaly operators:** attribute — {protocol['anomaly_generation']['attribute']['operator']}; class — {protocol['anomaly_generation']['class']['operator']}; mixed — {protocol['anomaly_generation']['mixed']['operator']}",
                      f"- **Ratios:** {protocol['ratios']['settings']} ({protocol['ratios']['denominator']})",
                      f"- **Evaluation:** {', '.join(protocol['evaluation']['metrics'])}; {protocol['evaluation']['repetitions']} repetitions; {protocol['evaluation']['reporting']}",
                      f"- **Code match:** `{protocol['code_evidence']['protocol_matches_paper']}` — {protocol['code_evidence']['discrepancy']}",
                      f"- **Completeness:** **{score}%** (dataset {sections['dataset_variants']}%, preprocessing {sections['preprocessing']}%, anomaly {sections['anomaly_generation']}%, evaluation {sections['evaluation']}%, code {sections['code_evidence']}%)",
                      f"- **Remaining blockers:** {', '.join(protocol['unresolved']) or 'none'}", ""])
    (ROOT / "docs" / "PROTOCOLS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_variant_doc(variants: list[dict]) -> None:
    grouped = defaultdict(list)
    for variant in variants:
        grouped[variant["canonical_dataset"]].append(variant)
    lines = ["# Dataset Variant Registry", "",
             "Generated from `data/dataset_variants.yaml`. A common dataset label is not evidence of a common N × V × feature × preprocessing protocol.", ""]
    for canonical in sorted(grouped, key=str.casefold):
        lines.extend([f"## {canonical}", ""])
        for item in grouped[canonical]:
            lines.extend([f"### `{item['id']}`", "",
                          f"- **Used by:** {', '.join(f'`{paper}`' for paper in item['papers']) or 'none (audit-only record)'}",
                          f"- **N / views / dimensions:** {item['samples']} / {item['views']} / {item['view_dimensions']}",
                          f"- **Features:** {item['feature_source']}",
                          f"- **Preprocessing:** {item['preprocessing']}",
                          f"- **Resolution:** `{item['resolution']}`", ""])
    (ROOT / "docs" / "DATASET_VARIANTS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_uncertainty_queue(protocols: list[dict], papers: list[dict]) -> None:
    by_id = {paper["id"]: paper for paper in papers}
    lines = ["# Remaining Uncertainty", "",
             "Generated evidence queue. P0 gaps block baseline comparison; P1 gaps materially affect reproduction; P2 gaps refine metadata. Unknown is preferred to unsupported inference.", ""]
    for protocol in protocols:
        if not protocol["unresolved"]:
            continue
        paper = by_id[protocol["paper_id"]]
        priority = "P0" if contains_unknown(protocol["dataset_variants"]) or contains_unknown(protocol["ratios"]) else "P1"
        checked = sorted({item["source_type"] for item in protocol["provenance"]})
        lines.extend([f"## {priority} — {paper.get('acronym') or paper['title']} / `{protocol['id']}`", "",
                      "**Unknown / unresolved:**", ""] + [f"- {item}" for item in protocol["unresolved"]] +
                     ["", f"**Evidence checked:** {', '.join(checked)}", "",
                      "**Next source:** author supplement, versioned official code/config, or dataset-generation artifact.", ""])
    (ROOT / "docs" / "REMAINING_UNCERTAINTY.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def uncertainty_report(papers: list[dict]) -> str:
    lines = [
        "# Remaining Uncertainty",
        "",
        "Generated from explicit registry uncertainty. These gaps are preserved rather than inferred. `not_found` means no official artifact was found in the cited audit; it is not proof that none exists.",
        "",
        "| Paper | Unresolved fields | Reason | Missing evidence needed |",
        "|---|---|---|---|",
    ]
    for paper in sorted(papers, key=lambda item: (-item["year"], item["title"].casefold())):
        unresolved = [f"protocol.{name}" for name, value in paper["protocol"].items() if contains_unknown(value)]
        if paper["code_status"] in {"unknown", "not_found"}:
            unresolved.append(f"code_status={paper['code_status']}")
        if paper["venue_status"] == "accepted":
            unresolved.append("publisher DOI / final proceedings record")
        if not unresolved:
            continue
        label = paper.get("acronym") or paper["title"]
        reason = "The currently cited official sources do not expose every required protocol/artifact field."
        needed = "Official full text/supplement or author-owned code/config with the missing protocol and artifact provenance."
        lines.append(f"| [{label}]({paper['links']['paper']}) | {', '.join(unresolved)} | {reason} | {needed} |")
    return "\n".join(lines).rstrip() + "\n"


def write_papers_doc(papers: list[dict]) -> None:
    tracks = [
        ("Core MVOD", "core_mvod"),
        ("Partial / Incomplete MVOD", "partial_mvod"),
        ("Related natural multimodal track", "related_natural_multimodal"),
        ("Uncertain scope", "uncertain"),
    ]
    sections = ["# Complete Paper Registry", "", "Generated from `data/papers.yaml`. Edit the registry, not this file.", ""]
    for heading, track in tracks:
        selected = [paper for paper in papers if paper["track"] == track]
        sections.extend([f"## {heading}", "", compact_papers(selected) if selected else "_No entries in this release._", ""])
    (ROOT / "docs" / "PAPERS.md").write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")


def write_dataset_doc(datasets: list[dict], papers: list[dict]) -> None:
    intro = """# Dataset Registry

The same base dataset is often converted into different multi-view feature sets by different papers. Counts and dimensions below describe the cited public variant only; `variant-dependent` is deliberate, not missing data. Always inspect the paper/code that defines the benchmark split before comparing results.

"""
    reverse = defaultdict(list)
    for paper in papers:
        for dataset in paper.get("datasets", []):
            reverse[dataset].append(paper)
    usage = ["", "## Registry usage map", ""]
    for dataset in sorted(datasets, key=lambda item: item["name"].casefold()):
        used = sorted(reverse[dataset["name"]], key=lambda item: (item["year"], item["title"]))
        labels = [f"[{paper.get('acronym') or paper['title']}]({paper['links']['paper']}) ({paper['year']})" for paper in used]
        usage.append(f"- **{dataset['name']}:** " + (", ".join(labels) if labels else "No paper entry currently names this exact public variant."))
    (ROOT / "docs" / "DATASETS.md").write_text(intro + dataset_table(datasets) + "\n" + "\n".join(usage) + "\n", encoding="utf-8")


def main() -> None:
    papers = load_yaml("papers.yaml")
    datasets = load_yaml("datasets.yaml")
    protocols = load_yaml("protocols.yaml")
    variants = load_yaml("dataset_variants.yaml")
    write_papers_doc(papers)
    write_dataset_doc(datasets, papers)
    (ROOT / "docs" / "BASELINE_MAP.md").write_text(baseline_cards(papers, protocols), encoding="utf-8")
    write_protocol_docs(protocols, papers)
    write_variant_doc(variants)
    write_uncertainty_queue(protocols, papers)
    readme = ROOT / "README.md"
    replace_region(readme, "RECENT", recent_research(papers))
    representative = [paper for paper in papers if paper.get("featured")]
    replace_region(readme, "PAPERS", compact_papers(representative))
    replace_region(readme, "DATASETS", dataset_table(datasets))
    counts = Counter(paper["track"] for paper in papers)
    print(f"Generated tables for {len(papers)} papers, {len(datasets)} datasets, {len(variants)} variants, and {len(protocols)} protocols: {dict(counts)}")


if __name__ == "__main__":
    main()
