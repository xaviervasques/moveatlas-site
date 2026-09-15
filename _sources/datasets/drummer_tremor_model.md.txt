# Expert drummers replicate physiological tremor signatures (Recherche Data Gouv)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Expert drummers replicate physiological tremor signatures (Recherche Data Gouv)",
 "description": "Expert drummers replicate physiological tremor signatures (Recherche Data Gouv). MoveAtlas imu family. 18 subjects. licence etalab 2.0.",
 "identifier": "https://doi.org/10.57745/thhwp2",
 "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A2 Myoclonus",
  "C2 Infant development",
  "M2 Inertial (IMU)",
  "M4 Silhouette"
 ],
 "url": "https://doi.org/10.57745/thhwp2",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>drummer_tremor_model</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">Infant development</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | A2 context; C2; M2 M4 |
| **Subjects** | 18 |
| **Status** | DOWNLOADED 2026-09-05: 136 files / 3.1 GB C3D, server-MD5 verified, sha256 journaled. CATALOGUED 2026-09-04 (closing sweep): raw kinematics + EMG of expert drummers at extreme movement frequencies - a healthy mechanistic model of physiological tremor, context lane for A2 |
| **License** | etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("drummer_tremor_model")
records, meta = ds.get_data()
```

## License and access

- **License**: etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version)
- **Redistribution**: yes (etalab 2.0: attribution obligatoire - fetch-verified 2026-09-05)
- **Access route**: rdg doi:10.57745/thhwp2
- **Source**: <https://doi.org/10.57745/thhwp2>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'imu'
- Source / URL: https://doi.org/10.57745/thhwp2
- License (fetch-verified 2026-09-05): etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version)
- Sweep's original licence guess: open per DataCite (re-verify when RDG returns)
- Access: rdg doi:10.57745/thhwp2
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); fetch 2026-09-05 via fetch_dataverse.py (RDG back from maintenance)
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): raw kinematics + EMG of expert drummers at extreme movement frequencies - a healthy mechanistic model of physiological tremor, context lane for A2
- Number of subjects: 18
- MoveAtlas cells: A2 context; C2; M2 M4

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
