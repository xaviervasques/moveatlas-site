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
| **Status** | documented access barrier (2026-09-05) |
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1 B2; M8
