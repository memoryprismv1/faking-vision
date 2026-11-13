# Example Corpus Visual Privacy Audit

- Branch: `work/fv-example-corpus-privacy-audit-20261112`
- Baseline: merge commit `0d5b05715c5529790cc83a318c5f081e87b628ce`
- Inventory at start: 305 images, 4 videos (309 media files)
- Method: visual inspection in small batches; this log records only assets actually opened and inspected.
- Scope caveat: visual inspection does not establish source licensing, metadata cleanliness, or full provenance. Those require separate checks.

## Progress

- Reviewed: 309 / 309 media files (305 images, 4 videos; video review sampled as described below)
- Remaining visual inventory: 0 images and 0 videos; all 309 media files received the visual review described in the batch records (video sampling limitations apply).
- The initial flags for the desk-image name and blanket CCTV face/plate/pole masking were reassessed in the addenda below. The desk-image flag was withdrawn; CCTV observations are context-dependent, not automatic privacy violations.
- No screenshot of a user's desktop, browser, application window, terminal, taskbar, or other personal system was identified in the supplied archive.
- Metadata review: basic embedded image EXIF and all four MP4 containers were inspected as described below. No GPS or user-account/system-path identifiers were found in the fields inspected. The desk photograph's Commons metadata does disclose camera make/model and capture time; this is source-photographer capture metadata, not a screenshot or evidence of the user's system.
- Remaining limitation: AAC audio in the three generated story MP4s was not listened to or transcribed. It is not audio-cleared. Source-specific licensing/provenance gaps remain for some legacy examples.

## Batch 1 — ordinary image examples (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/images/blue_chairs/Blue_chairs_and_table_in_the_Western_Market_seating_area_2.jpg` | Outdoor seating scene; no people or personal details visible. | No visual privacy concern |
| `PACKETS/examples/images/desk_with_objects/Desk_with_objects_for_editathon.jpg` | Indoor workspace; handwritten personal name visible on a bag/sign; Wikimedia-branded display also visible. No face visible. | **Flag for source/context check** |
| `PACKETS/examples/images/kitchen_interior_design/Kitchen_interior_design.jpg` | Kitchen interior; no people or personal information visible. | No visual privacy concern |
| `PACKETS/examples/images/restaurant_kitchen/RestaurantKitchen.jpg` | Commercial kitchen; two workers seen from behind, no faces or obvious identifying details. | No obvious personal-data concern; retain note that people are depicted |
| `PACKETS/examples/images/small_room_interior/Small_room_-_interior.JPG` | Bedroom interior; no person or personal information visible. | No visual privacy concern |

## Batch 2 — KITTI LiDAR visualizations (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/lidar/kitti/merged/KITTI_Merged_Global_Buildings/visualizations/06_kitti_persistent_building_ids.jpg` | Annotated top-down LiDAR point-cloud map. | No visual privacy concern |
| `PACKETS/examples/lidar/kitti/merged/KITTI_Merged_Global_Buildings/visualizations/07_kitti_54_building_map.jpg` | Annotated building point-cloud map and metadata panel. | No visual privacy concern |
| `PACKETS/examples/lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/visualizations/11_kitti_sequence00_assembled_map.jpg` | Diagrammatic building correspondence and merged map. | No visual privacy concern |
| `PACKETS/examples/lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/visualizations/12_kitti_sequence00_assembled_map_duplicate.jpg` | Height-coloured LiDAR point-cloud map. | No visual privacy concern |
| `PACKETS/examples/lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/visualizations/13_additional_lidar_visualization.jpg` | Explanatory LiDAR poster with building IDs and map legend. | No visual privacy concern |

## Batch 3 — KITTI and Mayan LiDAR visualizations (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/visualizations/14_additional_lidar_visualization.webp` | Stylized LiDAR point-cloud city scene; no people or personal information visible. | No visual privacy concern |
| `PACKETS/examples/lidar/kitti/odometry/KITTI_Sequence07_Assembled/visualizations/05_kitti_sequence07_pointcloud.webp` | Annotated top-down LiDAR map; no people or personal information visible. | No visual privacy concern |
| `PACKETS/examples/lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/visualizations/01_mayan_lidar_stitching.jpg` | Highly annotated synthetic/illustrative city map; no personal information visible. | No visual privacy concern |
| `PACKETS/examples/lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/visualizations/02_mayan_megacity_map.jpg` | LiDAR process infographic and illustrative pyramid scene; no personal information visible. | No visual privacy concern |
| `PACKETS/examples/lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/visualizations/03_mayan_semantic_segmentation.jpg` | Annotated aerial/terrain visualization; no people or personal information visible. | No visual privacy concern |

## Batch 4 — Hubble visualization and CCTV object crops (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/telescope/hubble/Telescope_Hubble_UDF_Stitching/visualizations/02_hubble_udf_stitching_craft_poster.jpg` | Astronomy data-stitching infographic with galaxy imagery, plots, and pipeline diagrams; no people or personal information visible. | No visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/blue_vehicle_t042.jpg` | CCTV parking-lot frame with a blue vehicle and surrounding cars; no person visible in this crop. Small background signage/vehicle details are not legible at this scale. | No obvious personal-data concern; vehicle identifiers need review in source-resolution frames |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/blue_vehicle_t050.jpg` | Similar parking-lot frame; no person visible in this crop. | No obvious personal-data concern; vehicle identifiers need review in source-resolution frames |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/dark_sedan_t098.jpg` | Parking-lot crop with several vehicles; registration plates are present on some vehicles but not confidently readable in this crop. | **Flag for source-resolution plate legibility check** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/pedestrian_t022.jpg` | Public parking-lot CCTV crop showing one pedestrian; face is visible, with multiple vehicle registration plates in the scene. | **Flag: identifiable person/face and vehicle identifiers; assess masking and source permissions** |

## Batch 5 — CCTV object crops (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/pedestrian_t028.jpg` | Parking-lot crop dominated by vehicles; no pedestrian face visible in this crop. Vehicle plates are present in the wider scene but not confidently legible at this scale. | **Flag for source-resolution vehicle-identifier check** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/silver_sedan_t020.jpg` | Wide parking-lot view; a pedestrian is visible between parked cars, with face too small here to assess identifiability. Multiple vehicle plates are present. | **Flag for face/plate review at source resolution** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/silver_sedan_t024.jpg` | Parking-lot crop with a silver sedan and multiple parked vehicles; no person visible. Vehicle plates appear but are not confidently readable at this scale. | **Flag for source-resolution vehicle-identifier check** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/white_pickup_t098.jpg` | Wide CCTV view of a white pickup and parking area; no person visible. No clearly readable personal information. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/white_pickup_t105.jpg` | Similar parking-area view with white pickup; no person visible. No clearly readable personal information. | No obvious visual privacy concern |

## Batch 6 — CCTV object crop and verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/objs/dark_sedan_t105.jpg` | Parking-lot crop showing a dark sedan and surrounding vehicles; no person visible. Registration plates are present on nearby cars but not confidently readable in this crop. | **Flag for source-resolution vehicle-identifier check** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_000s.jpg` | Full CCTV verification frame of a parking lot; a pedestrian is visible near the centre-left, with many vehicles and plates across the scene. No plate is confidently readable at this display scale. | **Flag: person present; vehicle identifiers and any business markings need source-context review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_003s.jpg` | Same parking-lot scene; pedestrian remains visible. | **Flag: person present; check face visibility and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_004s.jpg` | Same scene with pedestrian moving near parked vehicles; face is small at this scale. | **Flag: person present; check face visibility and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_008s.jpg` | Same scene; pedestrian is more clearly separated from the background, and vehicles/plates remain visible. | **Flag: person present; check face visibility and vehicle identifiers** |

