# Faking Vision: research foundations and operational translation

Date: 2026-11-11  
Status: research-to-design reference; supplementary to the authoritative Working Process Specification

## Purpose

Faking Vision (FV) is an operational framework intended to make AI systems perform more reliable image and video analysis. It is not primarily a theory of human perception.

The failure target is not simply that a model sometimes names an object incorrectly. A model can produce a coherent but wrong scene model: miss or merge entities, lose components, misassign boundaries, overlook low-salience changes, confuse appearance with identity, infer physical scale from an uncalibrated image, or silently turn a plausible interpretation into an observed fact.

This document records empirical and theoretical work relevant to those failures and maps it to FV procedures. It does **not** treat the Making Vision essay, FV's terminology, or any single paper as proof of a unified biological architecture.

## Evidence and interpretation labels

- **Empirical finding:** a result reported from a defined experiment or observational study. Its population, task, stimulus, and limitations matter.
- **Theory/model:** an explanatory account that may organize evidence but is not itself a complete description of perception.
- **FV design translation:** an operational rule adopted for reliable AI image analysis. It is motivated by research but is not claimed to reproduce a biological mechanism.
- **Working hypothesis:** a proposal requiring further evidence or direct FV testing. Do not present it as an established finding.

## Research-to-design map

### 1. Visual information can be available without being actively monitored

**Varakin and Levin (2006), “Change blindness and visual memory: visual representations get rich and act poor.”** In experiments where participants attended to objects for a cover task, later unexpected change detection was often very poor even though object recognition remained above chance. The result cautions against equating the ability to retain or recognise visual information with the tendency to use it to detect an unexpected change.

**Enders et al. (2024), “Evidence of elevated situational awareness for active duty soldiers during navigation of a virtual environment.”** In a virtual-environment search task, the active-duty group showed faster and farther scanning and less refixation/re-processing of objects than civilian participants, alongside better target-count performance. This is a task- and population-specific result, not a universal scan pattern.

**Sudkamp et al. (published online 2025; journal issue 2026), “Expertise modulates visual sampling strategies in authorised firearms police officers.”** Mobile eye tracking in simulated tactical scenarios found differences between expert and novice officers. Experts tended to make more, shorter, more broadly distributed fixations; their gaze was more consistent in expected threat locations, and fixation duration increased before operational responses. The study supports expertise-shaped, task-relevant sampling, not a universal prescription for where every observer should look.

**FV translation:** do not assume that a rich-looking description means the scene has been comprehensively inspected or that changes will be noticed automatically. Use an economical structural pass, allocate additional inspection where salience, uncertainty, task relevance, anomaly, or explanatory potential warrants it, and retain an explicit check of background and low-salience regions. A task objective may guide attention; it is not source evidence. Promotion in FV means allocating more processing, not confirming identity or committing a packet fact.

### 2. Boundaries belong to surfaces and figures, not merely to local pixels

**Zhou, Friedman, and von der Heydt (2000), “Coding of border ownership in monkey visual cortex.”** Single-cell recordings in awake macaques found neurons in V2 and V4 whose responses depended on which side of a contrast border contained the figure, even when the local edge was the same. The effect depended on image context beyond the classical receptive field.

**Qiu and von der Heydt (2005), “Figure and ground in the visual cortex: V2 combines stereoscopic cues with Gestalt rules.”** Recordings showed that V2 responses combine stereoscopic depth-order information with global contour configuration in figure-ground organisation. Contextual grouping cues can influence the interpretation of a border even when depth information is available.

**Zhaoping (2005), “Border ownership from intracortical interactions in visual area V2.”** This is a mechanistic model of how intracortical interactions in V2 could generate border-ownership signals. Treat it as a model with testable predictions, not as proof that FV's processing stages are neural stages.

**FV translation:** record boundaries, regions, occlusion, and spatial relations before assigning familiar names. A contour is not automatically an independent object boundary. Preserve which region appears to own an occluding edge where the evidence supports it; preserve ambiguity where figure-ground assignment is uncertain. Do not let a local crop erase the wider context needed to interpret a boundary.

### 3. Components and coarse shape can support candidates before full recognition

**Biederman (1987), “Recognition-by-components: a theory of human image understanding.”** Recognition-by-components proposes that object recognition can use arrangements of simple volumetric components derived from image edges and concavities. It is an influential theory of part-based object recognition, not a complete or universally accepted account of visual processing.

**Hayward, Tarr, and Corderoy (1999), “Recognizing silhouettes and shaded images across depth rotation.”** Experiments found that outline shape provides a coarse first-pass description useful for object structure and recognition across viewpoint changes. Shaded images also carry information; the relative advantage depended on which form was shown first.

**FV translation:** allow a visible component or structural arrangement to generate several plausible candidates without forcing whole-object recognition. Record the component and its location, preserve the candidate set, then search for discriminating components and relationships. Silhouette is useful structural evidence but is not always enough to distinguish instances or identities. A candidate is a hypothesis supported to some degree by observed structure, not an object declaration by itself.

