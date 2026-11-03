# FV Edit Visual Workbench (prototype)

Contribution origin: Meta's `Fv-Edit-Js-Editor.html` prototype. Integration/reimplementation and corrective pass: ChatGPT. Tracked by [issue #6](https://github.com/memoryprismv1/faking-vision/issues/6).

## What it does

- Provides seven built-in schematic fixtures covering wind, environmental baseline/edit, harsh-sun negative and active-response cases, and rainy shelter-seeking.
- Lets a worker inspect/edit environment fields and object properties, drag objects on a schematic canvas, append edit-log entries, run editor-level schema/reference checks, import a JSON packet bundle, and export a JSON packet bundle.
- Uses stable packet object IDs for affected-object references.
- Derives the environmental stress enum (`none`, `low`, `high`) from the chosen conditions.
- Treats environmental change as a reason to inspect affected objects, not proof that an active object must move. Object behaviour/location responses must be explicitly authored.
- Records object movement and property edits in the edit log.

## Important limits

This is a client-only prototype, not the authoritative FV validator and not a complete reconstruction workbench. The side-by-side scene view is a **schematic built from CSS shapes and object markers**, not an image renderer. It does not import, embed, alter, or export image assets. The export format is one JSON file (`fv-packet-bundle-v1`) containing packet records and a note that media is absent; it is not a ZIP directory of individual JSON files and images.

The fixtures are illustrative test records, not independently verified source observations. The UI's object-response labels and automated checks are not proof that the visual transformation is valid. Keep JSON/schema checks separate from FV semantic validation and human peer visual review. No website-sourced/stolen coastal art is included.

## Use

Open `FV_Edit_Visual_Workbench.html` in a modern desktop browser. It is self-contained and has no runtime package install. Import only JSON conforming to the documented editor bundle wrapper or the supported legacy JSON shape. Export creates a JSON packet bundle. Keep the original packet/version and provenance; importing then exporting does not automatically re-version the packet.

## Smoke check

With Node.js 18+ available, run:

```sh
node fv-editor-smoke-test.mjs FV_Edit_Visual_Workbench.html
```

The smoke test checks JavaScript syntax, seven fixture records, enum validity, unique IDs and resolving references, simulated JSON bundle round trips, stress derivation, the explicit negative test, and the import/export/disclaimer affordances. It is not browser end-to-end testing or the authoritative FV validator.

## Provenance of this integration

Meta supplied the original single-file React visual concept. The committed file is a streamlined, dependency-free browser implementation based on that concept and the v0.26 rules, not the unchanged original React bundle. ChatGPT's integration pass focused on eliminating implicit/random active responses, making object IDs consistent, making edits auditable, adding JSON import, and stating the schematic/media limitations explicitly.

## Current MVP contract (explicit; not a general FV packet schema)

The workbench imports/exports the editor bundle below. It is a constrained editing interchange format, not a promise that arbitrary FV packets can be loaded without an adapter.

### Bundle structure

```json
{
  "bundle_format": "fv-packet-bundle-v1",
  "packet_meta": {"id": "packet_id", "name": "packet name", "label": "display label", "fv_version": "0.25 or 0.26"},
  "fv_version.json": {"fv_version": "0.25 or 0.26"},
  "ENVIRONMENT.json": {"environmental_stress": "none | low | high", "affected_objects_passive": [], "affected_objects_active": []},
  "OI.json": [{"id": "stable packet-local object ID"}],
  "MSRM.json": {"reference": "schematic-percent-coordinates", "objects": {"stable packet-local object ID": {"x": 0, "y": 0}}},
  "edit_log.json": [],
  "media": {"included": false, "note": "Packet JSON only. Original and edited image assets are not embedded."}
}
```

The required import contract is: an ENVIRONMENT object, OI array with unique non-empty id values, an MSRM object containing an objects map, and an edit-log array. environmental_stress must be exactly none, low, or high. Legacy input may use either the named *.json keys or the documented short aliases (ENVIRONMENT, OI, MSRM, edit_log). The import preserves the supplied FV version; absent version metadata defaults to 0.26. The UI maps 0.25 to the legacy selector and other supplied versions to the 0.26 selector, with a warning if the selected rule set differs from the packet's stored version.

### Edit values and edit log

- The command-line-style editor accepts `fv edit <object-id> <property> <value>`; the value is stored as a string. It does not parse JSON literals or coerce numbers/booleans.
- `fv edit ENVIRONMENT <property> <value>` changes the draft only. The user must apply the environment edit to commit it.
- Object property edits change only the selected OI record. They do not silently alter MSRM coordinates or other objects.
- Dragging an object changes its MSRM x/y values and records before/after positions. A living object placed inside a named editor zone also authors an explicit response record; placement outside those zones does not infer a new behaviour.
- Every committed edit appends an edit-log object with a sequential edit_id, ISO timestamp, edit base, target, property changes, affected-object references, MSRM-change description, packet version, and explanatory note. Exact optional properties vary by edit type; consumers must preserve unknown fields.
- Environment edits recompute the derived stress enum and passive affected-object list. They do not move objects. Existing active responses are retained for review; new active responses must be explicitly authored.
- The editor does not automatically update arbitrary dependent records, resolve identity, or rewrite provenance. Affected-object references must resolve against the packet's OI IDs; the validator reports unresolved references according to its documented PASS/WARN/FAIL rules.

### Identifier and compatibility boundary

This prototype's current editor bundle requires OI id fields and MSRM keys using those same IDs. It is not yet a direct editor for packets whose entities use canonical_id (for example, the CCTV and Alice in Wonderland packets). Those packets need an explicit, reversible adapter that preserves original identifiers and provenance; do not rename source packet IDs to fit the prototype.

These details close the MVP's current interchange contract only. They do not establish a universal ENVIRONMENT schema, general typed edit language, canonical version migration, automatic dependent-record propagation, or authoritative FV validation.