## Batch 7 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_009s.jpg` | Full parking-lot frame; one pedestrian is visible near the centre, with numerous vehicles. Plates are present but not confidently readable at this scale. | **Flag: person present; retain vehicle-identifier review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_012s.jpg` | Pedestrian has moved further into the lot; face remains small in the full-frame view. | **Flag: person present; retain vehicle-identifier review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_015s.jpg` | Pedestrian is crossing between parked vehicles; no clearly readable personal text observed. | **Flag: person present; retain vehicle-identifier review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_016s.jpg` | Pedestrian continues through the parking area; face is not detailed enough here to determine identity. | **Flag: person present; retain vehicle-identifier review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_018s.jpg` | Pedestrian remains visible among parked vehicles; plates and commercial vehicle markings are present in the scene. | **Flag: person present; retain vehicle-identifier review** |

## Batch 8 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_020s.jpg` | Pedestrian continues walking towards the camera through the parking area; multiple vehicles and plates remain visible. | **Flag: identifiable person present; vehicle identifiers require review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_022s.jpg` | Pedestrian is closer to the camera; face and clothing are more apparent. A moving silver car is also visible. | **Flag: face/person visible; vehicle identifiers require review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_024s.jpg` | Pedestrian is beside a parked SUV; face is visible at a greater size than in earlier frames. | **Flag: face/person visible; vehicle identifiers require review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_026s.jpg` | Pedestrian is near the foreground; face is visibly distinguishable in this frame. | **Strong privacy flag: identifiable face/person; masking or replacement needed unless documented permission covers publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_028s.jpg` | Pedestrian is close to the foreground; face is clearly visible. | **Strong privacy flag: identifiable face/person; masking or replacement needed unless documented permission covers publication** |

## Batch 9 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_032s.jpg` | Parking-lot scene; the pedestrian seen in earlier frames is no longer visible. Vehicles remain throughout the scene. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_033s.jpg` | Same parking-lot scene; no pedestrian visible in this frame. A vehicle is moving in the far background. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_035s.jpg` | Parking lot with vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_036s.jpg` | Parking lot with vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_037s.jpg` | Parking lot with vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |

## Batch 10 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_040s.jpg` | Parking lot with vehicles; no pedestrian visible. A blue vehicle is moving along the distant access road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_042s.jpg` | Same scene; no person visible. Blue vehicle remains on the distant road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_043s.jpg` | Same scene; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_044s.jpg` | Same scene; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_046s.jpg` | Same scene; no person visible. Vehicle plates remain too small to read confidently in these full-frame images. | **Flag for vehicle-identifier/source permission review** |

## Batch 11 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_047s.jpg` | Parking lot and access road; no pedestrian visible. A blue vehicle is moving in the distant road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_048s.jpg` | Same scene; no pedestrian visible. Blue vehicle remains on the access road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_050s.jpg` | Parking lot with parked vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_051s.jpg` | Same scene; no person visible. A vehicle is visible on the distant access road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_052s.jpg` | Parking lot with parked vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |

## Batch 12 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_054s.jpg` | Parking lot with vehicles; no clearly visible pedestrian. Some dark shapes near a vehicle are too ambiguous to classify as a person. | **Flag for vehicle-identifier/source permission review; ambiguous shape not treated as confirmed person** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_056s.jpg` | Parking lot; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_060s.jpg` | Parking lot; a red car is entering/moving through the far-right access lane. No person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_061s.jpg` | Red car continues behind parked vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_064s.jpg` | Red car has moved across the lot and is now near the left side; no person visible. | **Flag for vehicle-identifier/source permission review** |

## Batch 13 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_068s.jpg` | Parking lot with parked vehicles; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_072s.jpg` | Several vehicles have shifted position; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_076s.jpg` | Parking lot; no person visible. Vehicle positions differ from prior frames. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_080s.jpg` | A pedestrian appears in the foreground between parked cars, reaching toward or interacting with a parking sign/vehicle area. Face is visible in profile/oblique view but not sufficiently detailed here to establish identity. | **Flag: person visible; source permissions and face masking need review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_084s.jpg` | Pedestrian is no longer visible; parking lot and vehicles remain. | **Flag for vehicle-identifier/source permission review** |

## Batch 14 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_087s.jpg` | Parking lot with vehicles; no pedestrian visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_088s.jpg` | Same scene; no pedestrian visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_089s.jpg` | Same scene; no pedestrian visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_092s.jpg` | A vehicle is moving along the distant access road; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_094s.jpg` | Vehicle continues along the distant access road; no person visible. | **Flag for vehicle-identifier/source permission review** |

## Batch 15 — CCTV verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_095s.jpg` | Parking lot and access road; no pedestrian visible. A vehicle is travelling along the distant road. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_096s.jpg` | Same scene; no pedestrian visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_097s.jpg` | A vehicle continues along the distant access road; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_098s.jpg` | A light-colored pickup is moving along the far access road; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_100s.jpg` | A light pickup continues along the far road and a dark sedan is moving through the foreground parking area; no person visible. | **Flag for vehicle-identifier/source permission review** |

## Batch 16 — CCTV frames and object crops (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_102s.jpg` | Parking lot scene; a dark sedan crosses the foreground and a light pickup is visible on the far access lane. No person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_104s.jpg` | Light pickup progresses along the far access lane; dark sedan continues across foreground. No person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/snapshot/verification/V_105s.jpg` | Light pickup and dark sedan remain visible in motion; no person visible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/camera_reframe_t050.jpg` | Wider reframed parking-lot view with multiple parked vehicles; no person discernible. Vehicle details/plates may be present at source resolution. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/dark_vehicle_t097.jpg` | Crop shows a section of pavement, curb/grass edge and painted parking line. No vehicle or person is visible in the supplied image despite the filename. | **Flag: filename/content mismatch; verify crop provenance and object association** |

## Batch 17 — CCTV-002 object crops (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/moving_dark_vehicle_t000.jpg` | Crop shows several parked vehicles and part of a moving dark vehicle. Registration plates are visible on multiple cars, though not all are legible at this crop size. | **Flag for vehicle-identifier masking/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/pedestrian_candidate_t015.jpg` | A pedestrian's head and upper body enter the lower edge of the crop; face is visible, though small. Vehicle plate also appears in background. | **Flag: person/face visible; vehicle identifier present** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/pedestrian_candidate_t039.jpg` | Pedestrian visible from head to upper torso at lower-right; face and clothing are distinguishable. A vehicle plate appears in background. | **Strong privacy flag: face/person visible; mask or replace unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/pole_signs_t100.jpg` | Close crop of roadside/pole signage includes a vehicle registration plate with several characters visibly discernible; upper sign is too blurred to read confidently. | **Strong privacy flag: partially legible registration identifier; mask plate and review sign context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/road_vehicle_t070.jpg` | Crop shows tree trunks, grass and a road; no vehicle or person is visible in the supplied image despite the filename. | **Flag: filename/content mismatch; verify crop provenance and object association** |

## Batch 18 — CCTV-002 scene and verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/objs/scene_zoom_t053.jpg` | Reframed view of an empty section of parking lot, trees and road; no people or vehicle identifiers visible. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_001.jpg` | Full parking-lot frame with numerous vehicles; a dark sedan is crossing the foreground. No pedestrian clearly visible in this frame. Commercial vehicle markings and plates appear in the scene but are not confidently readable at this scale. | **Flag for vehicle-identifier and commercial-marking/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_002.jpg` | A pedestrian in a light shirt is visible at the far-right edge; face is small but head and clothing are distinguishable. Numerous vehicles and plates remain in view. | **Flag: person present; review face visibility, plates and source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_003.jpg` | Pedestrian remains at the far-right edge, closer to the parked vehicles; face is still small. A light pickup is moving through the lot. | **Flag: person present; review face visibility, plates and source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_004.jpg` | Pedestrian remains visible near the right edge, with face/head discernible at this scale. Multiple vehicles and commercial markings are present. | **Flag: person present; review face visibility, plates and source permissions** |

