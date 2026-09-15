# VisionMD (TOOL, not a dataset)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "VisionMD (TOOL, not a dataset)",
 "description": "VisionMD (TOOL, not a dataset). MoveAtlas pose family. licence open-source software.",
 "identifier": "https://github.com/mea-lab/VisionMD",
 "license": "open-source software",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose"
 ],
 "url": "https://github.com/mea-lab/VisionMD",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>visionmd</code>

| | |
|---|---|
| **Taxonomy cells** | n/a |
| **Subjects** | n/a |
| **Status** | raw/ holds VisionMD-Tutorial-main: a TOOL for bradykinesia video analysis, not a data corpus; keep as tooling reference, excluded from the catalogue |
| **License** | open-source software |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("visionmd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open-source software
- **Redistribution**: no (software tool, not data; pointer to its repo)
- **Access route**: n/a
- **Source**: <https://github.com/mea-lab/VisionMD>

## Publications

- Acevedo, Gabriela; Lange, Florian; Calonge, Carolina; Peach, Robert; Wong, Joshua K.; Guarin, Diego L. (2025). *VisionMD: an open-source tool for video-based analysis of motor function in movement disorders*. npj Parkinson's Disease. DOI: [10.1038/s41531-025-00876-6](https://doi.org/10.1038/s41531-025-00876-6)

```bibtex
@article{visionmd_paper_2025,
  title = {VisionMD: an open-source tool for video-based analysis of motor function in movement disorders},
  author = {Acevedo, Gabriela and Lange, Florian and Calonge, Carolina and Peach, Robert and Wong, Joshua K. and Guarin, Diego L.},
  year = {2025},
  doi = {10.1038/s41531-025-00876-6},
  journal = {npj Parkinson's Disease}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: visionmd
- family: pose  (physical path: datasets/pose/visionMD)
- MoveAtlas cells: n/a
- population: n/a
- n_subjects: n/a
- signal: VisionMD video-based MDS-UPDRS analysis software (tutorial repo on disk)
- license: open-source software ; redistribution: no (software tool, not data; pointer to its repo)
- access: n/a
- status (2026-08-22): raw/ holds VisionMD-Tutorial-main: a TOOL for bradykinesia video analysis, not a data corpus; keep as tooling reference, excluded from the catalogue
- link: https://github.com/mea-lab/VisionMD
- citation: npj Parkinson's Disease 2025, doi 10.1038/s41531-025-00876-6
- notes: candidate pipeline for hubu_fis_fingertap processing once that video set arrives. Link resolved 2026-08-23 (raw/ holds the tutorial repo VisionMD-Tutorial; the tool itself is mea-lab/VisionMD)
