# Huntington wrist accelerometry (J-Net)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Huntington wrist accelerometry (J-Net)",
 "description": "Huntington wrist accelerometry (J-Net). MoveAtlas imu family. 34 subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/14384260",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A7 Chorea",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/14384260",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Schwartz, Dafna"
  },
  {
   "@type": "Person",
   "name": "Quinn, Lori"
  },
  {
   "@type": "Person",
   "name": "Fritz, Nora"
  },
  {
   "@type": "Person",
   "name": "Muratori, Lisa"
  },
  {
   "@type": "Person",
   "name": "Hausdorff, Jeffrey"
  },
  {
   "@type": "Person",
   "name": "Gilad-Bachrach, Ran"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>hd_accel_jnet</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A7; M2 |
| **Subjects** | 34 |
| **Status** | harmonized |
| **License** | CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("hd_accel_jnet")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://zenodo.org/records/14384260>

## Publications

- Schwartz, Dafna; Quinn, Lori; Fritz, Nora; Muratori, Lisa; Hausdorff, Jeffrey; Gilad-Bachrach, Ran (2024). *Accelerometer data of individuals with Huntington's disease and healthy controls from in-clinic assessment*. Zenodo. DOI: [10.5281/zenodo.14384260](https://doi.org/10.5281/zenodo.14384260)

```bibtex
@misc{hd_accel_jnet_data_2024,
  title = {Accelerometer data of individuals with Huntington's disease and healthy controls from in-clinic assessment},
  author = {Schwartz, Dafna and Quinn, Lori and Fritz, Nora and Muratori, Lisa and Hausdorff, Jeffrey and Gilad-Bachrach, Ran},
  year = {2024},
  doi = {10.5281/zenodo.14384260},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: hd_accel_jnet
- **family**: imu
- **MoveAtlas cells**: A7; M2
- **population**: 24 Huntington + 10 healthy; TMS, FA, TFC clinical scores
- **n_subjects**: 34
- **signal**: wrist accelerometer CSVs
- **license**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://zenodo.org/records/14384260
- **ingestion**: build_canonical_imu.py (hd_accel mapping)
- **known issues**: the CSV files carry no time column; the 100 Hz rate comes from the deposit's description and is stored in records built from 2026-09-17 (earlier records stored no rate)