## Batch 19 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_005.jpg` | Pedestrian in a light shirt remains near the far-right foreground; head/face and clothing are discernible, though small. A light pickup is crossing the lot; many vehicles and plates are present. | **Flag: person visible; vehicle identifiers and commercial markings need review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_006.jpg` | Same pedestrian continues walking along the right side of the parking lot. Face remains visible at small scale. | **Flag: person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_007.jpg` | Pedestrian is closer to the foreground vehicles; face/head and clothing remain distinguishable. Pickup has moved across the lot. | **Flag: person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_008.jpg` | Pedestrian continues past parked vehicles; face visible in the full frame. Pickup continues moving. | **Flag: person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_009.jpg` | Pedestrian remains visible near the foreground SUV; face/head and clothing are discernible. Vehicle plates and commercial markings remain in scene. | **Flag: person visible; review face masking, plates and source permissions** |

## Batch 20 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_010.jpg` | Pedestrian is close to a foreground SUV; head and face are discernible, with clothing visible. Multiple vehicle plates and commercial markings remain in frame. | **Flag: person visible; mask face and review vehicle identifiers/markings** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_011.jpg` | Pedestrian is largely occluded by the foreground SUV; only part of the head is visible. A pickup exits toward the left. Vehicle identifiers remain in scene. | **Flag: partial person visibility; vehicle identifiers require review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_012.jpg` | Pedestrian reappears beside the SUV, partly occluded; face/head and upper body visible. Several vehicles and plates remain. | **Flag: person visible; mask face and review vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_013.jpg` | Pedestrian walks across the open foreground toward the centre-left; face and clothing are visible at this scale. A dark sedan moves across the far-left row. | **Strong privacy flag: identifiable person visible; mask or replace unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_014.jpg` | Pedestrian continues across the open foreground; face/head and clothing remain discernible. Vehicle plates and commercial markings remain visible. | **Strong privacy flag: identifiable person visible; mask or replace unless publication permission is documented** |

## Batch 21 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_015.jpg` | The pedestrian is now crossing the open foreground toward the left side of the frame. Full body, face/head and clothing are visible, though facial detail is limited by the wide CCTV image. Vehicle plates and commercial markings remain in view. | **Strong privacy flag: person visible; mask face and review vehicle identifiers/markings** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_016.jpg` | The same pedestrian continues leftward across the open parking area; face/head and clothing remain discernible. Multiple vehicles and plates remain visible. | **Strong privacy flag: person visible; mask face and review vehicle identifiers/markings** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_017.jpg` | Pedestrian progresses farther left, approaching the row of foreground parked cars. Person remains clearly present; vehicle identifiers are also present in the scene. | **Strong privacy flag: person visible; mask face and review vehicle identifiers/markings** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_018.jpg` | Pedestrian reaches the left foreground and is partly occluded by a parked vehicle; head/face and upper body remain visible. | **Flag: partially occluded person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_019.jpg` | Pedestrian remains near the left foreground, partly obscured by parked vehicles. Head/upper body are still visible; plates and vehicle markings remain throughout the parking lot. | **Flag: partially occluded person visible; review face masking and vehicle identifiers** |

## Batch 22 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_020.jpg` | The pedestrian is at the extreme left foreground, partly hidden behind a white van; head and upper body remain visible. Vehicle plates appear throughout the scene, but their characters are not reliably readable at this full-frame scale. | **Flag: partially visible person; confirm publication permission or mask; inspect plates at native crop** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_021.jpg` | Only the pedestrian's head is visible above/behind the white van at the far-left edge. No face detail can be confidently assessed at this scale. | **Flag: partial person visibility; source/publication permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_022.jpg` | The pedestrian is almost entirely outside the frame at the far-left edge; a small portion of the person remains visible. Vehicle plates are present but not clearly legible in this view. | **Flag: marginal person visibility; native-resolution plate review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_023.jpg` | The pedestrian is no longer visible. The frame shows the parking lot and parked vehicles; plates are present but not reliably readable at full-frame scale. | **No person visible; review plates at native crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_024.jpg` | The pedestrian remains out of frame. Parking lot and vehicles only; plates/vehicle markings are present but not reliably readable at this scale. | **No person visible; review plates at native crop before publication** |

## Batch 23 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_025.jpg` | Parking lot and vehicles; no pedestrian discernible in the frame. Vehicle plates/markings remain visible but are not reliably readable at this full-frame scale. | **Flag for native-resolution vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_026.jpg` | A pedestrian reappears at the far-left edge beside parked vehicles; head and upper body are visible, with face detail limited by distance. | **Flag: person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_027.jpg` | Pedestrian remains at the far-left side, partly occluded by vehicles; head/upper body discernible. | **Flag: partially occluded person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_028.jpg` | Pedestrian remains partly visible at the far-left edge behind/alongside parked vehicles. | **Flag: partially occluded person visible; review face masking and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_029.jpg` | Pedestrian is no longer clearly visible; a small partial human-shaped area remains near the far-left edge and is partly obscured by vehicles. | **Flag: ambiguous partial person at edge; verify source frame and review vehicle identifiers** |

## Batch 24 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_030.jpg` | Pedestrian in a light shirt is visible at the far-left side between parked vehicles; head/face and upper body discernible. Vehicle plates remain throughout the scene. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_031.jpg` | Pedestrian moves along the left row of parked vehicles; face and clothing are visible at this scale. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_032.jpg` | Same pedestrian remains in the left foreground, partly aligned with a parked vehicle; head/face and upper body visible. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_033.jpg` | Pedestrian continues along the left foreground, partly occluded by vehicles; head/upper body remain discernible. | **Flag: partially occluded person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_034.jpg` | Pedestrian remains near the left edge of the lot, walking past parked vehicles; face/head and clothing visible at wide-frame scale. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |

## Batch 25 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_035.jpg` | The same pedestrian in a light shirt and dark trousers walks diagonally through the lower-left parking area, carrying a small blue item. Head/face and clothing are clearly visible at this scale. Vehicle plates remain in view. | **Strong privacy flag: person visible; mask or replace unless publication permission is documented; review vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_036.jpg` | Pedestrian continues toward the lower centre-left; face/head and clothing remain discernible. | **Strong privacy flag: person visible; mask or replace unless publication permission is documented; review vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_037.jpg` | Pedestrian progresses across the open foreground, with face/head and upper body visible. | **Strong privacy flag: person visible; mask or replace unless publication permission is documented; review vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_038.jpg` | Pedestrian continues diagonally across the foreground; head/face and carried item remain visible. | **Strong privacy flag: person visible; mask or replace unless publication permission is documented; review vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_039.jpg` | Pedestrian remains in the lower-centre foreground, still walking with the blue item; head/face and clothing clearly discernible. | **Strong privacy flag: person visible; mask or replace unless publication permission is documented; review vehicle identifiers** |

## Batch 26 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_040.jpg` | Pedestrian in a light shirt is walking across the lower foreground toward the right; head/face and clothing are discernible. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_041.jpg` | Pedestrian approaches a parked dark vehicle in the foreground; head/face and upper body visible. | **Flag: person visible; review face masking and vehicle identifiers/source permissions** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_042.jpg` | Pedestrian continues along the front of the parked vehicle; face/head and clothing are clearly discernible at this scale. | **Strong privacy flag: person clearly visible; mask or replace unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_043.jpg` | Only the pedestrian's head/upper portion remains at the lower edge of the frame; partly cropped. | **Flag: partial person visibility; review source frame and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_044.jpg` | Parking lot and vehicles only; pedestrian is no longer visible. Registration plates/vehicle markings remain present and need native-resolution review. | **Flag for vehicle-identifier/source permission review** |

## Batch 27 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_045.jpg` | Parking lot and parked vehicles; no pedestrian discernible. Vehicle plates and commercial markings remain visible in the wide frame. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_046.jpg` | Same parking-lot view; no person visible. Vehicle identifiers remain present but are not confidently readable at this scale. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_047.jpg` | Same scene with vehicles; no pedestrian discernible. Plates/markings remain in view. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_048.jpg` | Same parking-lot scene; no person visible. Vehicle identifiers remain present. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_049.jpg` | Same scene; no pedestrian visible. Vehicle plates and commercial markings remain in frame. | **Flag for vehicle-identifier/source permission review** |

