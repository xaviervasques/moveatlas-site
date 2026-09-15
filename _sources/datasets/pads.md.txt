# PADS: Parkinson's Disease Smartwatch dataset (PhysioNet)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PADS: Parkinson's Disease Smartwatch dataset (PhysioNet)",
 "description": "PADS: Parkinson's Disease Smartwatch dataset (PhysioNet). MoveAtlas imu family. 469 subjects. licence PhysioNet open.",
 "identifier": "https://physionet.org/content/pads/",
 "license": "PhysioNet open",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A1 Tremor",
  "B2 Bradykinesia",
  "D3 Pyramidal syndromes",
  "M2 Inertial (IMU)"
 ],
 "url": "https://physionet.org/content/pads/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>pads</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A1, B2, D3 (differential cohorts: ET, atypical parkinsonism, MS; D3 is the nearest cell for the MS arm, owner ruling 2026-09-01); M2 |
| **Subjects** | 469 |
| **Status** | INGESTED: 10,318 canonical IMU records / 469 subjects (the full run happened; the old 'TOWER RUN PENDING' text was stale until 2026-08-25). v1 had judged the preprocessed/ tree ambiguous; raw/movement/ is fully self-describing |
| **License** | PhysioNet open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pads")
records, meta = ds.get_data()
```

## License and access

- **License**: PhysioNet open
- **Redistribution**: yes
- **Access route**: downloaded (12,689 files, SHA256-verified mirror)
- **Source**: <https://physionet.org/content/pads/>

## Publications

- Varghese, Julian; Brenner, Alexander; Fujarski, Michael; van Alen, Catharina Marie; Plagwitz, Lucas; Warnecke, Tobias (2024). *Machine Learning in the Parkinson’s disease smartwatch (PADS) dataset*. npj Parkinson's Disease. DOI: [10.1038/s41531-023-00625-7](https://doi.org/10.1038/s41531-023-00625-7)

```bibtex
@article{pads_paper_2024,
  title = {Machine Learning in the Parkinson’s disease smartwatch (PADS) dataset},
  author = {Varghese, Julian and Brenner, Alexander and Fujarski, Michael and van Alen, Catharina Marie and Plagwitz, Lucas and Warnecke, Tobias},
  year = {2024},
  doi = {10.1038/s41531-023-00625-7},
  journal = {npj Parkinson's Disease}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: pads
- family: imu  (physical path: datasets/imu/pads)
- MoveAtlas cells: A1, B2, D3 (differential cohorts: ET, atypical parkinsonism, MS; D3 is the nearest cell for the MS arm, owner ruling 2026-09-01); M2
- population: 469 subjects: 276 PD, 79 healthy, 60 other movement disorders, 28 essential tremor, 15 atypical parkinsonism, 11 MS; NMS questionnaires
- n_subjects: 469
- signal: 2 Apple Watch (both wrists), 100 Hz, 11-task battery (Relaxed, StretchHold, LiftHold, HoldWeight, PointFinger, DrinkGlas, CrossArms, TouchIndex, TouchNose, Entrainment...), ~20.5 s each; channels+units self-described per observation (acc g, gyro rad/s)
- license: PhysioNet open ; redistribution: yes
- access: downloaded (12,689 files, SHA256-verified mirror)
- status (2026-08-22): INGESTED: 10,318 canonical IMU records / 469 subjects (the full run happened; the old 'TOWER RUN PENDING' text was stale until 2026-08-25). v1 had judged the preprocessed/ tree ambiguous; raw/movement/ is fully self-describing
- link: https://physionet.org/content/pads/
- ingestion: ingest_pads.py -> canonical_imu.pkl (one record per wrist, no cross-device resampling) + pads_subject_table.csv + audit. MEASURED CAVEAT: CoreMotion userAcceleration = gravity REMOVED at source (median |acc| ~0.004 g at rest); flagged as acc_content=linear_no_gravity
- notes: rare multi-disorder differential-diagnosis corpus; labels eval-only
