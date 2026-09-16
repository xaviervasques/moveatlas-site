# DBSMatchMaker: clinician-matching registry for DBS in rare monogenic movement disorders

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "DBSMatchMaker: clinician-matching registry for DBS in rare monogenic movement disorders",
 "description": "DBSMatchMaker: clinician-matching registry for DBS in rare monogenic movement disorders. MoveAtlas auxdata family. 158 cases subjects. licence no data distribution: a matching platform.",
 "identifier": "https://doi.org/10.1002/mds.70180",
 "license": "no data distribution: a matching platform, deliberately minimal and non-identifiable (first-year report: Mov Disord 2026",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A1 Tremor",
  "A4 Dystonia",
  "A8 Ballismus",
  "M9 Genetics"
 ],
 "url": "https://doi.org/10.1002/mds.70180",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dbsmatchmaker</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Dystonia</span><span class="ma-tag">Ballismus</span><span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | A1 A4-A8 genetic context; M9 |
| **Subjects** | 158 cases |
| **Status** | catalogued (2026-09-05) |
| **License** | no data distribution: a matching platform, deliberately minimal and non-identifiable (first-year report: Mov Disord 2026, 10.1002/mds.70180) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dbsmatchmaker")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: no data distribution: a matching platform, deliberately minimal and non-identifiable (first-year report: Mov Disord 2026, 10.1002/mds.70180)
- **Redistribution**: no
- **Access route**: web platform (def-lab.org; NCT06912841) - matchmaking access model: clinicians connect, data does not move
- **Source**: <https://doi.org/10.1002/mds.70180>
