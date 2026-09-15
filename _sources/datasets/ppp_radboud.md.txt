# Personalized Parkinson Project (Radboud; Verily watch 2-3 y)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Personalized Parkinson Project (Radboud; Verily watch 2-3 y)",
 "description": "Personalized Parkinson Project (Radboud; Verily watch 2-3 y). MoveAtlas imu family. 520 subjects. licence committee proposal.",
 "identifier": "https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3",
 "license": "https://opensource.org/license/mit",
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
 "url": "https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>ppp_radboud</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4; M2 |
| **Subjects** | 520 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (enclave family, with the AIHub pair): ~23 h/day watch signal for 2-3 years x 520 early-PD - among the densest wearable corpora anywhere, reachable only inside PEP/Workbench. Watch the Workbench rollout |
| **License** | committee proposal (RDSRC) + PEP polymorphic-encryption enclave; 2025: migrating to Verily Workbench as 'public resource' (enclave-style), rollout in progress |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ppp_radboud")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: committee proposal (RDSRC) + PEP polymorphic-encryption enclave; 2025: migrating to Verily Workbench as 'public resource' (enclave-style), rollout in progress
- **Redistribution**: no
- **Access route**: radboud PPP (NCT sisters 04985539/05501431)
- **Source**: <https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://bmcneurol.biomedcentral.com/articles/10.1186/s12883-019-1394-3
- License / access regime: committee proposal (RDSRC) + PEP polymorphic-encryption enclave; 2025: migrating to Verily Workbench as 'public resource' (enclave-style), rollout in progress
- Access route: radboud PPP (NCT sisters 04985539/05501431)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (enclave family, with the AIHub pair): ~23 h/day watch signal for 2-3 years x 520 early-PD - among the densest wearable corpora anywhere, reachable only inside PEP/Workbench. Watch the Workbench rollout
- Number of subjects: 520
- MoveAtlas cells: B1-B4; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
