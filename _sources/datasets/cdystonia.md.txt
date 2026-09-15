# cdystonia (TWSTRS trial scores, hbiostat)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "cdystonia (TWSTRS trial scores, hbiostat)",
 "description": "cdystonia (TWSTRS trial scores, hbiostat). MoveAtlas auxdata family. 109 subjects. licence free.",
 "identifier": "https://hbiostat.org/data/repo/cdystonia.html",
 "license": "free (hbiostat teaching repo)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A4 Dystonia",
  "M12 Clinical scales"
 ],
 "url": "https://hbiostat.org/data/repo/cdystonia.html",
 "isAccessibleForFree": true,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cdystonia</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Clinical scales</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M12 |
| **Subjects** | 109 |
| **Status** | DOWNLOADED 2026-08-22: cdystonia.sav, 4.4 KB. The .csv the registry pointed at is gone from hbiostat (404). CORRECTED 2026-08-28: despite the .sav extension this is NOT SPSS; it is a gzip-compressed R save file (RDX2 magic once decompressed), read in one line with pyreadr.read_r. 631 rows, 109 patie... |
| **License** | free (hbiostat teaching repo) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cdystonia")
records, meta = ds.get_data()
```

## License and access

- **License**: free (hbiostat teaching repo)
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only cdystonia, tower)
- **Source**: <https://hbiostat.org/data/repo/cdystonia.html>

## Publications

- Davis, Charles S. (2002). *Statistical Methods for the Analysis of Repeated Measurements*. Springer Texts in Statistics. DOI: [10.1007/b97287](https://doi.org/10.1007/b97287)

```bibtex
@article{cdystonia_paper_2002,
  title = {Statistical Methods for the Analysis of Repeated Measurements},
  author = {Davis, Charles S.},
  year = {2002},
  doi = {10.1007/b97287},
  journal = {Springer Texts in Statistics}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: cdystonia
- family: auxdata  (physical path: datasets/auxdata/cdystonia)
- MoveAtlas cells: A4; M12
- population: 109 cervical dystonia patients (botulinum-toxin RCT)
- n_subjects: 109
- signal: longitudinal TWSTRS score table (CSV)
- license: free (hbiostat teaching repo) ; redistribution: yes
- access: direct_download (fetch_p2_lot.py --only cdystonia, tower)
- status (2026-08-22): DOWNLOADED 2026-08-22: cdystonia.sav, 4.4 KB. The .csv the registry pointed at is gone from hbiostat (404). CORRECTED 2026-08-28: despite the .sav extension this is NOT SPSS; it is a gzip-compressed R save file (RDX2 magic once decompressed), read in one line with pyreadr.read_r. 631 rows, 109 patients across 9 sites, TWSTRS over 16 weeks, three arms. Aux table, no canonical ingestion
- link: https://hbiostat.org/data/repo/cdystonia.html
- notes: scale-harmonization aux (WBS 1.5 / M12)
