# Multi-planar cervical motion (IMU + goniometer, Sci Data 2024)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Multi-planar cervical motion (IMU + goniometer, Sci Data 2024)",
 "description": "Multi-planar cervical motion (IMU + goniometer, Sci Data 2024). MoveAtlas imu family. 14 subjects. licence CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23 and it was ours: .",
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
| **Status** | DOWNLOADED AND INGESTED 2026-08-22: 409 MB -> 127 canonical EMG records / 15 subjects, 0 failures. The registry description was wrong: this is a Delsys Avanti export with 2 EMG channels at 1785.7 Hz PLUS unit quaternions at 74.1 Hz (\|q\| median 1.0000), each channel on its own clock, not 2 IMU + goni... |
| **License** | CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23 and it was ours: the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. The paper Data Records section points at figshare 26935900, whose item licence is CC BY 4.0, and the figshare deposit governs the data. Two different objects, one of which we... |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cervical_motion_multiplanar")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23 and it was ours: the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. The paper Data Records section points at figshare 26935900, whose item licence is CC BY 4.0, and the figshare deposit governs the data. Two different objects, one of which we 
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

## Data card (verbatim, with its evidence trail)


- dataset: cervical_motion_multiplanar
- family: imu  (physical path: datasets/imu/cervical_motion_multiplanar)
- MoveAtlas cells: A4 normative, C1; M2
- population: 14 asymptomatic adults, 504 cervical movements in 3 planes
- n_subjects: 14
- age: 38 +/- 13 y
- signal: 2 Delsys Trigno Avanti IMUs (quaternion CSVs, 74 Hz) + goniometer gold standard
- license: CC BY 4.0. DISCREPANCY RESOLVED 2026-08-23 and it was ours: the CC BY-NC-ND we had recorded is the licence of the Scientific Data ARTICLE (Nature says "This article is licensed under CC BY-NC-ND"), not of the deposited data. The paper Data Records section points at figshare 26935900, whose item licence is CC BY 4.0, and the figshare deposit governs the data. Two different objects, one of which we mislabelled ; redistribution: yes
- access: direct_download (figshare; fetch_p2_lot.py resolve)
- status (2026-08-22): DOWNLOADED AND INGESTED 2026-08-22: 409 MB -> 127 canonical EMG records / 15 subjects, 0 failures. The registry description was wrong: this is a Delsys Avanti export with 2 EMG channels at 1785.7 Hz PLUS unit quaternions at 74.1 Hz (|q| median 1.0000), each channel on its own clock, not 2 IMU + goniometer. Orientation is not acc/gyro so it does NOT enter the IMU contract (vidimu precedent): quaternions go to processed/streams_orientation.pkl. The bundled README documents every column but NEVER states where sensors 1 and 2 were placed, so muscle, side and location stay unknown with resolved=False; read the paper to resolve, do not infer from convention
- link: https://doi.org/10.1038/s41597-024-04351-4
- notes: normative cervical ROM for cervical dystonia comparisons; ND license may restrict it to evaluation-only use, legal review required
