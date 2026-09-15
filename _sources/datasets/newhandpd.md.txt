# NewHandPD / HandPD: smart-pen signals + spiral/meander images (UNESP)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NewHandPD / HandPD: smart-pen signals + spiral/meander images (UNESP)",
 "description": "NewHandPD / HandPD: smart-pen signals + spiral/meander images (UNESP). MoveAtlas auxdata family. 92 subjects. licence open direct download.",
 "identifier": "https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/",
 "license": "open direct download, NO formal licence stated on the page (cite Pereira et al.) - the no-licence trap, adjudicate befor",
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
 "url": "https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>newhandpd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | B1 B2; M8 |
| **Subjects** | 92 |
| **Status** | CATALOGUED 2026-09-05: 74 PD + 18 HC, 736 spiral+meander images AND 6-sensor BiSP smart-pen time signals - the only fully open online-signal handwriting set; goodwin_smm-style licence adjudication needed |
| **License** | open direct download, NO formal licence stated on the page (cite Pereira et al.) - the no-licence trap, adjudicate before redistribution |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("newhandpd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open direct download, NO formal licence stated on the page (cite Pereira et al.) - the no-licence trap, adjudicate before redistribution
- **Redistribution**: unknown
- **Access route**: wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/
- **Source**: <https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata'
- Source / URL: https://wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/
- License / access: open direct download, NO formal licence stated on the page (cite Pereira et al.) - the no-licence trap, adjudicate before redistribution
- Access route: wwwp.fc.unesp.br/~papa/pub/datasets/Handpd/
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: 74 PD + 18 HC, 736 spiral+meander images AND 6-sensor BiSP smart-pen time signals - the only fully open online-signal handwriting set; goodwin_smm-style licence adjudication needed
- Number of subjects: 92
- MoveAtlas cells: B1 B2; M8

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
