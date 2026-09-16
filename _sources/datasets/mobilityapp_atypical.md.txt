# MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD)",
 "description": "MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD). MoveAtlas imu family. 84 (20 PSP + 23 MSA + 41 PD) subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/19819191",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/19819191",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mobilityapp_atypical</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 atypical; M2 |
| **Subjects** | 84 (20 PSP + 23 MSA + 41 PD) |
| **Status** | acquired (2026-09-05) |
| **License** | CC BY 4.0 (Zenodo record, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mobilityapp_atypical")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo record, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: zenodo 19819191
- **Source**: <https://zenodo.org/records/19819191>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4 atypical; M2
