# TUH EEG Corpus (Temple University)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "TUH EEG Corpus (Temple University)",
 "description": "TUH EEG Corpus (Temple University). MoveAtlas eeg family. licence free with signed usage agreement.",
 "identifier": "https://isip.piconepress.com/projects/nedc/",
 "license": "free with signed usage agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "M6 EEG",
  "D1 Epilepsy",
  "A2 Myoclonus"
 ],
 "url": "https://isip.piconepress.com/projects/nedc/",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>tuh_eeg</code>

<span class="ma-tag">EEG</span><span class="ma-tag">Epilepsy</span><span class="ma-tag">Myoclonus</span>

| | |
|---|---|
| **Taxonomy cells** | M6 socle; D1; A2 (myoclonic events) |
| **Subjects** | very large |
| **Status** | documented access barrier |
| **License** | free with signed usage agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("tuh_eeg")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: free with signed usage agreement
- **Redistribution**: no
- **Access route**: registration + signed form, then download (plan TB-scale storage)
- **Source**: <https://isip.piconepress.com/projects/nedc/>

## Publications

- Obeid, Iyad; Picone, Joseph (2016). *The Temple University Hospital EEG Data Corpus*. Frontiers in Neuroscience. DOI: [10.3389/fnins.2016.00196](https://doi.org/10.3389/fnins.2016.00196)

```bibtex
@article{tuh_eeg_paper_2016,
  title = {The Temple University Hospital EEG Data Corpus},
  author = {Obeid, Iyad and Picone, Joseph},
  year = {2016},
  doi = {10.3389/fnins.2016.00196},
  journal = {Frontiers in Neuroscience}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: tuh_eeg
- **family**: eeg
- **MoveAtlas cells**: M6 socle; D1; A2 (myoclonic events)
- **population**: hospital clinical corpus, >10,000 sessions
- **n_subjects**: very large
- **signal**: clinical EEG, many montages (EDF)
- **license**: free with signed usage agreement; redistribution: no (redistribution prohibited)
- **access**: registration + signed form, then download (plan TB-scale storage)
- **link**: https://isip.piconepress.com/projects/nedc/
