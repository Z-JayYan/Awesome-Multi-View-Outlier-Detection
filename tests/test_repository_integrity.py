from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_registry import (  # noqa: E402
    documented_path_errors,
    extract_doi,
    internal_link_errors,
    main as validate_registry,
    normalize_title,
)


def load_yaml(relative_path):
    return yaml.safe_load((ROOT / relative_path).read_text(encoding="utf-8"))


def normalized_text(path):
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


class RepositoryIntegrityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = load_yaml("data/papers.yaml")
        cls.datasets = load_yaml("data/datasets.yaml")
        cls.resources = load_yaml("data/resources.yaml")
        cls.taxonomy = load_yaml("data/taxonomy.yaml")

    def test_registry_validation(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = validate_registry()
        self.assertEqual(result, 0, output.getvalue())

    def test_duplicate_identity(self):
        paper_ids = [paper["id"] for paper in self.papers]
        canonical_papers = [
            (normalize_title(paper["title"]), paper["year"]) for paper in self.papers
        ]
        dois = [extract_doi(paper["links"]["paper"]) for paper in self.papers]
        dois = [doi for doi in dois if doi]
        resource_titles = [normalize_title(resource["title"]) for resource in self.resources]
        resource_urls = [resource["url"] for resource in self.resources]

        self.assertEqual(len(paper_ids), len(set(paper_ids)))
        self.assertEqual(len(canonical_papers), len(set(canonical_papers)))
        self.assertEqual(len(dois), len(set(dois)))
        self.assertEqual(len(resource_titles), len(set(resource_titles)))
        self.assertEqual(len(resource_urls), len(set(resource_urls)))

    def test_dataset_references(self):
        dataset_names = {dataset["name"] for dataset in self.datasets}
        paper_ids = {paper["id"] for paper in self.papers}
        for paper in self.papers:
            self.assertLessEqual(set(paper.get("datasets", [])), dataset_names)
        for dataset in self.datasets:
            declared = set(dataset.get("papers_using_dataset", []))
            actual = {
                paper["id"] for paper in self.papers
                if dataset["name"] in paper.get("datasets", [])
            }
            self.assertLessEqual(declared, paper_ids)
            self.assertEqual(declared, actual)

    def test_track_taxonomy(self):
        tracks = set(self.taxonomy["tracks"])
        self.assertEqual(
            tracks,
            {"core_mvod", "partial_mvod", "related_natural_multimodal", "uncertain"},
        )
        for paper in self.papers:
            self.assertIn(paper["track"], tracks)

    def test_generated_files_fresh(self):
        generated = [
            ROOT / "README.md",
            ROOT / "docs/PAPERS.md",
            ROOT / "docs/DATASETS.md",
            ROOT / "docs/BASELINE_MAP.md",
            ROOT / "docs/REMAINING_UNCERTAINTY.md",
            ROOT / "docs/PROTOCOLS.md",
            ROOT / "docs/DATASET_VARIANTS.md",
        ]
        before = {path: normalized_text(path) for path in generated}
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/generate_tables.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        changed = [
            str(path.relative_to(ROOT)) for path in generated
            if normalized_text(path) != before[path]
        ]
        self.assertEqual(changed, [], f"stale generated files: {changed}")

    def test_internal_paths(self):
        self.assertEqual(internal_link_errors(), [])
        self.assertEqual(documented_path_errors(), [])

    def test_public_release_files(self):
        citation = load_yaml("CITATION.cff")
        for field in (
            "cff-version", "message", "title", "authors", "version",
            "date-released", "repository-code", "url", "license",
        ):
            self.assertIn(field, citation)
        self.assertEqual(citation["version"], "0.3.0")
        self.assertEqual(citation["authors"], [{"name": "Z-JayYan"}])
        self.assertEqual(citation["license"], "CC-BY-4.0")
        self.assertFalse((ROOT / "CITATION.cff.template").exists())
        self.assertTrue((ROOT / "LICENSE-CODE").is_file())
        self.assertTrue((ROOT / "LICENSE-CONTENT").is_file())
        self.assertTrue((ROOT / "CHANGELOG.md").is_file())
        self.assertTrue((ROOT / "docs/COMMON_SYNTHETIC_PROTOCOLS.md").is_file())
        self.assertFalse((ROOT / "docs/D1_D6_PROTOCOL.md").exists())

    def test_bilingual_web_entry_points(self):
        pairs = [
            ("README.md", "README.zh-CN.md"),
            ("docs/RESEARCH_LANDSCAPE.md", "docs/RESEARCH_LANDSCAPE.zh-CN.md"),
            ("docs/DATASET_VARIANTS.md", "docs/DATASET_VARIANTS.zh-CN.md"),
            ("docs/COMPARABILITY.md", "docs/COMPARABILITY.zh-CN.md"),
            ("V0.3_REVIEW_REPORT.md", "V0.3_REVIEW_REPORT.zh-CN.md"),
        ]
        for english, chinese in pairs:
            english_path, chinese_path = ROOT / english, ROOT / chinese
            self.assertTrue(english_path.is_file(), english)
            self.assertTrue(chinese_path.is_file(), chinese)
            self.assertIn(chinese_path.name, english_path.read_text(encoding="utf-8"))
            self.assertIn(english_path.name, chinese_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
