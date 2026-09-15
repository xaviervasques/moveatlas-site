# REAL-PD / Parkinson@Home (BEAT-PD DREAM)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "REAL-PD / Parkinson@Home (BEAT-PD DREAM)",
 "description": "REAL-PD / Parkinson@Home (BEAT-PD DREAM). MoveAtlas imu family. 12 subjects. licence gated: Synapse registration + data-use terms.",
 "identifier": "https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208",
 "license": "gated: Synapse registration + data-use terms",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "A7 Chorea",
  "M2 Inertial (IMU)"
 ],
 "url": "https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>real_pd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Chorea</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 A7; M2 |
| **Subjects** | 12 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER: 782 symptom reports, home smartwatch+phone sensors, dyskinesia/tremor self-labels - CIS-PD's home-setting sibling |
| **License** | gated: Synapse registration + data-use terms |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("real_pd")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: gated: Synapse registration + data-use terms
- **Redistribution**: no
- **Access route**: synapse (BEAT-PD)
- **Source**: <https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208
- License / access: gated: Synapse registration + data-use terms
- Access route: synapse (BEAT-PD)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER: 782 symptom reports, home smartwatch+phone sensors, dyskinesia/tremor self-labels - CIS-PD's home-setting sibling
- Number of subjects: 12
- MoveAtlas cells: B1-B4 A7; M2

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
