# Free-living wearable + EMA monitoring in PD (DataverseNL)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Free-living wearable + EMA monitoring in PD (DataverseNL)",
 "description": "Free-living wearable + EMA monitoring in PD (DataverseNL). MoveAtlas imu family. 20 subjects. licence CC0.",
 "identifier": "https://doi.org/10.34894/5HHK8H",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B5 Freezing of gait",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.34894/5HHK8H",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dataversenl_pd_ema</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Freezing of gait</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B5; M2 |
| **Subjects** | 20 |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): 1129 EDF files of continuous free-living wearable movement recordings + ecological momentary assessment, 20 PD patients, 107 GB - the sweep's largest open find. DISK DECISION before fetch (107 GB) |
| **License** | CC0 (record page, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dataversenl_pd_ema")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (record page, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: dataverse doi:10.34894/5HHK8H
- **Source**: <https://doi.org/10.34894/5HHK8H>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://doi.org/10.34894/5HHK8H
- License: CC0 (record page, re-verify at fetch)
- Access: dataverse doi:10.34894/5HHK8H
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): 1129 EDF files of continuous free-living wearable movement recordings + ecological momentary assessment, 20 PD patients, 107 GB - the sweep's largest open find. DISK DECISION before fetch (107 GB)
- Number of subjects: 20
- MoveAtlas cells: B1-B5; M2

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
None. Catalogue-tier until fetched and adjudicated.
