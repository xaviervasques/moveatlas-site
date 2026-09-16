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
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Vellieux, Geoffroy"
  },
  {
   "@type": "Person",
   "name": "Apartis, Emmanuelle"
  },
  {
   "@type": "Person",
   "name": "Degos, Vincent"
  },
  {
   "@type": "Person",
   "name": "Fossati, Philippe"
  },
  {
   "@type": "Person",
   "name": "Navarro, Vincent"
  }
 ]
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>lance_adams_myoclonus</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | A2; M5 (leg EMG), M6 (EEG) |
| **Subjects** | 1 |
| **Status** | acquired (2026-09-01) |
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

## Publications

- Vellieux, Geoffroy; Apartis, Emmanuelle; Degos, Vincent; Fossati, Philippe; Navarro, Vincent (2023). *Effectiveness of electroconvulsive therapy in Lance-Adams syndrome*. Zenodo. DOI: [10.5281/zenodo.7620808](https://doi.org/10.5281/zenodo.7620808)
- Vellieux, Geoffroy; Apartis, Emmanuelle; Degos, Vincent; Fossati, Philippe; Navarro, Vincent (2023). *Effectiveness of electroconvulsive therapy in Lance-Adams syndrome*. Brain Stimulation. DOI: [10.1016/j.brs.2023.03.004](https://doi.org/10.1016/j.brs.2023.03.004)

```bibtex
@misc{lance_adams_myoclonus_data_2023,
  title = {Effectiveness of electroconvulsive therapy in Lance-Adams syndrome},
  author = {Vellieux, Geoffroy and Apartis, Emmanuelle and Degos, Vincent and Fossati, Philippe and Navarro, Vincent},
  year = {2023},
  doi = {10.5281/zenodo.7620808},
  howpublished = {Zenodo},
  note = {dataset}
}
@article{lance_adams_myoclonus_paper_2023,
  title = {Effectiveness of electroconvulsive therapy in Lance-Adams syndrome},
  author = {Vellieux, Geoffroy and Apartis, Emmanuelle and Degos, Vincent and Fossati, Philippe and Navarro, Vincent},
  year = {2023},
  doi = {10.1016/j.brs.2023.03.004},
  journal = {Brain Stimulation}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: lance_adams_myoclonus
- **family**: eeg
- **MoveAtlas cells**: A2; M5 (leg EMG), M6 (EEG)
- **population**: N=1 Lance-Adams syndrome case around ECT: EEG + lower-limb EMG polygraphy + jerk-locked back averaging + patient video
- **n_subjects**: 1
- **signal**: EEG-EMG polygraphy (~10.5 MB)
- **license**: CC BY 4.0 (verified on page 2026-09-01); redistribution: yes
- **access**: Zenodo direct download
- **link**: https://zenodo.org/records/7620808
