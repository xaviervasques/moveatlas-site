# CODY-2 (in-house pediatric inference split)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CODY-2 (in-house pediatric inference split)",
 "description": "CODY-2 (in-house pediatric inference split). MoveAtlas pose family. 12 subjects. licence derived data CC BY 4.0.",
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

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cody_2</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1-A8 pediatric; M1 |
| **Subjects** | 12 |
| **Status** | catalogued (2026-09-01) |
| **License** | derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house). |
| **MoveAtlas record** | [10.5281/zenodo.22313507](https://doi.org/10.5281/zenodo.22313507) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cody_2")
records, meta = ds.get_data()
```

## License and access

- **License**: derived data CC BY 4.0 (CODY Zenodo deposit, 2026-09-01); raw source private (in-house).
- **Redistribution**: yes
- **Access route**: PUBLIC (derived) since 2026-09-01: the pediatric SAM3 timeseries and results ship inside the CODY Zenodo deposit (10.5281/zenodo.22232609, CC BY 4.0) in the datasets_1_2_3 files; raw video stays in-house
- **Source**: <https://doi.org/10.5281/zenodo.22232609>

## Publications

- Cif, Laura; Demailly, Diane; Souei, Zohra; Rehman, Muhammad Mushhood Ur; Escobar, Juan Dario Ortigoza; Jiménez, Mayté Castro; Hubsch, Cécile A.; Huby, Sophie; Dornadic, Morgan; Hariz, Gun-Marie; Moraud, Eduardo M.; Bloch, Jocelyne; Horvath, Gabriella A.; Vasques, Xavier (2026). *Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model*. arXiv. DOI: [10.48550/arxiv.2606.07674](https://doi.org/10.48550/arxiv.2606.07674)

```bibtex
@article{cody_2_paper_2026,
  title = {Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model},
  author = {Cif, Laura and Demailly, Diane and Souei, Zohra and Rehman, Muhammad Mushhood Ur and Escobar, Juan Dario Ortigoza and Jiménez, Mayté Castro and Hubsch, Cécile A. and Huby, Sophie and Dornadic, Morgan and Hariz, Gun-Marie and Moraud, Eduardo M. and Bloch, Jocelyne and Horvath, Gabriella A. and Vasques, Xavier},
  year = {2026},
  doi = {10.48550/arxiv.2606.07674},
  journal = {arXiv}
}
```
