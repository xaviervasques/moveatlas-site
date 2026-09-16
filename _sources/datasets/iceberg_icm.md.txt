# ICEBERG cohort

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ICEBERG cohort",
 "description": "ICEBERG cohort. MoveAtlas imu family. licence 'available upon reasonable request from any qualified invest.",
 "identifier": "https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization",
 "license": "'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "M2 Inertial (IMU)",
  "M6 EEG"
 ],
 "url": "https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>iceberg_icm</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 prodromal; M2 M6 |
| **Subjects** | ~300 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | 'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("iceberg_icm")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: 'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal
- **Redistribution**: no
- **Access route**: ICM / NCT02305147
- **Source**: <https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4 prodromal; M2 M6
