# TIM-TREMOR (multi-etiology tremor video+depth)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "TIM-TREMOR (multi-etiology tremor video+depth)",
 "description": "TIM-TREMOR (multi-etiology tremor video+depth). MoveAtlas pose family. 55 subjects. licence 4TU.",
 "identifier": "https://data.4tu.nl/articles/dataset/TIM-Tremor_An_open-source_dataset_of_structured_tremor_time_series_data/12692869",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A1 Tremor",
  "M1 Pose / video"
 ],
 "url": "https://data.4tu.nl/articles/dataset/TIM-Tremor_An_open-source_dataset_of_structured_tremor_time_series_data/12692869",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>tim_tremor</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1 (multi-etiology incl. functional and enhanced physiological); M1 |
| **Subjects** | 55 |
| **Status** | WRITTEN OFF 2026-08-28: the owner authorized acquisition, but the DOI (10.4121/uuid:522d14ed-3019-4206-b49e-a4e674b6440a) now resolves to a 4TU tombstone reading 'CONTENT WAS REMOVED / The content of this page has been retracted' (verified in a real browser, robots-block ruled out). Nothing left to... |
| **License** | 4TU (default CC BY, unverifiable: the host robots-blocks every check) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("tim_tremor")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: 4TU (default CC BY, unverifiable: the host robots-blocks every check)
- **Redistribution**: no, DECIDED 2026-08-28: unverifiable licence = pointer to data.4tu.nl
- **Access route**: none: REMOVED AT SOURCE
- **Source**: <https://data.4tu.nl/articles/dataset/TIM-Tremor_An_open-source_dataset_of_structured_tremor_time_series_data/12692869>

## Publications

-  (). **. .

## Data card (verbatim, with its evidence trail)


- dataset: tim_tremor
- family: pose  (physical path: datasets/pose/tim_tremor)
- MoveAtlas cells: A1 (multi-etiology incl. functional and enhanced physiological); M1
- population: 55 tremor patients, 910 videos, 21 tasks, clips 18-112 s
- n_subjects: 55
- signal: RGB video + aligned Kinect depth + ground-truth accelerometer on the most affected hand
- license: 4TU (default CC BY, unverifiable: the host robots-blocks every check) ; redistribution: no, DECIDED 2026-08-28: unverifiable licence = pointer to data.4tu.nl
- access: none: REMOVED AT SOURCE
- status (2026-08-22): WRITTEN OFF 2026-08-28: the owner authorized acquisition, but the DOI (10.4121/uuid:522d14ed-3019-4206-b49e-a4e674b6440a) now resolves to a 4TU tombstone reading 'CONTENT WAS REMOVED / The content of this page has been retracted' (verified in a real browser, robots-block ruled out). Nothing left to download; mirroring a retracted deposit would be unauthorized redistribution. The v1 retirement (identifiable video) stands moot
- link: https://data.4tu.nl/articles/dataset/TIM-Tremor_An_open-source_dataset_of_structured_tremor_time_series_data/12692869
- notes: etiology labels per recording to verify on download
