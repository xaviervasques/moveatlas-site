# PD rest EEG, 149 subjects (OpenNeuro ds004584)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PD rest EEG, 149 subjects (OpenNeuro ds004584)",
 "description": "PD rest EEG, 149 subjects (OpenNeuro ds004584). MoveAtlas eeg family. 149 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds004584",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B2 Bradykinesia",
  "M6 EEG"
 ],
 "url": "https://openneuro.org/datasets/ds004584",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Arun Singh"
  },
  {
   "@type": "Person",
   "name": "Rachel Cole"
  },
  {
   "@type": "Person",
   "name": "Arturo Espinoza"
  },
  {
   "@type": "Person",
   "name": "Jim Cavanagh"
  },
  {
   "@type": "Person",
   "name": "Nandakumar Narayanan"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>pd_rest_eeg_ds004584</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M6 |
| **Subjects** | 149 |
| **Status** | harmonized (2026-08-22) |
| **License** | CC0 (OpenNeuro) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pd_rest_eeg_ds004584")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (OpenNeuro)
- **Redistribution**: yes
- **Access route**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds004584
- **Source**: <https://openneuro.org/datasets/ds004584>

## Publications

- Arun Singh; Rachel Cole; Arturo Espinoza; Jim Cavanagh; Nandakumar Narayanan (2023). *Rest eyes open*. OpenNeuro. DOI: [10.18112/openneuro.ds004584.v1.0.0](https://doi.org/10.18112/openneuro.ds004584.v1.0.0)

```bibtex
@misc{pd_rest_eeg_ds004584_data_2023,
  title = {Rest eyes open},
  author = {Arun Singh and Rachel Cole and Arturo Espinoza and Jim Cavanagh and Nandakumar Narayanan},
  year = {2023},
  doi = {10.18112/openneuro.ds004584.v1.0.0},
  howpublished = {OpenNeuro},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: pd_rest_eeg_ds004584
- **family**: eeg
- **MoveAtlas cells**: B2; M6
- **population**: 100 PD + 49 controls, 64-ch BrainVision, 2 min eyes-open rest
- **n_subjects**: 149
- **signal**: 64-ch resting EEG
- **license**: CC0 (OpenNeuro); redistribution: yes
- **access**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds004584
- **link**: https://openneuro.org/datasets/ds004584
