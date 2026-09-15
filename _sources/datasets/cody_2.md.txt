# CODY-2 (in-house pediatric inference split)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-2 (in-house pediatric inference split)",
 "description": "CODY-2 (in-house pediatric inference split). MoveAtlas pose family. 12 subjects. licence derived data CC BY 4.0.",
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

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_2</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8 pediatric; M1 |
| **Subjects** | 12 |
| **Status** | inventoried; paper on arXiv (10.48550/arXiv.2606.07674), journal acceptance near; derived data PUBLIC on Zenodo (2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). Same publication ruling as cody_1: non-video files publishable, patient raw video never (pediatric: extra caution) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_2")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). Same publication ruling as cody_1: non-video files publishable, patient raw video never (pediatric: extra caution)
- **Redistribution**: yes for the derived data the atlas serves (CC BY 4.0 on Zenodo); patient raw video never (pediatric: extra caution)
- **Access route**: PUBLIC (derived) since 2026-09-01: the pediatric SAM3 timeseries and results ship inside the CODY Zenodo deposit (10.5281/zenodo.22232609, CC BY 4.0) in the datasets_1_2_3 files; raw video stays in-house
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

- Cif, Laura; Demailly, Diane; Souei, Zohra; Rehman, Muhammad Mushhood Ur; Escobar, Juan Dario Ortigoza; Jiménez, Mayté Castro; Hubsch, Cécile A.; Huby, Sophie; Dornadic, Morgan; Hariz, Gun-Marie; Moraud, Eduardo M.; Bloch, Jocelyne; Horvath, Gabriella A.; Vasques, Xavier (2026). *Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model*. arXiv. DOI: [10.48550/arxiv.2606.07674](https://doi.org/10.48550/arxiv.2606.07674)

```bibtex
@article{cody_2_paper_2026,
  title = {Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model},
  author = {Cif, Laura and Demailly, Diane and Souei, Zohra and Rehman, Muhammad Mushhood Ur and Escobar, Juan Dario Ortigoza and Jiménez, Mayté Castro and Hubsch, Cécile A. and Huby, Sophie and Dornadic, Morgan and Hariz, Gun-Marie and Moraud, Eduardo M. and Bloch, Jocelyne and Horvath, Gabriella A. and Vasques, Xavier},
  year = {2026},
  doi = {10.48550/arxiv.2606.07674},
  journal = {arXiv}
}
```

## Data card (verbatim, with its evidence trail)


- Modality: pose (COCO-17 keypoints 2D) + per-frame labels (training) ;
  keypoints without labels (inference, pediatric)
- Source / URL: non-public in-house data (owner). NOT a public dataset.
- License: private, not shareable in current form (identifiable source video)
- Access: local only; raw video never leaves the machine (sovereignty constraint)
- Version / retrieval date: provided 2026-07-10
- Status: processed (inventoried; canonical ingestion pending)
- UPDATE 2026-09-02: the derived release is PUBLIC on Zenodo since
  2026-09-01 (CODY deposit, 10.5281/zenodo.22232609, CC BY 4.0): the
  pediatric cohort ships as dataset_2 inside the datasets_1_2_3_*
  files (SAM3 timeseries + results). Raw video stays in-house; the
  License/Access lines above describe the in-house source.
- UPDATE 2026-09-04 (v1.1.0 = 10.5281/zenodo.22275553, published,
  API-verified): CODY-2's OWN pediatric YOLOv8 keypoints are now
  deposited too - dataset_2_timeseries_cody_2_yolo.zip (48 MB), the
  12 unlabeled pediatric COCO-17 time-series this study's inference
  actually consumes (v1.0.0 only carried the SAM3 extraction of
  dataset_2). CODY-2 is therefore genuinely reproducible from public
  data as of v1.1.0; the training-side labels + adult YOLO keypoints
  are dataset_0_labels_raw_cody_1_2_yolo.zip (shared with CODY-1).
- Number of subjects: training = 25 adults (redundant with cody_1/cody_3) ;
  inference = 12 pediatric subjects ("PEDIA")
- Disorders covered: same 8-label hyperkinetic scheme
- Frequency / resolution: ~33 fps, keypoints in image PIXELS
- Specifics:
  - 137 real xlsx (147 AppleDouble excluded). Split: training/ (dataset_dd, dataset_lc,
    dataset_action, dataset_posture, dataset_rest) and inference/dataset_2 (12 pediatric
    timeseries).
  - REDUNDANCY: training/ holds the SAME 25 adults as cody_1 and cody_3. Canonical
    source = cody_3. inference/dataset_2 (pediatric) is mirrored in cody_3 external
    dataset_2.
  - Pediatric inference subjects have NO per-frame labels here; their subject-level
    multi-rater diagnosis is in cody_3/dataset_inference.xlsx (sheet dataset_2).

### Retrieval notes
Provided directly by the owner. Not downloaded. See
`datasets/pose/cody_2/processed/manifest.csv`.

### Processing
Inventoried by `build_cody_manifest.py` (2026-07-10). Ingest pediatric subjects from
cody_3 external dataset_2 (video + SAM3) to avoid duplication. Labels for evaluation
only.
