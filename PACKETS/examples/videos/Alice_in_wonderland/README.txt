FV PACKET — README
===================

SOURCE
------
Text: Alice's Adventures in Wonderland, Chapter I ("Down the Rabbit-Hole"), Lewis Carroll, 1865.
Provenance: Project Gutenberg eBook #11 (public domain — author died 1898, work far outside copyright).
Excerpt used as reconstruction source (verbatim):

"...when suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so very remarkable in that; nor did Alice think it so very much
out of the way to hear the Rabbit say to itself, "Oh dear! Oh dear! I shall be
late!" (when she thought it over afterwards, it occurred to her that she ought to
have wondered at this, but at the time it all seemed quite natural); but when the
Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and
then hurried on, Alice started to her feet, for it flashed across her mind that
she had never before seen a rabbit with either a waistcoat-pocket, or a watch to
take out of it, and burning with curiosity, she ran across the field after it,
and fortunately was just in time to see it pop down a large rabbit-hole under
the hedge.

In another moment down went Alice after it, never once considering how in the
world she was to get out again."

The excerpt is deliberately truncated at Alice entering the hole — the following
tunnel/falling paragraph is not included, so nothing about the tunnel interior
is packet-authorized. If a video continuation is later wanted, that is a second
packet, not an extrapolation of this one.

PACKET PURPOSE
--------------
Target: video reconstruction (OI + MSRM + TD), duration budget ≤ 60s.
Test class: whether the renderer preserves two persistent, continuously-acting
identities and a single-direction off-screen exit event without inventing
appearance detail the text never supplies (neither Alice nor the field/hedge
setting is described in this excerpt beyond what is recorded in OI/MSRM).

KNOWN LIMITATIONS / UNRESOLVED
-------------------------------
- Alice's appearance, clothing, age, and hair are NOT specified anywhere in this
  excerpt. Do not import the Tenniel illustration or any other Alice iconography.
  Renderer must choose a coherent but non-specific realization (rule 13.2) —
  this is an appearance-generation allowance, not license to add a named/branded
  identity.
- Alice's prior posture/location before "started to her feet" is inferred as
  seated (the phrase presupposes a seated posture) but the surface she was
  seated on is not stated in this excerpt and is left UNRESOLVED — do not add
  a riverbank, book, sister, or daisies; those appear elsewhere in the chapter,
  not in this excerpt.
- "Field" and "hedge" are stated; nothing about season, weather, or time of day
  beyond a generic outdoor daylight setting is stated. Left to PC as a minimal
  style default, flagged as renderer-realized, not textually confirmed.
- The watch's appearance (color/material) is not stated.

FORMAT
------
JSON files below. Version: FV-packet-schema, informal v0.4 (per MR's Working
Process Specification, Faking Vision).

FILES
-----
PC.json     — project-wide style constants (minimal, declared)
OI.json     — object/instance inventory
MSRM.json   — spatial relationships within the single scene
TD.json     — temporal diff log (the chase, the watch-check, the exit)
