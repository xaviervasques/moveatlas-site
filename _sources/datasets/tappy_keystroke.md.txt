# Tappy keystroke (PhysioNet)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Tappy keystroke (PhysioNet)",
 "description": "Tappy keystroke (PhysioNet). MoveAtlas auxdata family. 227 users subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/tappy/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "B2 Bradykinesia",
  "M11 Voice / writing"
 ],
 "url": "https://physionet.org/content/tappy/",
 "isAccessibleForFree": true,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Adams, Warwick"
  }
 ]
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>tappy_keystroke</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | B2 proxy; M11 |
| **Subjects** | 227 users |
| **Status** | acquired |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("tappy_keystroke")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/tappy/>

## Publications

- Adams, Warwick (2017). *Tappy Keystroke Data*. physionet.org. DOI: [10.13026/c2k08d](https://doi.org/10.13026/c2k08d)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{tappy_keystroke_data_2017,
  title = {Tappy Keystroke Data},
  author = {Adams, Warwick},
  year = {2017},
  doi = {10.13026/c2k08d},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{tappy_keystroke_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: tappy_keystroke
- **family**: auxdata
- **MoveAtlas cells**: B2 proxy; M11
- **population**: PD + controls, home typing
- **n_subjects**: 227 users
- **signal**: keystroke logs (User_*.txt)
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://physionet.org/content/tappy/
