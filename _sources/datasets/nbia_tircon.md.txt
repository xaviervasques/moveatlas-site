# TIRCON international NBIA/PKAN registry (LMU Munich)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "TIRCON international NBIA/PKAN registry (LMU Munich)",
 "description": "TIRCON international NBIA/PKAN registry (LMU Munich). MoveAtlas auxdata family. 700+ subjects. licence researcher application to the registry.",
 "identifier": "https://clinicaltrials.gov/study/NCT05522374",
 "license": "researcher application to the registry (contact at LMU); clinical/natural-history scales, no signal",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A4 Dystonia",
  "M9 Genetics"
 ],
 "url": "https://clinicaltrials.gov/study/NCT05522374",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>nbia_tircon</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | A4 genetic context; M9 |
| **Subjects** | 700+ |
| **Status** | documented access barrier (2026-09-05) |
| **License** | researcher application to the registry (contact at LMU); clinical/natural-history scales, no signal |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nbia_tircon")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: researcher application to the registry (contact at LMU); clinical/natural-history scales, no signal
- **Redistribution**: no
- **Access route**: nbiaalliance.org + NCT05522374
- **Source**: <https://clinicaltrials.gov/study/NCT05522374>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A4 genetic context; M9
