# NINDS PDBP Data Management Resource

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NINDS PDBP Data Management Resource",
 "description": "NINDS PDBP Data Management Resource. MoveAtlas bio family. licence account + Data Access Request.",
 "identifier": "https://pdbp.ninds.nih.gov/",
 "license": "account + Data Access Request",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "B1 Rigidity",
  "B2 Bradykinesia",
  "A1 Tremor",
  "M8 Imaging",
  "M9 Genetics",
  "M12 Clinical scales"
 ],
 "url": "https://pdbp.ninds.nih.gov/",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>pdbp</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Tremor</span><span class="ma-tag">Imaging</span><span class="ma-tag">Genetics</span><span class="ma-tag">Clinical scales</span>

| | |
|---|---|
| **Taxonomy cells** | B1, B2, A1; M8, M9, M12 |
| **Subjects** | ~4,298 |
| **Status** | DOCUMENTED BARRIER (owner, 2026-08-28): the publication focuses on genuinely open data; the application is not pursued. Procedure kept as evidence: NIH RAS login (Login.gov or ID.me) required before the portal, then account request + signed Data Use Certificate + DAC review; site banner notes the re... |
| **License** | account + Data Access Request |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pdbp")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: account + Data Access Request
- **Redistribution**: no
- **Access route**: application
- **Source**: <https://pdbp.ninds.nih.gov/>

## Publications

- Rosenthal, Liana S.; Drake, Daniel; Alcalay, Roy N.; Babcock, Debra; Bowman, F. DuBois; Chen‐Plotkin, Alice; Dawson, Ted M.; Dewey, Richard B.; German, Dwight C.; Huang, Xuemei; Landin, Barry; McAuliffe, Matthew; Petyuk, Vladislav A.; Scherzer, Clemens R.; Hillaire‐Clarke, Coryse St.; Sieber, Beth‐A (2016). *The NINDS Parkinson's disease biomarkers program*. Movement Disorders. DOI: [10.1002/mds.26438](https://doi.org/10.1002/mds.26438)

```bibtex
@article{pdbp_paper_2016,
  title = {The NINDS Parkinson's disease biomarkers program},
  author = {Rosenthal, Liana S. and Drake, Daniel and Alcalay, Roy N. and Babcock, Debra and Bowman, F. DuBois and Chen‐Plotkin, Alice and Dawson, Ted M. and Dewey, Richard B. and German, Dwight C. and Huang, Xuemei and Landin, Barry and McAuliffe, Matthew and Petyuk, Vladislav A. and Scherzer, Clemens R. and Hillaire‐Clarke, Coryse St. and Sieber, Beth‐Anne and Sutherland, Margaret and Tarn, Chi and West, Andrew and Vaillancourt, David and Zhang, Jing and Gwinn, Katrina},
  year = {2016},
  doi = {10.1002/mds.26438},
  journal = {Movement Disorders}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: pdbp
- family: bio  (physical path: datasets/bio/pdbp)
- MoveAtlas cells: B1, B2, A1; M8, M9, M12
- population: ~4,298 participants (AMP-linked), PD/LBD deep phenotyping: clinical, genetic, imaging, biomarkers
- n_subjects: ~4,298
- signal: query portal with join/filter
- license: account + Data Access Request ; redistribution: no
- access: application
- status (2026-08-22): DOCUMENTED BARRIER (owner, 2026-08-28): the publication focuses on genuinely open data; the application is not pursued. Procedure kept as evidence: NIH RAS login (Login.gov or ID.me) required before the portal, then account request + signed Data Use Certificate + DAC review; site banner notes the repository is under administrative review; embargo rules on recent data
- link: https://pdbp.ninds.nih.gov/
