# Activity-based accelerometry in essential tremor (Mendeley)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Activity-based accelerometry in essential tremor (Mendeley)",
 "description": "Activity-based accelerometry in essential tremor (Mendeley). MoveAtlas imu family. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.17632/fd6sdp6t7x.1",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A2 Myoclonus",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.17632/fd6sdp6t7x.1",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mendeley_et_accel</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A2; M2 |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): smartwatch + phone accelerometry rated against Fahn-Tolosa-Marin - an open RAW-signal A2 addition. CONTENT VERDICT: demo-plus-labels deposit (one subject raw stream + 770 labeled windows), not a full raw corpus - harmonization deferred |
| **License** | CC BY 4.0 (record, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mendeley_et_accel")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (record, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: mendeley doi:10.17632/fd6sdp6t7x.1
- **Source**: <https://doi.org/10.17632/fd6sdp6t7x.1>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://doi.org/10.17632/fd6sdp6t7x.1
- License: CC BY 4.0 (record, re-verify at fetch)
- Access: mendeley doi:10.17632/fd6sdp6t7x.1
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): smartwatch + phone accelerometry rated against Fahn-Tolosa-Marin - an open RAW-signal A2 addition
- Number of subjects: see record
- MoveAtlas cells: A2; M2

- CONTENT VERDICT 2026-09-05 (RData opened with pyreadr): the deposit
  is a DEMO-plus-labels package - one participant's raw smartwatch
  stream (df.p17: 19,456 samples x/y/z/amplitude + timestamps + Pebble
  MAC) plus 770 windowed activity labels and FTM scores (raw.lab,
  raw.score) and 6 subject-level ratings (sc1/sc2). NOT a full raw
  corpus: canonical harmonization deferred (one partial subject does
  not meet the record bar); stays a labeled-features holding.

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
None. Catalogue-tier until fetched and adjudicated.
