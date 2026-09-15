# Daphnet Freezing of Gait

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Daphnet Freezing of Gait",
 "description": "Daphnet Freezing of Gait. MoveAtlas imu family. 10 subjects. licence CC BY 4.0.",
 "identifier": "https://archive.ics.uci.edu/dataset/245/daphnet+freezing+of+gait",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B5 Freezing of gait",
  "M2 Inertial (IMU)"
 ],
 "url": "https://archive.ics.uci.edu/dataset/245/daphnet+freezing+of+gait",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Daniel Roggen, Meir Plotnik"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>daphnet</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M2 |
| **Subjects** | 10 |
| **Status** | INGESTED v1: 17 records |
| **License** | CC BY 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("daphnet")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: direct_download (UCI)
- **Source**: <https://archive.ics.uci.edu/dataset/245/daphnet+freezing+of+gait>

## Publications

- Daniel Roggen, Meir Plotnik (2010). *Daphnet Freezing of Gait*. UCI Machine Learning Repository. DOI: [10.24432/c56k78](https://doi.org/10.24432/c56k78)

```bibtex
@misc{daphnet_data_2010,
  title = {Daphnet Freezing of Gait},
  author = {Daniel Roggen, Meir Plotnik},
  year = {2010},
  doi = {10.24432/c56k78},
  howpublished = {UCI Machine Learning Repository},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: daphnet
- family: imu  (physical path: datasets/imu/daphnet)
- MoveAtlas cells: B5; M2
- population: 10 PD with FoG, walking protocols
- n_subjects: 10
- signal: 3 triaxial accelerometers (ankle, thigh, trunk) at 64 Hz + FoG annotations
- license: CC BY 4.0 ; redistribution: yes
- access: direct_download (UCI)
- status (2026-08-22): INGESTED v1: 17 records
- link: https://archive.ics.uci.edu/dataset/245/daphnet+freezing+of+gait
- ingestion: build_canonical_imu.py (daphnet mapping)
