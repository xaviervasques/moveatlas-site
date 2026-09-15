# MindTS-MMD: pediatric Tourette multimodal corpus (Mendeley)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MindTS-MMD: pediatric Tourette multimodal corpus (Mendeley)",
 "description": "MindTS-MMD: pediatric Tourette multimodal corpus (Mendeley). MoveAtlas video family. 60 subjects. licence CC BY 4.0 per the record.",
 "identifier": "https://doi.org/10.17632/kswgcms346.1",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "video",
  "A3 Tics",
  "M1 Pose / video",
  "M8 Imaging"
 ],
 "url": "https://doi.org/10.17632/kswgcms346.1",
 "isAccessibleForFree": false,
 "measurementTechnique": "video",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-video">video</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mindts_tourette</code>

<span class="ma-tag">Tics</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A3; M1 M8 |
| **Subjects** | 60 |
| **Ages** | 6-12 y |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): video + audio + text, >120 h of sessions, expert tic-frequency and affect annotations, 60 children. IF the content check confirms movement signal + de-identification, this REVISES the A3 tics absence (currently: refutation PENDING VERIFICATION). Ethics gate BEF... |
| **License** | CC BY 4.0 per the record (VERIFY AT FETCH - and verify the de-identification claim before ANY use: video of minors, the SSBD ethics precedent applies) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mindts_tourette")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 per the record (VERIFY AT FETCH - and verify the de-identification claim before ANY use: video of minors, the SSBD ethics precedent applies)
- **Redistribution**: unknown
- **Access route**: mendeley doi:10.17632/kswgcms346.1
- **Source**: <https://doi.org/10.17632/kswgcms346.1>

## Data card (verbatim, with its evidence trail)


- Modality: family 'video'
- Source / URL: https://doi.org/10.17632/kswgcms346.1
- License: CC BY 4.0 per the record (VERIFY AT FETCH - and verify the de-identification claim before ANY use: video of minors, the SSBD ethics precedent applies)
- Access: mendeley doi:10.17632/kswgcms346.1
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- LICENCE VERIFIED 2026-09-04 via the DataCite API: CC BY 4.0,
  Mendeley Data, publication year 2025. DataCite description
  confirms: "first Chinese pediatric Tourette syndrome multimodal
  dataset... synchronized video, audio, and text... capturing
  children's tic behaviors, emotional expressions and interactive
  contexts during mindfulness-based intervention". STILL OPEN: the
  de-identification claim (content-level check, the ethics gate
  before any fetch) and whether raw video downloads or only derived
  streams.
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): video + audio + text, >120 h of sessions, expert tic-frequency and affect annotations, 60 children. IF the content check confirms movement signal + de-identification, this REVISES the A3 tics absence (currently: refutation PENDING VERIFICATION). Ethics gate BEFORE fetch
- Number of subjects: 60
- MoveAtlas cells: A3; M1 M8

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
None. Catalogue-tier until fetched and adjudicated.