## Batch 28 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_050.jpg` | Wider reframed view of the parking lot from a different camera crop; numerous vehicles, but no pedestrian discernible. Registration plates and commercial vehicle markings are present. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_051.jpg` | Similar wide parking-lot view; no person visible. Vehicle plates/markings remain in scene. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_052.jpg` | Blurred, tighter crop of the parking lot and vehicles; no person discernible. Plate detail is too blurred to assess. | **No person visible; source/provenance and vehicle-identifier review at native resolution** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_053.jpg` | Reframed crop of an empty parking area with tree, pavement and parking lines; no person or vehicle identifier visible. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_054.jpg` | Close scene crop showing tree trunks, grass and roadway; no person or vehicle visible. | No obvious visual privacy concern |

## Batch 29 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_055.jpg` | Tight reframed view of tree, grass, curb and empty parking spaces; no person or vehicle visible. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_056.jpg` | Similar empty parking-space/tree crop; no person or vehicle visible. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_057.jpg` | Reframed view of empty pavement, parking lines, trees and grass; no person or vehicle visible. | No obvious visual privacy concern |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_058.jpg` | Tighter view of trees, road and parking spaces; no person or vehicle visible. Overlay at lower left reads `135.5,004.0`, which may be coordinate/telemetry data and needs source-context review. | **Flag: possible location/telemetry overlay; verify meaning and whether it reveals sensitive source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_059.jpg` | Tighter view of roadside trees, curb and empty spaces; no person or vehicle visible. Overlay at lower left reads `139.0,004.0`, potentially coordinate/telemetry data. | **Flag: possible location/telemetry overlay; verify meaning and whether it reveals sensitive source context** |

## Batch 30 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_060.jpg` | Tight crop of utility poles, grass, roadway and empty parking spaces. No person or vehicle visible. A small pole-mounted label is present; text is too small to read confidently. Lower-left overlay reads `140.3,004.0`. | **Flag: possible coordinate/telemetry overlay and pole label; verify source context and whether either reveals sensitive location/infrastructure details** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_061.jpg` | Similar pole/road/empty parking-space view. No person or vehicle visible. Pole-mounted labels are visible and lower-left overlay reads `141.8,004.0`. | **Flag: possible coordinate/telemetry overlay and pole labels; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_062.jpg` | Same scene; no person or vehicle visible. Pole labels remain visible; overlay reads `141.8,004.0`. | **Flag: possible coordinate/telemetry overlay and pole labels; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_063.jpg` | Reframed view of utility poles, grass and empty roadway/parking spaces. No person or vehicle visible. Pole-mounted labels and overlay `142.2,004.0` are present. | **Flag: possible coordinate/telemetry overlay and pole labels; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_064.jpg` | Similar empty roadside/parking crop. No person or vehicle visible. Small labels on pole and overlay `142.2,004.0` remain visible. | **Flag: possible coordinate/telemetry overlay and pole labels; verify source context** |

## Batch 31 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_065.jpg` | Tight crop of utility poles, hedge, grass, road and empty parking spaces. No person or vehicle visible. A pole-mounted sticker/label includes a short alphanumeric code; other small labels are present. | **Flag: pole-mounted identifier/signage; verify whether it is a location or infrastructure identifier and mask if sensitive** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_066.jpg` | Similar empty roadside crop; no person or vehicle visible. The same pole labels and alphanumeric code remain in view. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_067.jpg` | Same scene and pole labels; no person or vehicle visible. The short alphanumeric code is more central and legible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_068.jpg` | Empty parking/roadside crop with pole-mounted labels; no person or vehicle visible. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_069.jpg` | Same empty scene; no person or vehicle visible. Pole labels and short alphanumeric code remain present. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 32 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_070.jpg` | Utility-pole/roadside crop with a white vehicle partially visible on the distant road behind the hedge. No person visible. Pole-mounted labels and an alphanumeric code remain in frame. | **Flag: pole-mounted identifier/signage; review source context; vehicle only partially visible** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_071.jpg` | Empty roadside/parking crop with utility poles and labels; no person or vehicle visible. | **Flag: pole-mounted identifier/signage; verify whether it reveals infrastructure/location details** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_072.jpg` | Same empty scene; pole-mounted labels and short alphanumeric code remain visible. No person or vehicle. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_073.jpg` | Similar roadside/parking crop; no person or vehicle visible. Pole labels remain visible. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_074.jpg` | Same empty roadside/parking crop; no person or vehicle visible. Pole labels and alphanumeric code remain in frame. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 33 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_075.jpg` | Tight roadside crop with utility poles, hedge, grass and empty parking spaces. No person or vehicle visible. Pole-mounted labels and a short alphanumeric code remain visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_076.jpg` | Same empty roadside/parking scene; no person or vehicle visible. Pole labels remain in frame. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_077.jpg` | Same view; no person or vehicle visible. Alphanumeric pole label remains legible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_078.jpg` | Empty roadside and parking spaces; no person or vehicle visible. Pole-mounted labels remain present. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_079.jpg` | Same empty scene with pole labels and short alphanumeric code; no person or vehicle visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 34 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_080.jpg` | Empty roadside/parking crop with utility poles, hedge and grass. No person or vehicle visible. Pole-mounted labels and short alphanumeric code remain visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_081.jpg` | Same empty scene; no person or vehicle visible. Pole labels remain in frame. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_082.jpg` | Similar empty roadside view; no person or vehicle visible. The alphanumeric pole label remains legible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_083.jpg` | Same empty parking/roadside crop with pole labels; no person or vehicle visible. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_084.jpg` | Same empty roadside/parking crop; no person or vehicle visible. Pole-mounted labels and code remain in view. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 35 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_085.jpg` | Empty roadside/parking crop with utility poles, hedge and grass. No person or vehicle visible. Pole labels and short alphanumeric code remain in view. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_086.jpg` | Same empty scene; no person or vehicle visible. Pole-mounted labels remain. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_087.jpg` | Same roadside view; no person or vehicle visible. The alphanumeric pole label is still legible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_088.jpg` | Empty parking/roadside crop; no person or vehicle visible. Pole labels remain present. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_089.jpg` | Same empty scene with pole-mounted labels and alphanumeric code; no person or vehicle visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 36 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_090.jpg` | Static roadside/parking crop with utility poles, hedge and grass. No person or vehicle visible. Pole-mounted labels and alphanumeric code remain in view. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_091.jpg` | Same empty roadside scene; no person or vehicle visible. Pole labels remain present. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_092.jpg` | Same scene; no person or vehicle visible. The short alphanumeric pole label is legible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_093.jpg` | Empty roadside/parking crop with pole labels; no person or vehicle visible. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_094.jpg` | Same empty scene with pole-mounted labels and alphanumeric code; no person or vehicle visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 37 — CCTV-002 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_095.jpg` | Static roadside/parking crop with utility poles, hedge and grass. No person or vehicle visible. Pole-mounted labels and alphanumeric code remain visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_096.jpg` | Same empty scene; no person or vehicle visible. Pole labels remain in view. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_097.jpg` | A dark minivan passes from right to left across the road. A driver/occupant silhouette is visible through the side window, but facial detail is not discernible. Pole-mounted labels remain in frame. | **Flag: vehicle occupant potentially visible; review privacy treatment and pole identifier** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_098.jpg` | Rear portion of the passing dark vehicle exits at the far-left edge; no person discernible. Pole-mounted labels remain visible. | **Flag: partial vehicle at edge; pole identifier/source context review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_099.jpg` | Vehicle has exited; empty roadside/parking crop with utility poles and labels. No person visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |

