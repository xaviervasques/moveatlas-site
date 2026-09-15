# Clinical gait signals with wearables (2025; healthy/neuro/orthopedic)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Clinical gait signals with wearables (2025; healthy/neuro/orthopedic)",
 "description": "Clinical gait signals with wearables (2025; healthy/neuro/orthopedic). MoveAtlas imu family. 260 subjects. licence CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23.",
 "identifier": "https://doi.org/10.6084/m9.figshare.28806086",
 "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "D3 Pyramidal syndromes",
  "D4 Neuropathies",
  "E6 Iatrogenic",
  "E4 Musculoskeletal",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.28806086",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Voisard, Cyril"
  },
  {
   "@type": "Person",
   "name": "Barrois, Rémi"
  },
  {
   "@type": "Person",
   "name": "de l'Escalopier, Nicolas"
  },
  {
   "@type": "Person",
   "name": "Vayatis, Nicolas"
  },
  {
   "@type": "Person",
   "name": "Vidal, Pierre-Paul"
  },
  {
   "@type": "Person",
   "name": "Yelnik, Alain"
  },
  {
   "@type": "Person",
   "name": "Ricard, Damien"
  },
  {
   "@type": "Person",
   "name": "Oudre, Laurent"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>clinical_gait_signals_2025</code>

<span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Neuropathies</span><span class="ma-tag">Iatrogenic</span><span class="ma-tag">Musculoskeletal</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | D3 (stroke), D4+E6 (chemo-induced neuropathy), E4; M2 |
| **Subjects** | 260 |
| **Status** | SATISFIED 2026-08-23, nothing to fetch: this record IS clinical_gait_multipatho, already on disk and ingested (1,356 canonical IMU records). Proof: the resolved download URL is figshare file 53704514 and the md5 of clinical_gait_multipatho/raw/dataset.zip matches the published md5 e7701e2ee2d8e6164a... |
| **License** | CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23, same cause as cervical_motion: the CC BY-NC-ND belongs to the Scientific Data ARTICLE, not to the figshare deposit 28806086, whose item licence is CC BY 4.0 and which is what governs the data |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("clinical_gait_signals_2025")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23, same cause as cervical_motion: the CC BY-NC-ND belongs to the Scientific Data ARTICLE, not to the figshare deposit 28806086, whose item licence is CC BY 4.0 and which is what governs the data
- **Redistribution**: yes
- **Access route**: direct_download (figshare)
- **Source**: <https://doi.org/10.6084/m9.figshare.28806086>

## Publications

- Voisard, Cyril; Barrois, Rémi; de l'Escalopier, Nicolas; Vayatis, Nicolas; Vidal, Pierre-Paul; Yelnik, Alain; Ricard, Damien; Oudre, Laurent (2025). *A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts*. figshare. DOI: [10.6084/m9.figshare.28806086](https://doi.org/10.6084/m9.figshare.28806086)

```bibtex
@misc{clinical_gait_signals_2025_data_2025,
  title = {A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts},
  author = {Voisard, Cyril and Barrois, Rémi and de l'Escalopier, Nicolas and Vayatis, Nicolas and Vidal, Pierre-Paul and Yelnik, Alain and Ricard, Damien and Oudre, Laurent},
  year = {2025},
  doi = {10.6084/m9.figshare.28806086},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: clinical_gait_signals_2025
- family: imu  (physical path: datasets/imu/clinical_gait_signals_2025)
- MoveAtlas cells: D3 (stroke), D4+E6 (chemo-induced neuropathy), E4; M2
- population: 260 subjects: 73 healthy, 143 neurological (PD, stroke, CIPN, radiation leukoencephalopathy), 44 orthopedic; UPDRS, Fugl-Meyer, TNS, WOMAC
- n_subjects: 260
- signal: 4 IMUs (head, L4/L5, both feet) at 100 Hz, 1,356 trials, >11 h
- license: CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23, same cause as cervical_motion: the CC BY-NC-ND belongs to the Scientific Data ARTICLE, not to the figshare deposit 28806086, whose item licence is CC BY 4.0 and which is what governs the data ; redistribution: yes
- access: direct_download (figshare)
- status (2026-08-22): SATISFIED 2026-08-23, nothing to fetch: this record IS clinical_gait_multipatho, already on disk and ingested (1,356 canonical IMU records). Proof: the resolved download URL is figshare file 53704514 and the md5 of clinical_gait_multipatho/raw/dataset.zip matches the published md5 e7701e2ee2d8e6164a011f7c264d7649 exactly. Both flags dissolve: the licence is CC BY 4.0 (item licence via api.figshare.com) and the 'overlap' is identity
- link: https://doi.org/10.6084/m9.figshare.28806086
- citation: Sci Data 2025, doi 10.1038/s41597-025-05959-w
