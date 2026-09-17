# CODY-1 (in-house adult hyperkinetic cohort)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-1 (in-house adult hyperkinetic cohort)",
 "description": "CODY-1 (in-house adult hyperkinetic cohort). MoveAtlas pose family. 25 subjects. licence derived data CC BY 4.0.",
 "identifier": "https://doi.org/10.5281/zenodo.22232609",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A1 Tremor",
  "A8 Ballismus",
  "A3 Tics",
  "A6 Athetosis",
  "M1 Pose / video"
 ],
 "url": "https://doi.org/10.5281/zenodo.22232609",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_1</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Tics</span><span class="ma-tag">Athetosis</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8 (all eight hyperkinetic cells incl. the publicly-empty A3 tics, A6 athetosis, A8 ballismus); M1 |
| **Subjects** | 25 |
| **Status** | harmonized (2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). CONTROL raw videos are publishable; PATIENT raw videos are NOT, ever |
| **MoveAtlas record** | [10.5281/zenodo.22313505](https://doi.org/10.5281/zenodo.22313505) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_1")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). CONTROL raw videos are publishable; PATIENT raw videos are NOT, ever
- **Redistribution**: yes
- **Access route**: patient raw video stays in-house
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

- Cif, Laura; Demailly, Diane; Horvàth, Gabriella A.; Ortigoza Escobar, Juan Dario; Dorison, Nathalie; Castro Jiménez, Mayté; Hubsch, Cécile A.; Wirth, Thomas; Hariz, Gun‐Marie; Huby, Sophie; Dornadic, Morgan; Souei, Zohra; Mushhood Ur Rehman, Muhammad; Hemm, Simone; Boulaymen, Mehdi; Moraud, Eduardo  (2026). *Deep Learning Pose Estimation for Phenotyping of Co‐Occurring Hyperkinetic Movement Disorders*. Annals of Clinical and Translational Neurology. DOI: [10.1002/acn3.70474](https://doi.org/10.1002/acn3.70474)

```bibtex
@article{cody_1_paper_2026,
  title = {Deep Learning Pose Estimation for Phenotyping of Co‐Occurring Hyperkinetic Movement Disorders},
  author = {Cif, Laura and Demailly, Diane and Horvàth, Gabriella A. and Ortigoza Escobar, Juan Dario and Dorison, Nathalie and Castro Jiménez, Mayté and Hubsch, Cécile A. and Wirth, Thomas and Hariz, Gun‐Marie and Huby, Sophie and Dornadic, Morgan and Souei, Zohra and Mushhood Ur Rehman, Muhammad and Hemm, Simone and Boulaymen, Mehdi and Moraud, Eduardo M. and Bloch, Jocelyne and Vasques, Xavier},
  year = {2026},
  doi = {10.1002/acn3.70474},
  journal = {Annals of Clinical and Translational Neurology}
}
```
