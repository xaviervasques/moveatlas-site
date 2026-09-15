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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (DAUA tier): the big PLM-scored raw PSG masses - MrOS (piezo leg sensors, centrally scored PLMs) and WSC (leg EMG channel, LM/LMA scoring). Our open PLM needs stay covered by cap_sleep (10 PLM patients, held); these document the scale behind the gate |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://sleepdata.org/datasets/mros
- License / access: free NSRR account + per-dataset Data Access and Use Agreement
- Access route: sleepdata.org (mros + wsc)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); not fetched at card creation
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (DAUA tier): the big PLM-scored raw PSG masses - MrOS (piezo leg sensors, centrally scored PLMs) and WSC (leg EMG channel, LM/LMA scoring). Our open PLM needs stay covered by cap_sleep (10 PLM patients, held); these document the scale behind the gate
- Number of subjects: ~2907+1026 (MrOS) + ~2570 PSG (WSC)
- MoveAtlas cells: RLS/PLM context; M6

### Retrieval notes
RE-VERIFY at fetch/request. No-emails policy for request tiers.

### Processing
None. Catalogue-tier.
