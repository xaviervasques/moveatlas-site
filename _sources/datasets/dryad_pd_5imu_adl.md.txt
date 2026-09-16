# Five-sensor IMU PD + controls during activities of daily living (Dryad)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Five-sensor IMU PD + controls during activities of daily living (Dryad)",
 "description": "Five-sensor IMU PD + controls during activities of daily living (Dryad). MoveAtlas imu family. licence CC0.",
 "identifier": "https://doi.org/10.5061/dryad.fbg79cp1d",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.5061/dryad.fbg79cp1d",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dryad_pd_5imu_adl</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3; M2 |
| **Status** | blocked at the host for scripted clients (2026-09-05) |
| **License** | CC0 (Dryad, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dryad_pd_5imu_adl")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (Dryad, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: dryad doi:10.5061/dryad.fbg79cp1d
- **Source**: <https://doi.org/10.5061/dryad.fbg79cp1d>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B3; M2
