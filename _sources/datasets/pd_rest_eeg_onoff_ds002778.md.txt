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
| **Status** | harmonized (2026-09-01) |
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: pd_rest_eeg_onoff_ds002778
- **family**: eeg
- **MoveAtlas cells**: B2; M6
- **population**: ~16 PD recorded both ON and OFF levodopa + ~16 matched controls, rest EEG
- **n_subjects**: ~32
- **signal**: resting EEG (BIDS)
- **license**: CC0 (OpenNeuro standard, mirror-verified 2026-09-01; curators request a courtesy note pre-publication, non-binding); redistribution: yes
- **access**: OpenNeuro / S3 direct download
- **link**: https://openneuro.org/datasets/ds002778
