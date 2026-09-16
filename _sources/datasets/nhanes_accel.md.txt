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

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>nhanes_accel</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3 (age-conditioned normative); M2 |
| **Subjects** | thousands |
| **Status** | acquired (2026-08-26) |
| **License** | US public domain |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nhanes_accel")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: US public domain
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only nhanes_accel; exact CDC URLs in registry)
- **Source**: <https://wwwn.cdc.gov/nchs/nhanes/>

## Publications

-  (). **. .

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: nhanes_accel
- **family**: imu
- **MoveAtlas cells**: C1, C3 (age-conditioned normative); M2
- **population**: US general population incl. children and 80+; age via DEMO_G demographics
- **n_subjects**: thousands
- **signal**: wrist accelerometry: PAXHD/PAXDAY/PAXHR summaries (+ PAXMIN 7.6 GB, PAX80 raw 80 Hz as deliberate extras)
- **license**: US public domain; redistribution: yes
- **access**: direct_download (fetch_p2_lot.py --only nhanes_accel; exact CDC URLs in registry)
- **link**: https://wwwn.cdc.gov/nchs/nhanes/
