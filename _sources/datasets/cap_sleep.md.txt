# CAP Sleep Database (PhysioNet)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CAP Sleep Database (PhysioNet)",
 "description": "CAP Sleep Database (PhysioNet). MoveAtlas eeg family. 108 subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/capslpdb/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
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
| **Status** | harmonized (2026-08-24) |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |
| **MoveAtlas record** | [10.5281/zenodo.22300225](https://doi.org/10.5281/zenodo.22300225) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cap_sleep")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: cap_sleep
- **family**: eeg
- **MoveAtlas cells**: D6 (RBD); M5 chin, M6
- **population**: 108 polysomnographies incl. 22 RBD, other sleep disorders, controls
- **n_subjects**: 108
- **signal**: full PSG: EEG, chin EMG, ECG, EOG (EDF + annotations)
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: direct_download (fetch_p2_lot.py --only cap_sleep --cap-subset rbd,n)
- **link**: https://physionet.org/content/capslpdb/
