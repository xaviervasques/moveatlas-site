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
| **Status** | harmonized (2026-09-01) |
| **License** | CC BY 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("infant_pose_chambers")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: figshare + GitHub direct download
- **Source**: <https://doi.org/10.6084/m9.figshare.8161430>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: infant_pose_chambers
- **family**: pose
- **MoveAtlas cells**: C2; M1
- **population**: pose estimates for the 94-infant evaluation set + domain-adapted infant OpenPose model + normative YouTube metadata (85 infants)
- **n_subjects**: 94 + 85 meta
- **signal**: 2D pose estimate tables + model + video metadata CSV
- **license**: CC BY 4.0; redistribution: yes
- **access**: figshare + GitHub direct download
- **link**: https://doi.org/10.6084/m9.figshare.8161430
