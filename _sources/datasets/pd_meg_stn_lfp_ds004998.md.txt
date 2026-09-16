# MEG + STN-LFP + EMG in Parkinson's (OpenNeuro ds004998)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MEG + STN-LFP + EMG in Parkinson's (OpenNeuro ds004998)",
 "description": "MEG + STN-LFP + EMG in Parkinson's (OpenNeuro ds004998). MoveAtlas eeg family. 20 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds004998",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B2 Bradykinesia",
  "A1 Tremor",
  "M5 EMG",
  "M6 EEG",
  "M7 LFP / ECoG"
 ],
 "url": "https://openneuro.org/datasets/ds004998",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Fayed Rassoulou"
  },
  {
   "@type": "Person",
   "name": "Alexandra Steina"
  },
  {
   "@type": "Person",
   "name": "Christian J. Hartmann"
  },
  {
   "@type": "Person",
   "name": "Jan Vesper"
  },
  {
   "@type": "Person",
   "name": "Markus Butz"
  },
  {
   "@type": "Person",
   "name": "Alfons Schnitzler"
  },
  {
   "@type": "Person",
   "name": "Jan Hirschmann"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>pd_meg_stn_lfp_ds004998</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Tremor</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1, B2, A1 (PD); M5, M6 (MEG), M7 |
| **Subjects** | 20 |
| **Status** | acquired (2026-08-24) |
| **License** | CC0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pd_meg_stn_lfp_ds004998")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0
- **Redistribution**: yes
- **Access route**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds004998
- **Source**: <https://openneuro.org/datasets/ds004998>

## Publications

- Fayed Rassoulou; Alexandra Steina; Christian J. Hartmann; Jan Vesper; Markus Butz; Alfons Schnitzler; Jan Hirschmann (2024). *Exploring the electrophysiology of Parkinson's disease - magnetoencephalography combined with deep brain recordings from the subthalamic nucleus. *. OpenNeuro. DOI: [10.18112/openneuro.ds004998.v1.2.2](https://doi.org/10.18112/openneuro.ds004998.v1.2.2)

```bibtex
@misc{pd_meg_stn_lfp_ds004998_data_2024,
  title = {Exploring the electrophysiology of Parkinson's disease - magnetoencephalography combined with deep brain recordings from the subthalamic nucleus. },
  author = {Fayed Rassoulou and Alexandra Steina and Christian J. Hartmann and Jan Vesper and Markus Butz and Alfons Schnitzler and Jan Hirschmann},
  year = {2024},
  doi = {10.18112/openneuro.ds004998.v1.2.2},
  howpublished = {OpenNeuro},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: pd_meg_stn_lfp_ds004998
- **family**: eeg
- **MoveAtlas cells**: B1, B2, A1 (PD); M5, M6 (MEG), M7
- **population**: 20 PD with externalized DBS leads, med ON and OFF; rest, static forearm extension, repetitive fist-clenching
- **n_subjects**: 20
- **signal**: 306-ch MEG + STN LFP + EMG + EOG at 2 kHz
- **license**: CC0; redistribution: yes
- **access**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds004998
- **link**: https://openneuro.org/datasets/ds004998
- **citation**: Sci Data 2024, doi 10.1038/s41597-024-03768-1
