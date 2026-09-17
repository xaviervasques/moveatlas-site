# Parkinson's pose estimation dataset (Li/Taati)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Parkinson's pose estimation dataset (Li/Taati)",
 "description": "Parkinson's pose estimation dataset (Li/Taati). MoveAtlas pose family. licence CC BY 4.0.",
 "identifier": "https://github.com/limi44/Parkinson-s-Pose-Estimation-Dataset",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "A7 Chorea",
  "A4 Dystonia",
  "E6 Iatrogenic",
  "M1 Pose / video"
 ],
 "url": "https://github.com/limi44/Parkinson-s-Pose-Estimation-Dataset",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>li_taati</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Chorea</span><span class="ma-tag">Dystonia</span><span class="ma-tag">Iatrogenic</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | B2 + L-DOPA dyskinesia (A7/A4 + E6); M1 |
| **Subjects** | ~135 |
| **Status** | harmonized |
| **License** | CC BY 4.0 |
| **MoveAtlas record** | [10.5281/zenodo.22313475](https://doi.org/10.5281/zenodo.22313475) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("li_taati")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: free download (GitHub)
- **Source**: <https://github.com/limi44/Parkinson-s-Pose-Estimation-Dataset>

## Publications

- Li, Michael H.; Mestre, Tiago A.; Fox, Susan H.; Taati, Babak (2018). *Vision-based assessment of parkinsonism and levodopa-induced dyskinesia with pose estimation*. Journal of NeuroEngineering and Rehabilitation. DOI: [10.1186/s12984-018-0446-z](https://doi.org/10.1186/s12984-018-0446-z)

```bibtex
@article{li_taati_paper_2018,
  title = {Vision-based assessment of parkinsonism and levodopa-induced dyskinesia with pose estimation},
  author = {Li, Michael H. and Mestre, Tiago A. and Fox, Susan H. and Taati, Babak},
  year = {2018},
  doi = {10.1186/s12984-018-0446-z},
  journal = {Journal of NeuroEngineering and Rehabilitation}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: li_taati
- **family**: pose
- **MoveAtlas cells**: B2 + L-DOPA dyskinesia (A7/A4 + E6); M1
- **population**: ~135 PD patients; UDysRS, UPDRS, CAPSIT scores
- **n_subjects**: ~135
- **signal**: 2D joint trajectories (communication, drinking, leg agility) + optical flow (toe tapping); normalized 0-1 coordinates, no raw video
- **license**: CC BY 4.0; redistribution: yes
- **access**: free download (GitHub)
- **link**: https://github.com/limi44/Parkinson-s-Pose-Estimation-Dataset
- **ingestion**: build_canonical.py (li_taati mapping) + ingest_li_taati.py (leg_agility state suffixes)
