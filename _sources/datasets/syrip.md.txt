# SyRIP (synthetic + real infant pose)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "SyRIP (synthetic + real infant pose)",
 "description": "SyRIP (synthetic + real infant pose). MoveAtlas pose family. licence non-commercial; dataset password by email.",
 "identifier": "https://github.com/ostadabbas/Infant-Pose-Estimation",
 "license": "non-commercial; dataset password by email",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C2 Infant development",
  "M1 Pose / video"
 ],
 "url": "https://github.com/ostadabbas/Infant-Pose-Estimation",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>syrip</code>

<span class="ma-tag">Infant development</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C2; M1 |
| **Subjects** | not stated |
| **Ages** | infants |
| **Status** | DOCUMENTED BARRIER (owner, 2026-08-28): the password-by-email gate stays closed under the standing no-emails decision; not reopened |
| **License** | non-commercial; dataset password by email |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("syrip")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: non-commercial; dataset password by email
- **Redistribution**: no
- **Access route**: registration-like (password request)
- **Source**: <https://github.com/ostadabbas/Infant-Pose-Estimation>

## Publications

- Huang, Xiaofei; Fu, Nihang; Liu, Shuangjun; Ostadabbas, Sarah (2020). *Invariant Representation Learning for Infant Pose Estimation with Small Data*. arXiv. DOI: [10.48550/arxiv.2010.06100](https://doi.org/10.48550/arxiv.2010.06100)

```bibtex
@article{syrip_paper_2020,
  title = {Invariant Representation Learning for Infant Pose Estimation with Small Data},
  author = {Huang, Xiaofei and Fu, Nihang and Liu, Shuangjun and Ostadabbas, Sarah},
  year = {2020},
  doi = {10.48550/arxiv.2010.06100},
  journal = {arXiv}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: syrip
- family: pose  (physical path: datasets/pose/syrip)
- MoveAtlas cells: C2; M1
- population: real + synthetic infant images, COCO-format 2D keypoints
- n_subjects: not stated
- age: infants
- signal: annotated infant images (2D keypoints)
- license: non-commercial; dataset password by email ; redistribution: no
- access: registration-like (password request)
- status (2026-08-22): DOCUMENTED BARRIER (owner, 2026-08-28): the password-by-email gate stays closed under the standing no-emails decision; not reopened
- link: https://github.com/ostadabbas/Infant-Pose-Estimation
- notes: infant 2D pose pretraining aid for the infant-skeleton contract
