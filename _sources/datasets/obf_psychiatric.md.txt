# OBF-Psychiatric motor-activity actigraphy (incl. antipsychotic-treated schizophrenia)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "OBF-Psychiatric motor-activity actigraphy (incl. antipsychotic-treated schizophrenia)",
 "description": "OBF-Psychiatric motor-activity actigraphy (incl. antipsychotic-treated schizophrenia). MoveAtlas imu family. 162 subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/13754984",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "E6 Iatrogenic",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/13754984",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>obf_psychiatric</code>

<span class="ma-tag">Iatrogenic</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | E6 drug-exposed context; M2 |
| **Subjects** | 162 |
| **Status** | DOWNLOADED 2026-09-05: 10.4 MB zip, cc-by-4.0 API-verified, md5-verified. CATALOGUED 2026-09-05: 1565 days of wrist actigraphy across psychiatric cohorts incl. antipsychotic-treated schizophrenia - context lane for the drug-induced axis (no akathisia/AIMS labels: the tardive/akathisia absences stand... |
| **License** | CC BY 4.0 (Zenodo 13754984, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("obf_psychiatric")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo 13754984, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: zenodo 13754984
- **Source**: <https://zenodo.org/records/13754984>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://zenodo.org/records/13754984
- License / access: CC BY 4.0 (Zenodo 13754984, re-verify at fetch)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  drug-induced/functional pass; records verified at file level
  by the catalogue sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05: 1565 days of wrist actigraphy across psychiatric cohorts incl. antipsychotic-treated schizophrenia - context lane for the drug-induced axis (no akathisia/AIMS labels: the tardive/akathisia absences stand)
- MoveAtlas cells: E6 drug-exposed context; M2

### Retrieval notes
RE-VERIFY at fetch. The two OSF FMD deposits carry NO licence:
INTERNAL-ONLY after fetch until terms are adjudicated (goodwin_smm
precedent).

### Processing
None. Catalogue-tier.
