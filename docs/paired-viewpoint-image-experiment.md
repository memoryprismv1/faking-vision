# Paired-viewpoint image experiment

**Status: exploratory analysis complete; not independently peer-reviewed or validated.**

## Source set

Four user-supplied images, preserved outside the repository. Exact dimensions and SHA-256:

| Asset | Pair / viewpoint | Dimensions | SHA-256 |
|---|---|---:|---|
| `pexels-rdne-7464676.jpg` | Furniture / VP-FUR-01 | 2048×1365 | `8dd5e9dec28a74896e5de9f83faf4b71d974a04139ddd55f2a37572bf0811767` |
| `pexels-rdne-7464266.jpg` | Furniture / VP-FUR-02 | 2048×1365 | `027439c63d32acde38b75b0ba33623d26e126c985dcf7149139abf0da9825394` |
| `pexels-blue-bird-7243222.jpg` | Bicycle / VP-BIKE-01 | 1365×2048 | `adcdb5f4d82877aad0eee2e213c6b3d6e0889c5a085ea891c01bc19c8b2ec342` |
| `pexels-blue-bird-7243220.jpg` | Bicycle / VP-BIKE-02 | 1365×2048 | `e58ab84334104864fa1b548eaf737d17002739e69cc5736d6db2e66519bb3990` |

### Attribution and source provenance

These four images were downloaded from Pexels. Photographer attribution is included even though the standard Pexels License does not require it:

| Assets | Photographer credit | Pexels profile |
|---|---|---|
| `pexels-rdne-7464676.jpg`, `pexels-rdne-7464266.jpg` | Photo by **RDNE Stock project** on Pexels | https://www.pexels.com/@rdne/ |
| `pexels-blue-bird-7243222.jpg`, `pexels-blue-bird-7243220.jpg` | Photo by **Blue Bird** on Pexels | https://www.pexels.com/@blue-bird/ |

Source photo IDs are retained in the filenames. Individual photo-page URLs were not independently verified, so they are not fabricated here. Pexels recommends linking to the individual photo page when available and credits the photographer as “Photo by [name] on Pexels”.

**License reference:** https://www.pexels.com/license/ — Pexels License. Attribution is appreciated but not required. The Pexels rules prohibit, among other things, implying endorsement by depicted people/brands and redistributing the photos as standalone stock or wallpaper content.

**Important scope caution:** Pexels' current Terms/Help guidance also discusses restrictions on data mining, automated extraction, and use of Pexels content to build datasets or train/evaluate ML/AI models. These images were individually downloaded, not collected through the API or by automated scraping. However, this FV work is an AI/visual-analysis experiment, and the public guidance does not make the boundary for this specific one-off manual use sufficiently clear. Do not scale this into a dataset, publish or redistribute the source images, or treat Pexels attribution as permission for AI-model evaluation/training. Confirm applicability with Pexels before using these images for that purpose.

Original image files are not included in this repository.

## Method

Each image was first analysed independently. Only then were pairwise correspondences considered. Packet-local identities remain distinct; cross-view matches are hypotheses recorded below. Camera position, orientation, calibration, focal length, metric geometry, and physical dimensions are unknown.

## Pair A — furniture move

Shared anchors: white interior walls, three arched windows, exposed wooden ceiling beams, plank floor, large dark-green tufted sofa, and two movers in dark teal/blue clothing.

| Candidate | Assessment |
|---|---|
| Green sofa | Strong correspondence: distinctive upholstery, tufting, arms and wooden feet recur. Position/orientation relative to observer differs. |
| Light-haired mover with dark headband | Strong person-level correspondence across views; pose and visible body area differ. |
| Dark-haired, bearded mover | Strong person-level correspondence; first view is primarily a rear/partial view, second shows more of the person. |
| Small teal armchair | Visible only in VP-FUR-01; disposition in VP-FUR-02 unknown. |
| Two cardboard boxes | Visible only in VP-FUR-01; disposition in VP-FUR-02 unknown. |

**Interpretation:** this is a mixed viewpoint and scene-state-change pair. The sofa and people have moved. It is useful for testing continuity of the environment under changing object positions, but it does not isolate viewpoint effects. The chair and boxes must not be declared removed simply because they are not observed in the second image.

## Pair B — woman and bicycle

Shared anchors: red painted brick wall, woman with distinctive curly hair and consistent cream overshirt / striped top / white trousers, and silver bicycle with orange handlebar tape.

| Candidate | Assessment |
|---|---|
| Woman | Strong cross-view candidate: distinctive appearance and clothing recur; pose differs. |
| Bicycle | Strong cross-view candidate: silver frame and orange-taped handlebar recur. Full component-by-component identity is not verifiable in the tighter view. |
| Brick wall | Strong scene-anchor correspondence: brick colour and mortar courses recur; exact camera pose unknown. |

**Visibility:** VP-BIKE-01 shows most of the bicycle, with parts cut by the left/lower image boundaries and parts occluded by the woman. VP-BIKE-02 is closer and more oblique; only a limited handlebar/bicycle region is visible. The remaining bicycle is outside the supplied frame or occluded, not evidence of physical absence.

**Interpretation:** this is the cleaner viewpoint-conditioned visibility test. The images are not known to be simultaneous. Do not infer camera motion, metric depth, hidden bicycle geometry, or exact dimensions.

## FV distinctions under test

- **Observed:** structure directly visible in the supplied image.
- **Occluded:** inside the view but blocked by a nearer structure/person.
- **Outside supplied frame:** not included in the image; do not equate this with physical absence.
- **Unresolvable:** within the supplied image but insufficiently clear to classify reliably.

Do not infer unseen parts from object category expectations. Do not merge packet-local IDs merely because correspondence is plausible. Preserve unresolved correspondences.

## Initial conclusion

Use the bicycle pair first for viewpoint-conditioned visibility and cross-view correspondence. Use the furniture pair second for mixed viewpoint plus scene-state change. Keep the two conditions separate in evaluation; pooling them would conceal which condition caused a failure.

This is an exploratory image analysis, not a validated FV packet merge, general viewpoint model, or reconstruction audit.
