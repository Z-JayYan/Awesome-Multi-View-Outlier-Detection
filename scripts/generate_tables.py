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
    lines = ["| Year | Method | Venue | Mechanism | Anomaly | Code |",
             "|---:|---|---|---|---|---|"]
    for paper in sorted(papers, key=lambda item: (-item["year"], item["title"].casefold())):
        anomaly = "/".join(tag[0].upper() for tag in paper["anomaly_types"])
        mechanisms = ", ".join(tag.replace("_", " ") for tag in paper["mechanisms"][:2])
        lines.append(f"| {paper['year']} | {paper_link(paper)} | {paper['venue']} | {mechanisms} | {anomaly} | {code_link(paper)} |")
    return "\n".join(lines)


def recent_research(papers: list[dict]) -> str:
    grouped: dict[int, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for paper in papers:
        if paper["year"] >= 2024:
            grouped[paper["year"]][paper["venue"]].append(paper)
    lines: list[str] = []
    for year in sorted(grouped, reverse=True):
        lines.append(f"### {year}\n")
        for venue in sorted(grouped[year]):
            lines.append(f"**{venue}**")
            for paper in sorted(grouped[year][venue], key=lambda item: item["title"]):
                status = {
                    "preprint": " (preprint)",
                    "accepted": " (accepted; proceedings not yet verified)",
                }.get(paper["venue_status"], "")
                code = f" [[code]]({paper['links']['code']})" if paper["links"].get("code") else ""
                lines.append(f"- **{paper['title']}**{status} [[paper]]({paper['links']['paper']}){code}")
            lines.append("")
    return "\n".join(lines).rstrip()


def dataset_table(datasets: list[dict]) -> str:
    lines = ["| Dataset | Instances | Views | Feature dimensions | Domain | Notes |",
             "|---|---:|---:|---|---|---|"]
    for dataset in sorted(datasets, key=lambda item: item["name"].casefold()):
        source = dataset["source"]
        name = f"[{dataset['name']}]({source})"
        dims = dataset.get("feature_dimensions") or "variant-dependent"
        n = dataset.get("instances") if dataset.get("instances") is not None else "variant-dependent"
        views = dataset.get("views") if dataset.get("views") is not None else "variant-dependent"
        lines.append(f"| {name} | {n} | {views} | {dims} | {dataset['domain']} | {dataset['notes']} |")
    return "\n".join(lines)


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
    write_papers_doc(papers)
    write_dataset_doc(datasets, papers)
    readme = ROOT / "README.md"
    replace_region(readme, "RECENT", recent_research(papers))
    representative = [paper for paper in papers if paper.get("featured")]
    replace_region(readme, "PAPERS", compact_papers(representative))
    replace_region(readme, "DATASETS", dataset_table(datasets))
    counts = Counter(paper["track"] for paper in papers)
    print(f"Generated tables for {len(papers)} papers and {len(datasets)} datasets: {dict(counts)}")


if __name__ == "__main__":
    main()
