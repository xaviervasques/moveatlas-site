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
  "B1 Rigidity",
  "B2 Bradykinesia",
  "M8 Imaging"
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

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | B1 B2; M8 |
| **Subjects** | 77 |
| **Status** | CATALOGUED 2026-09-05: static + dynamic spiral tests on a graphics tablet - DISTINCT from our kaggle_spiral (images): this one has tablet dynamics |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata'
- Source / URL: https://archive.ics.uci.edu/ml/datasets/Parkinson+Disease+Spiral+Drawings+Using+Digitized+Graphics+tablet
- License / access: open (UCI; CC BY 4.0 on the new portal - verify at fetch)
- Access route: archive.ics.uci.edu
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: static + dynamic spiral tests on a graphics tablet - DISTINCT from our kaggle_spiral (images): this one has tablet dynamics
- Number of subjects: 77
- MoveAtlas cells: B1 B2; M8

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
