# CODY-1 (in-house adult hyperkinetic cohort)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-1 (in-house adult hyperkinetic cohort)",
 "description": "CODY-1 (in-house adult hyperkinetic cohort). MoveAtlas pose family. 25 subjects. licence derived data CC BY 4.0.",
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
  "A3 Tics",
  "A6 Athetosis",
  "M1 Pose / video"
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

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_1</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Tics</span><span class="ma-tag">Athetosis</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8 (all eight hyperkinetic cells incl. the publicly-empty A3 tics, A6 athetosis, A8 ballismus); M1 |
| **Subjects** | 25 |
| **Status** | INGESTED (cody source, 25 subjects); paper published (10.1002/acn3.70474); derived data PUBLIC on GitHub and Zenodo (2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). PUBLICATION RULING (owner, 2026-08-28): all NON-VIDEO files (keypoints, labels, silhouettes) are publishable; CONTROL raw videos are publishable; PATIENT raw videos are NOT, ever |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_1")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). PUBLICATION RULING (owner, 2026-08-28): all NON-VIDEO files (keypoints, labels, silhouettes) are publishable; CONTROL raw videos are publishable; PATIENT raw videos are NOT, ever
- **Redistribution**: yes for the derived data the atlas serves (CC BY 4.0 on Zenodo); patient raw video never
- **Access route**: PUBLIC: the derived data (keypoints + labels) is published on GitHub by the owner (github.com/xaviervasques/CODY, MIT, verified 2026-08-28) and, since 2026-09-01, in the CODY Zenodo deposit (10.5281/zenodo.22232609, CC BY 4.0, open access, verified 2026-09-02: the 25 adults are dataset_0 there, labels + merged kinematics + SAM3 timeseries); patient raw video stays in-house
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

- Cif, Laura; Demailly, Diane; Horvàth, Gabriella A.; Ortigoza Escobar, Juan Dario; Dorison, Nathalie; Castro Jiménez, Mayté; Hubsch, Cécile A.; Wirth, Thomas; Hariz, Gun‐Marie; Huby, Sophie; Dornadic, Morgan; Souei, Zohra; Mushhood Ur Rehman, Muhammad; Hemm, Simone; Boulaymen, Mehdi; Moraud, Eduardo  (2026). *Deep Learning Pose Estimation for Phenotyping of Co‐Occurring Hyperkinetic Movement Disorders*. Annals of Clinical and Translational Neurology. DOI: [10.1002/acn3.70474](https://doi.org/10.1002/acn3.70474)

```bibtex
@article{cody_1_paper_2026,
  title = {Deep Learning Pose Estimation for Phenotyping of Co‐Occurring Hyperkinetic Movement Disorders},
  author = {Cif, Laura and Demailly, Diane and Horvàth, Gabriella A. and Ortigoza Escobar, Juan Dario and Dorison, Nathalie and Castro Jiménez, Mayté and Hubsch, Cécile A. and Wirth, Thomas and Hariz, Gun‐Marie and Huby, Sophie and Dornadic, Morgan and Souei, Zohra and Mushhood Ur Rehman, Muhammad and Hemm, Simone and Boulaymen, Mehdi and Moraud, Eduardo M. and Bloch, Jocelyne and Vasques, Xavier},
  year = {2026},
  doi = {10.1002/acn3.70474},
  journal = {Annals of Clinical and Translational Neurology}
}
```

## Data card (verbatim, with its evidence trail)


- Modality: pose (COCO-17 keypoints 2D) + per-frame phenomenology labels
- Source / URL: non-public in-house data (owner). NOT a public dataset.
- License: private, not shareable in current form (identifiable source video)
- Access: local only; raw video never leaves the machine (sovereignty constraint)
- Version / retrieval date: provided 2026-07-10
- Status: processed (inventoried; canonical ingestion pending)
- UPDATE 2026-09-02: the derived release is PUBLIC on Zenodo since
  2026-09-01: CODY deposit, concept DOI 10.5281/zenodo.22232609
  (v1.0.0 = 10.5281/zenodo.22232610), CC BY 4.0, open access, verified
  on the record page 2026-09-02. The License/Access lines above
  describe the in-house SOURCE (raw patient video), which stays
  private; the deposit carries only de-identified derived data.
- UPDATE 2026-09-04 (v1.1.0 = 10.5281/zenodo.22275553, published,
  API-verified): archive names now carry study + extraction pipeline.
  What CODY-1 uses is dataset_0_labels_raw_cody_1_2_yolo.zip: the
  per-rater expert labels TOGETHER WITH the YOLOv8 COCO-17 keypoint
  time-series of the 25 adults (the earlier claim that the adult
  kinematics lived in the merged archives was wrong - those, and all
  *_cody_3_sam3 archives, are CODY-3 SAM3 products, a different
  extraction of the same subjects).
- Number of subjects: 25 (4 controls C1-C4 + 21 patients)
- Disorders covered: hyperkinetic (Dystonia, Tremor, Myoclonus, Chorea, Tics,
  Athetosis, Ballismus, Stereotypie), multi-label per frame
- Frequency / resolution: ~33 fps (dt=0.03s), keypoints in image PIXELS
- Specifics:
  - 125 real xlsx (134 AppleDouble ._* + 3 .DS_Store = macOS noise, excluded).
  - Two raters (dataset_dd, dataset_lc). Exam conditions in rest_posture_action
    (Rest / Posture / Action), French labels ("Repos" = rest).
  - Columns: time, 17 COCO keypoints x/y, per-keypoint *_distance, 8 ordinal
    phenomenology labels (e.g. Dystonia {0,1,2}).
  - REDUNDANCY: these 25 adults are the SAME subjects as cody_2/training and
    cody_3/01-03. Canonical source for the adult labeled cohort = cody_3.
    cody_1 is a flattened legacy export; do NOT ingest it as independent samples.

### Retrieval notes
Provided directly by the owner on the external disk. Not downloaded. See
`build_cody_manifest.py` and `datasets/pose/cody_1/processed/manifest.csv`.

### Processing
Inventoried by `build_cody_manifest.py` (2026-07-10). Namespaced subject registry:
`datasets/pose/_cody_registry.csv` (adult:* ids). Canonical-skeleton ingestion pending
(COCO-17 -> canonical mapping, `configs/canonical_skeleton.yaml`). Labels are for
fine-tuning and evaluation probes only, never for pretraining.
