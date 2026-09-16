# Luxembourg Parkinson's Study wearable gait (NCER-PD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Luxembourg Parkinson's Study wearable gait (NCER-PD)",
 "description": "Luxembourg Parkinson's Study wearable gait (NCER-PD). MoveAtlas imu family. 162 PD + 129 controls subjects. licence no cost published; no self-serve.",
 "identifier": "https://www.nature.com/articles/s41746-024-01236-z",
 "license": "no cost published; no self-serve",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://www.nature.com/articles/s41746-024-01236-z",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>ncer_pd_gait</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M2 |
| **Subjects** | 162 PD + 129 controls |
| **Status** | documented access barrier (2026-09-05) |
| **License** | no cost published; no self-serve |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ncer_pd_gait")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: no cost published; no self-serve
- **Redistribution**: no
- **Access route**: parkinson.lu
- **Source**: <https://www.nature.com/articles/s41746-024-01236-z>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B2; M2
