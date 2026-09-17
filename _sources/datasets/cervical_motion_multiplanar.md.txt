# Multi-planar cervical motion (IMU + goniometer, Sci Data 2024)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Multi-planar cervical motion (IMU + goniometer, Sci Data 2024)",
 "description": "Multi-planar cervical motion (IMU + goniometer, Sci Data 2024). MoveAtlas imu family. 14 subjects. licence CC BY 4.0. DISCREPANCY the CC BY-NC-ND we had recorded is th.",
 "identifier": "https://doi.org/10.1038/s41597-024-04351-4",
 "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A4 Dystonia",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.1038/s41597-024-04351-4",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Keidan, Lee"
  },
  {
   "@type": "Person",
   "name": "Ibrahim, Rawan"
  },
  {
   "@type": "Person",
   "name": "Ohayon, Evyatar"
  },
  {
   "@type": "Person",
   "name": "Pick, Chaim G."
  },
  {
   "@type": "Person",
   "name": "Been, Ella"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cervical_motion_multiplanar</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A4 normative, C1; M2 |
| **Subjects** | 14 |
| **Ages** | 38 +/- 13 y |
| **Status** | harmonized (2026-08-22) |
| **License** | CC BY 4.0. DISCREPANCY the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. Two different objects, one of which we mislabelled |
| **MoveAtlas record** | [10.5281/zenodo.22310376](https://doi.org/10.5281/zenodo.22310376) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cervical_motion_multiplanar")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0. DISCREPANCY the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. Two different objects, one of which we mislabelled
- **Redistribution**: yes
- **Access route**: direct_download (figshare; fetch_p2_lot.py resolve)
- **Source**: <https://doi.org/10.1038/s41597-024-04351-4>

## Publications

- Keidan, Lee; Ibrahim, Rawan; Ohayon, Evyatar; Pick, Chaim G.; Been, Ella (2025). *Multi-Planar Cervical Motion Dataset: IMU Measurements and Goniometer*. Scientific Data. DOI: [10.1038/s41597-024-04351-4](https://doi.org/10.1038/s41597-024-04351-4)

```bibtex
@misc{cervical_motion_multiplanar_data_2025,
  title = {Multi-Planar Cervical Motion Dataset: IMU Measurements and Goniometer},
  author = {Keidan, Lee and Ibrahim, Rawan and Ohayon, Evyatar and Pick, Chaim G. and Been, Ella},
  year = {2025},
  doi = {10.1038/s41597-024-04351-4},
  howpublished = {Scientific Data},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: cervical_motion_multiplanar
- **family**: imu
- **MoveAtlas cells**: A4 normative, C1; M2
- **population**: 14 asymptomatic adults, 504 cervical movements in 3 planes
- **n_subjects**: 14
- **age**: 38 +/- 13 y
- **signal**: 2 Delsys Trigno Avanti IMUs (quaternion CSVs, 74 Hz) + goniometer gold standard
- **license**: CC BY 4.0. DISCREPANCY the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. Two different objects, one of which we mislabelled; redistribution: yes
- **access**: direct_download (figshare; fetch_p2_lot.py resolve)
- **link**: https://doi.org/10.1038/s41597-024-04351-4
