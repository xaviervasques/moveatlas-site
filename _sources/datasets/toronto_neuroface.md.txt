# Toronto NeuroFace (orofacial)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Toronto NeuroFace (orofacial)",
 "description": "Toronto NeuroFace (orofacial). MoveAtlas pose family. 36 subjects. licence application form.",
 "identifier": "https://slp.utoronto.ca/faculty/yana-yunusova/speech-production-lab/datasets/",
 "license": "application form",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "D3 Pyramidal syndromes",
  "M1 Pose / video"
 ],
 "url": "https://slp.utoronto.ca/faculty/yana-yunusova/speech-production-lab/datasets/",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>toronto_neuroface</code>

<span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | D3 (ALS, stroke); M1 |
| **Subjects** | 36 |
| **Status** | documented access barrier (2026-08-28) |
| **License** | application form |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("toronto_neuroface")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: application form
- **Redistribution**: no
- **Access route**: application (request form)
- **Source**: <https://slp.utoronto.ca/faculty/yana-yunusova/speech-production-lab/datasets/>

## Publications

- Bandini, Andrea; Rezaei, Sia; Guarin, Diego L.; Kulkarni, Madhura; Lim, Derrick; Boulos, Mark I.; Zinman, Lorne; Yunusova, Yana; Taati, Babak (2021). *A New Dataset for Facial Motion Analysis in Individuals With Neurological Disorders*. IEEE Journal of Biomedical and Health Informatics. DOI: [10.1109/jbhi.2020.3019242](https://doi.org/10.1109/jbhi.2020.3019242)

```bibtex
@article{toronto_neuroface_paper_2021,
  title = {A New Dataset for Facial Motion Analysis in Individuals With Neurological Disorders},
  author = {Bandini, Andrea and Rezaei, Sia and Guarin, Diego L. and Kulkarni, Madhura and Lim, Derrick and Boulos, Mark I. and Zinman, Lorne and Yunusova, Yana and Taati, Babak},
  year = {2021},
  doi = {10.1109/jbhi.2020.3019242},
  journal = {IEEE Journal of Biomedical and Health Informatics}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: toronto_neuroface
- **family**: pose
- **MoveAtlas cells**: D3 (ALS, stroke); M1
- **population**: 36 subjects (ALS, stroke, controls), 68 facial landmarks, 30 fps
- **n_subjects**: 36
- **signal**: orofacial video landmark tracks + clinical scores
- **license**: application form; redistribution: no
- **access**: application (request form)
- **link**: https://slp.utoronto.ca/faculty/yana-yunusova/speech-production-lab/datasets/
