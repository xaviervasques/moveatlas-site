# REMPARK home FOG accelerometry (UPC Barcelona / STAT-ON lineage)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "REMPARK home FOG accelerometry (UPC Barcelona / STAT-ON lineage)",
 "description": "REMPARK home FOG accelerometry (UPC Barcelona / STAT-ON lineage). MoveAtlas imu family. 21 subjects. licence no open release: 'available under reasonable request' from C.",
 "identifier": "https://pubmed.ncbi.nlm.nih.gov/35720090/",
 "license": "no open release: 'available under reasonable request' from CETpD-UPC; the STAT-ON commercial training DB is proprietary ",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B5 Freezing of gait",
  "M2 Inertial (IMU)"
 ],
 "url": "https://pubmed.ncbi.nlm.nih.gov/35720090/",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>rempark_staton</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M2 |
| **Subjects** | 21 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | no open release: 'available under reasonable request' from CETpD-UPC; the STAT-ON commercial training DB is proprietary (Sense4Care) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("rempark_staton")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: no open release: 'available under reasonable request' from CETpD-UPC; the STAT-ON commercial training DB is proprietary (Sense4Care)
- **Redistribution**: no
- **Access route**: CETpD-UPC
- **Source**: <https://pubmed.ncbi.nlm.nih.gov/35720090/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B5; M2
