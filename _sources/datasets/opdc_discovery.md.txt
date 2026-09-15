# Oxford OPDC Discovery cohort wearable/smartphone substudies

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Oxford OPDC Discovery cohort wearable/smartphone substudies",
 "description": "Oxford OPDC Discovery cohort wearable/smartphone substudies. MoveAtlas imu family. licence ACCESS PROCESS SUSPENDED.",
 "identifier": "https://www.dpag.ox.ac.uk/opdc/research/external-collaborations",
 "license": "ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests ",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://www.dpag.ox.ac.uk/opdc/research/external-collaborations",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>opdc_discovery</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3 prodromal; M2 |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER - the most journal-worthy of the sweep: the access process itself is OFFLINE mid-governance-migration. A cohort can be temporarily unreachable for reasons of paperwork, not policy. Recheck ~2027 |
| **License** | ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests paused ~12 months while the cohort migrates to Oxford Brain Bank governance; afterwards: OBB panel + complexity-scaled fee |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("opdc_discovery")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests paused ~12 months while the cohort migrates to Oxford Brain Bank governance; afterwards: OBB panel + complexity-scaled fee
- **Redistribution**: no
- **Access route**: dpag.ox.ac.uk/opdc
- **Source**: <https://www.dpag.ox.ac.uk/opdc/research/external-collaborations>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://www.dpag.ox.ac.uk/opdc/research/external-collaborations
- License / access regime: ACCESS PROCESS SUSPENDED (verified 2026-09-05 on the DPAG external-collaborations page): formal biosample/data requests paused ~12 months while the cohort migrates to Oxford Brain Bank governance; afterwards: OBB panel + complexity-scaled fee
- Access route: dpag.ox.ac.uk/opdc
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER - the most journal-worthy of the sweep: the access process itself is OFFLINE mid-governance-migration. A cohort can be temporarily unreachable for reasons of paperwork, not policy. Recheck ~2027
- Number of subjects: see record
- MoveAtlas cells: B1-B3 prodromal; M2

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
