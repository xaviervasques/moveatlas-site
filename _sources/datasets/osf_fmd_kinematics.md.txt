# FMD sensorimotor limb-movement kinematics (OSF 78xun; ETUDE MSCA)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "FMD sensorimotor limb-movement kinematics (OSF 78xun; ETUDE MSCA)",
 "description": "FMD sensorimotor limb-movement kinematics (OSF 78xun; ETUDE MSCA). MoveAtlas imu family. licence NO EXPLICIT LICENCE on the OSF project.",
 "identifier": "https://osf.io/78xun",
 "license": "NO EXPLICIT LICENCE on the OSF project (same adjudication gate)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "D7 Functional movement disorders",
  "M2 Inertial (IMU)",
  "M4 Silhouette"
 ],
 "url": "https://osf.io/78xun",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>osf_fmd_kinematics</code>

<span class="ma-tag">Functional movement disorders</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | D7 functional; M2 M4 |
| **Status** | DOWNLOADED 2026-09-05: 24 files 117.5 MB (FMD.mat + pipeline), OSF sha256-verified; INTERNAL-ONLY pending licence adjudication. CATALOGUED 2026-09-05: trial-level limb velocity traces (FMD.mat 110 MB) + full analysis pipeline - the second genuine open FMD deposit; with osf_fmd_eeg it revises D7 from... |
| **License** | NO EXPLICIT LICENCE on the OSF project (same adjudication gate) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("osf_fmd_kinematics")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NO EXPLICIT LICENCE on the OSF project (same adjudication gate)
- **Redistribution**: unknown
- **Access route**: osf.io/78xun
- **Source**: <https://osf.io/78xun>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://osf.io/78xun
- License / access: NO EXPLICIT LICENCE on the OSF project (same adjudication gate)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  drug-induced/functional pass; records verified at file level
  by the catalogue sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05: trial-level limb velocity traces (FMD.mat 110 MB) + full analysis pipeline - the second genuine open FMD deposit; with osf_fmd_eeg it revises D7 from 'nothing at all' to 'two processed-signal deposits, licence-pending'
- MoveAtlas cells: D7 functional; M2 M4

### Retrieval notes
RE-VERIFY at fetch. The two OSF FMD deposits carry NO licence:
INTERNAL-ONLY after fetch until terms are adjudicated (goodwin_smm
precedent).

### Processing
None. Catalogue-tier.
