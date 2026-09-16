# WATCH-PD (Apple Watch + iPhone + APDM in early PD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "WATCH-PD (Apple Watch + iPhone + APDM in early PD)",
 "description": "WATCH-PD (Apple Watch + iPhone + APDM in early PD). MoveAtlas imu family. 132 subjects. licence consortium-only.",
 "identifier": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11169239/",
 "license": "https://opensource.org/license/mit",
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
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11169239/",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>watch_pd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3; M2 |
| **Subjects** | 132 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | consortium-only (C-Path 3DT Stage 2) or ad-hoc proposal to the steering committee via the corresponding author; NO public release (paper's own availability statement) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("watch_pd")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: consortium-only (C-Path 3DT Stage 2) or ad-hoc proposal to the steering committee via the corresponding author; NO public release (paper's own availability statement)
- **Redistribution**: no
- **Access route**: URMC / C-Path 3DT
- **Source**: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11169239/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B3; M2
