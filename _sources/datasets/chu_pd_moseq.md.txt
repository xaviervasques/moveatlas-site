# 6-OHDA and MitoPark mouse open-field locomotion (Keypoint-MoSeq)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "6-OHDA and MitoPark mouse open-field locomotion (Keypoint-MoSeq)",
 "description": "6-OHDA and MitoPark mouse open-field locomotion (Keypoint-MoSeq). MoveAtlas animal family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/14555868",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://zenodo.org/records/14555868",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>chu_pd_moseq</code>

| | |
|---|---|
| **Taxonomy cells** | animal: PD models -> bradykinesia/hypokinesia analogs; depth/RGB video-derived kinematic syllables |
| **Subjects** | cohort per model (see paper) |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (Zenodo API, verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("chu_pd_moseq")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo API, verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: Zenodo direct download (record 14555868)
- **Source**: <https://zenodo.org/records/14555868>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: chu_pd_moseq
- **family**: animal
- **MoveAtlas cells**: animal: PD models -> bradykinesia/hypokinesia analogs; depth/RGB video-derived kinematic syllables
- **population**: mouse: unilateral 6-OHDA MFB lesion + MitoPark progressive genetic PD model, open field
- **n_subjects**: cohort per model (see paper)
- **signal**: Keypoint-MoSeq behavioral modules + raw depth/RGB recordings (Kinect 2.0 / FLIR), ~10.2 GB raw
- **license**: CC BY 4.0 (Zenodo API, verified 2026-09-01); redistribution: yes
- **access**: Zenodo direct download (record 14555868)
- **link**: https://zenodo.org/records/14555868
