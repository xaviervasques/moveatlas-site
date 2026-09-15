# CAP Sleep Database (PhysioNet)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CAP Sleep Database (PhysioNet)",
 "description": "CAP Sleep Database (PhysioNet). MoveAtlas eeg family. 108 subjects. licence PhysioNet open.",
 "identifier": "https://physionet.org/content/capslpdb/",
 "license": "PhysioNet open",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "D6 Sleep disorders",
  "M5 EMG",
  "M6 EEG"
 ],
 "url": "https://physionet.org/content/capslpdb/",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Terzano, Mario Giovanni"
  },
  {
   "@type": "Person",
   "name": "Parrino, Liborio"
  },
  {
   "@type": "Person",
   "name": "Sherieri, Adriano"
  },
  {
   "@type": "Person",
   "name": "Chervin, Ronald"
  },
  {
   "@type": "Person",
   "name": "Chokroverty, Sudhansu"
  },
  {
   "@type": "Person",
   "name": "Guilleminault, Christian"
  },
  {
   "@type": "Person",
   "name": "Hirshkowitz, Max"
  },
  {
   "@type": "Person",
   "name": "Mahowald, Mark"
  },
  {
   "@type": "Person",
   "name": "Moldofsky, Harvey"
  },
  {
   "@type": "Person",
   "name": "Rosa, Agostino"
  },
  {
   "@type": "Person",
   "name": "Thomas, Robert"
  },
  {
   "@type": "Person",
   "name": "Walters, Arthur"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cap_sleep</code>

<span class="ma-tag">Sleep disorders</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | D6 (RBD); M5 chin, M6 |
| **Subjects** | 108 |
| **Status** | INGESTED IN FULL 2026-08-24 (Paris session): the whole rbd,n subset, 38 EDF on disk (12.9 GB), 35 canonical EEG records / 35 subjects (22 RBD + 13 normals) / 332 h, plus 4 chin-EMG records to canonical_emg. n13/n14/n15 REFUSED as designed: their headers declare no physical dimension for any channel... |
| **License** | PhysioNet open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cap_sleep")
records, meta = ds.get_data()
```

## License and access

- **License**: PhysioNet open
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only cap_sleep --cap-subset rbd,n)
- **Source**: <https://physionet.org/content/capslpdb/>

## Publications

- Terzano, Mario Giovanni; Parrino, Liborio; Sherieri, Adriano; Chervin, Ronald; Chokroverty, Sudhansu; Guilleminault, Christian; Hirshkowitz, Max; Mahowald, Mark; Moldofsky, Harvey; Rosa, Agostino; Thomas, Robert; Walters, Arthur (2001). *CAP Sleep Database*. physionet.org. DOI: [10.13026/c2vc79](https://doi.org/10.13026/c2vc79)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{cap_sleep_data_2001,
  title = {CAP Sleep Database},
  author = {Terzano, Mario Giovanni and Parrino, Liborio and Sherieri, Adriano and Chervin, Ronald and Chokroverty, Sudhansu and Guilleminault, Christian and Hirshkowitz, Max and Mahowald, Mark and Moldofsky, Harvey and Rosa, Agostino and Thomas, Robert and Walters, Arthur},
  year = {2001},
  doi = {10.13026/c2vc79},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{cap_sleep_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: cap_sleep
- family: eeg  (physical path: datasets/eeg/cap_sleep)
- MoveAtlas cells: D6 (RBD); M5 chin, M6
- population: 108 polysomnographies incl. 22 RBD, other sleep disorders, controls
- n_subjects: 108
- signal: full PSG: EEG, chin EMG, ECG, EOG (EDF + annotations)
- license: PhysioNet open ; redistribution: yes
- access: direct_download (fetch_p2_lot.py --only cap_sleep --cap-subset rbd,n)
- status (2026-08-22): INGESTED IN FULL 2026-08-24 (Paris session): the whole rbd,n subset, 38 EDF on disk (12.9 GB), 35 canonical EEG records / 35 subjects (22 RBD + 13 normals) / 332 h, plus 4 chin-EMG records to canonical_emg. n13/n14/n15 REFUSED as designed: their headers declare no physical dimension for any channel and C-EEG-4 forbids guessing a scale; costing 3 of 38 is the cheaper error. Unrecognized labels (SX1-SX2 / DX1-DX2, STAT, TAG/THE) stay in aux exactly as surveyed: left/right of an unnamed muscle is not an identification. Validation after ingest: no errors. Ingestion chain: build_canonical_eeg.py --only cap_sleep (EDF reader + sleep-montage parser validated on synthetic EDF; first real batch is the field verification; chin EMG routes to canonical_emg, EOG/ECG to aux, C-EEG-3)
- link: https://physionet.org/content/capslpdb/
- notes: opens the sleep cell; synucleinopathy prodrome; REM-atonia reference
