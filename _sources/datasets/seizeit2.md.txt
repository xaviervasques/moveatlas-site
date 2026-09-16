# SeizeIT2 (focal epilepsy wearables, OpenNeuro ds005873)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "SeizeIT2 (focal epilepsy wearables, OpenNeuro ds005873)",
 "description": "SeizeIT2 (focal epilepsy wearables, OpenNeuro ds005873). MoveAtlas eeg family. 125 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds005873",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "D1 Epilepsy",
  "A2 Myoclonus",
  "M2 Inertial (IMU)",
  "M5 EMG",
  "M6 EEG"
 ],
 "url": "https://openneuro.org/datasets/ds005873",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Miguel Bhagubai"
  },
  {
   "@type": "Person",
   "name": "Christos Chatzichristos"
  },
  {
   "@type": "Person",
   "name": "Lauren Swinnen"
  },
  {
   "@type": "Person",
   "name": "Jaiver Macea"
  },
  {
   "@type": "Person",
   "name": "Jingwei Zhang"
  },
  {
   "@type": "Person",
   "name": "Lieven Lagae"
  },
  {
   "@type": "Person",
   "name": "Katrien Jansen"
  },
  {
   "@type": "Person",
   "name": "Andreas Schulze-Bonhage"
  },
  {
   "@type": "Person",
   "name": "Francisco Sales"
  },
  {
   "@type": "Person",
   "name": "Benno Mahler"
  },
  {
   "@type": "Person",
   "name": "Yvonne Weber"
  },
  {
   "@type": "Person",
   "name": "Wim Van Paesschen"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>seizeit2</code>

<span class="ma-tag">Epilepsy</span><span class="ma-tag">Myoclonus</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | D1; A2 proxy; M2, M5, M6 |
| **Subjects** | 125 |
| **Status** | harmonized (2026-08-24) |
| **License** | CC0 (verified in dataset_description.json) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("seizeit2")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC0 (verified in dataset_description.json)
- **Redistribution**: yes
- **Access route**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds005873 (fetch_p2_lot.py --only seizeit2 prints it)
- **Source**: <https://openneuro.org/datasets/ds005873>

## Publications

- Miguel Bhagubai; Christos Chatzichristos; Lauren Swinnen; Jaiver Macea; Jingwei Zhang; Lieven Lagae; Katrien Jansen; Andreas Schulze-Bonhage; Francisco Sales; Benno Mahler; Yvonne Weber; Wim Van Paesschen; Maarten De Vos   (2025). *SeizeIT2*. OpenNeuro. DOI: [10.18112/openneuro.ds005873.v1.1.0](https://doi.org/10.18112/openneuro.ds005873.v1.1.0)
- Bhagubai, Miguel; Chatzichristos, Christos; Swinnen, Lauren; Macea, Jaiver; Zhang, Jingwei; Lagae, Lieven; Jansen, Katrien; Schulze-Bonhage, Andreas; Sales, Francisco; Mahler, Benno; Weber, Yvonne; Van Paesschen, Wim; De Vos, Maarten (2025). *SeizeIT2: Wearable Dataset Of Patients With Focal Epilepsy*. Scientific Data. DOI: [10.1038/s41597-025-05580-x](https://doi.org/10.1038/s41597-025-05580-x)

```bibtex
@misc{seizeit2_data_2025,
  title = {SeizeIT2},
  author = {Miguel Bhagubai and Christos Chatzichristos and Lauren Swinnen and Jaiver Macea and Jingwei Zhang and Lieven Lagae and Katrien Jansen and Andreas Schulze-Bonhage and Francisco Sales and Benno Mahler and Yvonne Weber and Wim Van Paesschen and Maarten De Vos  },
  year = {2025},
  doi = {10.18112/openneuro.ds005873.v1.1.0},
  howpublished = {OpenNeuro},
  note = {dataset}
}
@article{seizeit2_paper_2025,
  title = {SeizeIT2: Wearable Dataset Of Patients With Focal Epilepsy},
  author = {Bhagubai, Miguel and Chatzichristos, Christos and Swinnen, Lauren and Macea, Jaiver and Zhang, Jingwei and Lagae, Lieven and Jansen, Katrien and Schulze-Bonhage, Andreas and Sales, Francisco and Mahler, Benno and Weber, Yvonne and Van Paesschen, Wim and De Vos, Maarten},
  year = {2025},
  doi = {10.1038/s41597-025-05580-x},
  journal = {Scientific Data}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: seizeit2
- **family**: eeg
- **MoveAtlas cells**: D1; A2 proxy; M2, M5, M6
- **population**: 125 focal epilepsy patients, 5 European EMUs, 11,640 h, 886 annotated focal seizures
- **n_subjects**: 125
- **signal**: behind-the-ear EEG (2-3 ch) + ECG + deltoid EMG + IMU; 250 Hz (EEG/ECG/EMG), 25 Hz (IMU)
- **license**: CC0 (verified in dataset_description.json); redistribution: yes
- **access**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds005873 (fetch_p2_lot.py --only seizeit2 prints it)
- **link**: https://openneuro.org/datasets/ds005873
- **citation**: doi 10.1038/s41597-025-05580-x
- **ingestion**: build_canonical_eeg.py --only seizeit2 (BIDS-EDF builder, C-EEG-7 EAR_L/EAR_R bipolar encoding; seizure labels for evaluation only, never pretraining)
- **known issues**: a screen on 2026-09-16 found 168 of 2,850 EEG records outside 0.5-250 µV, 4 of them flat, and 10 flat deltoid-EMG records; the values are kept as recorded
