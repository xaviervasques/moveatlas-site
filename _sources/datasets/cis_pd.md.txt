# CIS-PD: smartwatch + symptom reports (BEAT-PD DREAM)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CIS-PD: smartwatch + symptom reports (BEAT-PD DREAM)",
 "description": "CIS-PD: smartwatch + symptom reports (BEAT-PD DREAM). MoveAtlas imu family. 16 subjects. licence gated: Synapse registration + data-use terms.",
 "identifier": "https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208",
 "license": "gated: Synapse registration + data-use terms (BEAT-PD challenge artifacts, syn22024261 family)",
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

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>cis_pd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Chorea</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 A7 dyskinesia labels; M2 |
| **Subjects** | 16 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (synapse-DUA tier): 2476 symptom reports incl. dyskinesia self-ratings against smartwatch accel - one of the only dyskinesia-labeled sensor corpora anywhere (ungated LID sensors: explicit negative) |
| **License** | gated: Synapse registration + data-use terms (BEAT-PD challenge artifacts, syn22024261 family) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cis_pd")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: gated: Synapse registration + data-use terms (BEAT-PD challenge artifacts, syn22024261 family)
- **Redistribution**: no
- **Access route**: synapse (BEAT-PD)
- **Source**: <https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000208
- License / access: gated: Synapse registration + data-use terms (BEAT-PD challenge artifacts, syn22024261 family)
- Access route: synapse (BEAT-PD)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (synapse-DUA tier): 2476 symptom reports incl. dyskinesia self-ratings against smartwatch accel - one of the only dyskinesia-labeled sensor corpora anywhere (ungated LID sensors: explicit negative)
- Number of subjects: 16
- MoveAtlas cells: B1-B4 A7 dyskinesia labels; M2

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