## Batch 38 — CCTV-002 pole-label close-ups (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_100.jpg` | Close-up of a pole-mounted alphanumeric label and a second blurred sign. No person or vehicle visible. The lower label is clearly readable as a short code. | **Strong privacy/context flag: legible infrastructure/location identifier; determine what it identifies and mask unless confirmed non-sensitive** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_101.jpg` | Same close-up; alphanumeric code remains legible, with another blurred sign above. No person or vehicle visible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_102.jpg` | Same pole-label close-up; no person or vehicle visible. The alphanumeric code is legible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_103.jpg` | Same close-up of pole labels; no person or vehicle visible. Code remains legible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_104.jpg` | Same close-up; no person or vehicle visible. Alphanumeric pole label is legible and fills a substantial part of the crop. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |

## Batch 39 — CCTV-002 close-ups and CCTV-003 parking-lot views (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_105.jpg` | Close-up of the same pole-mounted alphanumeric label and a second blurred sign. No person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-002/snapshot/verification/frame_106.jpg` | Same close-up of pole labels; no person or vehicle visible. The alphanumeric code remains legible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/first_wide_parking_view_t008.jpg` | Wide parking-lot view with many parked vehicles, visible registration plates and commercial vehicle markings. No pedestrian clearly discernible; occupants through windows are not sufficiently resolved to assess. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/late_lot_state_t100.jpg` | Wide parking-lot view with many vehicles and visible plates. No pedestrian clearly discernible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/mid_lot_later_state_t060.jpg` | Parking lot with a light-colored car door open; two people are standing beside/leaning into the vehicle. Heads and upper bodies are visible, though facial detail is limited by distance. Numerous vehicle plates are also present. | **Strong privacy flag: people visible; mask/replace unless publication permission is documented; review vehicle identifiers** |

## Batch 40 — CCTV-003 parking-lot and pole-sign examples (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/mid_lot_vehicle_arrangement_t042.jpg` | Wide parking-lot scene with numerous vehicles and visible registration plates; no pedestrian clearly discernible. | **Flag for vehicle-identifier/source permission review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/moving_light_vehicle_t090.jpg` | A light-colored sedan is moving through the parking lot; a driver/occupant is faintly visible through the side window, but facial detail is not discernible. Vehicle plates remain visible elsewhere in the frame. | **Flag: vehicle occupant potentially visible; review privacy treatment and vehicle identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/opening_sign_and_pole_t000.jpg` | Close-up of a pole-mounted alphanumeric label and additional signage; no person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/sign_pole_wider_view_t003.jpg` | Wider crop of the same pole and multiple labels, including the alphanumeric code; no person visible. | **Strong privacy/context flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/objs/wide_lot_and_background_t027.jpg` | Wide parking-lot/background view with many vehicles and visible plates/markings; no pedestrian clearly discernible. | **Flag for vehicle-identifier/source permission review** |
## Batch 41 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_000.jpg` | Close-up of pole-mounted alphanumeric label and a second blurred sign; no person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_001.jpg` | Same close-up; no person or vehicle visible. The code remains legible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_002.jpg` | Same pole-label close-up; no person or vehicle visible. Code remains legible. | **Strong privacy/context flag: legible identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_003.jpg` | Wider pole/roadside view with multiple stickers and the same alphanumeric code; no person or vehicle visible. | **Flag: potentially identifying infrastructure/location label and signage; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_004.jpg` | Wider roadside/parking crop with pole labels and code; no person or vehicle visible. | **Flag: potentially identifying infrastructure/location label and signage; review and mask if needed** |

## Batch 42 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_005.jpg` | Wider roadside/parking view with utility poles, hedge, empty spaces and a red vehicle partly entering at the lower-right edge. Pole-mounted labels and alphanumeric code remain visible. No pedestrian discernible. | **Flag: pole identifier and partial vehicle/source context review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_006.jpg` | Similar view with red vehicle partly visible at lower-right; pole labels remain in view. No person discernible. | **Flag: pole-mounted identifier/signage and partial vehicle review** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_007.jpg` | Wider parking-lot scene with several vehicles, visible plates and commercial markings. No pedestrian clearly discernible. | **Flag for vehicle-identifier/source permission review; pole labels also visible** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_008.jpg` | Parking lot with red minivan and multiple other vehicles; plates/markings visible. No person discernible. | **Flag for vehicle-identifier/source permission review; pole labels also visible** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_009.jpg` | Blurred tighter crop of roadside pole/labels with part of a red vehicle at lower right. No person discernible. The alphanumeric pole label remains visible though blurred. | **Flag: pole identifier and vehicle fragment; verify source context and masking needs** |

## Batch 43 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_010.jpg` | Tight roadside crop with utility poles, empty parking spaces and pole-mounted labels; no person or vehicle visible. The alphanumeric code is present but blurred at this scale. | **Flag: infrastructure/location label; verify source context and masking needs** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_011.jpg` | Similar empty roadside crop; pole labels remain visible, with code partly legible. No person or vehicle visible. | **Flag: potentially identifying infrastructure/location label; review and mask if needed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_012.jpg` | Tighter crop of pole labels and code; no person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_013.jpg` | Close crop of pole-mounted labels and alphanumeric code; no person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_014.jpg` | Close crop of the same pole labels/code; no person or vehicle visible. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |

## Batch 44 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_015.jpg` | Empty parking/roadside view with utility poles, hedge, grass and road. No person or vehicle visible. Pole-mounted labels remain visible; lower-right `ID:001` is a generic overlay. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_016.jpg` | Same empty roadside/parking view. No person or vehicle visible. Pole labels and generic `ID:001` overlay remain. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_017.jpg` | Similar empty parking/roadside view; no person or vehicle visible. Pole-mounted labels and generic `ID:001` overlay remain. | **Flag: pole-mounted identifier/signage; verify source context** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_018.jpg` | Tighter crop of the pole-mounted labels; no person or vehicle visible. A short alphanumeric pole label is discernible. Generic `ID:001` overlay remains. | **Strong privacy/context flag: legible infrastructure/location identifier; establish what it identifies and mask unless confirmed non-sensitive** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_019.jpg` | Close-up of the same pole-mounted alphanumeric label; no person or vehicle visible. The code is clearly legible in this crop. Generic `ID:001` overlay remains. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |

## Batch 45 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_020.jpg` | Tight crop of pole-mounted labels. A short alphanumeric infrastructure code is clearly legible; no person or vehicle visible. Generic `ID:001` overlay remains. | **Strong privacy/context flag: legible infrastructure/location identifier; establish what it identifies and mask unless confirmed non-sensitive** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_021.jpg` | Same close-up and legible pole-mounted code; no person or vehicle visible. Generic `ID:001` overlay remains. | **Strong privacy/context flag: legible infrastructure/location identifier; source-context review and masking required before clearance** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_022.jpg` | Wider view of the same labelled pole in an otherwise empty parking area. No person or vehicle visible; code remains discernible. Generic `ID:001` overlay. | **Flag: potentially identifying infrastructure/location label; verify source context and masking needs** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_023.jpg` | Wide empty parking-lot view with utility poles, hedge and road. No people or vehicles visible; pole labels are small in this view. Generic `ID:001` overlay. | **Flag: infrastructure label present; no direct personal information observed** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_024.jpg` | Wider empty parking-lot view; no person visible. A partial vehicle enters at the lower-right edge, with no registration plate discernible. Pole-mounted labels remain visible; generic `ID:001` overlay. | **Flag: pole identifier/source context; partial vehicle fragment, no plate or occupant discernible** |

## Batch 46 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_025.jpg` | Parking lot with several cars and a few commercial vehicles. Multiple vehicle registration plates are present; at this image scale characters are not reliably readable. No people or occupants discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; assess source-resolution plate legibility and masking** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_026.jpg` | Wider parking-lot view with numerous cars and commercial vehicles. Registration plates are present on multiple vehicles, but are small/soft at displayed scale. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; verify plate legibility at source resolution** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_027.jpg` | Wider parking-lot view with many parked vehicles and several commercial vehicles. Plates are present; no individual characters confidently readable from this frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; verify plate legibility at source resolution** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_028.jpg` | Similar parking-lot view with numerous vehicles and visible registration plates. No people discernible; plate characters not confidently readable at this scale. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; verify plate legibility at source resolution** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_029.jpg` | Parking lot with many vehicles, including several facing the camera; multiple plates are clearly present, though characters remain too small/soft to transcribe reliably from this frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; inspect source-resolution plates and mask unless publication permission is documented** |

