# STIL Orthosis essential tremor suppression accelerometry (DANS)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "STIL Orthosis essential tremor suppression accelerometry (DANS)",
 "description": "STIL Orthosis essential tremor suppression accelerometry (DANS). MoveAtlas imu family. 24 subjects. licence gated: DANS registration/request.",
 "identifier": "https://doi.org/10.17026/LS/WV4ASD",
 "license": "gated: DANS registration/request",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A2 Myoclonus",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.17026/LS/WV4ASD",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>stil_orthosis_tremor</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A2; M2 |
| **Subjects** | 24 |
| **Status** | catalogued (2026-09-04) |
| **License** | gated: DANS registration/request |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("stil_orthosis_tremor")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: gated: DANS registration/request
- **Redistribution**: unknown
- **Access route**: dans doi:10.17026/LS/WV4ASD
- **Source**: <https://doi.org/10.17026/LS/WV4ASD>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A2; M2
