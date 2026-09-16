# UCI Parkinson spiral drawings on digitized tablet (Isenkul)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "UCI Parkinson spiral drawings on digitized tablet (Isenkul)",
 "description": "UCI Parkinson spiral drawings on digitized tablet (Isenkul). MoveAtlas auxdata family. 77 subjects. licence open.",
 "identifier": "https://archive.ics.uci.edu/ml/datasets/Parkinson+Disease+Spiral+Drawings+Using+Digitized+Graphics+tablet",
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
 "url": "https://archive.ics.uci.edu/ml/datasets/Parkinson+Disease+Spiral+Drawings+Using+Digitized+Graphics+tablet",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>uci_spiral_isenkul</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Voice / writing</span>

| | |
|---|---|
| **Taxonomy cells** | B2 proxy (spiral drawing); M11 |
| **Subjects** | 77 |
| **Status** | catalogued (2026-09-05) |
| **License** | open (UCI; CC BY 4.0 on the new portal - verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("uci_spiral_isenkul")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open (UCI; CC BY 4.0 on the new portal - verify at fetch)
- **Redistribution**: unknown
- **Access route**: archive.ics.uci.edu
- **Source**: <https://archive.ics.uci.edu/ml/datasets/Parkinson+Disease+Spiral+Drawings+Using+Digitized+Graphics+tablet>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B2 proxy (spiral drawing); M11
