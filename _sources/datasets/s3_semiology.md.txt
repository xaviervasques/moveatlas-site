# Seizure-Semiology-Suite (S3, UCLA)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Seizure-Semiology-Suite (S3, UCLA)",
 "description": "Seizure-Semiology-Suite (S3, UCLA). MoveAtlas pose family. 116 subjects. licence repo has NO LICENSE FILE.",
 "identifier": "https://arxiv.org/abs/2605.21852",
 "license": "repo has NO LICENSE FILE (checked 2026-08-22) = all rights reserved by default; videos under a DUA that is not open yet",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "D1 Epilepsy",
  "M1 Pose / video"
 ],
 "url": "https://arxiv.org/abs/2605.21852",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>s3_semiology</code>

<span class="ma-tag">Epilepsy</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | D1; M1 (video), labels |
| **Subjects** | 116 |
| **Status** | documented access barrier (2026-08-22) |
| **License** | repo has NO LICENSE FILE (checked 2026-08-22) = all rights reserved by default; videos under a DUA that is not open yet |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("s3_semiology")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: repo has NO LICENSE FILE (checked 2026-08-22) = all rights reserved by default; videos under a DUA that is not open yet
- **Redistribution**: no
- **Access route**: application (DUA) for videos; repo artefacts unlicensed
- **Source**: <https://arxiv.org/abs/2605.21852>

## Publications

- Zhang, Lina; Monsoor, Tonmoy; Li, Peizheng; Cui, Jiarui; Peng, Xinyi; Han, Chong; Sinha, Prateik; Dai, Siyuan; Pasqua, Jessica Nichole; McCrimmon, Colin M; Liu, Weiting; Miranda, Hailey Marie; Hu, Bing; Wu, Xiangting; Xu, Tengyou; Li, Chunhan; Tian, Jiaye; Tang, Jiarui; Ma, Detao; Kong, Lingye; Lyu, (2026). *Seizure-Semiology-Suite (S3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding*. arXiv. DOI: [10.48550/arxiv.2605.21852](https://doi.org/10.48550/arxiv.2605.21852)

```bibtex
@article{s3_semiology_paper_2026,
  title = {Seizure-Semiology-Suite (S3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding},
  author = {Zhang, Lina and Monsoor, Tonmoy and Li, Peizheng and Cui, Jiarui and Peng, Xinyi and Han, Chong and Sinha, Prateik and Dai, Siyuan and Pasqua, Jessica Nichole and McCrimmon, Colin M and Liu, Weiting and Miranda, Hailey Marie and Hu, Bing and Wu, Xiangting and Xu, Tengyou and Li, Chunhan and Tian, Jiaye and Tang, Jiarui and Ma, Detao and Kong, Lingye and Lyu, Junnan and Li, Jungang and Zan, Yan and Huang, Junhua and Mazumder, Rajarshi and Roychowdhury, Vwani},
  year = {2026},
  doi = {10.48550/arxiv.2605.21852},
  journal = {arXiv}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: s3_semiology
- **family**: pose
- **MoveAtlas cells**: D1; M1 (video), labels
- **population**: 116 adult epilepsy patients, 438 seizure videos, >35,000 dense labels on 20 ILAE semiology features
- **n_subjects**: 116
- **signal**: seizure videos (not yet released) + benchmark/annotation artefacts in the authors' GitHub repo
- **license**: repo has NO LICENSE FILE (checked 2026-08-22) = all rights reserved by default; videos under a DUA that is not open yet; redistribution: no (neither part)
- **access**: application (DUA) for videos; repo artefacts unlicensed
- **link**: https://arxiv.org/abs/2605.21852
