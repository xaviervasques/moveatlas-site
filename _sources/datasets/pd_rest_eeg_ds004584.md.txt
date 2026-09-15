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
   "name": "Arun Singh arun.singh@usd.edu"
  },
  {
   "@type": "Person",
   "name": "Rachel Cole rachel-cole@uiowa.edu"
  },
  {
   "@type": "Person",
   "name": "Arturo Espinoza arturo-espinoza@uiowa.edu"
  },
  {
   "@type": "Person",
   "name": "Jim Cavanagh jcavanagh@unm.edu"
  },
  {
   "@type": "Person",
   "name": "Nandakumar Narayanan nandakumar-narayanan@uiowa.edu"
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
| **Status** | DOWNLOADED AND INGESTED 2026-08-22: 5.5 GB BIDS on disk -> 149 canonical EEG records, one per subject, 63 channels at 500 Hz, ALL channels parsed onto the site vocabulary. 9 of the 149 records are flagged for artifact-level amplitude (p99 above 500 uV, up to ~1700), which in resting EEG is ordinary... |
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

- Arun Singh arun.singh@usd.edu; Rachel Cole rachel-cole@uiowa.edu; Arturo Espinoza arturo-espinoza@uiowa.edu; Jim Cavanagh jcavanagh@unm.edu; Nandakumar Narayanan nandakumar-narayanan@uiowa.edu (2023). *Rest eyes open*. OpenNeuro. DOI: [10.18112/openneuro.ds004584.v1.0.0](https://doi.org/10.18112/openneuro.ds004584.v1.0.0)

```bibtex
@misc{pd_rest_eeg_ds004584_data_2023,
  title = {Rest eyes open},
  author = {Arun Singh arun.singh@usd.edu and Rachel Cole rachel-cole@uiowa.edu and Arturo Espinoza arturo-espinoza@uiowa.edu and Jim Cavanagh jcavanagh@unm.edu and Nandakumar Narayanan nandakumar-narayanan@uiowa.edu},
  year = {2023},
  doi = {10.18112/openneuro.ds004584.v1.0.0},
  howpublished = {OpenNeuro},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: pd_rest_eeg_ds004584
- family: eeg  (physical path: datasets/eeg/pd_rest_eeg_ds004584)
- MoveAtlas cells: B2; M6
- population: 100 PD + 49 controls, 64-ch BrainVision, 2 min eyes-open rest
- n_subjects: 149
- signal: 64-ch resting EEG
- license: CC0 (OpenNeuro) ; redistribution: yes
- access: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds004584
- status (2026-08-22): DOWNLOADED AND INGESTED 2026-08-22: 5.5 GB BIDS on disk -> 149 canonical EEG records, one per subject, 63 channels at 500 Hz, ALL channels parsed onto the site vocabulary. 9 of the 149 records are flagged for artifact-level amplitude (p99 above 500 uV, up to ~1700), which in resting EEG is ordinary electrode and movement artifact rather than a scale error; the other 140 sit in a normal range. Reference PZ, read from eeg.json EEGReference, not assumed. One subject (sub-068) carries three extra traces named X/Y/Z with no type and no description: routed to aux and FLAGGED, not guessed as accelerometer
- link: https://openneuro.org/datasets/ds004584
