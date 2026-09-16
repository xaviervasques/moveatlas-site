# MJFF Levodopa Response Study (motor-fluctuation accelerometry)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MJFF Levodopa Response Study (motor-fluctuation accelerometry)",
 "description": "MJFF Levodopa Response Study (motor-fluctuation accelerometry). MoveAtlas imu family. licence MJFF data use agreement.",
 "identifier": "https://www.michaeljfox.org/data-sets",
 "license": "MJFF data use agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B4 Akinesia",
  "B2 Bradykinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://www.michaeljfox.org/data-sets",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>accel_fluctuations</code>

<span class="ma-tag">Akinesia</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B4 (motor fluctuations around dosing), B2; M2 |
| **Subjects** | unknown |
| **Status** | documented access barrier (2026-09-01) |
| **License** | MJFF data use agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("accel_fluctuations")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: MJFF data use agreement
- **Redistribution**: no
- **Access route**: application via MJFF data portal
- **Source**: <https://www.michaeljfox.org/data-sets>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: accel_fluctuations
- **family**: imu
- **MoveAtlas cells**: B4 (motor fluctuations around dosing), B2; M2
- **population**: PD patients, wearable accelerometry around levodopa dosing
- **n_subjects**: unknown
- **signal**: wrist/waist accelerometry with dosing schedule and symptom ratings
- **license**: MJFF data use agreement; redistribution: no
- **access**: application via MJFF data portal
- **link**: https://www.michaeljfox.org/data-sets
