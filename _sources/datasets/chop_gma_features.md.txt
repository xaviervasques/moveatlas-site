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
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Segado, Melanie"
  }
 ]
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
| **MoveAtlas record** | [10.5281/zenodo.22313491](https://doi.org/10.5281/zenodo.22313491) |

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

- Segado, Melanie (2023). *Update: Predicting clinical assessments of infants’ risk of neuromotor disease from 2-dimensional videos*. OSF. DOI: [10.17605/osf.io/bwgek](https://doi.org/10.17605/osf.io/bwgek)
- Segado, Melanie; Prosser, Laura A; Duncan, Andrea F; Johnson, Michelle J; Kording, Konrad P (2026). *A preregistered, open pipeline for early cerebral palsy risk assessment from infant videos*. GigaScience. DOI: [10.1093/gigascience/giag003](https://doi.org/10.1093/gigascience/giag003)

```bibtex
@misc{chop_gma_features_data_2023,
  title = {Update: Predicting clinical assessments of infants’ risk of neuromotor disease from 2-dimensional videos},
  author = {Segado, Melanie},
  year = {2023},
  doi = {10.17605/osf.io/bwgek},
  howpublished = {OSF},
  note = {dataset}
}
@article{chop_gma_features_paper_2026,
  title = {A preregistered, open pipeline for early cerebral palsy risk assessment from infant videos},
  author = {Segado, Melanie and Prosser, Laura A and Duncan, Andrea F and Johnson, Michelle J and Kording, Konrad P},
  year = {2026},
  doi = {10.1093/gigascience/giag003},
  journal = {GigaScience}
}
```

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
