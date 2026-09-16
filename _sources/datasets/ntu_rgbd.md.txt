# NTU RGB+D 120 (3D skeletons)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NTU RGB+D 120 (3D skeletons)",
 "description": "NTU RGB+D 120 (3D skeletons). MoveAtlas socle family. 106 subjects. licence academic research only.",
 "identifier": "https://rose1.ntu.edu.sg/dataset/actionRecognition",
 "license": "academic research only",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://rose1.ntu.edu.sg/dataset/actionRecognition",
 "isAccessibleForFree": false,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ntu_rgbd</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1 |
| **Subjects** | 106 |
| **Status** | harmonized |
| **License** | academic research only |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ntu_rgbd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: academic research only
- **Redistribution**: no
- **Access route**: ROSE portal (approved 2026-07-12)
- **Source**: <https://rose1.ntu.edu.sg/dataset/actionRecognition>

## Publications

- Liu, Jun; Shahroudy, Amir; Perez, Mauricio; Wang, Gang; Duan, Ling-Yu; Kot, Alex C. (2020). *NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding*. IEEE Transactions on Pattern Analysis and Machine Intelligence. DOI: [10.1109/tpami.2019.2916873](https://doi.org/10.1109/tpami.2019.2916873)

```bibtex
@article{ntu_rgbd_paper_2020,
  title = {NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding},
  author = {Liu, Jun and Shahroudy, Amir and Perez, Mauricio and Wang, Gang and Duan, Ling-Yu and Kot, Alex C.},
  year = {2020},
  doi = {10.1109/tpami.2019.2916873},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **known issues**: a screen on 2026-09-16 found 17,073 of 113,945 skeleton records outside the thigh-to-torso length band used for the other pose sources; the Kinect joint definitions differ from those sources
