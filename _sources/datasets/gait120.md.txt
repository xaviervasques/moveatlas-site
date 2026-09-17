# Gait120 (mocap + sEMG, Sci Data 2025)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Gait120 (mocap + sEMG, Sci Data 2025)",
 "description": "Gait120 (mocap + sEMG, Sci Data 2025). MoveAtlas emg family. 120 subjects. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.1038/s41597-025-05391-0",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "emg",
  "C1 Normal adult movement",
  "M1 Pose / video",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.1038/s41597-025-05391-0",
 "isAccessibleForFree": true,
 "measurementTechnique": "emg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Boo, Junyo"
  },
  {
   "@type": "Person",
   "name": "Seo, Dongwook"
  },
  {
   "@type": "Person",
   "name": "Kim, Minseung"
  },
  {
   "@type": "Person",
   "name": "Koo, Seungbum"
  }
 ]
}
</script>
```

<span class="ma-fam ma-emg">emg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>gait120</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1, M5 |
| **Subjects** | 120 |
| **Ages** | 20-59 y (35.4 +/- 12.8) |
| **Status** | catalogued (2026-08-28) |
| **License** | CC BY 4.0 (figshare item metadata, verified 2026-08-22) |
| **MoveAtlas record** | [10.5281/zenodo.22310188](https://doi.org/10.5281/zenodo.22310188) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gait120")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (figshare item metadata, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download
- **Source**: <https://doi.org/10.1038/s41597-025-05391-0>

## Publications

- Boo, Junyo; Seo, Dongwook; Kim, Minseung; Koo, Seungbum (2025). *Comprehensive human locomotion and electromyography dataset: Gait120*. Scientific Data. DOI: [10.1038/s41597-025-05391-0](https://doi.org/10.1038/s41597-025-05391-0)

```bibtex
@misc{gait120_data_2025,
  title = {Comprehensive human locomotion and electromyography dataset: Gait120},
  author = {Boo, Junyo and Seo, Dongwook and Kim, Minseung and Koo, Seungbum},
  year = {2025},
  doi = {10.1038/s41597-025-05391-0},
  howpublished = {Scientific Data},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: gait120
- **family**: emg
- **MoveAtlas cells**: C1; M1, M5
- **population**: 120 healthy adult males, 7 locomotion tasks, 6,882 movement cycles
- **n_subjects**: 120
- **age**: 20-59 y (35.4 +/- 12.8)
- **signal**: full-body optical mocap (.trc/.mot) + sEMG of 12 lower-limb muscles (.mat)
- **license**: CC BY 4.0 (figshare item metadata, verified 2026-08-22); redistribution: yes
- **access**: direct_download
- **link**: https://doi.org/10.1038/s41597-025-05391-0
