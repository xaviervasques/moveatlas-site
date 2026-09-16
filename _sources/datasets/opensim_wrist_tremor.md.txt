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
  "A1 Tremor",
  "B2 Bradykinesia",
  "M2 Inertial (IMU)",
  "M5 EMG"
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

<span class="ma-tag">Tremor</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | A1; B2 context; M2 M5 |
| **Subjects** | 5 |
| **Status** | catalogued (2026-09-05) |
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A1; B2 context; M2 M5
