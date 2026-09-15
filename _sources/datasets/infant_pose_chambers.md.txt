# Chambers infant pose estimates + normative video metadata

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Chambers infant pose estimates + normative video metadata",
 "description": "Chambers infant pose estimates + normative video metadata. MoveAtlas pose family. 94 + 85 meta subjects. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.8161430",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C2 Infant development",
  "M1 Pose / video"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.8161430",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>infant_pose_chambers</code>

<span class="ma-tag">Infant development</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C2; M1 |
| **Subjects** | 94 + 85 meta |
| **Status** | DOWNLOADED AND INGESTED 2026-09-01 (owner GO): all 12 files md5 MATCHED, then 116 canonical pose records / 104 infants (85 YouTube normative with age_in_weeks + 31 clinical trials from 19 CHOP infants with sex, ages and BINS risk as eval-only attributes). New chambers_coco18 joint map added to confi... |
| **License** | CC BY 4.0 (confirmed via the figshare API at fetch 2026-09-01; UNDECIDED resolved) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("infant_pose_chambers")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (confirmed via the figshare API at fetch 2026-09-01; UNDECIDED resolved)
- **Redistribution**: yes
- **Access route**: figshare + GitHub direct download
- **Source**: <https://doi.org/10.6084/m9.figshare.8161430>

## Data card (verbatim, with its evidence trail)


- dataset: infant_pose_chambers
- family: pose  (physical path: datasets/pose/infant_pose_chambers)
- MoveAtlas cells: C2; M1
- population: pose estimates for the 94-infant evaluation set + domain-adapted infant OpenPose model + normative YouTube metadata (85 infants)
- n_subjects: 94 + 85 meta
- signal: 2D pose estimate tables + model + video metadata CSV
- license: CC BY 4.0 (confirmed via the figshare API at fetch 2026-09-01; UNDECIDED resolved) ; redistribution: yes
- access: figshare + GitHub direct download
- status (2026-08-22): DOWNLOADED AND INGESTED 2026-09-01 (owner GO): all 12 files md5 MATCHED, then 116 canonical pose records / 104 infants (85 YouTube normative with age_in_weeks + 31 clinical trials from 19 CHOP infants with sex, ages and BINS risk as eval-only attributes). New chambers_coco18 joint map added to configs/canonical_skeleton.yaml (pelvis=midpoint hips, neck direct, head=proxy nose, eyes/ears dropped); missing detections -> valid_mask False. The first REAL (non-synthetic) open infant pose in the corpus
- link: https://doi.org/10.6084/m9.figshare.8161430
