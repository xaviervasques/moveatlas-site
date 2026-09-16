# PPMI digital-sensor substudies (Verily watch + Roche app + Axivity)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PPMI digital-sensor substudies (Verily watch + Roche app + Axivity)",
 "description": "PPMI digital-sensor substudies (Verily watch + Roche app + Axivity). MoveAtlas imu family. licence PPMI DUA + application.",
 "identifier": "https://www.ppmi-info.org/access-data-specimens/download-data",
 "license": "PPMI DUA + application (~1 week, free); Verily RAW device data needs a SECOND request form (Study Docs) - derived tables",
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
 "url": "https://www.ppmi-info.org/access-data-specimens/download-data",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>ppmi_sensors</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4; M2 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | PPMI DUA + application (~1 week, free); Verily RAW device data needs a SECOND request form (Study Docs) - derived tables come with the standard download |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ppmi_sensors")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: PPMI DUA + application (~1 week, free); Verily RAW device data needs a SECOND request form (Study Docs) - derived tables come with the standard download
- **Redistribution**: no
- **Access route**: ppmi-info.org + LONI
- **Source**: <https://www.ppmi-info.org/access-data-specimens/download-data>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4; M2
