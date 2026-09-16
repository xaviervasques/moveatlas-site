# NIATS spiral + wave drawings

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NIATS spiral + wave drawings",
 "description": "NIATS spiral + wave drawings. MoveAtlas auxdata family. 408 images (not per-subject) subjects. licence Kaggle/UCI mirror terms.",
 "identifier": "https://www.kaggle.com/datasets/kmader/parkinsons-drawings",
 "license": "Kaggle/UCI mirror terms (verify before redistribution)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A1 Tremor",
  "B2 Bradykinesia",
  "M11 Voice / writing"
 ],
 "url": "https://www.kaggle.com/datasets/kmader/parkinsons-drawings",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>kaggle_spiral</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | A1 proxy, B2 proxy; M11 |
| **Subjects** | 408 images (not per-subject) |
| **Status** | acquired |
| **License** | Kaggle/UCI mirror terms (verify before redistribution) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("kaggle_spiral")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: Kaggle/UCI mirror terms (verify before redistribution)
- **Redistribution**: no (fetch from Kaggle)
- **Access route**: downloaded
- **Source**: <https://www.kaggle.com/datasets/kmader/parkinsons-drawings>

## Publications

- Zham, Poonam; Kumar, Dinesh K.; Dabnichki, Peter; Poosapadi Arjunan, Sridhar; Raghav, Sanjay (2017). *Distinguishing Different Stages of Parkinson’s Disease Using Composite Index of Speed and Pen-Pressure of Sketching a Spiral*. Frontiers in Neurology. DOI: [10.3389/fneur.2017.00435](https://doi.org/10.3389/fneur.2017.00435)

```bibtex
@article{kaggle_spiral_paper_2017,
  title = {Distinguishing Different Stages of Parkinson’s Disease Using Composite Index of Speed and Pen-Pressure of Sketching a Spiral},
  author = {Zham, Poonam and Kumar, Dinesh K. and Dabnichki, Peter and Poosapadi Arjunan, Sridhar and Raghav, Sanjay},
  year = {2017},
  doi = {10.3389/fneur.2017.00435},
  journal = {Frontiers in Neurology}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: kaggle_spiral
- **family**: auxdata
- **MoveAtlas cells**: A1 proxy, B2 proxy; M11
- **population**: PD patients + healthy, drawing tests
- **n_subjects**: 408 images (not per-subject)
- **signal**: spiral/wave drawing images
- **license**: Kaggle/UCI mirror terms (verify before redistribution); redistribution: no, no written licence found (the Kaggle page is JS-only, the mirror chain unclear); pointer to Kaggle
- **access**: downloaded
- **link**: https://www.kaggle.com/datasets/kmader/parkinsons-drawings
- **citation**: source study: Zham et al., Front. Neurol. 2017, doi 10.3389/fneur.2017.00435
