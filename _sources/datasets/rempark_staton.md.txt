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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (request tier): 21 PD, waist accel 200 Hz, ON/OFF states, >1000 video-labeled home FOG episodes - uniquely labeled home data locked behind email-the-owner; commercial descendant proprietary |
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
- **Access route**: CETpD-UPC (owner request)
- **Source**: <https://pubmed.ncbi.nlm.nih.gov/35720090/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://pubmed.ncbi.nlm.nih.gov/35720090/
- License / access regime: no open release: 'available under reasonable request' from CETpD-UPC; the STAT-ON commercial training DB is proprietary (Sense4Care)
- Access route: CETpD-UPC (owner request)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (request tier): 21 PD, waist accel 200 Hz, ON/OFF states, >1000 video-labeled home FOG episodes - uniquely labeled home data locked behind email-the-owner; commercial descendant proprietary
- Number of subjects: 21
- MoveAtlas cells: B5; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
