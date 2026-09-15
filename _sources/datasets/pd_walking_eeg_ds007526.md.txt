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
| **Status** | DOWNLOADED AND INGESTED 2026-08-22: 8.4 GB BIDS on disk -> 277 canonical EEG records from 144 subjects (144 rest + 133 walk), 60 EEG channels at 250 Hz, 0 unrecognized. AMPLITUDE CAVEAT, surfaced by validate_canonical.py: ALL 277 records carry a p99 near 5e4 uV, about 1000x too large for scalp EEG.... |
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

- Zoya Katzir; Daniel Vered; Inbal Maidan (inbalm@tlvmc.gov.il) (2026). *PD-EEG: Resting-State & Walking EEG in Parkinson's Disease*. OpenNeuro. DOI: [10.18112/openneuro.ds007526.v1.0.0](https://doi.org/10.18112/openneuro.ds007526.v1.0.0)

```bibtex
@misc{pd_walking_eeg_ds007526_data_2026,
  title = {PD-EEG: Resting-State & Walking EEG in Parkinson's Disease},
  author = {Zoya Katzir and Daniel Vered and Inbal Maidan (inbalm@tlvmc.gov.il)},
  year = {2026},
  doi = {10.18112/openneuro.ds007526.v1.0.0},
  howpublished = {OpenNeuro},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: pd_walking_eeg_ds007526
- family: eeg  (physical path: datasets/eeg/pd_walking_eeg_ds007526)
- MoveAtlas cells: B2, B5-adjacent; M6
- population: 116 PD + 28 healthy controls; 64-ch EGI; ~4 min rest + ~4 min treadmill walking; MDS-UPDRS, MoCA, LEDD
- n_subjects: 144
- signal: 64-ch scalp EEG during rest and real walking
- license: CC0 (OpenNeuro) ; redistribution: yes
- access: tool: aws s3 sync --no-sign-request s3://openneuro.org/ds007526
- status (2026-08-22): DOWNLOADED AND INGESTED 2026-08-22: 8.4 GB BIDS on disk -> 277 canonical EEG records from 144 subjects (144 rest + 133 walk), 60 EEG channels at 250 Hz, 0 unrecognized. AMPLITUDE CAVEAT, surfaced by validate_canonical.py: ALL 277 records carry a p99 near 5e4 uV, about 1000x too large for scalp EEG. Chased to the source rather than assumed: the .set files themselves store values with p99 ~2.7e5, mne applies the standard EEGLAB microvolt convention, and the dataset's own channels.tsv also declares uV, so the declaration and the values disagree by three orders of magnitude. The pipeline carries the declaration faithfully and FLAGS every record instead of rescaling on a hunch. Treat this set as SCALE-UNRESOLVED until the authors answer, and do not mix it with other EEG sources in an amplitude-sensitive objective. subject_ns is the BIDS subject, so a person's rest and walk runs share a subject and cannot straddle a split. EEGReference is n/a in the sidecars, so the records honestly carry REF_COMMON_UNKNOWN. EOG1-4 and VREF are labelled type=EEG by the dataset but are routed by NAME to eog and aux
- link: https://openneuro.org/datasets/ds007526
- notes: largest walking-EEG pathology cohort found; upgrade of ds002778