### 4. Shadows and shading are useful cues, but can also create misleading contours

**Braje, Legge, and Kersten (2000), “Invariant recognition of natural objects in the presence of shadows.”** Their experiments found that shadows could be confused with object or surface edges in some two-tone displays and impaired performance in early trials, while ordinary natural-object recognition was generally robust to the tested shadow changes. Shadows are not simply helpful or harmful in every condition.

**Norman, Dawson, and Raines (2000), “The perception and recognition of natural object shape from deforming and static shadows.”** Observers could use invariant information in deforming shadow boundaries to discriminate object shape; recognition from static shadows depended more on the particular views shown.

**Cutler et al. (2026), “Three-dimensional shape cues affect human and artificial recognition systems differently.”** In controlled tests using texture-substituted object images across viewpoints, humans relied more strongly on shape than the tested neural networks. Shading and attached-shadow cues reduced network texture bias, but the human and network benefits differed with viewpoint. This is direct comparative evidence, but its conclusions are bounded by the tested models and stimulus set.

**FV translation:** preserve outline, internal contour, shading, cast shadow, and attached-shadow observations as distinct cues where useful. Do not automatically turn every dark region into an object, hole, or boundary. Do not discard shadows as irrelevant either: they can carry shape and depth information. When an interpretation depends on a shadow, test whether the proposed object boundary remains supported by other contours, motion, viewpoint, or context.

### 5. Motion can reveal structure that a still image does not

**Johansson (1973), “Visual perception of biological motion and a model for its analysis.”** Classic point-light displays showed that observers can perceive biological movement from sparse moving lights attached to a person's joints. The result demonstrates the information carried by coordinated motion patterns even when appearance is largely absent.

**FV translation:** preserve temporal trajectories, component motion, relative movement, contact, and interaction. Motion can generate or strengthen candidates and guide sampling. It does not by itself establish persistent identity, intention, motivation, or a specific action label. Keep observed kinematics distinct from behavioural interpretation.

### 6. Size judgements require calibration and reliable anchors

**de Silva et al. (2013), “Demographic variables for wild Asian elephants using longitudinal observations.”** The study used repeated observations and comparisons with known individuals and environmental references to estimate age classes. It also notes that body condition and weight loss can alter apparent age, and that body size alone has substantial variability and limited value without calibration.

**FV translation:** distinguish image-relative size from physical size, and physical size from age or developmental status. Use an anchor only when its identity and relevant dimensions are sufficiently reliable. State the anchor, measurement basis, and assumptions. If the anchor is uncertain or the view is uncalibrated, preserve the scale uncertainty rather than manufacturing a physical measurement.

### 7. Sensory-regime change is an adjacent research question, not an FV rule

**Mason and Brady (2009), “The psychotomimetic effects of short-term sensory deprivation.”** This study examined perceptual disturbances after a brief period of complete visual and auditory isolation in groups differing in hallucination proneness. It is relevant to the broader question of how sensory conditions relate to perception, but it does not establish a general law that deprivation causes hallucinations or that a change in sensory richness necessarily produces a particular recalibration process.

**Working hypothesis to retain separately:** a system adapted to a constrained or monotonous sensory regime may need to recalibrate when moved into a richer, more variable regime; the reverse transition may also change what is attended to or generated internally. This is a hypothesis for investigation, not an established biological mechanism and not a rule to impose on an FV analysis.

## Operational requirements for FV

The research above motivates the following design constraints. These are FV procedures, not claims that an AI reproduces the human visual system.

1. **Observe before naming.** Preserve visible boundaries, regions, contours, components, texture, shading, relative position, occlusion, and motion before semantic classification.
2. **Separate evidence levels.** Distinguish direct image/video evidence, relational derivation from observed elements, calibrated inference using declared anchors or external measurements, and unsupported extrapolation. Never silently promote the last category into a fact.
3. **Generate candidates without premature collapse.** A component may support several candidates. Preserve alternatives and the evidence that would discriminate between them.
4. **Allocate processing selectively.** Promotion changes processing priority only. It does not increase confidence, establish identity, or authorize packet commitment.
5. **Verify with discriminating evidence.** Search for components and relationships that could strengthen or falsify candidates, not only for confirming details.
6. **Preserve context and low-salience structure.** Inspect background, occlusion, boundaries, and scene relationships. A narrow crop or salient foreground object must not erase relevant wider context.
7. **Keep time and identity separate.** Record observed movement and state transitions; resolve persistent identity only when correspondence evidence supports it.
8. **Calibrate scale and uncertainty.** Record anchor identity, dimensions, and assumptions. Do not infer physical size or age from apparent size alone.
9. **Keep source and reconstruction distinct.** Generated imagery can be compared against the packet, but it is not new source evidence for what the original scene contained.

## What this research does not establish

