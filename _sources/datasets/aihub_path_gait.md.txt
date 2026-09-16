# AIHub normal and pathological gait fusion data (Korea)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "AIHub normal and pathological gait fusion data (Korea)",
 "description": "AIHub normal and pathological gait fusion data (Korea). MoveAtlas imu family. 500 subjects. licence gated: Korean nationals only.",
 "identifier": "https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71425",
 "license": "gated: Korean nationals only, IRB + security agreement, analysis in the 'Online Safety Zone' enclave - NO raw export",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)"
 ],
 "url": "https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71425",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>aihub_path_gait</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2; C1; M2 |
| **Subjects** | 500 |
| **Ages** | elderly |
| **Status** | documented access barrier (2026-09-04) |
| **License** | gated: Korean nationals only, IRB + security agreement, analysis in the 'Online Safety Zone' enclave - NO raw export |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("aihub_path_gait")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: gated: Korean nationals only, IRB + security agreement, analysis in the 'Online Safety Zone' enclave - NO raw export
- **Redistribution**: no
- **Access route**: aihub.or.kr dataSetSn=71425
- **Source**: <https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71425>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B2; C1; M2
