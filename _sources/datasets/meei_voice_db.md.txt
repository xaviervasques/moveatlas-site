# MEEI / KayPENTAX disordered voice database (Model 4337)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MEEI / KayPENTAX disordered voice database (Model 4337)",
 "description": "MEEI / KayPENTAX disordered voice database (Model 4337). MoveAtlas auxdata family. licence COMMERCIAL: paid purchase licence from PENTAX Medical.",
 "identifier": "https://www.pentaxmedical.com/",
 "license": "COMMERCIAL: paid purchase licence from PENTAX Medical",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A1 Tremor",
  "M8 Imaging"
 ],
 "url": "https://www.pentaxmedical.com/",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>meei_voice_db</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A1 laryngeal context; M8 |
| **Subjects** | ~700 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | COMMERCIAL: paid purchase licence from PENTAX Medical |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("meei_voice_db")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: COMMERCIAL: paid purchase licence from PENTAX Medical
- **Redistribution**: no
- **Access route**: PENTAX Medical product
- **Source**: <https://www.pentaxmedical.com/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A1 laryngeal context; M8
