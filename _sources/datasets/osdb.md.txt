# OpenSeizureDatabase (smartwatch seizure movement)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "OpenSeizureDatabase (smartwatch seizure movement)",
 "description": "OpenSeizureDatabase (smartwatch seizure movement). MoveAtlas imu family. licence custom CC-Share-Alike variant + publish-back obligation.",
 "identifier": "https://github.com/OpenSeizureDetector/OpenSeizureDatabase",
 "license": "custom CC-Share-Alike variant + publish-back obligation",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "D1 Epilepsy",
  "M2 Inertial (IMU)"
 ],
 "url": "https://github.com/OpenSeizureDetector/OpenSeizureDatabase",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>osdb</code>

<span class="ma-tag">Epilepsy</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | D1; M2 |
| **Subjects** | not stated |
| **Status** | DOCUMENTED BARRIER (owner, 2026-08-28): the email-gated access stays closed under the standing no-emails decision; not reopened |
| **License** | custom CC-Share-Alike variant + publish-back obligation |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("osdb")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: custom CC-Share-Alike variant + publish-back obligation
- **Redistribution**: no
- **Access route**: application: email osdb@openseizuredetector.org.uk (data in private repo)
- **Source**: <https://github.com/OpenSeizureDetector/OpenSeizureDatabase>

## Publications

-  (). **. .

## Data card (verbatim, with its evidence trail)


- dataset: osdb
- family: imu  (physical path: datasets/imu/osdb)
- MoveAtlas cells: D1; M2
- population: crowdsourced OpenSeizureDetector users; seizure / seizure-like / false-alarm labeled events
- n_subjects: not stated
- signal: wrist 3-axis accelerometer (+HR) JSON event snippets, ~25 Hz
- license: custom CC-Share-Alike variant + publish-back obligation ; redistribution: no
- access: application: email osdb@openseizuredetector.org.uk (data in private repo)
- status (2026-08-22): DOCUMENTED BARRIER (owner, 2026-08-28): the email-gated access stays closed under the standing no-emails decision; not reopened
- link: https://github.com/OpenSeizureDetector/OpenSeizureDatabase
- notes: toolkit code public (GPL-3); only real-world wearable seizure corpus found
