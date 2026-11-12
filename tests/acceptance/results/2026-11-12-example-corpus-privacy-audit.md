# Example Corpus Visual Privacy Audit

- Branch: `work/fv-example-corpus-privacy-audit-20261112`
- Baseline: merge commit `0d5b05715c5529790cc83a318c5f081e87b628ce`
- Inventory at start: 305 images, 4 videos (309 media files)
- Method: visual inspection in small batches; this log records only assets actually opened and inspected.
- Scope caveat: visual inspection does not establish source licensing, metadata cleanliness, or full provenance. Those require separate checks.

## Progress

- Reviewed: 45 / 309 media files (45 images, 0 videos)
- Remaining: 260 images and 4 videos (264 media files)
- Confirmed personal/user-owned material: none established.
- Follow-up flags: (1) handwritten personal name on a bag/sign in Batch 1; (2) a pedestrian's face is visible in the CCTV object crop below; (3) vehicle registration plates appear in the CCTV parking-lot crops, but are too small here to determine whether they are legible. Check source/context and whether masking is required before final clearance.

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

## Next

Continue with the next small batch from the repository media inventory. Do not mark the corpus cleared until all 305 images and 4 videos have been visually inspected and the flagged items have been resolved.
