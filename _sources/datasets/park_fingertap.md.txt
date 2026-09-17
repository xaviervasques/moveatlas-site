# PARK finger tapping (ROC-HCI)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PARK finger tapping (ROC-HCI)",
 "description": "PARK finger tapping (ROC-HCI). MoveAtlas pose family. licence MIT.",
 "identifier": "https://github.com/ROC-HCI/finger-tapping-severity",
 "license": "https://opensource.org/license/mit",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "M1 Pose / video"
 ],
 "url": "https://github.com/ROC-HCI/finger-tapping-severity",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>park_fingertap</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M1 (features) |
| **Subjects** | unknown |
| **Status** | acquired |
| **License** | MIT (LICENSE file in the repo, read 2026-08-28) |
| **MoveAtlas record** | [10.5281/zenodo.22313481](https://doi.org/10.5281/zenodo.22313481) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("park_fingertap")
records, meta = ds.get_data()
```

## License and access

- **License**: MIT (LICENSE file in the repo, read 2026-08-28)
- **Redistribution**: yes (the feature tables are MIT)
- **Access route**: downloaded
- **Source**: <https://github.com/ROC-HCI/finger-tapping-severity>

## Publications

- Islam, Md Saiful; Rahman, Wasifur; Abdelkader, Abdelrahman; Lee, Sangwu; Yang, Phillip T.; Purks, Jennifer Lynn; Adams, Jamie Lynn; Schneider, Ruth B.; Dorsey, Earl Ray; Hoque, Ehsan (2023). *Using AI to measure Parkinson’s disease severity at home*. npj Digital Medicine. DOI: [10.1038/s41746-023-00905-9](https://doi.org/10.1038/s41746-023-00905-9)

```bibtex
@article{park_fingertap_paper_2023,
  title = {Using AI to measure Parkinson’s disease severity at home},
  author = {Islam, Md Saiful and Rahman, Wasifur and Abdelkader, Abdelrahman and Lee, Sangwu and Yang, Phillip T. and Purks, Jennifer Lynn and Adams, Jamie Lynn and Schneider, Ruth B. and Dorsey, Earl Ray and Hoque, Ehsan},
  year = {2023},
  doi = {10.1038/s41746-023-00905-9},
  journal = {npj Digital Medicine}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: park_fingertap
- **family**: pose
- **MoveAtlas cells**: B2; M1 (features)
- **population**: 489 videos, subjects not individuated (features keyed by video filename)
- **n_subjects**: unknown
- **signal**: 488-row feature table, no raw pose
- **license**: MIT (LICENSE file in the repo, read 2026-08-28); redistribution: yes (the feature tables are MIT)
- **access**: downloaded
- **link**: https://github.com/ROC-HCI/finger-tapping-severity
