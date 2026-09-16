# PD-EEG rest + treadmill walking (OpenNeuro ds007526)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PD-EEG rest + treadmill walking (OpenNeuro ds007526)",
 "description": "PD-EEG rest + treadmill walking (OpenNeuro ds007526). MoveAtlas eeg family. 144 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds007526",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B2 Bradykinesia",
  "B5 Freezing of gait",
  "M6 EEG"
 ],
 "url": "https://openneuro.org/datasets/ds007526",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Zoya Katzir"
  },
  {
   "@type": "Person",
   "name": "Daniel Vered"
  },
  {
   "@type": "Person",
   "name": "Inbal Maidan (inbalm@tlvmc.gov.il)"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>pd_walking_eeg_ds007526</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Freezing of gait</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B5-adjacent; M6 |
| **Subjects** | 144 |
| **Status** | harmonized (2026-08-22) |
| **License** | CC0 (OpenNeuro) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pd_walking_eeg_ds007526")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (OpenNeuro)
- **Redistribution**: yes
- **Access route**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds007526
- **Source**: <https://openneuro.org/datasets/ds007526>

## Publications

- Zoya Katzir; Daniel Vered; Inbal Maidan (inbalm@tlvmc.gov.il) (2026). *PD-EEG: Resting-State & Walking EEG in Parkinson's Disease*. OpenNeuro. DOI: [10.18112/openneuro.ds007526.v1.0.2](https://doi.org/10.18112/openneuro.ds007526.v1.0.2)

```bibtex
@misc{pd_walking_eeg_ds007526_data_2026,
  title = {PD-EEG: Resting-State & Walking EEG in Parkinson's Disease},
  author = {Zoya Katzir and Daniel Vered and Inbal Maidan (inbalm@tlvmc.gov.il)},
  year = {2026},
  doi = {10.18112/openneuro.ds007526.v1.0.2},
  howpublished = {OpenNeuro},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: pd_walking_eeg_ds007526
- **family**: eeg
- **MoveAtlas cells**: B2, B5-adjacent; M6
- **population**: 116 PD + 28 healthy controls; 64-ch EGI; ~4 min rest + ~4 min treadmill walking; MDS-UPDRS, MoCA, LEDD
- **n_subjects**: 144
- **signal**: 64-ch scalp EEG during rest and real walking
- **license**: CC0 (OpenNeuro); redistribution: yes
- **access**: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds007526
- **link**: https://openneuro.org/datasets/ds007526
- **known issues**: the stored amplitudes are about 1000 times larger than scalp EEG although the source declares µV; every record carries the flag and nothing is rescaled
