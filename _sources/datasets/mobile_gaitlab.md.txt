# mobile-gaitlab: video-derived gait keypoints of 1026 CP patients (Stanford/Gillette)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "mobile-gaitlab: video-derived gait keypoints of 1026 CP patients (Stanford/Gillette)",
 "description": "mobile-gaitlab: video-derived gait keypoints of 1026 CP patients (Stanford/Gillette). MoveAtlas pose family. 1026 subjects. licence free on GitHub.",
 "identifier": "https://github.com/stanfordnmbl/mobile-gaitlab",
 "license": "free on GitHub (stanfordnmbl); processed OpenPose keypoints + gait labels, raw video NOT included - read the repo licenc",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://github.com/stanfordnmbl/mobile-gaitlab",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mobile_gaitlab</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | D CP; C1; M1 |
| **Subjects** | 1026 |
| **Ages** | children (1994-2015 visits) |
| **Status** | DOWNLOADED 2026-09-06: shallow clone at 4167ee6, 462 files ~1.0 GB (keypoint trajectories + labels + code), repo licence Apache 2.0 (covers the repo contents; goodwin-style adjudication note: the DATA licence is the repo licence unless the paper says otherwise). CATALOGUED 2026-09-05 (deep-dive): Op... |
| **License** | free on GitHub (stanfordnmbl); processed OpenPose keypoints + gait labels, raw video NOT included - read the repo licence at fetch |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mobile_gaitlab")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: free on GitHub (stanfordnmbl); processed OpenPose keypoints + gait labels, raw video NOT included - read the repo licence at fetch
- **Redistribution**: unknown
- **Access route**: github stanfordnmbl/mobile-gaitlab
- **Source**: <https://github.com/stanfordnmbl/mobile-gaitlab>

## Data card (verbatim, with its evidence trail)


- Modality: family 'pose'
- Source / URL: https://github.com/stanfordnmbl/mobile-gaitlab
- License / access: free on GitHub (stanfordnmbl); processed OpenPose keypoints + gait labels, raw video NOT included - read the repo licence at fetch
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  pediatric/genetic-rare pass); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): OpenPose keypoint trajectories from 1792 clinical gait videos + ground-truth labels (GDI, speed, cadence, knee flexion) - the LARGEST CP video-derived signal release in existence (predominantly spastic; dyskinetic fraction not delineated). FETCH CANDIDATE
- MoveAtlas cells: D CP; C1; M1

### Retrieval notes
RE-VERIFY at fetch. No-emails policy for application tiers.

### Processing
None. Catalogue-tier.
