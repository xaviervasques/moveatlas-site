# MDSGene (genotype-phenotype knowledge base)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MDSGene (genotype-phenotype knowledge base)",
 "description": "MDSGene (genotype-phenotype knowledge base). MoveAtlas bio family. 23,830 (literature) subjects. licence personal/educational/research only; commercial needs MDS per.",
 "identifier": "https://www.mdsgene.org/",
 "license": "personal/educational/research only; commercial needs MDS permission",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M9 Genetics"
 ],
 "url": "https://www.mdsgene.org/",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mdsgene</code>

<span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | M9 |
| **Subjects** | 23,830 (literature) |
| **Status** | NEW 2026-08-22 (second hunt): reference resource, NOT ingestible; cite and hand-extract at need |
| **License** | personal/educational/research only; commercial needs MDS permission |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mdsgene")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: personal/educational/research only; commercial needs MDS permission
- **Redistribution**: NO
- **Access route**: browse only
- **Source**: <https://www.mdsgene.org/>

## Publications

- Lill, Christina M.; Mashychev, Andriy; Hartmann, Corinna; Lohmann, Katja; Marras, Connie; Lang, Anthony E.; Klein, Christine; Bertram, Lars (2016). *Launching the movement disorders society genetic mutation database (MDSGene)*. Movement Disorders. DOI: [10.1002/mds.26651](https://doi.org/10.1002/mds.26651)

```bibtex
@article{mdsgene_paper_2016,
  title = {Launching the movement disorders society genetic mutation database (MDSGene)},
  author = {Lill, Christina M. and Mashychev, Andriy and Hartmann, Corinna and Lohmann, Katja and Marras, Connie and Lang, Anthony E. and Klein, Christine and Bertram, Lars},
  year = {2016},
  doi = {10.1002/mds.26651},
  journal = {Movement Disorders}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: mdsgene
- family: bio  (physical path: datasets/bio/mdsgene)
- MoveAtlas cells: M9
- population: 2,695 causative variants, 23,830 literature patients, movement-disorder genes incl. new Ataxia Resource (548 genes)
- n_subjects: 23,830 (literature)
- signal: curated genotype-phenotype summaries (web only, no bulk export)
- license: personal/educational/research only; commercial needs MDS permission ; redistribution: NO
- access: browse only
- status (2026-08-22): NEW 2026-08-22 (second hunt): reference resource, NOT ingestible; cite and hand-extract at need
- link: https://www.mdsgene.org/
