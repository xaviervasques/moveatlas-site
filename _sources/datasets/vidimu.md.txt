# VIDIMU (daily activities: video pose + IMU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "VIDIMU (daily activities: video pose + IMU)",
 "description": "VIDIMU (daily activities: video pose + IMU). MoveAtlas socle family. 53 subjects. licence Zenodo open.",
 "identifier": "https://zenodo.org/records/15075076",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/15075076",
 "isAccessibleForFree": true,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Martínez-Zarzuela, Mario"
  },
  {
   "@type": "Person",
   "name": "González-Alonso, Javier"
  },
  {
   "@type": "Person",
   "name": "Antón-Rodríguez, Míriam"
  },
  {
   "@type": "Person",
   "name": "Díaz-Pernas, Francisco J."
  },
  {
   "@type": "Person",
   "name": "Müller, Henning"
  },
  {
   "@type": "Person",
   "name": "Simón-Martínez, Cristina"
  }
 ]
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>vidimu</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1, M2 (paired) |
| **Subjects** | 53 |
| **Status** | harmonized (2026-08-22) |
| **License** | Zenodo open (CC BY 4.0 per record) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("vidimu")
records, meta = ds.get_data()
```

## License and access

- **License**: Zenodo open (CC BY 4.0 per record)
- **Redistribution**: yes
- **Access route**: direct download (on disk)
- **Source**: <https://zenodo.org/records/15075076>

## Publications

- Martínez-Zarzuela, Mario; González-Alonso, Javier; Antón-Rodríguez, Míriam; Díaz-Pernas, Francisco J.; Müller, Henning; Simón-Martínez, Cristina (2023). *Multimodal video and IMU kinematic dataset on daily life activities using affordable devices*. Scientific Data. DOI: [10.1038/s41597-023-02554-9](https://doi.org/10.1038/s41597-023-02554-9)

```bibtex
@misc{vidimu_data_2023,
  title = {Multimodal video and IMU kinematic dataset on daily life activities using affordable devices},
  author = {Martínez-Zarzuela, Mario and González-Alonso, Javier and Antón-Rodríguez, Míriam and Díaz-Pernas, Francisco J. and Müller, Henning and Simón-Martínez, Cristina},
  year = {2023},
  doi = {10.1038/s41597-023-02554-9},
  howpublished = {Scientific Data},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: vidimu
- **family**: socle
- **MoveAtlas cells**: C1; M1, M2 (paired)
- **population**: 53 healthy subjects on disk (54 published); 13 daily activities (walks, sit-to-stand, arm tasks)
- **n_subjects**: 53
- **signal**: video-derived 3D keypoints (34 landmarks, ~30 fps measured 29.42) for all; 5 orientation-quaternion IMUs (dynamic lower-body or upper-body sets) for 16 subjects, ~208 same-trial pose+IMU pairs
- **license**: Zenodo open (CC BY 4.0 per record); redistribution: yes
- **access**: direct download (on disk)
- **link**: https://zenodo.org/records/15075076
- **citation**: Sci Data 2023, doi 10.1038/s41597-023-02554-9
- **ingestion**: ingest_vidimu.py -> canonical.pkl (skeleton contract) + streams_pose_imu.pkl (stage B alignment asset; quaternions are NOT the 9-channel IMU contract) + audit + manifest
