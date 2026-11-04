# FV Media Object Editor MVP

Experimental next step from the CSS-schematic FV Edit Visual Workbench.

## Run it

Open `FV_Media_Object_Editor_MVP.html` in a current desktop browser. No server or build step is required.

1. Load a local video, or load a still image in the new image-viewpoint mode.
2. Load an FV JSON file, such as an `OI.json` or an exported packet bundle.
3. Select an existing object ID discovered in the packet.
4. Draw a polygon around that object in the current frame.
5. Save a shape keyframe. Repeat at later times as the object moves.
6. Set a property/value and apply the edit. The matching packet records receive the property and the edit is logged.
7. Export the edited packet bundle and/or render an edited WebM video.

## What works in this MVP

- Displays actual user-supplied video frames.
- Reads existing `id` and `canonical_id` values from the loaded JSON rather than inventing IDs.
- Lets the user author polygon mask keyframes on frames.
- Interpolates polygon vertices between keyframes when the vertex counts match.
- Blends a chosen tint into pixels inside the interpolated polygon and records a WebM render.
- Adds a property to matching records' `properties` object and exports a separate JSON bundle with an edit log.

## Deliberate limits

This is a first working behaviour, not a full editor or authoritative FV packet writer.

- **Masking is manual.** There is no automatic segmentation, optical flow, or persistent-object tracker yet. The user must place keyframes as needed.
- **The render is a pixel tint.** It is not semantic recolouring, texture reconstruction, or an object-aware fill.
- Interpolation is only valid for masks with matching polygon vertex counts and may fail at scene cuts or shape changes.
- The input packet is retained as a nested source object in the export bundle. Property changes are applied to matching records using `canonical_id` (preferred) or `id`; review the result before treating it as canonical OI/TD/MSRM data.
- WebM export depends on browser MediaRecorder support and runs in real time. Keep the tab open until it finishes.
- Exported visual output and packet JSON must be audited separately. This tool does not claim FV semantic validation.

## Next test

Use a short, locally available clip with one clearly visible object and a packet containing that object's stable `canonical_id` or `id`. The browser CI downloads a short VP9/WebM excerpt from the source CCTV clip documented in the CCTV experiment's SOURCE_AND_PROVENANCE.md, then tests it against the corresponding Part 1 packet. The source is hosted on Wikimedia Commons; its file page records the original WebM as VP9/Opus and identifies it as public domain. Verify: the selected ID, property record, mask keyframes, exported WebM, and edit log all agree. Then improve tracking based on the failure observed, rather than assuming it works.

## Reusable viewpoint object (VPO)

The editor now accepts still-image input for viewpoint editing. A draggable camera icon overlays the loaded image; dragging it stores an image-relative `pose.image_anchor` in the selected VPO. The edit is logged and survives packet-bundle export/reload. This is an image-space camera marker/pose annotation, not a synthesized alternate perspective or pixel transformation.

The editor also loads, creates, edits, and exports reusable camera-pose presets in the packet's root `viewpoint` array. It keeps source `initial_state` provenance separate from the render `pose`; a missing viewpoint array receives an explicitly labelled virtual render preset with unknown source state. Existing viewpoint records are preserved.

The VPO controls cover position, intrinsic Y-X-Z yaw/pitch/roll in degrees, perspective/orthographic projection, perspective FOV, optional target, aspect ratio, and preset name. A draggable camera icon overlays the source frame as a camera-position control; dragging updates the position fields and commits/logs the VPO edit. The editor records before/after pose values in its edit log. Saving the packet bundle persists the VPO along with the source packet; the input file is never overwritten.

**Important limitation:** this is currently a portable pose editor and packet writer, not a 3D renderer. Changing the VPO does not transform pixels in the video canvas. A 2D image/video alone cannot provide arbitrary unseen geometry. The editor therefore does not claim to generate a geometrically correct new camera view. The camera icon is a pose-control handle, not a physical camera simulation or a new-view renderer. A future render adapter can consume the same VPO contract and must report when scene geometry is insufficient.

The canonical frame and field semantics are specified in `SPECIFICATION/FV_Working_Process_Specification.md` and `SPECIFICATION/FV_Viewpoint_Schema.json`. The `fv edit viewpoint` skill command describes the matching command-line operation set; implementations must share these conventions and validation rules.
