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
| **Status** | CATALOGUED 2026-09-04 (closing sweep): raw tremor accelerometry with/without a suppression device + TETRAS, randomized crossover, 30 files - a rare RAW-signal ET deposit, A2 candidate if the registration route is self-serve (verify: registration vs request) |
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

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'imu'
- Source / URL: https://doi.org/10.17026/LS/WV4ASD
- License: gated: DANS registration/request
- Access: dans doi:10.17026/LS/WV4ASD
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): raw tremor accelerometry with/without a suppression device + TETRAS, randomized crossover, 30 files - a rare RAW-signal ET deposit, A2 candidate if the registration route is self-serve (verify: registration vs request)
- Number of subjects: 24
- MoveAtlas cells: A2; M2

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
