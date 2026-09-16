# PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults)",
 "description": "PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults). MoveAtlas eeg family. 59 subjects. licence CC BY 4.0.",
 "identifier": "https://physionet.org/content/multimodal-gait-dataset/1.0.0/",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)",
  "M3 Plantar force",
  "M5 EMG",
  "M6 EEG"
 ],
 "url": "https://physionet.org/content/multimodal-gait-dataset/1.0.0/",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>physionet_multimodal_gait</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Plantar force</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M2 M3 M5 M6 |
| **Subjects** | 59 |
| **Ages** | 24 +/- 5 y |
| **Status** | acquired (2026-09-08) |
| **License** | CC BY 4.0 (page-verified at fetch 2026-09-07; open access) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("physionet_multimodal_gait")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (page-verified at fetch 2026-09-07; open access)
- **Redistribution**: yes
- **Access route**: physionet multimodal-gait-dataset
- **Source**: <https://physionet.org/content/multimodal-gait-dataset/1.0.0/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: C1; M2 M3 M5 M6
