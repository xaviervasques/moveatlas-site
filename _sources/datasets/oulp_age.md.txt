# OU-ISIR OULP-Age (silhouette gait, ages 2-90)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "OU-ISIR OULP-Age (silhouette gait, ages 2-90)",
 "description": "OU-ISIR OULP-Age (silhouette gait, ages 2-90). MoveAtlas pose family. 63,846 subjects. licence Osaka University signed release agreement.",
 "identifier": "http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLPAge.html",
 "license": "Osaka University signed release agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "C1 Normal adult movement",
  "C2 Infant development",
  "C3 Aging",
  "M4 Silhouette"
 ],
 "url": "http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLPAge.html",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>oulp_age</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Infant development</span><span class="ma-tag">Aging</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C2, C3 (age axis at scale); M4 |
| **Subjects** | 63,846 |
| **Ages** | 2-90 y |
| **Status** | DOCUMENTED BARRIER (owner, 2026-08-28): the postal-mail institutional form is declined as not worth the slow lane; written off |
| **License** | Osaka University signed release agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("oulp_age")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: Osaka University signed release agreement
- **Redistribution**: no
- **Access route**: application (signed institutional form)
- **Source**: <http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLPAge.html>

## Publications

- Xu, Chi; Makihara, Yasushi; Ogi, Gakuto; Li, Xiang; Yagi, Yasushi; Lu, Jianfeng (2017). *The OU-ISIR Gait Database comprising the Large Population Dataset with Age and performance evaluation of age estimation*. IPSJ Transactions on Computer Vision and Applications. DOI: [10.1186/s41074-017-0035-2](https://doi.org/10.1186/s41074-017-0035-2)

```bibtex
@article{oulp_age_paper_2017,
  title = {The OU-ISIR Gait Database comprising the Large Population Dataset with Age and performance evaluation of age estimation},
  author = {Xu, Chi and Makihara, Yasushi and Ogi, Gakuto and Li, Xiang and Yagi, Yasushi and Lu, Jianfeng},
  year = {2017},
  doi = {10.1186/s41074-017-0035-2},
  journal = {IPSJ Transactions on Computer Vision and Applications}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: oulp_age
- family: pose  (physical path: datasets/pose/oulp_age)
- MoveAtlas cells: C1, C2, C3 (age axis at scale); M4
- population: 63,846 subjects, 2-90 y, size-normalized gait energy images
- n_subjects: 63,846
- age: 2-90 y
- signal: GEIs 88x128 from 30 fps gait video
- license: Osaka University signed release agreement ; redistribution: no
- access: application (signed institutional form)
- status (2026-08-22): DOCUMENTED BARRIER (owner, 2026-08-28): the postal-mail institutional form is declined as not worth the slow lane; written off
- link: http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLPAge.html
- notes: largest age-conditioned silhouette resource in existence; feeds the silhouette contract's age-normativity at population scale
