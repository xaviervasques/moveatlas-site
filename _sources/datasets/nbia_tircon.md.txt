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
  "A1 Tremor",
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

<span class="ma-tag">Tremor</span><span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | A1 genetic context; M9 |
| **Subjects** | 700+ |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (application tier, Dystonia-Coalition family): 700+ entries / 12 countries of NBIA natural history - scales not signal; completes the rare-dystonia registry corner |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata'
- Source / URL: https://clinicaltrials.gov/study/NCT05522374
- License / access: researcher application to the registry (contact at LMU); clinical/natural-history scales, no signal
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  pediatric/genetic-rare pass); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (application tier, Dystonia-Coalition family): 700+ entries / 12 countries of NBIA natural history - scales not signal; completes the rare-dystonia registry corner
- MoveAtlas cells: A1 genetic context; M9

### Retrieval notes
RE-VERIFY at fetch. No-emails policy for application tiers.

### Processing
None. Catalogue-tier.
