# MINI-RGBD (synthetic infants, TUM SMIL)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MINI-RGBD (synthetic infants, TUM SMIL)",
 "description": "MINI-RGBD (synthetic infants, TUM SMIL). MoveAtlas pose family. 12 sequences subjects. licence research use.",
 "identifier": "https://www.iosb.fraunhofer.de/en/competences/image-exploitation/object-recognition/sensor-networks/motion-analysis.html",
 "license": "research use",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C2 Infant development",
  "M1 Pose / video"
 ],
 "url": "https://www.iosb.fraunhofer.de/en/competences/image-exploitation/object-recognition/sensor-networks/motion-analysis.html",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mini_rgbd</code>

<span class="ma-tag">Infant development</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C2; M1 |
| **Subjects** | 12 sequences |
| **Ages** | synthetic infants |
| **Status** | acquired (2026-08-25) |
| **License** | research use |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mini_rgbd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: research use
- **Redistribution**: no
- **Access route**: direct download
- **Source**: <https://www.iosb.fraunhofer.de/en/competences/image-exploitation/object-recognition/sensor-networks/motion-analysis.html>

## Publications

- Hesse, Nikolas; Bodensteiner, Christoph; Arens, Michael; Hofmann, Ulrich G.; Weinberger, Raphael; Sebastian Schroeder, A. (2019). *Computer Vision for Medical Infant Motion Analysis: State of the Art and RGB-D Data Set*. Lecture Notes in Computer Science. DOI: [10.1007/978-3-030-11024-6_3](https://doi.org/10.1007/978-3-030-11024-6_3)

```bibtex
@article{mini_rgbd_paper_2019,
  title = {Computer Vision for Medical Infant Motion Analysis: State of the Art and RGB-D Data Set},
  author = {Hesse, Nikolas and Bodensteiner, Christoph and Arens, Michael and Hofmann, Ulrich G. and Weinberger, Raphael and Sebastian Schroeder, A.},
  year = {2019},
  doi = {10.1007/978-3-030-11024-6_3},
  journal = {Lecture Notes in Computer Science}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: mini_rgbd
- **family**: pose
- **MoveAtlas cells**: C2; M1
- **population**: 12 synthetic RGB-D sequences from the SMIL infant model, with ground-truth joints
- **n_subjects**: 12 sequences
- **age**: synthetic infants
- **signal**: RGB-D + joint ground truth
- **license**: research use; redistribution: no
- **access**: direct download
- **link**: https://www.iosb.fraunhofer.de/en/competences/image-exploitation/object-recognition/sensor-networks/motion-analysis.html
