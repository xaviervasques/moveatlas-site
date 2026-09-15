# PaHaW: PD handwriting online dynamics (Brno; Wacom x/y/pressure/altitude/azimuth)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PaHaW: PD handwriting online dynamics (Brno; Wacom x/y/pressure/altitude/azimuth)",
 "description": "PaHaW: PD handwriting online dynamics (Brno; Wacom x/y/pressure/altitude/azimuth). MoveAtlas auxdata family. 75 subjects. licence gated-lite: sign the licence agreement on the site and email.",
 "identifier": "http://bdalab.utko.feec.vutbr.cz/",
 "license": "gated-lite: sign the licence agreement on the site and email the Brno maintainers; free for research",
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
 "url": "http://bdalab.utko.feec.vutbr.cz/",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>pahaw</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | B1 B2; M8 |
| **Subjects** | 75 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (sign+email tier): 37 PD / 38 HC, 8 tasks, full online dynamics - the canonical PD handwriting set; request = owner decision (no-emails policy) |
| **License** | gated-lite: sign the licence agreement on the site and email the Brno maintainers; free for research |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pahaw")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: gated-lite: sign the licence agreement on the site and email the Brno maintainers; free for research
- **Redistribution**: no
- **Access route**: bdalab.utko.feec.vutbr.cz
- **Source**: <http://bdalab.utko.feec.vutbr.cz/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata'
- Source / URL: http://bdalab.utko.feec.vutbr.cz/
- License / access: gated-lite: sign the licence agreement on the site and email the Brno maintainers; free for research
- Access route: bdalab.utko.feec.vutbr.cz
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (sign+email tier): 37 PD / 38 HC, 8 tasks, full online dynamics - the canonical PD handwriting set; request = owner decision (no-emails policy)
- Number of subjects: 75
- MoveAtlas cells: B1 B2; M8

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