## Batch 47 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_030.jpg` | Elevated wide parking-lot view with numerous parked vehicles. Registration plates are present on several cars; at source resolution the plate areas remain too small/soft for reliable character reading. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_031.jpg` | Similar parking-lot view with many vehicles and visible plates. Characters are not reliably legible in the source frame. No people discernible. Generic `ID:001` and numeric camera/time-style overlay appear at the lower edge. | **Flag for vehicle-identifier/source permission review; overlays appear generic, not personal identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_032.jpg` | Wide view of the same lot; multiple vehicle plates are visible but too small/soft for confident reading. No people discernible. Generic `ID:001` and numeric camera/time-style overlay. | **Flag for vehicle-identifier/source permission review; overlays appear generic, not personal identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_033.jpg` | Nearly the same parking-lot composition as frame 032, with multiple visible plates but no reliably readable characters. No people discernible. Generic `ID:001` and numeric camera/time-style overlay. | **Flag for vehicle-identifier/source permission review; overlays appear generic, not personal identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_034.jpg` | Similar wide parking-lot view with numerous vehicles and visible plates; no plate characters reliably readable. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |

## Batch 48 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_035.jpg` | Elevated wide parking-lot view with many parked vehicles. Registration plates are present on several cars; inspected at 1920×1080 and plate characters are too small/soft to read reliably. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_036.jpg` | Similar elevated parking-lot view; multiple plates visible but not reliably legible at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_037.jpg` | Wide view of the same lot, with numerous parked cars and visible plates. Characters remain too small/soft for reliable reading at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_038.jpg` | Similar parking-lot view with multiple vehicles and plates. No plate characters reliably readable at source resolution; no people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_039.jpg` | Similar wide parking-lot scene; multiple registration plates are visible but too small/soft to transcribe reliably. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |

## Batch 49 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_040.jpg` | Elevated wide parking-lot view with numerous parked vehicles. Registration plates are present on vehicles in the foreground and middle distance; characters are not reliably readable at source resolution. No people discernible. Generic camera/date-time-style overlay and `ID:001` overlay appear along the bottom. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_041.jpg` | Similar parking-lot view with multiple visible vehicle plates; no characters reliably readable at source resolution. No people discernible. Generic camera/date-time-style and `ID:001` overlays. | **Flag for vehicle-identifier/source permission review; overlays appear generic, not personal identifiers** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_042.jpg` | Wide lot view with many parked vehicles and visible plates; plate characters are too small/soft for reliable reading. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_043.jpg` | Similar wide parking-lot view; multiple plates visible but not reliably legible at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_044.jpg` | Similar wide lot view with numerous vehicles and visible registration plates; no plate characters reliably readable. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |

## Batch 50 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_045.jpg` | Elevated parking-lot view with numerous vehicles. Several registration plates are discernible at source resolution, including front-facing plates; no pedestrians visible. Generic `ID:001` overlay. | **Strong privacy flag: vehicle registration plates visibly readable; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_046.jpg` | Similar parking-lot view with numerous vehicles and readable registration plates. No pedestrians discernible. Generic `ID:001` overlay. | **Strong privacy flag: vehicle registration plates visibly readable; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_047.jpg` | Same lot view; a pedestrian begins entering at the bottom edge, with head/upper body partly visible. Multiple vehicle plates are readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: identifiable pedestrian partially visible and readable vehicle plates; mask/replace pedestrian and plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_048.jpg` | Pedestrian is more fully visible at the bottom of frame, including side profile/head and upper body. Multiple vehicle plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: identifiable person visible and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_049.jpg` | Two pedestrians are visible at the bottom of frame, viewed mostly from behind/side; heads and upper bodies are visible. Multiple vehicle plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: two people visible and readable vehicle plates; mask/replace people and plates before publication unless permission is documented** |

## Batch 51 — CCTV-003 verification frames (5 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_050.jpg` | Parking-lot view with numerous vehicles. A pedestrian is partly visible at the bottom edge, mainly lower body/legs; head and face are outside the frame. Multiple vehicle registration plates are visible and several appear readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle plates; partial pedestrian body also present. Mask plates and assess whether crop should exclude the person before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_051.jpg` | Similar parking-lot view; pedestrian remains partly visible at bottom edge, mainly legs/lower body, with no face visible. Multiple vehicle plates are visible; several appear readable. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle plates; partial pedestrian body present. Mask plates and assess crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_052.jpg` | Similar scene; a pedestrian's lower body/legs remain at the bottom edge, no head or face visible. Multiple vehicle plates are visible, some readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle plates; partial pedestrian body present. Mask plates and assess crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_053.jpg` | Pedestrian has moved out of the visible crop. Numerous vehicles remain; multiple registration plates are visible and some appear readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_054.jpg` | Similar parking-lot view with numerous vehicles; no pedestrian discernible. Multiple registration plates are visible, some readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |

## Batch 52 — CCTV-003 verification frames (10 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_055.jpg` | Elevated parking-lot view. Two people are visible beside a light-colored vehicle at the lower-left/center; heads and upper bodies are visible, one person partly occluded by the vehicle/door. Numerous vehicle registration plates are visible and several are readable at source resolution. Generic `ID:001` overlay. | **Strong privacy flag: people and readable vehicle plates; mask/replace people and plates before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_056.jpg` | Same parking-lot scene; two people remain beside the light-colored vehicle, with heads/upper bodies visible. Multiple plates remain readable. Generic `ID:001` overlay. | **Strong privacy flag: people and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_057.jpg` | Two people are clearly visible beside the vehicle, one standing near the driver-side area and another leaning/standing at the open door; heads and upper bodies visible. Numerous registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: two people and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_058.jpg` | Same two people beside the vehicle, one partly occluded by the open door; heads and upper bodies visible. Multiple registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: two people and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_059.jpg` | Two people remain beside the open vehicle door. A dark sedan is also moving through the lot; occupant not clearly discernible. Numerous parked-vehicle plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: people and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_060.jpg` | Two people remain at the open vehicle; one leans into the passenger compartment. A dark sedan crosses the central driving lane; occupant detail is not clear. Numerous parked-vehicle plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: people and readable vehicle plates; mask/replace both before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_061.jpg` | Dark sedan continues across the lot. One person remains partly visible beside the open vehicle door, with head/upper-body area partly obscured by the adjacent vehicle. Numerous registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: partial person and readable vehicle plates; mask plates and assess person crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_062.jpg` | Moving sedan has progressed toward the left side. A person is still partly visible/occluded beside the open vehicle at the lower-left. Numerous registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: partial person and readable vehicle plates; mask plates and assess person crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_063.jpg` | Sedan is nearly out of frame at the left. A small portion of a person remains visible beside the open vehicle, largely occluded. Numerous registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: partial person and readable vehicle plates; mask plates and assess person crop before publication** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_064.jpg` | Sedan has exited. A person remains partly visible behind/next to the open vehicle door; only a limited portion of the upper body is visible. Numerous registration plates are readable. Generic `ID:001` overlay. | **Strong privacy flag: partial person and readable vehicle plates; mask plates and assess person crop before publication** |


