# NINDS Common Data Elements, motor scales (machine-readable)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NINDS Common Data Elements, motor scales (machine-readable)",
 "description": "NINDS Common Data Elements, motor scales (machine-readable). MoveAtlas auxdata family. licence US public resource; MDS-UPDRS/UHDRS full text remain MDS/HSG.",
 "identifier": "https://commondataelements.ninds.nih.gov/",
 "license": "US public resource; MDS-UPDRS/UHDRS full text remain MDS/HSG copyright",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "M12 Clinical scales"
 ],
 "url": "https://commondataelements.ninds.nih.gov/",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>clinical_scales</code>

<span class="ma-tag">Clinical scales</span>

| | |
|---|---|
| **Taxonomy cells** | M12 |
| **Subjects** | n/a |
| **Status** | NEW 2026-08-22 (second hunt): queued |
| **License** | US public resource; MDS-UPDRS/UHDRS full text remain MDS/HSG copyright |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("clinical_scales")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: US public resource; MDS-UPDRS/UHDRS full text remain MDS/HSG copyright
- **Redistribution**: no, DECIDED 2026-08-28: the copyrighted scale wording contaminates any bulk copy; pointer to NINDS
- **Access route**: direct_download (tower queue)
- **Source**: <https://commondataelements.ninds.nih.gov/>

## Publications

- Grinnon, Stacie T; Miller, Kristy; Marler, John R; Lu, Yun; Stout, Alexandra; Odenkirchen, Joanne; Kunitz, Selma (2012). *National Institute of Neurological Disorders and Stroke Common Data Element Project – approach and methods*. Clinical Trials. DOI: [10.1177/1740774512438980](https://doi.org/10.1177/1740774512438980)

```bibtex
@article{clinical_scales_paper_2012,
  title = {National Institute of Neurological Disorders and Stroke Common Data Element Project – approach and methods},
  author = {Grinnon, Stacie T and Miller, Kristy and Marler, John R and Lu, Yun and Stout, Alexandra and Odenkirchen, Joanne and Kunitz, Selma},
  year = {2012},
  doi = {10.1177/1740774512438980},
  journal = {Clinical Trials}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: clinical_scales
- family: auxdata  (physical path: datasets/auxdata/clinical_scales)
- MoveAtlas cells: M12
- population: n/a (metadata resource: PD / HD / Friedreich CRF modules)
- n_subjects: n/a
- signal: CDE catalog Excel/Word exports of motor assessment item structures
- license: US public resource; MDS-UPDRS/UHDRS full text remain MDS/HSG copyright ; redistribution: no, DECIDED 2026-08-28: the copyrighted scale wording contaminates any bulk copy; pointer to NINDS
- access: direct_download (tower queue)
- status (2026-08-22): NEW 2026-08-22 (second hunt): queued
- link: https://commondataelements.ninds.nih.gov/
- notes: label-ontology substrate for M12 harmonization (WBS 1.5)
