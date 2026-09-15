# NHANES accelerometry (CDC, cycle G 2011-2012)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NHANES accelerometry (CDC, cycle G 2011-2012)",
 "description": "NHANES accelerometry (CDC, cycle G 2011-2012). MoveAtlas imu family. licence US public domain.",
 "identifier": "https://wwwn.cdc.gov/nchs/nhanes/",
 "license": "US public domain",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "C1 Normal adult movement",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://wwwn.cdc.gov/nchs/nhanes/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>nhanes_accel</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3 (age-conditioned normative); M2 |
| **Subjects** | thousands |
| **Status** | DOWNLOADED 2026-08-26: the 4 summary files (139 MB) AND PAXMIN_G.xpt (8.1 GB, sha256 logged; the CDC link needed three resumes across two days, mid-stream timeouts are its normal weather). PAX80 raw 80 Hz deliberately not pulled. Aux/bio lane, no canonical ingestion |
| **License** | US public domain |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nhanes_accel")
records, meta = ds.get_data()
```

## License and access

- **License**: US public domain
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only nhanes_accel; exact CDC URLs in registry)
- **Source**: <https://wwwn.cdc.gov/nchs/nhanes/>

## Publications

-  (). **. .

## Data card (verbatim, with its evidence trail)


- dataset: nhanes_accel
- family: imu  (physical path: datasets/imu/nhanes_accel)
- MoveAtlas cells: C1, C3 (age-conditioned normative); M2
- population: US general population incl. children and 80+; age via DEMO_G demographics
- n_subjects: thousands
- signal: wrist accelerometry: PAXHD/PAXDAY/PAXHR summaries (+ PAXMIN 7.6 GB, PAX80 raw 80 Hz as deliberate extras)
- license: US public domain ; redistribution: yes
- access: direct_download (fetch_p2_lot.py --only nhanes_accel; exact CDC URLs in registry)
- status (2026-08-22): DOWNLOADED 2026-08-26: the 4 summary files (139 MB) AND PAXMIN_G.xpt (8.1 GB, sha256 logged; the CDC link needed three resumes across two days, mid-stream timeouts are its normal weather). PAX80 raw 80 Hz deliberately not pulled. Aux/bio lane, no canonical ingestion
- link: https://wwwn.cdc.gov/nchs/nhanes/
- notes: population age-normativity at low cost; take only needed variables
