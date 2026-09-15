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
| **Status** | CATALOGUED 2026-09-05 (owner request): NOT a signal dataset - a living registry of clinician-reported DBS outcomes in 58 monogenic movement disorders (GNAO1, KMT2B, PANK2, ADCY5, SGCE...), 41 clinicians / 20 countries / 158 cases, 3-point outcome scale, 84.6% strong-or-moderate benefit among rated e... |
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

## Data card (verbatim, with its evidence trail)


- Modality: none - no signal, no downloadable records. A web
  matchmaking platform: clinicians submit gene + DBS target
  (+ optional 3-point outcome) and get connected to peers who
  treated the same gene.
- Source / URL: https://doi.org/10.1002/mds.70180 (first-year
  report, Movement Disorders 2026); founding paper def-lab.org
  (Zubair et al. 2025); trial NCT06912841. Launched 2024-12.
- License: n/a (no data distributed; entries deliberately minimal
  and non-identifiable)
- Access: the platform itself is freely accessible; the CASES are
  reachable only through the matchmaking workflow - data does not
  move, connections do.
- Version / retrieval date: catalogued 2026-09-05 (owner request,
  session web check of the two papers + trial page)
- Status (2026-09-05): CATALOGUED, knowledge-lane only. First-year
  figures: 41 clinicians / 39 institutions / 20 countries, 158
  unique cases across 58 monogenic movement disorders (GNAO1,
  KMT2B, PANK2, ADCY5, SGCE most common), 84.6% strong-or-moderate
  benefit among outcome-rated entries.
- Why this card exists despite the no-signal rule: (a) it completes
  the aux knowledge lane (mdsgene/hpo family: gene -> DBS target ->
  outcome); (b) its MATCHMAKING access model is a distinct entry in
  the barriers/access taxonomy - a living repository that lowers
  sharing barriers by moving connections instead of bytes. Candidate
  paragraph for the access-models discussion in the paper.

### Retrieval notes
Nothing to retrieve. If aggregate tables are ever published as
supplements, they would be the fetchable artifact.

### Processing
None; never enters manifests (no records).
