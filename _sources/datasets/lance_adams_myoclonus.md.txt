# Lance-Adams posthypoxic myoclonus EEG-EMG case (Zenodo 7620808)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Lance-Adams posthypoxic myoclonus EEG-EMG case (Zenodo 7620808)",
 "description": "Lance-Adams posthypoxic myoclonus EEG-EMG case (Zenodo 7620808). MoveAtlas eeg family. 1 subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/7620808",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "A2 Myoclonus",
  "M5 EMG",
  "M6 EEG"
 ],
 "url": "https://zenodo.org/records/7620808",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>lance_adams_myoclonus</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | A2; M5 (leg EMG), M6 (EEG) |
| **Subjects** | 1 |
| **Status** | DOWNLOADED 2026-09-01 (owner GO): all 5 supplementary files (10.5 MB, sha256 journaled; two Zenodo 504 throttles resumed same day). Includes the patient video (.mov): INTERNAL raw only; release_lint hard-refuses .mov by design, so it can never ship |
| **License** | CC BY 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("lance_adams_myoclonus")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: Zenodo direct download
- **Source**: <https://zenodo.org/records/7620808>

## Data card (verbatim, with its evidence trail)


- dataset: lance_adams_myoclonus
- family: eeg  (physical path: datasets/eeg/lance_adams_myoclonus)
- MoveAtlas cells: A2; M5 (leg EMG), M6 (EEG)
- population: N=1 Lance-Adams syndrome case around ECT: EEG + lower-limb EMG polygraphy + jerk-locked back averaging + patient video
- n_subjects: 1
- signal: EEG-EMG polygraphy (~10.5 MB)
- license: CC BY 4.0 (verified on page 2026-09-01) ; redistribution: yes
- access: Zenodo direct download
- status (2026-08-22): DOWNLOADED 2026-09-01 (owner GO): all 5 supplementary files (10.5 MB, sha256 journaled; two Zenodo 504 throttles resumed same day). Includes the patient video (.mov): INTERNAL raw only; release_lint hard-refuses .mov by design, so it can never ship
- link: https://zenodo.org/records/7620808
