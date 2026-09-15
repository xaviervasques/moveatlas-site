# open-DBS: precision imaging during DBS (ScienceDB)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "open-DBS: precision imaging during DBS (ScienceDB)",
 "description": "open-DBS: precision imaging during DBS (ScienceDB). MoveAtlas bio family. 14 subjects. licence CC0.",
 "identifier": "https://doi.org/10.57760/sciencedb.26302",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
 "url": "https://doi.org/10.57760/sciencedb.26302",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>open_dbs_pd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 context; M5 |
| **Subjects** | 14 |
| **Status** | STILL PUBLIC 2026-09-07 (re-checked during the PIET withdrawal finding, case 13): no withdrawal statement, now V2 (updated 2025-12-19), page says 571.16 GB / 12413 files. CATALOGUED 2026-09-04: fMRI/sMRI under 7 DBS stimulation conditions x 5 timepoints + UPDRS, ~11.7 h fMRI per patient. TWO owner g... |
| **License** | CC0 (page re-verified 2026-09-07: PUBLIC banner + CC0 logo) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("open_dbs_pd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (page re-verified 2026-09-07: PUBLIC banner + CC0 logo)
- **Redistribution**: unknown
- **Access route**: sciencedb doi:10.57760/sciencedb.26302
- **Source**: <https://doi.org/10.57760/sciencedb.26302>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'bio'
- Source / URL: https://doi.org/10.57760/sciencedb.26302
- License: CC0 (ScienceDB record, to re-verify at fetch)
- Access: sciencedb doi:10.57760/sciencedb.26302
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): fMRI/sMRI under 7 DBS stimulation conditions x 5 timepoints + UPDRS, 613 GB / 12413 files, ~11.7 h fMRI per patient. SIZE DECISION needed before any fetch (disk); anti-bot as PIET
- Number of subjects: 14
- MoveAtlas cells: B1-B4 context; M5

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