These sources do **not** establish that:
- FV's promotion terminology is a literal neural mechanism;
- the FV pipeline or Making Vision's maplet/local-inset architecture is an established biological sequence;
- one scan pattern is optimal across tasks, people, or environments;
- every contour, shadow, component, or motion pattern uniquely identifies an object;
- part-based recognition guarantees correct instance identity;
- a plausible size anchor makes all scale or age estimates reliable;
- sensory deprivation or sensory-regime change produces one inevitable perceptual outcome;
- findings from human or primate vision transfer directly to every AI model.

Treat the architecture as a testable design synthesis. Use research to motivate procedures and test conditions; do not turn analogy into evidence.

## References

1. Varakin, D. A., & Levin, D. T. (2006). Change blindness and visual memory: Visual representations get rich and act poor. *British Journal of Psychology, 97*(1), 51–77. [https://doi.org/10.1348/000712605X68906](https://doi.org/10.1348/000712605X68906)
2. Enders, L. R., Gordon, S. M., Roy, H., Rohaly, T., Dalangin, B., Jeter, A., Villarreal, J., Boykin, G. L., & Touryan, J. (2024). Evidence of elevated situational awareness for active duty soldiers during navigation of a virtual environment. *PLOS ONE, 19*(5), e0298867. [https://doi.org/10.1371/journal.pone.0298867](https://doi.org/10.1371/journal.pone.0298867)
3. Sudkamp, J., Roach, N., Beebe, S., Metcalf, J., & McGraw, P. (online 2025; issue 2026). Expertise modulates visual sampling strategies in authorised firearms police officers. *Ergonomics, 69*(9), 1769–1785. [https://doi.org/10.1080/00140139.2025.2540417](https://doi.org/10.1080/00140139.2025.2540417)
4. Zhou, H., Friedman, H. S., & von der Heydt, R. (2000). Coding of border ownership in monkey visual cortex. *Journal of Neuroscience, 20*(17), 6594–6611. [https://doi.org/10.1523/JNEUROSCI.20-17-06594.2000](https://doi.org/10.1523/JNEUROSCI.20-17-06594.2000)
5. Qiu, F. T., & von der Heydt, R. (2005). Figure and ground in the visual cortex: V2 combines stereoscopic cues with Gestalt rules. *Neuron, 47*(1), 155–166. [https://doi.org/10.1016/j.neuron.2005.05.028](https://doi.org/10.1016/j.neuron.2005.05.028)
6. Zhaoping, L. (2005). Border ownership from intracortical interactions in visual area V2. *Neuron, 47*(1), 143–153. [https://doi.org/10.1016/j.neuron.2005.04.005](https://doi.org/10.1016/j.neuron.2005.04.005)
7. Biederman, I. (1987). Recognition-by-components: A theory of human image understanding. *Psychological Review, 94*(2), 115–147. [https://doi.org/10.1037/0033-295X.94.2.115](https://doi.org/10.1037/0033-295X.94.2.115)
8. Hayward, W. G., Tarr, M. J., & Corderoy, A. K. (1999). Recognizing silhouettes and shaded images across depth rotation. *Perception, 28*(10), 1197–1215. [https://doi.org/10.1068/p2971](https://doi.org/10.1068/p2971)
9. Braje, W. L., Legge, G. E., & Kersten, D. (2000). Invariant recognition of natural objects in the presence of shadows. *Perception, 29*(4). [https://doi.org/10.1068/p3051](https://doi.org/10.1068/p3051)
10. Norman, J. F., Dawson, T. E., & Raines, S. R. (2000). The perception and recognition of natural object shape from deforming and static shadows. *Perception, 29*(2), 135–148. [https://doi.org/10.1068/p2994](https://doi.org/10.1068/p2994)
11. Cutler, M., Baumel, L., Tocco, J., Friebel, W., Thiruvathukal, G. K., & Baker, N. (2026). Three-dimensional shape cues affect human and artificial recognition systems differently. *PLOS ONE, 21*(5), e0338885. [https://doi.org/10.1371/journal.pone.0338885](https://doi.org/10.1371/journal.pone.0338885)
12. Johansson, G. (1973). Visual perception of biological motion and a model for its analysis. *Perception & Psychophysics, 14*, 201–211.
13. de Silva, S., Webber, C. E., Weerathunga, U. S., Pushpakumara, T. V., Weerakoon, D. K., & Wittemyer, G. (2013). Demographic variables for wild Asian elephants using longitudinal observations. *PLOS ONE, 8*(12), e82788. [https://doi.org/10.1371/journal.pone.0082788](https://doi.org/10.1371/journal.pone.0082788)
14. Mason, O. J., & Brady, F. (2009). The psychotomimetic effects of short-term sensory deprivation. *The Journal of Nervous and Mental Disease, 197*(10), 783–785. [https://doi.org/10.1097/NMD.0b013e3181b9760b](https://doi.org/10.1097/NMD.0b013e3181b9760b)
