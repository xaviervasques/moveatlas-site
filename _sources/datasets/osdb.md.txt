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
| **Status** | documented access barrier (2026-08-28) |
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: osdb
- **family**: imu
- **MoveAtlas cells**: D1; M2
- **population**: crowdsourced OpenSeizureDetector users; seizure / seizure-like / false-alarm labeled events
- **n_subjects**: not stated
- **signal**: wrist 3-axis accelerometer (+HR) JSON event snippets, ~25 Hz
- **license**: custom CC-Share-Alike variant + publish-back obligation; redistribution: no
- **access**: application: email osdb@openseizuredetector.org.uk (data in private repo)
- **link**: https://github.com/OpenSeizureDetector/OpenSeizureDatabase
