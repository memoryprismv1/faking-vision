import copy
import itertools
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "SPECIFICATION" / "FV_Packet_Provenance_Schema.json"


def valid_packet():
    return {
        "schema_version": "1.0",
        "packet_id": "PKT-TEST-001",
        "fv_spec_version": "0.24",
        "packet_generator": {
            "agent_id": "agent:test",
            "model_provider": "OpenAI",
            "model_name": "GPT",
            "model_version": None,
            "run_id": "run-test",
            "generated_at": "2026-11-06T12:00:00Z",
            "identity_source": "agent_declaration",
        },
        "media": {
            "media_id": "media:test",
            "media_type": "image",
            "sha256": None,
            "media_generator": None,
            "embedded_provenance": [],
        },
    }


class PacketProvenanceSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.validator = Draft202012Validator(
            cls.schema, format_checker=FormatChecker()
        )

    def errors(self, instance):
        return list(self.validator.iter_errors(instance))

    def test_all_optional_addons_can_be_omitted_independently(self):
        addon_values = {
            "attribution": {"creator": "Source creator"},
            "organizations": [{"name": "Example Organization"}],
            "contributions": [{
                "username": "analyst",
                "email": "analyst@example.org",
                "organization": "Example Organization",
                "timestamp": "2026-11-06T12:05:00Z",
                "role": "annotator",
            }],
        }
        names = list(addon_values)
        for count in range(len(names) + 1):
            for selected in itertools.combinations(names, count):
                with self.subTest(included=selected):
                    packet = valid_packet()
                    packet["media"].update(
                        {name: copy.deepcopy(addon_values[name]) for name in selected}
                    )
                    self.assertEqual(self.errors(packet), [])

    def test_addon_properties_are_not_required_by_media_schema(self):
        required = set(self.schema["properties"]["media"]["required"])
        self.assertTrue(
            {"attribution", "organizations", "contributions"}.isdisjoint(required)
        )

    def test_attribution_is_open_for_later_property_design(self):
        packet = valid_packet()
        packet["media"]["attribution"] = {
            "creator": "Original creator",
            "source_reference": "source-123",
            "future_property": {"preserved": True},
        }
        self.assertEqual(self.errors(packet), [])

    def test_contribution_fields_are_required_but_values_may_be_unknown(self):
        packet = valid_packet()
        packet["media"]["contributions"] = [{
            "username": None,
            "email": None,
            "organization": None,
            "timestamp": None,
            "role": None,
        }]
        self.assertEqual(self.errors(packet), [])

        del packet["media"]["contributions"][0]["role"]
        self.assertTrue(self.errors(packet))

    def test_invalid_optional_addon_shapes_are_rejected(self):
        cases = [
            ("attribution", []),
            ("organizations", {}),
            ("contributions", {}),
        ]
        for field, value in cases:
            with self.subTest(field=field):
                packet = valid_packet()
                packet["media"][field] = value
                self.assertTrue(self.errors(packet))


if __name__ == "__main__":
    unittest.main()
