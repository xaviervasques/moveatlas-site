# Huntington wrist accelerometry (J-Net)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Huntington wrist accelerometry (J-Net)",
 "description": "Huntington wrist accelerometry (J-Net). MoveAtlas imu family. 34 subjects. licence Zenodo open.",
 "identifier": "https://zenodo.org/records/14384260",
 "license": "Zenodo open",
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
| **Status** | INGESTED v1: 35 records |
| **License** | Zenodo open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("hd_accel_jnet")
records, meta = ds.get_data()
```

## License and access

- **License**: Zenodo open
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

## Data card (verbatim, with its evidence trail)


- dataset: hd_accel_jnet
- family: imu  (physical path: datasets/imu/hd_accel_jnet)
- MoveAtlas cells: A7; M2
- population: 24 Huntington + 10 healthy; TMS, FA, TFC clinical scores
- n_subjects: 34
- signal: wrist accelerometer CSVs
- license: Zenodo open ; redistribution: yes
- access: downloaded
- status (2026-08-22): INGESTED v1: 35 records
- link: https://zenodo.org/records/14384260
- ingestion: build_canonical_imu.py (hd_accel mapping)
