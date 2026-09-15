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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER: 82 early untreated PD + 50 controls x 12 months of consumer+research wearables; access is consortium membership or a steering-committee proposal - the pay-to-play consortium model for the barriers taxonomy |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11169239/
- License / access regime: consortium-only (C-Path 3DT Stage 2) or ad-hoc proposal to the steering committee via the corresponding author; NO public release (paper's own availability statement)
- Access route: URMC / C-Path 3DT
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER: 82 early untreated PD + 50 controls x 12 months of consumer+research wearables; access is consortium membership or a steering-committee proposal - the pay-to-play consortium model for the barriers taxonomy
- Number of subjects: 132
- MoveAtlas cells: B1-B3; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
