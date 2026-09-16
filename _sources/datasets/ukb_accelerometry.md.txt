# UK Biobank 7-day wrist accelerometry (PD cases within)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "UK Biobank 7-day wrist accelerometry (PD cases within)",
 "description": "UK Biobank 7-day wrist accelerometry (PD cases within). MoveAtlas imu family. licence bona-fide researcher + institutional MTA + tiered 3-year fee.",
 "identifier": "https://www.ukbiobank.ac.uk/use-our-data/fees/",
 "license": "bona-fide researcher + institutional MTA + tiered 3-year fee (~GBP 9000 standard UK tier, GBP 500 student) + Research An",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "C1 Normal adult movement",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://www.ukbiobank.ac.uk/use-our-data/fees/",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>ukb_accelerometry</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 context; C1 C3; M2 |
| **Subjects** | ~103000 total |
| **Status** | documented access barrier (2026-09-05) |
| **License** | bona-fide researcher + institutional MTA + tiered 3-year fee (~GBP 9000 standard UK tier, GBP 500 student) + Research Analysis Platform compute at user expense; ~15 weeks to release |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ukb_accelerometry")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: bona-fide researcher + institutional MTA + tiered 3-year fee (~GBP 9000 standard UK tier, GBP 500 student) + Research Analysis Platform compute at user expense; ~15 weeks to release
- **Redistribution**: no
- **Access route**: ukbiobank.ac.uk (AMS)
- **Source**: <https://www.ukbiobank.ac.uk/use-our-data/fees/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4 context; C1 C3; M2
