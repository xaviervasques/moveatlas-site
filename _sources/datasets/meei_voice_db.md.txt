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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER - the PAID-PRODUCT access model (with ukb_accelerometry's fee tier, completes the commercial corner of the taxonomy): ~1400 samples incl. confirmed adductor SD |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata' (speech-motor signal)
- Source / URL: https://www.pentaxmedical.com/
- License / access: COMMERCIAL: paid purchase licence from PENTAX Medical
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER - the PAID-PRODUCT access model (with ukb_accelerometry's fee tier, completes the commercial corner of the taxonomy): ~1400 samples incl. confirmed adductor SD
- MoveAtlas cells: A1 laryngeal context; M8

### Retrieval notes
RE-VERIFY at fetch/request; no-emails policy for gated tiers.

### Processing
None. Catalogue-tier.
