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
| **Status** | REPO LOCATED 2026-08-22: github.com/LinaZhangUCLA/SeizureSemiologySuite (ICML 2026 spotlight, pushed 2026-05-26, ~57 MB, 801 csv + 36 json + 7 jsonl). It holds the benchmark/fine-tuning artefacts and split tables, NOT the videos; the paper's Dataset link is still a placeholder. NOTHING FETCHED INTO... |
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
- **Redistribution**: no (neither part)
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

## Data card (verbatim, with its evidence trail)


- dataset: s3_semiology
- family: pose  (physical path: datasets/pose/s3_semiology)
- MoveAtlas cells: D1; M1 (video), labels
- population: 116 adult epilepsy patients, 438 seizure videos, >35,000 dense labels on 20 ILAE semiology features
- n_subjects: 116
- signal: seizure videos (not yet released) + benchmark/annotation artefacts in the authors' GitHub repo
- license: repo has NO LICENSE FILE (checked 2026-08-22) = all rights reserved by default; videos under a DUA that is not open yet ; redistribution: no (neither part)
- access: application (DUA) for videos; repo artefacts unlicensed
- status (2026-08-22): REPO LOCATED 2026-08-22: github.com/LinaZhangUCLA/SeizureSemiologySuite (ICML 2026 spotlight, pushed 2026-05-26, ~57 MB, 801 csv + 36 json + 7 jsonl). It holds the benchmark/fine-tuning artefacts and split tables, NOT the videos; the paper's Dataset link is still a placeholder. NOTHING FETCHED INTO THIS REPO: no license means no redistribution right, and the DUA is still in the human queue. DOCUMENTED BARRIER (owner, 2026-08-28): the publication focuses on genuinely open data; the DUA route is not pursued. Evidence recorded 2026-08-28: the videos NEVER leave UCLA; authorized users analyze inside a UCLA-hosted secure enclave after an institutional DUA plus project IRB approval, so local training was off the table anyway; the repo's annotation CSVs stay look-don't-mirror (no licence file)
- link: https://arxiv.org/abs/2605.21852
- notes: exactly the D1 target: movement during seizures with ILAE feature labels. 438 videos / 116 adults (300 ES, 138 NES), ages 18-64, tertiary EMU 2019-2023, IRB-approved and de-identified; 20 ILAE features each with presence, MM:SS boundaries and free-text justification. Labels: eval only (R1), never pretraining
