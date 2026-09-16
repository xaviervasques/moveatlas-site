# Motion-X++ (healthy motion base)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Motion-X++ (healthy motion base)",
 "description": "Motion-X++ (healthy motion base). MoveAtlas socle family. licence non-commercial research.",
 "identifier": "https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus",
 "license": "non-commercial research",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus",
 "isAccessibleForFree": false,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>motion_x</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1 |
| **Subjects** | clip-indexed |
| **Status** | harmonized |
| **License** | non-commercial research |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("motion_x")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: non-commercial research
- **Redistribution**: no
- **Access route**: public HuggingFace download
- **Source**: <https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus>

## Publications

- Lin, Jing; Zeng, Ailing; Lu, Shunlin; Cai, Yuanhao; Zhang, Ruimao; Wang, Haoqian; Zhang, Lei (2023). *Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset*. arXiv. DOI: [10.48550/arxiv.2307.00818](https://doi.org/10.48550/arxiv.2307.00818)

```bibtex
@article{motion_x_paper_2023,
  title = {Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset},
  author = {Lin, Jing and Zeng, Ailing and Lu, Shunlin and Cai, Yuanhao and Zhang, Ruimao and Wang, Haoqian and Zhang, Lei},
  year = {2023},
  doi = {10.48550/arxiv.2307.00818},
  journal = {arXiv}
}
```
