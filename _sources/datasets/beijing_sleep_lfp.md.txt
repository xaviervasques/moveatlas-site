# Beijing basal-ganglia sleep LFP (121 patients, NOT public)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Beijing basal-ganglia sleep LFP (121 patients, NOT public)",
 "description": "Beijing basal-ganglia sleep LFP (121 patients, NOT public). MoveAtlas eeg family. 121 subjects. licence no public repository.",
 "identifier": "https://www.nature.com/articles/s41746-024-01115-7",
 "license": "no public repository",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "D6 Sleep disorders",
  "M7 LFP / ECoG"
 ],
 "url": "https://www.nature.com/articles/s41746-024-01115-7",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>beijing_sleep_lfp</code>

<span class="ma-tag">Sleep disorders</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | D6; M7 |
| **Subjects** | 121 |
| **Status** | documented access barrier (2026-08-22) |
| **License** | no public repository |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("beijing_sleep_lfp")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: no public repository
- **Redistribution**: no
- **Access route**: application: contact the authors (Jianguo Zhang lab)
- **Source**: <https://www.nature.com/articles/s41746-024-01115-7>

## Publications

- Yin, Zixiao; Yu, Huiling; Yuan, Tianshuo; Smyth, Clay; Anjum, Md Fahim; Zhu, Guanyu; Ma, Ruoyu; Xu, Yichen; An, Qi; Gan, Yifei; Merk, Timon; Qin, Guofan; Xie, Hutao; Zhang, Ning; Wang, Chunxue; Jiang, Yin; Meng, Fangang; Yang, Anchao; Neumann, Wolf-Julian; Starr, Philip; Little, Simon; Li, Luming; Z (2024). *Generalized sleep decoding with basal ganglia signals in multiple movement disorders*. npj Digital Medicine. DOI: [10.1038/s41746-024-01115-7](https://doi.org/10.1038/s41746-024-01115-7)

```bibtex
@article{beijing_sleep_lfp_paper_2024,
  title = {Generalized sleep decoding with basal ganglia signals in multiple movement disorders},
  author = {Yin, Zixiao and Yu, Huiling and Yuan, Tianshuo and Smyth, Clay and Anjum, Md Fahim and Zhu, Guanyu and Ma, Ruoyu and Xu, Yichen and An, Qi and Gan, Yifei and Merk, Timon and Qin, Guofan and Xie, Hutao and Zhang, Ning and Wang, Chunxue and Jiang, Yin and Meng, Fangang and Yang, Anchao and Neumann, Wolf-Julian and Starr, Philip and Little, Simon and Li, Luming and Zhang, Jianguo},
  year = {2024},
  doi = {10.1038/s41746-024-01115-7},
  journal = {npj Digital Medicine}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: beijing_sleep_lfp
- **family**: eeg
- **MoveAtlas cells**: D6; M7
- **population**: 121 patients (PD, dystonia, HD, Tourette, ET), PSG + LFP, 140 nights
- **n_subjects**: 121
- **signal**: sleep-stage-scored polysomnography + DBS-lead LFP
- **license**: no public repository; redistribution: no
- **access**: application: contact the authors (Jianguo Zhang lab)
- **link**: https://www.nature.com/articles/s41746-024-01115-7
