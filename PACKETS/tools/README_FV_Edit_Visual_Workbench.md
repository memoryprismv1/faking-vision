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