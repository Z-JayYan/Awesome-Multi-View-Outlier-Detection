from pathlib import Path
import unittest
import yaml


ROOT = Path(__file__).resolve().parents[1]


class ProtocolIntegrityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = yaml.safe_load((ROOT / "data/papers.yaml").read_text(encoding="utf-8"))
        cls.variants = yaml.safe_load((ROOT / "data/dataset_variants.yaml").read_text(encoding="utf-8"))
        cls.protocols = yaml.safe_load((ROOT / "data/protocols.yaml").read_text(encoding="utf-8"))

    def test_no_dangling_references(self):
        paper_ids = {item["id"] for item in self.papers}
        variant_ids = {item["id"] for item in self.variants}
        for variant in self.variants:
            self.assertLessEqual(set(variant["papers"]), paper_ids)
        for protocol in self.protocols:
            self.assertIn(protocol["paper_id"], paper_ids)
            self.assertLessEqual(set(protocol["dataset_variants"]), variant_ids)

    def test_ratio_values_are_probabilities(self):
        for protocol in self.protocols:
            for anomaly in protocol["anomaly_generation"].values():
                values = anomaly["ratio"] if isinstance(anomaly["ratio"], list) else [anomaly["ratio"]]
                for value in values:
                    if isinstance(value, (int, float)):
                        self.assertGreaterEqual(value, 0)
                        self.assertLessEqual(value, 1)

    def test_disabled_anomaly_has_zero_ratio(self):
        for protocol in self.protocols:
            for anomaly in protocol["anomaly_generation"].values():
                if anomaly["enabled"] is False:
                    self.assertEqual(anomaly["ratio"], 0)

    def test_partial_track_is_not_declared_complete(self):
        paper_by_id = {item["id"]: item for item in self.papers}
        for protocol in self.protocols:
            if paper_by_id[protocol["paper_id"]]["track"] == "partial_mvod":
                self.assertEqual(protocol["view_setting"], "partial")

    def test_provenance_enum(self):
        allowed = {"paper", "supplement", "official_code", "official_project", "derived", "unknown"}
        for protocol in self.protocols:
            self.assertTrue(protocol["provenance"])
            for evidence in protocol["provenance"]:
                self.assertIn(evidence["source_type"], allowed)


if __name__ == "__main__":
    unittest.main()
