# Oxford OPDC Discovery cohort wearable/smartphone substudies

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Oxford OPDC Discovery cohort wearable/smartphone substudies",
 "description": "Oxford OPDC Discovery cohort wearable/smartphone substudies. MoveAtlas imu family. licence ACCESS PROCESS SUSPENDED.",
 "identifier": "https://www.dpag.ox.ac.uk/opdc/research/external-collaborations",
 "license": "ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests ",
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
 "url": "https://www.dpag.ox.ac.uk/opdc/research/external-collaborations",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>opdc_discovery</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3 prodromal; M2 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests paused ~12 months while the cohort migrates to Oxford Brain Bank governance; afterwards: OBB panel + complexity-scaled fee |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("opdc_discovery")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests paused ~12 months while the cohort migrates to Oxford Brain Bank governance; afterwards: OBB panel + complexity-scaled fee
- **Redistribution**: no
- **Access route**: dpag.ox.ac.uk/opdc
- **Source**: <https://www.dpag.ox.ac.uk/opdc/research/external-collaborations>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B3 prodromal; M2
