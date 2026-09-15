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
| **Status** | CATALOGUED 2026-09-04 (closing sweep): DOCUMENTED BARRIER (enclave model - usable for benchmarking claims, never for corpus redistribution). Kinect skeletons + multi-site IMU + voice, PD/sarcopenia/frailty, ~1.19 M records, medication-state labels. The strongest enclave example for the barriers pape... |
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

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'imu'
- Source / URL: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71425
- License: gated: Korean nationals only, IRB + security agreement, analysis in the 'Online Safety Zone' enclave - NO raw export
- Access: aihub.or.kr dataSetSn=71425
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): DOCUMENTED BARRIER (enclave model - usable for benchmarking claims, never for corpus redistribution). Kinect skeletons + multi-site IMU + voice, PD/sarcopenia/frailty, ~1.19 M records, medication-state labels. The strongest enclave example for the barriers paper
- Number of subjects: 500
- MoveAtlas cells: B2; C1; M2

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
