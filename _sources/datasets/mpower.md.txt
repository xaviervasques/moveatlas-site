# mPower v1: smartphone PD study (Sage/Synapse)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "mPower v1: smartphone PD study (Sage/Synapse)",
 "description": "mPower v1: smartphone PD study (Sage/Synapse). MoveAtlas imu family. 3101 walk / 8003 tap / 5826 voice participants subjects. licence qualified-researcher tier.",
 "identifier": "https://www.synapse.org/mpower",
 "license": "qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + cond",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)",
  "M8 Imaging"
 ],
 "url": "https://www.synapse.org/mpower",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mpower</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3; M2 M8 |
| **Subjects** | 3101 walk / 8003 tap / 5826 voice participants |
| **Status** | catalogued (2026-09-05) |
| **License** | qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + conditions of use (non-reidentification); free |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mpower")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + conditions of use (non-reidentification); free
- **Redistribution**: no
- **Access route**: synapse syn4993293
- **Source**: <https://www.synapse.org/mpower>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B3; M2 M8
