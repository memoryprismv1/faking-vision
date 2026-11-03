import json
import tempfile
import unittest
from pathlib import Path

from fv_audit_batch import aggregate


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "SPECIFICATION" / "FV_Audit_Report_Schema.json"


def report(audit_id="A-1", numerator=1, denominator=4, unit="object", agent="agent:a"):
    return {
        "schema_version": "1.0",
        "audit_id": audit_id,
        "created_at": "2026-11-03T00:00:00Z",
        "auditor": {
            "agent_id": "agent:auditor", "model_provider": "OpenAI",
            "model_name": "GPT", "model_version": "test",
            "run_id": "run-1", "identity_source": "agent_declaration",
        },
        "inputs": {
            "expected_packet": {"packet_id": "P1", "provenance_status": "present"},
            "generated_media_packet": {"packet_id": "P2", "provenance_status": "present"},
            "generated_media": {"media_id": "M1", "sha256": None, "media_type": "image"},
        },
        "comparison": {
            "method": "packet_to_packet", "expected_packet_id": "P1",
            "generated_media_packet_id": "P2", "audit_spec_version": "1.0",
        },
        "metrics": [{
            "metric_code": "omission_rate", "numerator": numerator,
            "denominator": denominator, "uncertain_units": 1,
            "rate_percent": 100 * numerator / denominator if denominator else None,
            "unit_definition": unit, "scope": "objects",
        }],
        "deviations": [],
        "limitations": [],
        "provenance": {
            "expected_packet": {"packet_generator": {
                "agent_id": agent, "model_provider": "OpenAI",
                "model_name": "GPT", "model_version": "test",
            }}
        },
    }


class BatchAggregationTests(unittest.TestCase):
    def run_batch(self, reports):
        with tempfile.TemporaryDirectory() as directory:
            paths = []
            for index, item in enumerate(reports):
                path = Path(directory) / f"{index}.json"
                path.write_text(json.dumps(item), encoding="utf-8")
                paths.append(path)
            return aggregate(paths, SCHEMA)

    def test_pools_counts_not_percentages(self):
        result = self.run_batch([report(numerator=1, denominator=4), report("A-2", 3, 6)])
        profile = next(p for p in result["profiles"] if p["role"] == "auditor")
        self.assertEqual(profile["numerator"], 4)
        self.assertEqual(profile["denominator"], 10)
        self.assertEqual(profile["rate_percent"], 40.0)

    def test_identical_duplicate_counted_once(self):
        item = report()
        result = self.run_batch([item, item])
        self.assertEqual(result["valid_unique_audit_count"], 1)
        self.assertEqual(result["duplicate_identical_group_count"], 1)

    def test_conflicting_duplicate_excluded(self):
        result = self.run_batch([report(), report(numerator=2)])
        self.assertEqual(result["valid_unique_audit_count"], 0)
        self.assertEqual(result["duplicate_conflict_group_count"], 1)

    def test_incompatible_units_separate_profiles(self):
        result = self.run_batch([report(), report("A-2", unit="frame")])
        profiles = [p for p in result["profiles"] if p["role"] == "auditor"]
        self.assertEqual(len(profiles), 2)

    def test_zero_denominator_is_null(self):
        result = self.run_batch([report(denominator=0, numerator=0)])
        profile = next(p for p in result["profiles"] if p["role"] == "auditor")
        self.assertIsNone(profile["rate_percent"])


if __name__ == "__main__":
    unittest.main()
