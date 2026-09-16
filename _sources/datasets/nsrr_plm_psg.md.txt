# NSRR PLM-scored PSG family (MrOS Visit1/2 + Wisconsin Sleep Cohort)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NSRR PLM-scored PSG family (MrOS Visit1/2 + Wisconsin Sleep Cohort)",
 "description": "NSRR PLM-scored PSG family (MrOS Visit1/2 + Wisconsin Sleep Cohort). MoveAtlas eeg family. licence free NSRR account + per-dataset Data Access and Use Agreemen.",
 "identifier": "https://sleepdata.org/datasets/mros",
 "license": "free NSRR account + per-dataset Data Access and Use Agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "M6 EEG"
 ],
 "url": "https://sleepdata.org/datasets/mros",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>nsrr_plm_psg</code>

<span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | RLS/PLM context; M6 |
| **Subjects** | ~2907+1026 (MrOS) + ~2570 PSG (WSC) |
| **Status** | documented access barrier (2026-09-05) |
| **License** | free NSRR account + per-dataset Data Access and Use Agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nsrr_plm_psg")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: free NSRR account + per-dataset Data Access and Use Agreement
- **Redistribution**: no
- **Access route**: sleepdata.org (mros + wsc)
- **Source**: <https://sleepdata.org/datasets/mros>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: RLS/PLM context; M6
