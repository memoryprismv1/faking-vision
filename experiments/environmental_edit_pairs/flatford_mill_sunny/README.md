# Flatford Mill — sunny environmental edit

**Source:** John Constable, *Flatford Mill (Scene on a Navigable River)*, 1816–1817. Tate Britain, accession N01273. Source reproduction: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_Constable_-_Flatford_Mill.jpg).

## Requested edit
Make the existing scene sunny: blue sky with scattered fair-weather clouds, bright direct daylight, coherent stronger cast shadows, and brighter river reflections.

## FV boundaries
- Environmental edit is passive. No object behaviour or spatial change is asserted.
- Preserve the original viewpoint, framing, composition, identities, counts, positions, poses, and relationships.
- Do not add, remove, duplicate, merge, relocate, or reinterpret scene entities.
- Preserve the 19th-century oil-painting character.
- Sun position and physical illumination geometry are not calibrated.

## Artifacts
- `OI.json`: source-grounded scene inventory.
- `MSRM.json`: relative spatial structure.
- `ENVIRONMENT.json`: edited environmental state.
- `edit_log.json`: before/after change and provenance.
- `COMPILED_RENDER_SPEC.json`: reconstruction constraints.

## Image evidence
The original uploaded source and sunny reconstruction are retained in the conversation's accompanying FV packet ZIP. This branch currently contains the structured text records; image binaries have not yet been committed. The source image is also linked above. Do not treat the packet ZIP attachment as a Git repository commit.

## Validation status
This is a working FV packet. Formal repository schema validation and independent `fv audit` have not been run. The generated reconstruction is not claimed to be pixel-faithful; fine details were reinterpreted and require independent audit.
