# FV Media Object Editor MVP

Experimental next step from the CSS-schematic FV Edit Visual Workbench.

## Run it

Open `FV_Media_Object_Editor_MVP.html` in a current desktop browser. No server or build step is required.

1. Load a local video.
2. Load an FV JSON file, such as an `OI.json` or an exported packet bundle.
3. Select an existing object ID discovered in the packet.
4. Draw a polygon around that object in the current frame.
5. Save a shape keyframe. Repeat at later times as the object moves.
6. Set a property/value and apply the edit. The matching packet records receive the property and the edit is logged.
7. Export the edited packet bundle and/or render an edited WebM video.

## What works in this MVP

- Displays actual user-supplied video frames.
- Reads object IDs from the loaded JSON rather than inventing IDs.
- Lets the user author polygon mask keyframes on frames.
- Interpolates polygon vertices between keyframes when the vertex counts match.
- Blends a chosen tint into pixels inside the interpolated polygon and records a WebM render.
- Adds a property to matching records' `properties` object and exports a separate JSON bundle with an edit log.

## Deliberate limits

This is a first working behaviour, not a full editor or authoritative FV packet writer.

- **Masking is manual.** There is no automatic segmentation, optical flow, or persistent-object tracker yet. The user must place keyframes as needed.
- **The render is a pixel tint.** It is not semantic recolouring, texture reconstruction, or an object-aware fill.
- Interpolation is only valid for masks with matching polygon vertex counts and may fail at scene cuts or shape changes.
- The input packet is retained as a nested source object in the export bundle. Property changes are applied to records with the selected `id`; review the result before treating it as canonical OI/TD/MSRM data.
- WebM export depends on browser MediaRecorder support and runs in real time. Keep the tab open until it finishes.
- Exported visual output and packet JSON must be audited separately. This tool does not claim FV semantic validation.

## Next test

Use a short, locally available clip with one clearly visible object and a packet containing that object's stable ID. Verify: the selected ID, property record, mask keyframes, exported WebM, and edit log all agree. Then improve tracking based on the failure observed, rather than assuming it works.
