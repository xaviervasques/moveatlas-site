# AIHub multimodal Parkinson diagnosis imaging (Korea)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "AIHub multimodal Parkinson diagnosis imaging (Korea)",
 "description": "AIHub multimodal Parkinson diagnosis imaging (Korea). MoveAtlas bio family. 3719 subjects. licence gated: same AIHub Safety Zone enclave regime.",
 "identifier": "https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=516",
 "license": "gated: same AIHub Safety Zone enclave regime",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "B1 Rigidity",
  "B4 Akinesia",
  "M5 EMG"
 ],
 "url": "https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=516",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>aihub_pd_imaging</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 context; M5 |
| **Subjects** | 3719 |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): DOCUMENTED BARRIER (enclave). MRI + FDG-PET + FP-CIT PET DICOM + EMR across PD/MSA/CBD-PSP/DLB-PDD/ET, ~821k images - large differential-diagnosis parkinsonism cohort, no kinematics |
| **License** | gated: same AIHub Safety Zone enclave regime |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("aihub_pd_imaging")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: gated: same AIHub Safety Zone enclave regime
- **Redistribution**: no
- **Access route**: aihub.or.kr dataSetSn=516
- **Source**: <https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=516>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'bio'
- Source / URL: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=516
- License: gated: same AIHub Safety Zone enclave regime
- Access: aihub.or.kr dataSetSn=516
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): DOCUMENTED BARRIER (enclave). MRI + FDG-PET + FP-CIT PET DICOM + EMR across PD/MSA/CBD-PSP/DLB-PDD/ET, ~821k images - large differential-diagnosis parkinsonism cohort, no kinematics
- Number of subjects: 3719
- MoveAtlas cells: B1-B4 context; M5

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
