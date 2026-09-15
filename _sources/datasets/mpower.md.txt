# mPower v1: smartphone PD study (Sage/Synapse)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "mPower v1: smartphone PD study (Sage/Synapse)",
 "description": "mPower v1: smartphone PD study (Sage/Synapse). MoveAtlas imu family. 3101 walk / 8003 tap / 5826 voice participants subjects. licence qualified-researcher tier.",
 "identifier": "https://www.synapse.org/mpower",
 "license": "qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + cond",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B1 Rigidity",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)",
  "M8 Imaging"
 ],
 "url": "https://www.synapse.org/mpower",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mpower</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B3; M2 M8 |
| **Subjects** | 3101 walk / 8003 tap / 5826 voice participants |
| **Status** | CATALOGUED 2026-09-05 (deep-dive): 35410 walking recordings (accel+gyro) / 78887 tapping / 65022 voice from the 2015 v1 cohort (~1087 self-reported PD). FETCHABLE VIA THE OWNER'S SYNAPSE ROUTE (weargait_pd precedent: token worked, no DUA prompt - mPower adds profile validation + IDU statement, days-... |
| **License** | qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + conditions of use (non-reidentification); free |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mpower")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + conditions of use (non-reidentification); free
- **Redistribution**: no (conditions of use)
- **Access route**: synapse syn4993293
- **Source**: <https://www.synapse.org/mpower>

## Data card (verbatim, with its evidence trail)


- Modality: family 'imu'
- Source / URL: https://www.synapse.org/mpower
- License / access regime: qualified-researcher tier (Synapse): validated profile + certified-user quiz + public Intended-Data-Use statement + conditions of use (non-reidentification); free
- Access route: synapse syn4993293
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): 35410 walking recordings (accel+gyro) / 78887 tapping / 65022 voice from the 2015 v1 cohort (~1087 self-reported PD). FETCHABLE VIA THE OWNER'S SYNAPSE ROUTE (weargait_pd precedent: token worked, no DUA prompt - mPower adds profile validation + IDU statement, days-to-weeks). mPower 2.0: never publicly released (explicit negative). OWNER QUEUE: complete the Synapse qualified tier, then fetch
- Number of subjects: 3101 walk / 8003 tap / 5826 voice participants
- MoveAtlas cells: B1-B3; M2 M8

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
