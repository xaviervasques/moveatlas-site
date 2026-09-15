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

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>chu_pd_moseq</code>

| | |
|---|---|
| **Taxonomy cells** | animal: PD models -> bradykinesia/hypokinesia analogs; depth/RGB video-derived kinematic syllables |
| **Subjects** | cohort per model (see paper) |
| **Status** | DOWNLOADED 2026-09-01 (animal hunt): 3/3 files (Raw datasets.zip 6.98 GB + figure source data + ASAP readme), cc-by-4.0 confirmed via the API at fetch, sha256 journaled |
| **License** | CC BY 4.0 (Zenodo API, verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("chu_pd_moseq")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (Zenodo API, verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: Zenodo direct download (record 14555868)
- **Source**: <https://zenodo.org/records/14555868>

## Data card (verbatim, with its evidence trail)


- dataset: chu_pd_moseq
- family: animal  (physical path: datasets/animal/chu_pd_moseq)
- MoveAtlas cells: animal: PD models -> bradykinesia/hypokinesia analogs; depth/RGB video-derived kinematic syllables
- population: mouse: unilateral 6-OHDA MFB lesion + MitoPark progressive genetic PD model, open field
- n_subjects: cohort per model (see paper)
- signal: Keypoint-MoSeq behavioral modules + raw depth/RGB recordings (Kinect 2.0 / FLIR), ~10.2 GB raw
- license: CC BY 4.0 (Zenodo API, verified 2026-09-01) ; redistribution: yes
- access: Zenodo direct download (record 14555868)
- status (2026-08-22): DOWNLOADED 2026-09-01 (animal hunt): 3/3 files (Raw datasets.zip 6.98 GB + figure source data + ASAP readme), cc-by-4.0 confirmed via the API at fetch, sha256 journaled
- link: https://zenodo.org/records/14555868
