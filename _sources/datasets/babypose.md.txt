# babyPose (preterm infants, NICU depth video)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "babyPose (preterm infants, NICU depth video)",
 "description": "babyPose (preterm infants, NICU depth video). MoveAtlas pose family. 16 subjects. licence on request from the VRAI lab.",
 "identifier": "https://vrai.dii.univpm.it/content/babypose-dataset",
 "license": "on request from the VRAI lab",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C2 Infant development",
  "M1 Pose / video"
 ],
 "url": "https://vrai.dii.univpm.it/content/babypose-dataset",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>babypose</code>

<span class="ma-tag">Infant development</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C2; M1 |
| **Subjects** | 16 |
| **Ages** | preterm neonates |
| **Status** | documented access barrier (2026-08-28) |
| **License** | on request from the VRAI lab |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("babypose")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: on request from the VRAI lab
- **Redistribution**: no
- **Access route**: application: email the lab
- **Source**: <https://vrai.dii.univpm.it/content/babypose-dataset>

## Publications

- Migliorelli, Lucia; Moccia, Sara; Pietrini, Rocco; Carnielli, Virgilio Paolo; Frontoni, Emanuele (2020). *The babyPose dataset*. Data in Brief. DOI: [10.1016/j.dib.2020.106329](https://doi.org/10.1016/j.dib.2020.106329)

```bibtex
@article{babypose_paper_2020,
  title = {The babyPose dataset},
  author = {Migliorelli, Lucia and Moccia, Sara and Pietrini, Rocco and Carnielli, Virgilio Paolo and Frontoni, Emanuele},
  year = {2020},
  doi = {10.1016/j.dib.2020.106329},
  journal = {Data in Brief}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: babypose
- **family**: pose
- **MoveAtlas cells**: C2; M1
- **population**: 16 preterm infants in incubator, limb-joint annotated depth video
- **n_subjects**: 16
- **age**: preterm neonates
- **signal**: depth video, 16,000 annotated frames
- **license**: on request from the VRAI lab; redistribution: no (until granted)
- **access**: application: email the lab
- **link**: https://vrai.dii.univpm.it/content/babypose-dataset