## Batch 53 — CCTV-003 verification frames (10 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_065.jpg` | Elevated wide parking-lot view with many parked vehicles. Several front-facing registration plates in the foreground are readable at source resolution; other plates are present at distance. No pedestrian discernible. Some windshields show indistinct interior shapes/reflections, not classifiable as identifiable occupants. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_066.jpg` | Same parking-lot composition with small vehicle-position changes. Multiple foreground plates remain readable; no pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_067.jpg` | Same wide lot; several foreground registration plates are readable. No pedestrian discernible; indistinct windshield reflections/interiors do not establish identifiable occupants. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_068.jpg` | Same lot and parked vehicles; readable plates remain on several foreground cars. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_069.jpg` | Similar wide parking-lot view; multiple readable foreground plates. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_070.jpg` | Same lot with slight changes in vehicle positions; several plates remain readable in the foreground. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_071.jpg` | Wide lot view; multiple readable registration plates remain visible. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_072.jpg` | Same parking-lot scene; foreground vehicle plates remain readable. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_073.jpg` | Similar wide lot view; multiple foreground plates remain readable. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_074.jpg` | Same parking-lot view; readable foreground plates remain visible. No pedestrian discernible. Generic `ID:001` overlay. | **Strong privacy flag: readable vehicle registration plates; mask before publication unless explicit permission is documented** |


## Batch 54 — CCTV-003 verification frames (10 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_075.jpg` | Elevated wide parking-lot view with numerous parked vehicles. Registration plates are visible on several foreground and middle-distance cars; individual characters are small and not consistently legible in the full-resolution frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_076.jpg` | Same lot with slight vehicle-position changes. Multiple plates remain visible; characters are not consistently legible at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_077.jpg` | Wide parking-lot view; several foreground plates visible, but not consistently readable in the full frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_078.jpg` | Similar scene; multiple registration plates visible on foreground vehicles, with character-level legibility limited at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_079.jpg` | Same elevated lot view; vehicle positions shift slightly. Plates remain visible, but characters are not consistently legible in the full-resolution frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_080.jpg` | Similar parking-lot composition. Numerous vehicle plates are visible; individual characters are small and not consistently readable. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_081.jpg` | Wide lot with minor vehicle-position changes. Multiple plates visible; character-level reading is not reliable at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_082.jpg` | Same parking-lot scene; several vehicle plates visible, not consistently legible in the full frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_083.jpg` | Similar wide view; multiple plates remain visible, with characters too small/soft for reliable reading at source resolution. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_084.jpg` | Same elevated parking-lot scene; visible plates on several vehicles, but no reliable character-level reading from the full frame. No people discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier/source permission review; mask plates unless publication permission is documented** |


## Batch 55 — CCTV-003 verification frames (10 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_085.jpg` | Elevated parking-lot view with many parked vehicles. Multiple front-facing and rear-facing registration plates are visible; a few are partially legible in enlarged source crops, though most are too small/soft for reliable transcription. No clearly identifiable person discernible; windshield reflections/interior shapes remain ambiguous. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_086.jpg` | Same lot view with slight changes in vehicle positions. Multiple plates visible; some plate areas partially legible in source crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_087.jpg` | Similar parking-lot scene; multiple registration plates visible, with limited partial legibility in enlarged crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_088.jpg` | Same scene with small vehicle-position changes. Multiple plates visible; some partially legible in source crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_089.jpg` | Elevated lot view; multiple vehicle plates visible, some partly legible when enlarged. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_090.jpg` | Same parking-lot composition; multiple plates remain visible, with some partial character legibility in enlarged source crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_091.jpg` | Similar lot view; multiple plates visible, some partially legible in enlarged crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_092.jpg` | Same parking-lot view with minor vehicle movement; plates remain visible and some are partly legible in enlarged source crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_093.jpg` | Similar elevated lot view; several registration plates visible, with partial legibility in enlarged crop. No clearly identifiable person discernible. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_094.jpg` | Same scene; multiple plates visible, some partly legible in enlarged crop. No clearly identifiable person discernible; windshield shapes/reflections are ambiguous and not treated as confirmed occupants. Generic `ID:001` overlay. | **Flag for vehicle-identifier review; mask any legible plates before publication unless permission is documented** |


## Batch 56 — CCTV-003 verification frames (10 images)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_095.jpg` | Elevated parking-lot view with numerous parked vehicles. Several front-facing registration plates are visible; at least some characters are discernible in enlarged source crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_096.jpg` | Same lot view with minor vehicle-position changes. Several front-facing plates remain visible, with limited character legibility in enlarged crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_097.jpg` | Similar parking-lot view; multiple vehicle plates visible, some partly legible when enlarged. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_098.jpg` | Same scene with slight vehicle movement; front-facing plates remain visible, some partly legible in source crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_099.jpg` | Parking-lot view with numerous vehicles; several foreground plates visible and partly legible when enlarged. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_100.jpg` | Similar view with minor vehicle-position changes. Multiple front-facing plates remain visible, with some partial legibility in enlarged source crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_101.jpg` | Same lot view; several plates visible, some partially legible in enlarged crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_102.jpg` | Similar parking-lot scene; multiple plates visible, with limited character legibility when enlarged. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_103.jpg` | Same scene; several vehicle plates visible, some partly legible in source crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-003/snapshot/verification/frame_104.jpg` | Parking-lot view with multiple front-facing vehicle plates; some characters partly legible in enlarged source crops. No pedestrian discernible. Generic `ID:001` overlay. | **Flag: vehicle registration plates; mask visible/legible plates before publication unless permission is documented** |


## Batch 57 — MP4 video visual review (4 videos)

| Asset | Visual finding | Status |
|---|---|---|
| `PACKETS/examples/videos/A_Trip_to_the_Moon_FV_Packet/omni_rendering.mp4` | 10-second, 1280×720 rendered sequence. Sampled at 1-second intervals. Stylized theatrical/fictional male characters in costume move through illustrated moon, mushroom-grotto and stage scenes. No real-person identity, personal text, or other personal information observed. An AAC audio stream is present; audio content was not reviewed in this visual audit. | **No visual personal-data concern observed; audio review remains open** |
| `PACKETS/examples/videos/Alice_in_wonderland/omni_rendering.mp4` | 10-second, 1280×720 rendered sequence. Sampled at 1-second intervals. Stylized storybook girl and anthropomorphic white rabbit in a field and burrow scene. Human figure is a rendered story character; no real-person identity or personal text observed. An AAC audio stream is present; audio content was not reviewed in this visual audit. | **No visual personal-data concern observed; audio review remains open** |
| `PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/FV_CCTV_snapshot_TD_reconstruction.mp4` | 212-second, 1280×720 reconstruction/timeline video at 1 frame per second. Reviewed a 2-second-interval sample across the complete duration, including CCTV-001/002/003 segments, pole-label close-ups and parking-lot views. No clearly discernible pedestrians/faces in sampled frames. Multiple vehicle registration plates are visible in parking-lot segments; a pole-mounted alphanumeric label is legible in the CCTV-002/003 close-up segment. Generic camera/time and `ID:001` overlays are present. No audio stream. | **Strong privacy/context flag: mask visible vehicle plates and the legible pole-mounted identifier; verify source context before publication** |
| `PACKETS/examples/videos/Old_macdonald/omni_rendering.mp4` | 10-second, 1280×720 rendered sequence. Sampled at 1-second intervals. Stylized cartoon farmer and farm animals in an illustrated setting. No real-person identity, personal text, or other personal information observed. An AAC audio stream is present; audio content was not reviewed in this visual audit. | **No visual personal-data concern observed; audio review remains open** |

**Video-review limitation:** The three 10-second clips were sampled once per second; the 212-second CCTV reconstruction was sampled every two seconds (the source is 1 fps). This is a visual sampling audit, not a frame-by-frame examination. Audio tracks in the three rendered clips were not listened to or transcribed, so spoken names or other audio-only personal data are not cleared.

## Historical next-step note

The initial next-step list above is superseded by the dated reassessment and closeout addenda below. In particular, the handwritten-name flag was withdrawn and blanket CCTV masking was downgraded after source-context review. The three AAC audio tracks remain unreviewed and are explicitly not audio-cleared.


## Addendum — privacy-context and screen-capture reassessment (2026-11-12)

This addendum refines earlier flags without deleting the historical visual observations above.

