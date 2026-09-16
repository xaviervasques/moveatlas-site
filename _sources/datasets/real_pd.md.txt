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
| **Status** | documented access barrier (2026-09-05) |
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4 A7; M2
