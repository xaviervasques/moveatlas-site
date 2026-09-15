# Automated video-based tic detection (OSF 46vxm)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Automated video-based tic detection (OSF 46vxm)",
 "description": "Automated video-based tic detection (OSF 46vxm). MoveAtlas pose family. licence open OSF project.",
 "identifier": "https://osf.io/46vxm/",
 "license": "open OSF project (licence + de-identification level UNVERIFIED)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A3 Tics",
  "M1 Pose / video"
 ],
 "url": "https://osf.io/46vxm/",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>osf_tic_video_46vxm</code>

<span class="ma-tag">Tics</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A3; M1 |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): data folders (02-cleaned, 11-sample) + R analysis, likely video-derived features/landmarks for Tourette tic detection. Second A3 candidate; same verification gate as mindts_tourette |
| **License** | open OSF project (licence + de-identification level UNVERIFIED) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("osf_tic_video_46vxm")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open OSF project (licence + de-identification level UNVERIFIED)
- **Redistribution**: unknown
- **Access route**: osf.io/46vxm
- **Source**: <https://osf.io/46vxm/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'pose'
- Source / URL: https://osf.io/46vxm/
- License: open OSF project (licence + de-identification level UNVERIFIED)
- Access: osf.io/46vxm
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): data folders (02-cleaned, 11-sample) + R analysis, likely video-derived features/landmarks for Tourette tic detection. Second A3 candidate; same verification gate as mindts_tourette
- Number of subjects: see record
- MoveAtlas cells: A3; M1

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
None. Catalogue-tier until fetched and adjudicated.
