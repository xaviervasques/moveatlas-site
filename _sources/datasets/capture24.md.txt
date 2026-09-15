# Capture-24 (free-living wrist accel)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Capture-24 (free-living wrist accel)",
 "description": "Capture-24 (free-living wrist accel). MoveAtlas imu family. 151 subjects. licence CC BY 4.0.",
 "identifier": "https://ora.ox.ac.uk/objects/uuid:99d7c092-d865-4a19-b096-cc16440cd001",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "C1 Normal adult movement",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://ora.ox.ac.uk/objects/uuid:99d7c092-d865-4a19-b096-cc16440cd001",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Wong, A"
  },
  {
   "@type": "Person",
   "name": "Gray, N"
  },
  {
   "@type": "Person",
   "name": "Chan Chang, S"
  },
  {
   "@type": "Person",
   "name": "Harms, T"
  },
  {
   "@type": "Person",
   "name": "Thomas, E"
  },
  {
   "@type": "Person",
   "name": "Walmsley, R"
  },
  {
   "@type": "Person",
   "name": "Milton, K"
  },
  {
   "@type": "Person",
   "name": "Kelly, P"
  },
  {
   "@type": "Person",
   "name": "Doherty, A"
  },
  {
   "@type": "Person",
   "name": "Hollowell, S"
  },
  {
   "@type": "Person",
   "name": "Gershuny, J"
  },
  {
   "@type": "Person",
   "name": "Foster, C"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>capture24</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3; M2 |
| **Subjects** | 151 |
| **Status** | FULLY INGESTED 2026-08-22: 3,941 canonical records, 151 subjects, 3,883 HOURS. v1 had read only the first 60,000 lines of each subject (10 minutes) and kept 20 windows of 30 s: 3,020 records, 25 hours, i.e. 0.6 percent of a corpus already on disk. Per-subject shards under processed/canonical/, 1-hou... |
| **License** | CC BY 4.0 (ORA record licence, verified 2026-08-23) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("capture24")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (ORA record licence, verified 2026-08-23)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://ora.ox.ac.uk/objects/uuid:99d7c092-d865-4a19-b096-cc16440cd001>

## Publications

- Wong, A; Gray, N; Chan Chang, S; Harms, T; Thomas, E; Walmsley, R; Milton, K; Kelly, P; Doherty, A; Hollowell, S; Gershuny, J; Foster, C; Haque, S (2021). *Capture-24: Activity tracker dataset for human activity recognition*. University of Oxford. DOI: [10.5287/bodleian:ngx0jomp5](https://doi.org/10.5287/bodleian:ngx0jomp5)
- Chan, Shing; Hang, Yuan; Tong, Catherine; Acquah, Aidan; Schonfeldt, Abram; Gershuny, Jonathan; Doherty, Aiden (2024). *CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition*. Scientific Data. DOI: [10.1038/s41597-024-03960-3](https://doi.org/10.1038/s41597-024-03960-3)

```bibtex
@misc{capture24_data_2021,
  title = {Capture-24: Activity tracker dataset for human activity recognition},
  author = {Wong, A and Gray, N and Chan Chang, S and Harms, T and Thomas, E and Walmsley, R and Milton, K and Kelly, P and Doherty, A and Hollowell, S and Gershuny, J and Foster, C and Haque, S},
  year = {2021},
  doi = {10.5287/bodleian:ngx0jomp5},
  howpublished = {University of Oxford},
  note = {dataset}
}
@article{capture24_paper_2024,
  title = {CAPTURE-24: A large dataset of wrist-worn activity tracker data collected in the wild for human activity recognition},
  author = {Chan, Shing and Hang, Yuan and Tong, Catherine and Acquah, Aidan and Schonfeldt, Abram and Gershuny, Jonathan and Doherty, Aiden},
  year = {2024},
  doi = {10.1038/s41597-024-03960-3},
  journal = {Scientific Data}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: capture24
- family: imu  (physical path: datasets/imu/capture24)
- MoveAtlas cells: C1, C3; M2
- population: 151 healthy adults, ~24 h free living each
- n_subjects: 151
- signal: wrist accelerometer 100 Hz + activity annotations
- license: CC BY 4.0 (ORA record licence, verified 2026-08-23) ; redistribution: yes
- access: downloaded
- status (2026-08-22): FULLY INGESTED 2026-08-22: 3,941 canonical records, 151 subjects, 3,883 HOURS. v1 had read only the first 60,000 lines of each subject (10 minutes) and kept 20 windows of 30 s: 3,020 records, 25 hours, i.e. 0.6 percent of a corpus already on disk. Per-subject shards under processed/canonical/, 1-hour records, 48 GB. Units verified per subject rather than assumed: median |acc| runs 0.888 to 1.051 across all 151, so the values are already in g and nothing is rescaled. 0 refusals. Activity annotations are now kept too (v1 discarded them), run-length encoded against the bundled 206-entry label dictionary, plus age band and sex from metadata.csv
- link: https://ora.ox.ac.uk/objects/uuid:99d7c092-d865-4a19-b096-cc16440cd001
- ingestion: ingest_capture24.py (full). LATERALITY IS UNRESOLVED ON PURPOSE: the device is worn on the DOMINANT wrist and handedness is not distributed, so no subject side is knowable. Records keep the wrist_L slot for continuity and carry laterality=unknown with worn_on=dominant_wrist; the slot is NOMINAL, so do not use this source for anything laterality-sensitive. Writing wrist_R instead would be right for the right-handed majority and wrong for the rest. SPLIT FOLDER, do not be fooled: the datacard and raw/ live under datasets/socle/capture24 while the 3,020 canonical records sit in datasets/imu/capture24/processed/. The v2 reorganization moved cards and raw into the new family folders but left processed/ alone on purpose, because manifest paths are load-bearing. Looking only at socle/ shows raw with no output and invites a re-ingestion that would duplicate every record
