# PIET: Precision Imaging Essential Tremor (ScienceDB)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PIET: Precision Imaging Essential Tremor (ScienceDB)",
 "description": "PIET: Precision Imaging Essential Tremor (ScienceDB). MoveAtlas bio family. 45 subjects. licence CC0 banner still displayed.",
 "identifier": "https://doi.org/10.57760/sciencedb.28935",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A2 Myoclonus",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.57760/sciencedb.28935",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>piet_essential_tremor</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | A2 context; M5 |
| **Subjects** | 45 |
| **Status** | WITHDRAWN AT SOURCE (found 2026-09-07 at fetch time, case 13): the download section now carries a Dataset Withdrawal Statement - not publicly available per hospital requirements, contact corresponding authors. PUBLIC/CC0 had been page-verified 2026-09-05; DataCite metadata and the page's PUBLIC/CC0... |
| **License** | CC0 banner still displayed, but access WITHDRAWN (page 2026-09-07) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("piet_essential_tremor")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 banner still displayed, but access WITHDRAWN (page 2026-09-07)
- **Redistribution**: no
- **Access route**: sciencedb doi:10.57760/sciencedb.28935
- **Source**: <https://doi.org/10.57760/sciencedb.28935>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'bio'
- Source / URL: https://doi.org/10.57760/sciencedb.28935
- License: CC0 (ScienceDB record, to re-verify at fetch)
- Access: sciencedb doi:10.57760/sciencedb.28935
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): structural MRI + 5 fMRI runs/subject, 30.6 GB / 589 files - the neuroimaging arm for tremor phenotyping; no kinematics. ScienceDB blocks generic fetchers (anti-bot): fetch via DataCite-resolved links or browser route
- Number of subjects: 45
- MoveAtlas cells: A2 context; M5

- ACCESS VERDICT 2026-09-05 (browser check): the page banner reads
  "PUBLIC Dataset, CC0" - self-serve confirmed. FETCH DEFERRED until
  the 000947 pull completes (30.6 GB on the shared link; owner
  sequencing: current transfers first).

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
