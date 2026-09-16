# UCI Parkinson's voice

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "UCI Parkinson's voice",
 "description": "UCI Parkinson's voice. MoveAtlas auxdata family. 31 (195 recordings) subjects. licence CC BY 4.0.",
 "identifier": "https://archive.ics.uci.edu/dataset/174/parkinsons",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "B2 Bradykinesia",
  "M11 Voice / writing"
 ],
 "url": "https://archive.ics.uci.edu/dataset/174/parkinsons",
 "isAccessibleForFree": true,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Little, Max"
  }
 ]
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>uci_parkinson_voix</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | B2 proxy (hypokinetic dysarthria); M11 |
| **Subjects** | 31 (195 recordings) |
| **Status** | acquired |
| **License** | CC BY 4.0 (stated on the UCI repository page, read 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("uci_parkinson_voix")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (stated on the UCI repository page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://archive.ics.uci.edu/dataset/174/parkinsons>

## Publications

- Little, Max (2007). *Parkinsons*. UCI Machine Learning Repository. DOI: [10.24432/c59c74](https://doi.org/10.24432/c59c74)

```bibtex
@misc{uci_parkinson_voix_data_2007,
  title = {Parkinsons},
  author = {Little, Max},
  year = {2007},
  doi = {10.24432/c59c74},
  howpublished = {UCI Machine Learning Repository},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: uci_parkinson_voix
- **family**: auxdata
- **MoveAtlas cells**: B2 proxy (hypokinetic dysarthria); M11
- **population**: PD + controls, sustained phonation
- **n_subjects**: 31 (195 recordings)
- **signal**: voice feature table
- **license**: CC BY 4.0 (stated on the UCI repository page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://archive.ics.uci.edu/dataset/174/parkinsons
