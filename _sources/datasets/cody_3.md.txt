# CODY-3 (in-house canonical superset + SAM3)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-3 (in-house canonical superset + SAM3)",
 "description": "CODY-3 (in-house canonical superset + SAM3). MoveAtlas pose family. 59 subjects. licence derived data CC BY 4.0.",
 "identifier": "https://doi.org/10.5281/zenodo.22232609",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A1 Tremor",
  "A8 Ballismus",
  "M1 Pose / video",
  "M4 Silhouette"
 ],
 "url": "https://doi.org/10.5281/zenodo.22232609",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_3</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8; M1, M4 |
| **Subjects** | 59 |
| **Status** | harmonized (2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). (2) segmentation renders where the patient remains visible NEVER; (3) segmentation-only files (pure contours/masks, no identifiable imagery) publishable, as are keypoints and labels |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_3")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). (2) segmentation renders where the patient remains visible NEVER; (3) segmentation-only files (pure contours/masks, no identifiable imagery) publishable, as are keypoints and labels
- **Redistribution**: yes
- **Access route**: PUBLIC (derived) since 2026-09-01: the CODY Zenodo deposit v1.0.0 (concept DOI 10.5281/zenodo.22232609, version 10.5281/zenodo.22232610, CC BY 4.0, open access, 15.4 GB, Vasques/Cif/Demailly, verified 2026-09-02) ships dataset_0 (labels raw + merged-by-patient + merged-by-video kinematics + SAM3 timeseries: the 25 adults) and datasets_1_2_3 (SAM3 timeseries + results: the 2 adult, 12 pediatric and
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

-  (). **. .
