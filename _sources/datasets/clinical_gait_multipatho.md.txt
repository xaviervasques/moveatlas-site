# Clinical gait, multi-pathology 9-axis wearables

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Clinical gait, multi-pathology 9-axis wearables",
 "description": "Clinical gait, multi-pathology 9-axis wearables. MoveAtlas imu family. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.28806086",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "D3 Pyramidal syndromes",
  "D4 Neuropathies",
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

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>clinical_gait_multipatho</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Neuropathies</span><span class="ma-tag">Musculoskeletal</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3, D3, D4, E4; M2 |
| **Subjects** | unresolved from zip (needs extraction count) |
| **Status** | harmonized |
| **License** | CC BY 4.0 (figshare item licence, read via api.figshare.com 2026-08-23) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("clinical_gait_multipatho")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (figshare item licence, read via api.figshare.com 2026-08-23)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://doi.org/10.6084/m9.figshare.28806086>

## Publications

- Voisard, Cyril; Barrois, Rémi; de l'Escalopier, Nicolas; Vayatis, Nicolas; Vidal, Pierre-Paul; Yelnik, Alain; Ricard, Damien; Oudre, Laurent (2025). *A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts*. figshare. DOI: [10.6084/m9.figshare.28806086](https://doi.org/10.6084/m9.figshare.28806086)
- Voisard, Cyril; Barrois, Rémi; l’Escalopier, Nicolas de; Vayatis, Nicolas; Vidal, Pierre-Paul; Yelnik, Alain; Ricard, Damien; Oudre, Laurent (2025). *A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts*. Scientific Data. DOI: [10.1038/s41597-025-05959-w](https://doi.org/10.1038/s41597-025-05959-w)

```bibtex
@misc{clinical_gait_multipatho_data_2025,
  title = {A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts},
  author = {Voisard, Cyril and Barrois, Rémi and de l'Escalopier, Nicolas and Vayatis, Nicolas and Vidal, Pierre-Paul and Yelnik, Alain and Ricard, Damien and Oudre, Laurent},
  year = {2025},
  doi = {10.6084/m9.figshare.28806086},
  howpublished = {figshare},
  note = {dataset}
}
@article{clinical_gait_multipatho_paper_2025,
  title = {A Dataset of Clinical Gait Signals with Wearable Sensors from Healthy, Neurological, and Orthopedic Cohorts},
  author = {Voisard, Cyril and Barrois, Rémi and l’Escalopier, Nicolas de and Vayatis, Nicolas and Vidal, Pierre-Paul and Yelnik, Alain and Ricard, Damien and Oudre, Laurent},
  year = {2025},
  doi = {10.1038/s41597-025-05959-w},
  journal = {Scientific Data}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: clinical_gait_multipatho
- **family**: imu
- **MoveAtlas cells**: B2, B3, D3, D4, E4; M2
- **population**: multi-pathology clinical gait (PD, stroke, neuropathies, orthopedic), 6,780 files
- **n_subjects**: unresolved from zip (needs extraction count)
- **signal**: Xsens 9-axis (acc+gyro+mag) at ~100 Hz, 4 sensor sites (feet + shanks)
- **license**: CC BY 4.0 (figshare item licence, read via api.figshare.com 2026-08-23); redistribution: yes
- **access**: downloaded
- **link**: https://doi.org/10.6084/m9.figshare.28806086
- **ingestion**: build_canonical_imu.py (clinical_gait mapping)
