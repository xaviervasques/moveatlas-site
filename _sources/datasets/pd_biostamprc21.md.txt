# PD-BioStampRC21 (5-sensor IMU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PD-BioStampRC21 (5-sensor IMU)",
 "description": "PD-BioStampRC21 (5-sensor IMU). MoveAtlas imu family. 34 subjects. licence IEEE DataPort open access.",
 "identifier": "https://dx.doi.org/10.21227/g2g8-1503",
 "license": "IEEE DataPort open access (no explicit reuse licence shown on the page, checked 2026-08-28)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://dx.doi.org/10.21227/g2g8-1503",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Adams, Jamie L."
  },
  {
   "@type": "Person",
   "name": "Dinesh, Karthik"
  },
  {
   "@type": "Person",
   "name": "Snyder, Christopher W."
  },
  {
   "@type": "Person",
   "name": "Xiong, Mulin"
  },
  {
   "@type": "Person",
   "name": "Tarolli, Christopher G."
  },
  {
   "@type": "Person",
   "name": "Sharma, Saloni"
  },
  {
   "@type": "Person",
   "name": "Dorsey, E. Ray"
  },
  {
   "@type": "Person",
   "name": "Sharma, Gaurav"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>pd_biostamprc21</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3; M2 |
| **Subjects** | 34 |
| **Status** | DOWNLOADED 2026-08-25 (owner's IEEE account) AND INGESTED 2026-08-26: 7,682 canonical IMU records / 34 subjects / 7,658 sensor-hours, 1-hour segments, fs measured 31.250 Hz on every stream, gravity 0.99-1.04 g. Forearm sensors sit in PROXY wrist slots (the grid has no forearm; placement carried verb... |
| **License** | IEEE DataPort open access (no explicit reuse licence shown on the page, checked 2026-08-28) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pd_biostamprc21")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: IEEE DataPort open access (no explicit reuse licence shown on the page, checked 2026-08-28)
- **Redistribution**: no, DECIDED: pointer to IEEE DataPort
- **Access route**: registration (free IEEE account)
- **Source**: <https://dx.doi.org/10.21227/g2g8-1503>

## Publications

- Adams, Jamie L.; Dinesh, Karthik; Snyder, Christopher W.; Xiong, Mulin; Tarolli, Christopher G.; Sharma, Saloni; Dorsey, E. Ray; Sharma, Gaurav (2020). *PD-BioStampRC21: Parkinson's Disease Accelerometry Dataset from Five Wearable Sensor Study*. IEEE DataPort. DOI: [10.21227/g2g8-1503](https://doi.org/10.21227/g2g8-1503)

```bibtex
@misc{pd_biostamprc21_data_2020,
  title = {PD-BioStampRC21: Parkinson's Disease Accelerometry Dataset from Five Wearable Sensor Study},
  author = {Adams, Jamie L. and Dinesh, Karthik and Snyder, Christopher W. and Xiong, Mulin and Tarolli, Christopher G. and Sharma, Saloni and Dorsey, E. Ray and Sharma, Gaurav},
  year = {2020},
  doi = {10.21227/g2g8-1503},
  howpublished = {IEEE DataPort},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: pd_biostamprc21
- family: imu  (physical path: datasets/imu/pd_biostamprc21)
- MoveAtlas cells: B2, B3; M2
- population: 34 PD
- n_subjects: 34
- signal: 5 BioStamp RC sensors, 10.8 GB
- license: IEEE DataPort open access (no explicit reuse licence shown on the page, checked 2026-08-28) ; redistribution: no, DECIDED: pointer to IEEE DataPort
- access: registration (free IEEE account)
- status (2026-08-22): DOWNLOADED 2026-08-25 (owner's IEEE account) AND INGESTED 2026-08-26: 7,682 canonical IMU records / 34 subjects / 7,658 sensor-hours, 1-hour segments, fs measured 31.250 Hz on every stream, gravity 0.99-1.04 g. Forearm sensors sit in PROXY wrist slots (the grid has no forearm; placement carried verbatim, G2 owns any grid change). UPDRS windows and medication ON/OFF kept per subject under processed/annotations/, eval only. ingest_pd_biostamprc21.py
- link: https://dx.doi.org/10.21227/g2g8-1503
