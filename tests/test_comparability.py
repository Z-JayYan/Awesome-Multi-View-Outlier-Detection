from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from compare_protocols import compare, load_papers  # noqa: E402


class ComparabilityRulesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = load_papers()

    def test_same_record_is_direct(self):
        paper = self.papers["rnamod-2026"]
        self.assertEqual(compare(paper, paper)[0], "DIRECTLY_COMPARABLE")

    def test_core_and_partial_are_not_direct(self):
        status, _ = compare(self.papers["rnamod-2026"], self.papers["rcpmod-2024"])
        self.assertEqual(status, "NOT_DIRECTLY_COMPARABLE")

    def test_core_and_industrial_are_not_direct(self):
        status, _ = compare(self.papers["iamod-2024"], self.papers["multi-flow-2025"])
        self.assertEqual(status, "NOT_DIRECTLY_COMPARABLE")

    def test_missing_protocol_evidence_stays_unknown(self):
        status, _ = compare(self.papers["iamod-2024"], self.papers["modgd-2024"])
        self.assertEqual(status, "UNKNOWN")

    @staticmethod
    def known_protocol_paper(paper_id, metric="AUROC"):
        return {
            "id": paper_id,
            "view_setting": "complete",
            "datasets": ["Synthetic benchmark"],
            "protocol": {
                "anomaly_generation": {
                    "attribute": {"mechanism": "view permutation", "affected_views": 1, "ratio": 0.1, "verified": True},
                    "class": {"mechanism": "label mismatch", "affected_views": 1, "ratio": 0.1, "verified": True},
                },
                "contamination": {"values": [0.1], "training_contamination": 0.1},
                "preprocessing": {
                    "normalization": "z-score",
                    "dimension_reduction": "none",
                    "feature_source": "provided features",
                    "backbone": "not applicable",
                },
                "evaluation": {"metrics": [metric], "endpoint": ["sample"], "repetitions": 10, "seeds": [0, 1]},
                "data_setting": {
                    "dataset_variants": ["v1"],
                    "train_split": "transductive full data",
                    "test_split": "transductive full data",
                    "normal_only_training": False,
                },
            },
        }

    def test_matching_complete_fingerprints_are_direct(self):
        left = self.known_protocol_paper("synthetic-left-2026")
        right = self.known_protocol_paper("synthetic-right-2026")
        self.assertEqual(compare(left, right)[0], "DIRECTLY_COMPARABLE")

    def test_known_fingerprint_difference_is_conditional(self):
        left = self.known_protocol_paper("synthetic-left-2026")
        right = self.known_protocol_paper("synthetic-right-2026", metric="AUPRC")
        self.assertEqual(compare(left, right)[0], "CONDITIONALLY_COMPARABLE")


if __name__ == "__main__":
    unittest.main()
