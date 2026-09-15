# Ankle-sensor FoG semi-free-living (4TU.ResearchData)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Ankle-sensor FoG semi-free-living (4TU.ResearchData)",
 "description": "Ankle-sensor FoG semi-free-living (4TU.ResearchData). MoveAtlas imu family. licence open on 4TU.",
 "identifier": "https://data.4tu.nl/datasets/40e06061-f441-43b5-9235-006829206509",
 "license": "open on 4TU (version/licence to read on the record page at fetch)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B5 Freezing of gait",
  "M2 Inertial (IMU)"
 ],
 "url": "https://data.4tu.nl/datasets/40e06061-f441-43b5-9235-006829206509",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ankle_fog_4tu</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M2 |
| **Status** | CATALOGUED 2026-09-05: semi-free-living ankle IMU FoG recordings on 4TU (the tim_tremor host - watch for the empty-folder trap of that precedent) |
| **License** | open on 4TU (version/licence to read on the record page at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ankle_fog_4tu")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open on 4TU (version/licence to read on the record page at fetch)
- **Redistribution**: unknown
- **Access route**: 4tu doi record 40e06061-f441-43b5-9235-006829206509
- **Source**: <https://data.4tu.nl/datasets/40e06061-f441-43b5-9235-006829206509>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://data.4tu.nl/datasets/40e06061-f441-43b5-9235-006829206509
- License / access: open on 4TU (version/licence to read on the record page at fetch)
- Access route: 4tu doi record 40e06061-f441-43b5-9235-006829206509
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: semi-free-living ankle IMU FoG recordings on 4TU (the tim_tremor host - watch for the empty-folder trap of that precedent)
- Number of subjects: see record
- MoveAtlas cells: B5; M2

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
