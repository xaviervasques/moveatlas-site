# HUBU-FIS finger tapping (video + UPDRS ratings)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "HUBU-FIS finger tapping (video + UPDRS ratings)",
 "description": "HUBU-FIS finger tapping (video + UPDRS ratings). MoveAtlas pose family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/17738775",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "M1 Pose / video"
 ],
 "url": "https://zenodo.org/records/17738775",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Amo-Salas, Javier"
  },
  {
   "@type": "Person",
   "name": "García-Bustillo, Álvaro"
  },
  {
   "@type": "Person",
   "name": "Cubo, Esther"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>hubu_fis_fingertap</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M1 (video) |
| **Subjects** | not stated (234 videos) |
| **Status** | acquired (2026-08-22) |
| **License** | CC BY 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("hubu_fis_fingertap")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: direct_download (Zenodo)
- **Source**: <https://zenodo.org/records/17738775>

## Publications

- Amo-Salas, Javier; García-Bustillo, Álvaro; Cubo, Esther (2025). *HUBU-FIS Finger Tapping dataset*. Zenodo. DOI: [10.5281/zenodo.17738775](https://doi.org/10.5281/zenodo.17738775)

```bibtex
@misc{hubu_fis_fingertap_data_2025,
  title = {HUBU-FIS Finger Tapping dataset},
  author = {Amo-Salas, Javier and García-Bustillo, Álvaro and Cubo, Esther},
  year = {2025},
  doi = {10.5281/zenodo.17738775},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: hubu_fis_fingertap
- **family**: pose
- **MoveAtlas cells**: B2; M1 (video)
- **population**: PD patients + controls, both hands, standardized MDS-UPDRS finger-tapping; per-clip ratings in fis_diagnostic.csv
- **n_subjects**: not stated (234 videos)
- **signal**: 234 videos, 10.8 GB single zip
- **license**: CC BY 4.0; redistribution: yes
- **access**: direct_download (Zenodo)
- **link**: https://zenodo.org/records/17738775
