# OpenSim closed-loop wrist tremor model dataset (IEEE DataPort)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "OpenSim closed-loop wrist tremor model dataset (IEEE DataPort)",
 "description": "OpenSim closed-loop wrist tremor model dataset (IEEE DataPort). MoveAtlas emg family. 5 subjects. licence open access on IEEE DataPort.",
 "identifier": "https://ieee-dataport.org/keywords/tremor",
 "license": "open access on IEEE DataPort (licence on record, verify at fetch)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "emg",
  "A2 Myoclonus",
  "B1 Rigidity",
  "M2 Inertial (IMU)",
  "M4 Silhouette"
 ],
 "url": "https://ieee-dataport.org/keywords/tremor",
 "isAccessibleForFree": false,
 "measurementTechnique": "emg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-emg">emg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>opensim_wrist_tremor</code>

<span class="ma-tag">Myoclonus</span><span class="ma-tag">Rigidity</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | A2 B1; M2 M4 |
| **Subjects** | 5 |
| **Status** | CATALOGUED 2026-09-05: 4 PD + 1 ET, IMU + sEMG of pathological wrist tremor for a closed-loop OpenSim model - small but genuine pathological-tremor EMG (rare). NOTE the same pass VETTED AND REJECTED the 2025 'Tremor dataset' (Chatterjee): 10.66 KB promotional xlsx, subscription-only, no raw signal |
| **License** | open access on IEEE DataPort (licence on record, verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("opensim_wrist_tremor")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open access on IEEE DataPort (licence on record, verify at fetch)
- **Redistribution**: unknown
- **Access route**: ieee-dataport
- **Source**: <https://ieee-dataport.org/keywords/tremor>

## Data card (verbatim, with its evidence trail)


- Modality: family 'emg'
- Source / URL: https://ieee-dataport.org/keywords/tremor
- License / access: open access on IEEE DataPort (licence on record, verify at fetch)
- Access route: ieee-dataport
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: 4 PD + 1 ET, IMU + sEMG of pathological wrist tremor for a closed-loop OpenSim model - small but genuine pathological-tremor EMG (rare). NOTE the same pass VETTED AND REJECTED the 2025 'Tremor dataset' (Chatterjee): 10.66 KB promotional xlsx, subscription-only, no raw signal
- Number of subjects: 5
- MoveAtlas cells: A2 B1; M2 M4

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
