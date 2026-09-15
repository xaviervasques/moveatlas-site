# 3D gait of typically developing children 3-13 y (Shanghai)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "3D gait of typically developing children 3-13 y (Shanghai)",
 "description": "3D gait of typically developing children 3-13 y (Shanghai). MoveAtlas pose family. 431 subjects. licence controlled access: ScienceDB access-request form + DUA.",
 "identifier": "https://doi.org/10.57760/sciencedb.40305",
 "license": "controlled access: ScienceDB access-request form + DUA (page verified 2026-09-05); anonymized pediatric mocap",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C1 Normal adult movement"
 ],
 "url": "https://doi.org/10.57760/sciencedb.40305",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>shanghai_child_gait3d</code>

<span class="ma-tag">Normal adult movement</span>

| | |
|---|---|
| **Taxonomy cells** | C1; D |
| **Subjects** | 431 |
| **Ages** | 3-13 y |
| **Status** | REQUEST TIER (verified 2026-09-05, browser): restricted-access banner, DUA-gated. CATALOGUED 2026-09-04 (closing sweep): raw C3D optical mocap marker trajectories, 379 MB / 6 files - pediatric normative gait reference; anti-bot as PIET |
| **License** | controlled access: ScienceDB access-request form + DUA (page verified 2026-09-05); anonymized pediatric mocap |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("shanghai_child_gait3d")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: controlled access: ScienceDB access-request form + DUA (page verified 2026-09-05); anonymized pediatric mocap
- **Redistribution**: unknown
- **Access route**: sciencedb doi:10.57760/sciencedb.40305
- **Source**: <https://doi.org/10.57760/sciencedb.40305>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'pose'
- Source / URL: https://doi.org/10.57760/sciencedb.40305
- License: open (anonymized; conditions in record - read at fetch)
- Access: sciencedb doi:10.57760/sciencedb.40305
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): raw C3D optical mocap marker trajectories, 379 MB / 6 files - pediatric normative gait reference; anti-bot as PIET
- Number of subjects: 431
- MoveAtlas cells: C1; D

- ACCESS VERDICT 2026-09-05 (browser check of the record page): the
  page banner reads "Restricted Access Dataset" - controlled access
  via a ScienceDB access-request form + Data Use Agreement (the only
  self-serve file is Data_Use_Agreement.pdf; pediatric mocap,
  anonymized but gated). The sweep's "open" was wrong. Per the
  no-emails/no-DUA house policy this moves to the REQUEST tier: the
  owner decides whether to submit the form (MJFF precedent). NOT
  fetchable autonomously.

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
