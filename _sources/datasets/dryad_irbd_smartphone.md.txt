# Smartphone motor testing iRBD vs controls vs PD (Dryad)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Smartphone motor testing iRBD vs controls vs PD (Dryad)",
 "description": "Smartphone motor testing iRBD vs controls vs PD (Dryad). MoveAtlas imu family. licence CC0.",
 "identifier": "https://doi.org/10.5061/dryad.3qm0152",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "D6 Sleep disorders",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)",
  "M11 Voice / writing"
 ],
 "url": "https://doi.org/10.5061/dryad.3qm0152",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dryad_irbd_smartphone</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Sleep disorders</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 (PD); D6 prodromal (iRBD); C1 (controls); M2 M11 |
| **Status** | acquired (2026-09-05) |
| **License** | CC0 (Dryad, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dryad_irbd_smartphone")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (Dryad, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: dryad doi:10.5061/dryad.3qm0152
- **Source**: <https://doi.org/10.5061/dryad.3qm0152>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4 (PD); D6 prodromal (iRBD); C1 (controls); M2 M11
