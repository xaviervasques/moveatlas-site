# Resting and postural tremor amplitude classification (OSF)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Resting and postural tremor amplitude classification (OSF)",
 "description": "Resting and postural tremor amplitude classification (OSF). MoveAtlas imu family. licence CC BY-NC-SA 4.0.",
 "identifier": "https://osf.io/mp5ha/",
 "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A2 Myoclonus",
  "B1 Rigidity",
  "M2 Inertial (IMU)"
 ],
 "url": "https://osf.io/mp5ha/",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>osf_tremor_amplitude</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">Rigidity</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A2; B1 context; M2 |
| **Status** | DOWNLOADED 2026-09-05: 719 files, OSF sha256-verified, journaled. CATALOGUED 2026-09-04 (closing sweep): wrist accelerometry feature CSVs + scripts spanning PD and ET tremor in a DBS context - small but cross-disorder A2/B1 bridge |
| **License** | CC BY-NC-SA 4.0 (VERIFIED 2026-09-05 from the fetched license.txt; NC-SA - licence-matrix decision needed before public release) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("osf_tremor_amplitude")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-NC-SA 4.0 (VERIFIED 2026-09-05 from the fetched license.txt; NC-SA - licence-matrix decision needed before public release)
- **Redistribution**: unknown
- **Access route**: osf.io/mp5ha
- **Source**: <https://osf.io/mp5ha/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://osf.io/mp5ha/
- License: CC BY-NC-SA 4.0 - VERIFIED 2026-09-05 from the fetched
  license.txt itself ((c) 2023 van der Linden; Dembek). The catalogue sweep's "open" was under-specified: NC-SA means NO commercial use
  and share-alike on derivatives. LICENCE-MATRIX DECISION NEEDED
  before this dataset enters any public MoveAtlas release (the NC
  clause is the question; SA is compatible with per-record licences)
- Access: osf.io/mp5ha
- Version / retrieval date: FETCHED 2026-09-05 (fetch_osf.py):
  719 files, every one verified against OSF's own sha256, journaled
  in downloads.sha256. One OSF rate-limit episode mid-fetch (500s on
  listings), resolved by a spaced probe - no retry storm
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): wrist accelerometry feature CSVs + scripts spanning PD and ET tremor in a DBS context - small but cross-disorder A2/B1 bridge
- Number of subjects: see record
- MoveAtlas cells: A2; B1 context; M2

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
None. Catalogue-tier until fetched and adjudicated.
