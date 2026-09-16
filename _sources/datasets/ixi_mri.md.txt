# IXI (healthy adult/aging brain MRI)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "IXI (healthy adult/aging brain MRI)",
 "description": "IXI (healthy adult/aging brain MRI). MoveAtlas bio family. licence CC BY-SA 3.0.",
 "identifier": "https://brain-development.org/ixi-dataset/",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "C1 Normal adult movement",
  "C3 Aging",
  "M8 Imaging"
 ],
 "url": "https://brain-development.org/ixi-dataset/",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ixi_mri</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3; M8 |
| **Subjects** | ~600 |
| **Ages** | 20-86 y |
| **Status** | catalogued (2026-08-28) |
| **License** | CC BY-SA 3.0 (stated) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ixi_mri")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-SA 3.0 (stated)
- **Redistribution**: yes (share-alike)
- **Access route**: direct_download
- **Source**: <https://brain-development.org/ixi-dataset/>

## Publications

-  (). **. .

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: ixi_mri
- **family**: bio
- **MoveAtlas cells**: C1, C3; M8
- **population**: ~600 healthy subjects, 3 London sites, T1/T2/PD + MRA + DTI + demographics
- **n_subjects**: ~600
- **age**: 20-86 y
- **signal**: NIfTI tarballs (~10-15 GB total)
- **license**: CC BY-SA 3.0 (stated); redistribution: yes (share-alike)
- **access**: direct_download
- **link**: https://brain-development.org/ixi-dataset/
