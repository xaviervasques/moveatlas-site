# Personalized Parkinson Project (Radboud; Verily watch 2-3 y)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Personalized Parkinson Project (Radboud; Verily watch 2-3 y)",
 "description": "Personalized Parkinson Project (Radboud; Verily watch 2-3 y). MoveAtlas imu family. 520 subjects. licence committee proposal.",
 "identifier": "https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3",
 "license": "https://opensource.org/license/mit",
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
 "url": "https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>ppp_radboud</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4; M2 |
| **Subjects** | 520 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | committee proposal (RDSRC) + PEP polymorphic-encryption enclave; 2025: migrating to Verily Workbench as 'public resource' (enclave-style), rollout in progress |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ppp_radboud")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: committee proposal (RDSRC) + PEP polymorphic-encryption enclave; 2025: migrating to Verily Workbench as 'public resource' (enclave-style), rollout in progress
- **Redistribution**: no
- **Access route**: radboud PPP (NCT sisters 04985539/05501431)
- **Source**: <https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4; M2
