# UCSD resting-state EEG, PD ON and OFF medication (OpenNeuro ds002778)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "UCSD resting-state EEG, PD ON and OFF medication (OpenNeuro ds002778)",
 "description": "UCSD resting-state EEG, PD ON and OFF medication (OpenNeuro ds002778). MoveAtlas eeg family. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds002778",
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
 "url": "https://openneuro.org/datasets/ds002778",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>pd_rest_eeg_onoff_ds002778</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M6 |
| **Subjects** | ~32 |
| **Status** | DOWNLOADED AND INGESTED 2026-09-01 (owner GO): full S3 sync (332 files / 0.57 GB), then 46/46 canonical EEG records via the extended BIDS builder (.bdf support added; sessions ride in the task: rest_ses-hc 16 / ses-off 15 / ses-on 15; subject_ns keeps a person whole across ON and OFF for split safet... |
| **License** | CC0 (OpenNeuro standard, mirror-verified 2026-09-01; curators request a courtesy note pre-publication, non-binding) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pd_rest_eeg_onoff_ds002778")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (OpenNeuro standard, mirror-verified 2026-09-01; curators request a courtesy note pre-publication, non-binding)
- **Redistribution**: yes
- **Access route**: OpenNeuro / S3 direct download
- **Source**: <https://openneuro.org/datasets/ds002778>

## Data card (verbatim, with its evidence trail)


- dataset: pd_rest_eeg_onoff_ds002778
- family: eeg  (physical path: datasets/eeg/pd_rest_eeg_onoff_ds002778)
- MoveAtlas cells: B2; M6
- population: ~16 PD recorded both ON and OFF levodopa + ~16 matched controls, rest EEG
- n_subjects: ~32
- signal: resting EEG (BIDS)
- license: CC0 (OpenNeuro standard, mirror-verified 2026-09-01; curators request a courtesy note pre-publication, non-binding) ; redistribution: yes
- access: OpenNeuro / S3 direct download
- status (2026-08-22): DOWNLOADED AND INGESTED 2026-09-01 (owner GO): full S3 sync (332 files / 0.57 GB), then 46/46 canonical EEG records via the extended BIDS builder (.bdf support added; sessions ride in the task: rest_ses-hc 16 / ses-off 15 / ses-on 15; subject_ns keeps a person whole across ON and OFF for split safety). BioSemi DC-coupled recordings: amplitude plausibility measured on the demeaned signal (declared low_cutoff 0.0), offsets preserved; 2 records carry genuine artifact-level amplitude flags
- link: https://openneuro.org/datasets/ds002778
