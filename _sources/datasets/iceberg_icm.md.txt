# ICEBERG cohort (Paris ICM: PSG + gait + eye movement + speech in early PD/iRBD)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ICEBERG cohort (Paris ICM: PSG + gait + eye movement + speech in early PD/iRBD)",
 "description": "ICEBERG cohort (Paris ICM: PSG + gait + eye movement + speech in early PD/iRBD). MoveAtlas imu family. licence 'available upon reasonable request from any qualified invest.",
 "identifier": "https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization",
 "license": "'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B4 Akinesia",
  "M2 Inertial (IMU)",
  "M6 EEG"
 ],
 "url": "https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>iceberg_icm</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4 prodromal; M2 M6 |
| **Subjects** | ~300 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (reasonable-request tier): multi-signal early-PD/iRBD cohort incl. oculomotor and speech; no self-serve route exists - the availability-statement barrier at cohort scale |
| **License** | 'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("iceberg_icm")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: 'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal
- **Redistribution**: no
- **Access route**: ICM / NCT02305147
- **Source**: <https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://parisbraininstitute.org/news/iceberg-cohort-10-years-collective-scientific-and-medical-mobilization
- License / access regime: 'available upon reasonable request from any qualified investigator' (papers' statements); sponsor-controlled, no portal
- Access route: ICM / NCT02305147
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (reasonable-request tier): multi-signal early-PD/iRBD cohort incl. oculomotor and speech; no self-serve route exists - the availability-statement barrier at cohort scale
- Number of subjects: ~300
- MoveAtlas cells: B1-B4 prodromal; M2 M6

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
