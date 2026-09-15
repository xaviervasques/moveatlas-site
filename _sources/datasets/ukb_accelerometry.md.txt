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

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 E; M2 |
| **Subjects** | ~103000 total |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (fee + MTA + enclave drift): raw 100 Hz AX3 for ~103k participants incl. several hundred PD cases (the prodromal-PD-7-years-before-diagnosis literature). The FEE-BARRIER exemplar for the taxonomy |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://www.ukbiobank.ac.uk/use-our-data/fees/
- License / access regime: bona-fide researcher + institutional MTA + tiered 3-year fee (~GBP 9000 standard UK tier, GBP 500 student) + Research Analysis Platform compute at user expense; ~15 weeks to release
- Access route: ukbiobank.ac.uk (AMS)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (fee + MTA + enclave drift): raw 100 Hz AX3 for ~103k participants incl. several hundred PD cases (the prodromal-PD-7-years-before-diagnosis literature). The FEE-BARRIER exemplar for the taxonomy
- Number of subjects: ~103000 total
- MoveAtlas cells: B1-B4 E; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
