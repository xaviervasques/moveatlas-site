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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (two-stage): standard PPMI DUA unlocks derived Verily sleep/activity/vitals tables; raw watch accel/gyro/PPG requires the separate Verily Raw Device Data Request Form. A clean example of layered gating inside one cohort |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://www.ppmi-info.org/access-data-specimens/download-data
- License / access regime: PPMI DUA + application (~1 week, free); Verily RAW device data needs a SECOND request form (Study Docs) - derived tables come with the standard download
- Access route: ppmi-info.org + LONI
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (two-stage): standard PPMI DUA unlocks derived Verily sleep/activity/vitals tables; raw watch accel/gyro/PPG requires the separate Verily Raw Device Data Request Form. A clean example of layered gating inside one cohort
- Number of subjects: see record
- MoveAtlas cells: B1-B4; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
