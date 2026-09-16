# CHOP infant GMA pipeline release (feature tables + weights)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CHOP infant GMA pipeline release (feature tables + weights)",
 "description": "CHOP infant GMA pipeline release (feature tables + weights). MoveAtlas pose family. 1,053 subjects. licence CC0 1.0.",
 "identifier": "https://osf.io/gztmd/",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C2 Infant development",
  "M1 Pose / video"
 ],
 "url": "https://osf.io/gztmd/",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>chop_gma_features</code>

<span class="ma-tag">Infant development</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C2; M1 (derived features) |
| **Subjects** | 1,053 |
| **Ages** | 10-20 weeks post-term |
| **Status** | acquired (2026-08-22) |
| **License** | CC0 1.0 (OSF node license, verified 2026-08-22) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("chop_gma_features")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 1.0 (OSF node license, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download (OSF)
- **Source**: <https://osf.io/gztmd/>

## Publications

-  (). **. .

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: chop_gma_features
- **family**: pose
- **MoveAtlas cells**: C2; M1 (derived features)
- **population**: 1,053 infants filmed for GMA / fidgety-movement outcome (~10-12% FM-negative); clinical videos NOT shared
- **n_subjects**: 1,053
- **age**: 10-20 weeks post-term
- **signal**: de-identified kinematic feature tables + model weights + ViTPose keypoints for YouTube-8M infant videos
- **license**: CC0 1.0 (OSF node license, verified 2026-08-22); redistribution: yes
- **access**: direct_download (OSF)
- **link**: https://osf.io/gztmd/
- **citation**: GigaScience 2026, giag003
