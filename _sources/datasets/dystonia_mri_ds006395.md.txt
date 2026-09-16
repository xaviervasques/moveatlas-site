# Upper-limb and cervical dystonia MRI (OpenNeuro ds006395)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Upper-limb and cervical dystonia MRI (OpenNeuro ds006395)",
 "description": "Upper-limb and cervical dystonia MRI (OpenNeuro ds006395). MoveAtlas bio family. 91 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds006395",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A4 Dystonia",
  "M8 Imaging"
 ],
 "url": "https://openneuro.org/datasets/ds006395",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dystonia_mri_ds006395</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M8 |
| **Subjects** | 91 |
| **Status** | acquired (2026-09-01) |
| **License** | CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dystonia_mri_ds006395")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01)
- **Redistribution**: yes
- **Access route**: OpenNeuro / S3 direct download
- **Source**: <https://openneuro.org/datasets/ds006395>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: dystonia_mri_ds006395
- **family**: bio
- **MoveAtlas cells**: A4; M8
- **population**: 37 healthy controls + 25 cervical dystonia + 29 upper-limb dystonia; T1, 60-dir DWI, rs-fMRI, finger-tapping task fMRI
- **n_subjects**: 91
- **signal**: structural + diffusion + functional MRI (BIDS)
- **license**: CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01); redistribution: yes
- **access**: OpenNeuro / S3 direct download
- **link**: https://openneuro.org/datasets/ds006395
