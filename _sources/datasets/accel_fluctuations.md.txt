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
| **Status** | DOCUMENTED BARRIER: access request refused (ACT), recorded in the 2026-08 hunt; RECOVERED INTO THE REGISTRY 2026-09-01 (adjudication item 21: it existed only in taxonomy_map). The only B4 candidate in either source; nothing to fetch |
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

## Data card (verbatim, with its evidence trail)


- dataset: accel_fluctuations
- family: imu  (physical path: datasets/imu/accel_fluctuations)
- MoveAtlas cells: B4 (motor fluctuations around dosing), B2; M2
- population: PD patients, wearable accelerometry around levodopa dosing
- n_subjects: unknown
- signal: wrist/waist accelerometry with dosing schedule and symptom ratings
- license: MJFF data use agreement ; redistribution: no
- access: application via MJFF data portal
- status (2026-08-22): DOCUMENTED BARRIER: access request refused (ACT), recorded in the 2026-08 hunt; RECOVERED INTO THE REGISTRY 2026-09-01 (adjudication item 21: it existed only in taxonomy_map). The only B4 candidate in either source; nothing to fetch
- link: https://www.michaeljfox.org/data-sets
