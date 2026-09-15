# CODY-3 (in-house canonical superset + SAM3)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-3 (in-house canonical superset + SAM3)",
 "description": "CODY-3 (in-house canonical superset + SAM3). MoveAtlas pose family. 59 subjects. licence derived data CC BY 4.0.",
 "identifier": "https://doi.org/10.5281/zenodo.22232609",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A1 Tremor",
  "A8 Ballismus",
  "M1 Pose / video",
  "M4 Silhouette"
 ],
 "url": "https://doi.org/10.5281/zenodo.22232609",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_3</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8; M1, M4 |
| **Subjects** | 59 |
| **Status** | INGESTED (cody + cody_external silhouettes); paper in submission, arXiv within days; the FLAGSHIP derived-data release SHIPPED (Zenodo, 2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). REFINED RULING (owner, 2026-08-28): cody_3 holds THREE classes of imagery and only one is publishable: (1) patient raw videos NEVER; (2) segmentation renders where the patient remains visible NEVER; (3) segmentation-only files (pure contours/masks, no identifiable imagery) publishable, as are keypoints and lab... |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_3")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). REFINED RULING (owner, 2026-08-28): cody_3 holds THREE classes of imagery and only one is publishable: (1) patient raw videos NEVER; (2) segmentation renders where the patient remains visible NEVER; (3) segmentation-only files (pure contours/masks, no identifiable imagery) publishable, as are keypoints and lab
- **Redistribution**: yes for keypoints, labels and PURE segmentations (CC BY 4.0 on Zenodo); anything where a patient is visible never
- **Access route**: PUBLIC (derived) since 2026-09-01: the CODY Zenodo deposit v1.0.0 (concept DOI 10.5281/zenodo.22232609, version 10.5281/zenodo.22232610, CC BY 4.0, open access, 15.4 GB, Vasques/Cif/Demailly, verified 2026-09-02) ships dataset_0 (labels raw + merged-by-patient + merged-by-video kinematics + SAM3 timeseries: the 25 adults) and datasets_1_2_3 (SAM3 timeseries + results: the 2 adult, 12 pediatric and
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

-  (). **. .

## Data card (verbatim, with its evidence trail)


- Modality: pose (COCO-17 keypoints 2D + per-frame labels) AND SAM3 dense silhouette
  timeseries ; plus raw external video
- Source / URL: non-public in-house data (owner). NOT a public dataset.
- License: private, not shareable in current form (identifiable source video)
- Access: local only; raw video (100 GB) never leaves the machine (sovereignty)
- Version / retrieval date: provided 2026-07-10
- Status: processed (inventoried; canonical ingestion pending)
- UPDATE 2026-09-02: the FLAGSHIP derived release SHIPPED. CODY Zenodo
  deposit v1.0.0, published 2026-09-01 (Vasques, Cif, Demailly), concept
  DOI 10.5281/zenodo.22232609, version DOI 10.5281/zenodo.22232610,
  CC BY 4.0, open access, 15.4 GB, verified on the record page
  2026-09-02. Files: dataset_0_labels_raw.zip (373.3 MB),
  dataset_0_merged_by_patient.zip (5.0 GB), dataset_0_merged_by_video.zip
  (5.0 GB), dataset_0_sam3_timeseries.zip (4.0 GB),
  datasets_1_2_3_sam3_timeseries.zip (972.9 MB), datasets_1_2_3_results.zip
  (521.9 kB), MD5SUMS.txt, README.md. The deposit's dataset_0..3 numbering
  matches THIS card's internal numbering (dataset_0 = the 25 canonical
  adults), NOT the repo ids cody_1..3. Per the 2026-08-28 ruling, raw
  videos and patient-visible renders stay in-house; the deposit carries
  only de-identified derived data.
- UPDATE 2026-09-04: v1.1.0 published (version DOI
  10.5281/zenodo.22275553, API-verified, 9 files, 15.4 GB). The
  correction release: archive names now carry study + extraction
  pipeline, fixing the v1.0.0 provenance gap (v1.0.0 never named the
  pipelines: the YOLOv8 COCO-17 keypoints in labels_raw were
  described as "labels" only and SAM3 was not credited for the dense
  extraction; its description/MD5SUMS also listed a models.zip that
  was never uploaded - owner ruling 2026-09-03: models are not
  deposited, the listing is removed). Renames: dataset_0_labels_raw ->
  dataset_0_labels_raw_cody_1_2_yolo.zip (373 MB);
  dataset_0_merged_by_patient/video -> *_cody_3_sam3.zip (5.03/5.01
  GB); dataset_0_sam3_timeseries ->
  dataset_0_timeseries_cody_3_sam3.zip (3.97 GB);
  datasets_1_2_3_sam3_timeseries ->
  datasets_1_2_3_timeseries_cody_3_sam3.zip (973 MB);
  datasets_1_2_3_results -> datasets_1_2_3_results_cody_3_sam3.zip.
  NEW file: dataset_2_timeseries_cody_2_yolo.zip (48 MB, the
  pediatric YOLO keypoints CODY-2 inference consumes). Same bytes
  for the six carried-over archives (md5-identical to the local
  v1.0.0-named mirror; no re-pull needed - rename locally if a
  v1.1.0-named mirror is ever wanted).
- Number of subjects: 25 adults (C1-C4 + 21 P, canonical) + external cohorts
  (dataset_1: P28,P29 ; dataset_2: 12 pediatric ; dataset_3: 20) = 59 namespaced total
- Disorders covered: full 8-label hyperkinetic scheme (Dystonia, Tremor, Myoclonus,
  Chorea, Tics, Athetosis, Ballismus, Stereotypie)
- Frequency / resolution: ~33 fps ; keypoints in PIXELS ; SAM3 = ~160 contour points
- Specifics:
  - 555 real xlsx + 144 videos (mp4/wmv/mov, the 100 GB) + 2 summary csv + 1 py.
    Only 7 AppleDouble. This is the AUTHORITATIVE superset for the adult cohort.
  - Provenance pipeline: 01_train_labels_raw (per-rater dd/lc, per-patient, per-video)
    -> 02_train_merged_by_video -> 03_train_merged_by_patient (+ dataset_consensus).
  - External cohorts: 05_external_videos (raw video) + 06_external_sam3_outputs
    (SAM3 silhouette timeseries + mask/overlay/sidebyside mp4). These reuse P-numbers
    for DIFFERENT people (P1 in ds2 != P1 in ds3 != adult P1): namespaced as
    ext_ds1/ds2/ds3 in `datasets/pose/_cody_registry.csv`. LEAKAGE TRAP.
  - Subject-level multi-rater diagnosis for the external cohorts:
    `dataset_inference.xlsx` (sheets dataset_1/2/3; raters ds1: LC,DD,MCJ,CH,TW;
    ds2: LC,DD,GH,MCJ,JDOE; ds3: LC,DD). "JDOE" looks like a placeholder, confirm.
    A duplicate copy exists at 05_external_videos/dataset_inference.xlsx (identical).

### Retrieval notes
Provided directly by the owner. Not downloaded. See
`datasets/pose/cody_3/processed/manifest.csv`.

### Processing
Inventoried by `build_cody_manifest.py` (2026-07-10). Both modalities kept in parallel
(owner decision): COCO-17 keypoints -> canonical skeleton, and SAM3 silhouette as a
separate modality stream. Adult labels from dataset_consensus; external labels at
subject level from dataset_inference.xlsx. Raw video stays local; only derived
timeseries enter processed/. Splits at PATIENT level on namespaced ids. Owner still to
provide the calibration/test patient lists from the published CODY papers for leakage
tracing.
