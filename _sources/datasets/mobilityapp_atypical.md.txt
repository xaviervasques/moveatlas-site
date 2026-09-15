# MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD)",
 "description": "MobilityAPP: daily-life mobility in atypical parkinsonism (PSP+MSA+PD). MoveAtlas imu family. 84 (20 PSP + 23 MSA + 41 PD) subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/19819191",
 "license": "https://creativecommons.org/licenses/by/4.0/",
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
 "url": "https://zenodo.org/records/19819191",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mobilityapp_atypical</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 atypical; M2 |
| **Subjects** | 84 (20 PSP + 23 MSA + 41 PD) |
| **Status** | DOWNLOADED 2026-09-05 (31 KB: 5 CSVs of DERIVED gait/TUG/activity parameters - NO raw IMU; cc-by-4.0 API-verified). CATALOGUED 2026-09-05 (deep-dive): instrumented gait (10m walk, TUG) + multi-day wearable activity + clinical scores - the ONLY open sensor deposit with PSP and MSA arms found anywhere... |
| **License** | CC BY 4.0 (Zenodo record, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mobilityapp_atypical")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo record, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: zenodo 19819191
- **Source**: <https://zenodo.org/records/19819191>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://zenodo.org/records/19819191
- License / access: CC BY 4.0 (Zenodo record, re-verify at fetch)
- Access route: zenodo 19819191
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep). FETCHED 2026-09-05 same session: cc-by-4.0 confirmed via the
  Zenodo API, server-md5 verified, sha256 journaled. CONTENT VERDICT:
  the zip is 31 KB - five CSVs of DERIVED parameters (IGA.csv gait
  analysis, TUG.csv, PAM.csv activity monitoring + metadata), NO raw
  IMU streams. The caveat is confirmed: parameters-tier, still the
  only open PSP/MSA sensor-derived deposit anywhere
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): instrumented gait (10m walk, TUG) + multi-day wearable activity + clinical scores - the ONLY open sensor deposit with PSP and MSA arms found anywhere. Caveat: record page describes gait/activity PARAMETERS; confirm raw IMU streams after download
- Number of subjects: 84 (20 PSP + 23 MSA + 41 PD)
- MoveAtlas cells: B1-B4 atypical; M2

### Retrieval notes
RE-VERIFY at fetch/request. No-emails policy for request tiers.

### Processing
None. Catalogue-tier.
