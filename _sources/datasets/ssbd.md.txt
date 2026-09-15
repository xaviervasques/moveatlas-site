# SSBD (Self-Stimulatory Behaviour Dataset)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "SSBD (Self-Stimulatory Behaviour Dataset)",
 "description": "SSBD (Self-Stimulatory Behaviour Dataset). MoveAtlas pose family. 75 videos subjects. licence SSBD academic.",
 "identifier": "https://rolandgoecke.net/research/datasets/ssbd/",
 "license": "SSBD academic, non-commercial, not-for-profit licence (verbatim PDF read and archived in raw/ 2026-09-01): the dataset d",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A5 Stereotypies",
  "M1 Pose / video"
 ],
 "url": "https://rolandgoecke.net/research/datasets/ssbd/",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ssbd</code>

<span class="ma-tag">Stereotypies</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A5; M1 |
| **Subjects** | 75 videos |
| **Status** | DOWNLOADED 2026-09-01 (owner GO): ssbd-release.zip (1.7 MB, 81 entries: 75 XML annotations + URL xlsx + licence + ssbd.m), sha256 journaled; licence PDF fetched and read the same day (UNDECIDED resolved: pointer tier). The YouTube videos are DELIBERATELY not fetched: identifiable children + platform... |
| **License** | SSBD academic, non-commercial, not-for-profit licence (verbatim PDF read and archived in raw/ 2026-09-01): the dataset distributes URLs + annotations + code, NOT the videos (YouTube ToS apply) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ssbd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: SSBD academic, non-commercial, not-for-profit licence (verbatim PDF read and archived in raw/ 2026-09-01): the dataset distributes URLs + annotations + code, NOT the videos (YouTube ToS apply)
- **Redistribution**: no (academic non-commercial terms; fetch from origin)
- **Access route**: direct download at rolandgoecke.net/research/datasets/ssbd
- **Source**: <https://rolandgoecke.net/research/datasets/ssbd/>

## Data card (verbatim, with its evidence trail)


- dataset: ssbd
- family: pose  (physical path: datasets/pose/ssbd)
- MoveAtlas cells: A5; M1
- population: 75 in-the-wild YouTube videos of children: arm flapping, head banging, spinning; XML temporal annotations + STIP features
- n_subjects: 75 videos
- signal: video (YouTube-sourced) + XML annotations + precomputed STIP features
- license: SSBD academic, non-commercial, not-for-profit licence (verbatim PDF read and archived in raw/ 2026-09-01): the dataset distributes URLs + annotations + code, NOT the videos (YouTube ToS apply) ; redistribution: no (academic non-commercial terms; fetch from origin)
- access: direct download at rolandgoecke.net/research/datasets/ssbd
- status (2026-08-22): DOWNLOADED 2026-09-01 (owner GO): ssbd-release.zip (1.7 MB, 81 entries: 75 XML annotations + URL xlsx + licence + ssbd.m), sha256 journaled; licence PDF fetched and read the same day (UNDECIDED resolved: pointer tier). The YouTube videos are DELIBERATELY not fetched: identifiable children + platform ToS; any video work runs from origin URLs under the privacy gate
- link: https://rolandgoecke.net/research/datasets/ssbd/
