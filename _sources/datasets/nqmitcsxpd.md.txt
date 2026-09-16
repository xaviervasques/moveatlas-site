# neuroQWERTY MIT-CSXPD (keystroke)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "neuroQWERTY MIT-CSXPD (keystroke)",
 "description": "neuroQWERTY MIT-CSXPD (keystroke). MoveAtlas auxdata family. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/nqmitcsxpd/",
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
 "url": "https://physionet.org/content/nqmitcsxpd/",
 "isAccessibleForFree": true,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Giancardo, Luca"
  }
 ]
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>nqmitcsxpd</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | B2 proxy; M11 |
| **Subjects** | ~85 published; on-disk count TBD |
| **Status** | acquired |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nqmitcsxpd")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/nqmitcsxpd/>

## Publications

- Giancardo, Luca (2022). *neuroQWERTY MIT-CSXPD Dataset*. PhysioNet. DOI: [10.13026/c2859q](https://doi.org/10.13026/c2859q)
- Giancardo, L.; Sánchez-Ferro, A.; Arroyo-Gallego, T.; Butterworth, I.; Mendoza, C. S.; Montero, P.; Matarazzo, M.; Obeso, J. A.; Gray, M. L.; Estépar, R. San José (2016). *Computer keyboard interaction as an indicator of early Parkinson’s disease*. Scientific Reports. DOI: [10.1038/srep34468](https://doi.org/10.1038/srep34468)

```bibtex
@misc{nqmitcsxpd_data_2022,
  title = {neuroQWERTY MIT-CSXPD Dataset},
  author = {Giancardo, Luca},
  year = {2022},
  doi = {10.13026/c2859q},
  howpublished = {PhysioNet},
  note = {dataset}
}
@article{nqmitcsxpd_paper_2016,
  title = {Computer keyboard interaction as an indicator of early Parkinson’s disease},
  author = {Giancardo, L. and Sánchez-Ferro, A. and Arroyo-Gallego, T. and Butterworth, I. and Mendoza, C. S. and Montero, P. and Matarazzo, M. and Obeso, J. A. and Gray, M. L. and Estépar, R. San José},
  year = {2016},
  doi = {10.1038/srep34468},
  journal = {Scientific Reports}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: nqmitcsxpd
- **family**: auxdata
- **MoveAtlas cells**: B2 proxy; M11
- **population**: PD + controls, natural typing
- **n_subjects**: ~85 published; on-disk count TBD
- **signal**: keystroke hold/flight time series (CSV)
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://physionet.org/content/nqmitcsxpd/