### Screen-capture / system-privacy check
- Reviewed the complete media inventory and its paths (305 raster images and 4 videos). No desktop, browser, application-window, terminal, taskbar, or other user-system screenshot was identified.
- The non-CCTV image examples are scene photographs, LiDAR visualizations, and an astronomy visualization. The remaining media are the three rendered story videos and the CCTV source/reconstruction material.
- This is a corpus-content finding, not a claim about material outside this archive. No user-system screenshot has been added, generated, or uploaded as part of this audit.

### Reassessment of the desk image
- Re-opened `PACKETS/examples/images/desk_with_objects/Desk_with_objects_for_editathon.jpg`.
- The handwritten text reads as a display/sign referring to **Mileva Marić Einstein** in a Wikimedia event/workspace scene. It is a historical/public name in an exhibit-like context, not evidence of a private individual's name on a personal bag as previously recorded.
- Withdraw the earlier “personal name” privacy flag. Retain ordinary source/licensing and provenance checks for the photograph.

### CCTV context and disposition
- The source is identified in the packet provenance notes as Supercircuits' BLK-HDPTZ12 camera demonstration, and the Wikimedia Commons file description explicitly describes the pole-mounted license plate as a distant test target (approximately 360 ft from the camera).
- Accordingly, the pole-mounted alphanumeric plate/label should not be treated as a personal identifier by default: it appears to be part of the demonstration target. Retain its source-context explanation in the audit; do not automatically require masking solely because it is legible.
- Vehicle registration plates on parked cars are contextual details in a public-facing parking-lot camera demonstration. Their presence alone is not a finding that the example exposes the user's system or a private record. Do not impose blanket masking of every plate as an automatic corpus rule. Escalate only where an identifier is clearly legible and the intended reuse, jurisdiction, context, or associated information creates a concrete privacy/legal concern.
- People seen in the public-facing parking-lot scene are incidental bystanders in the source demonstration, not evidence of targeted surveillance of the user. Presence alone is not a privacy breach. Reassess any clearly identifiable face or sensitive/private activity in the actual publication context rather than treating every person-shaped figure as a mandatory removal.
- These contextual judgments do not constitute legal advice or a final rights clearance. Commons' public-domain status and its stated automated-recording rationale remain a separate copyright/provenance question; the PTZ camera's deliberate pan/tilt/zoom/product-demo context warrants retaining that question for source verification.

### Metadata and audio checks
- A basic embedded-image EXIF scan of the 305 raster images found no GPS metadata and no populated camera-owner/artist fields. One image carried a whitespace-only description field. This does not inspect every possible container, sidecar, or video metadata field.
- The three rendered MP4 audio tracks remain unreviewed. This environment did not provide a dependable speech-listening/transcription pass, so audio-only names or personal information are not cleared.
- Video container metadata is addressed in this follow-up. Source permissions/provenance are reviewed in the 2026-11-13 closeout below.

### Updated disposition
- No user-system screenshot identified in the supplied archive.
- Desk-image “personal name” flag withdrawn after direct reinspection.
- CCTV blanket face/plate/pole-label masking flags downgraded to context-dependent review; preserve the observed content and source rationale, do not silently erase it.
- Corpus is **not yet fully cleared**: audio, source licensing/provenance, and any genuinely identifiable/sensitive CCTV content in the exact publication outputs remain to be resolved. Video container metadata was subsequently inspected in the follow-up below.


### Follow-up — video container metadata (2026-11-12)
- Inspected all four MP4 containers and stream metadata with ffprobe.
- The three rendered story MP4s identify Google as the muxing/encoding tool and contain H.264 video plus AAC audio. Their stream tags are generic handler/language/vendor fields; no author, owner, GPS, device serial, filesystem path, or user-account field was present in the inspected container metadata.
- The CCTV reconstruction identifies FFmpeg/libx264 as its encoder and contains H.264 video only; no audio stream or personal metadata fields were present in the inspected tags.
- This is a metadata-field inspection, not a content review of the AAC audio. The audio remains the one unresolved media-content check.


## Closeout — source rights and provenance review (2026-11-13)

This is a source-record review, not a legal opinion or a blanket grant of redistribution rights. The source pages and packet READMEs were checked to classify what is documented and what remains missing.

### Source records with identifiable published terms
- The five still-image packets cite Wikimedia Commons source pages. The current Commons pages list CC0 1.0 for the blue-chairs, desk/display, restaurant-kitchen, and small-room photographs; the kitchen-interior-design image is marked public domain by its author. The packet READMEs retain author/source attribution where provided. These terms are recorded at the source pages; they do not waive privacy/personality rights in depicted people.
- The desk/display photograph is a CC0 image by Medea7. Its Commons metadata includes iPhone 14 Pro camera make/model and capture timestamp, but the inspected metadata does not include GPS coordinates. These are source-photographer capture details, not evidence of a user's computer or system screenshot.
- Cat_jumping_backwards.webm is listed on Commons under CC BY 3.0, with author Mary Qin and source Vimeo URL recorded in the packet README. Attribution and licence-link requirements must be retained. The source video is not stored in the repository and the packet explicitly says its analysis was metadata-only; it is not visually verified by this audit.
- The Alice example identifies Project Gutenberg eBook #11 as its public-domain literary source. The Trip to the Moon example identifies the 1902 Georges Méliès film as its public-domain source. Both are text-/source-derived generation examples, not direct source-video analysis packets.
- The Supercircuits CCTV source is listed on Commons as public domain using the PD-automated rationale. The Commons description says the pole-mounted plate is a camera test target. The uploader's copyright rationale is recorded, but the factual premise that the footage was entirely automated without human input has not been independently established; the PTZ/product-demonstration context remains an open source-rights qualification.

### Provenance gaps retained
- The three CCTV working source segments are not stored in the repository. Packet snapshots and the derived reconstruction are not substitutes for the original media. Legacy packet folders lack current root-level viewpoint.json and packet_provenance.json; packet-local time intervals and sampling limitations remain as recorded in the CCTV README and manifests.
- The separate CCTV_Storage_Crisis example family has no source URL or acquisition record in its README and does not include its source video. Its source identity and reuse rights cannot be confirmed from the repository contents.
- KITTI example READMEs identify benchmark/sequence references, but the raw scans, calibration/pose inputs, and reproducible registration logs are absent. The exact acquisition and the rights/terms applicable to any source-derived visualizations are not established by the retained evidence. These examples remain illustrative and blocked for reproduction as their packet READMEs state.
- Mayan LiDAR examples cite PACUNAM / Garrison et al. research context, but the exact flight transects and raw point clouds are absent. The cited research context does not prove the provenance or licence of the particular generated/illustrative assets.
- The Hubble example lacks original exposures, archive identifiers, calibration data, and a reproducible registration log. Its visualization is illustrative; source-exposure provenance and rights for any source-derived material are not fully established by the retained packet.
- Environmental-edit pairs explicitly have unresolved source-asset provenance/licensing in their README and source-provenance records. The underlying source images were not supplied for independent inspection in this audit.
- The Old MacDonald MP4 is a generated packet-to-video experiment, not a source-video example. Its AAC soundtrack is an output track; it was not listened to or transcribed. The same audio limitation applies to the Alice and Trip to the Moon generated MP4s.

### Final disposition
- **System screenshot check: no screenshot of the user's system identified in the supplied archive.**
- Visual inventory: complete for the 305 images and four videos, with the sampling limits recorded above.
- Metadata: the inspected image EXIF and MP4 container fields revealed no GPS coordinates or user-account/system-path fields. Source-photographer camera metadata and capture timestamps may remain in source images.
- Audio: three AAC tracks remain unreviewed and are not audio-cleared; this is a known limitation, not a positive finding of personal information.
- Source rights/provenance: documented for some Wikimedia/public-domain examples; unresolved or incomplete for several CCTV, LiDAR, telescope, and environmental-edit examples as itemized above.
- **Do not describe the entire example corpus as fully privacy-, rights-, or provenance-cleared.** The visual privacy review did not identify a user-system screenshot; it does not cure missing source records or clear unreviewed audio.
