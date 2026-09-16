# Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge)",
 "description": "Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge). MoveAtlas pose family. 188 subjects. licence CC0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.6503791",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "D3 Pyramidal syndromes",
  "M1 Pose / video",
  "M3 Plantar force",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.c.6503791",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Van Criekinge, Tamaya"
  },
  {
   "@type": "Person",
   "name": "Saeys, Wim"
  },
  {
   "@type": "Person",
   "name": "Truijen, Steven"
  },
  {
   "@type": "Person",
   "name": "Vereeck, Luc"
  },
  {
   "@type": "Person",
   "name": "Sloot, Lizeth"
  },
  {
   "@type": "Person",
   "name": "Hallemans, Ann"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>stroke_gait_vancriekinge</code>

<span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Plantar force</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | D3; M1, M3, M5 (pathological EMG) |
| **Subjects** | 188 |
| **Ages** | 19-85 y |
| **Status** | harmonized (2026-08-28) |
| **License** | CC0 (all 13 figshare collection items, verified 2026-08-22) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("stroke_gait_vancriekinge")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (all 13 figshare collection items, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download
- **Source**: <https://doi.org/10.6084/m9.figshare.c.6503791>

## Publications

- Van Criekinge, Tamaya; Saeys, Wim; Truijen, Steven; Vereeck, Luc; Sloot, Lizeth; Hallemans, Ann (2023). *A full-body motion capture gait dataset of 138 able-bodied adults across the life span and 50 stroke survivors*. figshare. DOI: [10.6084/m9.figshare.c.6503791](https://doi.org/10.6084/m9.figshare.c.6503791)

```bibtex
@misc{stroke_gait_vancriekinge_data_2023,
  title = {A full-body motion capture gait dataset of 138 able-bodied adults across the life span and 50 stroke survivors},
  author = {Van Criekinge, Tamaya and Saeys, Wim and Truijen, Steven and Vereeck, Luc and Sloot, Lizeth and Hallemans, Ann},
  year = {2023},
  doi = {10.6084/m9.figshare.c.6503791},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: stroke_gait_vancriekinge
- **family**: pose
- **MoveAtlas cells**: D3; M1, M3, M5 (pathological EMG)
- **population**: 50 stroke survivors + 138 able-bodied adults across the lifespan
- **n_subjects**: 188
- **age**: 19-85 y
- **signal**: 3D marker trajectories, joint angles, GRF, joint moments/powers + EMG of 14 back/lower-limb muscles (C3D + MAT/XLSX)
- **license**: CC0 (all 13 figshare collection items, verified 2026-08-22); redistribution: yes
- **access**: direct_download
- **link**: https://doi.org/10.6084/m9.figshare.c.6503791
- **citation**: Sci Data 2023, doi 10.1038/s41597-023-02767-y
- **known issues**: 555 of 559 EMG records carry an amplitude flag: the declared volts convert to about 476 mV at the 99th percentile, about 1000 times the surface-EMG range, and are not rescaled; the 4 other records come from a 7-channel acquisition within range
