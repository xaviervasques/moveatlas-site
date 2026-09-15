# Luxembourg Parkinson's Study wearable gait (NCER-PD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Luxembourg Parkinson's Study wearable gait (NCER-PD)",
 "description": "Luxembourg Parkinson's Study wearable gait (NCER-PD). MoveAtlas imu family. 162 PD + 129 controls subjects. licence documented request route: form to request.ncer-pd@uni.lu.",
 "identifier": "https://www.nature.com/articles/s41746-024-01236-z",
 "license": "documented request route: form to request.ncer-pd@uni.lu, internal review; no cost published; no self-serve",
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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (form tier, low friction): eGaIT IMU gait on 291 subjects inside an ~800-PD national cohort. The cleanest request route of the sweep - a candidate if the owner ever opens the request lane (no-emails policy holds otherwise) |
| **License** | documented request route: form to request.ncer-pd@uni.lu, internal review; no cost published; no self-serve |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ncer_pd_gait")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: documented request route: form to request.ncer-pd@uni.lu, internal review; no cost published; no self-serve
- **Redistribution**: no
- **Access route**: parkinson.lu
- **Source**: <https://www.nature.com/articles/s41746-024-01236-z>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://www.nature.com/articles/s41746-024-01236-z
- License / access regime: documented request route: form to request.ncer-pd@uni.lu, internal review; no cost published; no self-serve
- Access route: parkinson.lu
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (form tier, low friction): eGaIT IMU gait on 291 subjects inside an ~800-PD national cohort. The cleanest request route of the sweep - a candidate if the owner ever opens the request lane (no-emails policy holds otherwise)
- Number of subjects: 162 PD + 129 controls
- MoveAtlas cells: B2; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
