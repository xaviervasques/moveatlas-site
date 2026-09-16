# Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford)",
 "description": "Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford). MoveAtlas eeg family. 7 patients / 12 hemispheres subjects. licence CC BY-SA 4.0.",
 "identifier": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "A4 Dystonia",
  "M2 Inertial (IMU)",
  "M5 EMG",
  "M7 LFP / ECoG"
 ],
 "url": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mrc_lfp_dystonia</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EMG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | A4 (cervical dystonia); M2 M5 M7 |
| **Subjects** | 7 patients / 12 hemispheres |
| **Status** | catalogued (2026-09-05) |
| **License** | CC BY-SA 4.0 (verified on the portal record; SA clause: licence-matrix check before redistribution); free registration/login then direct download |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mrc_lfp_dystonia")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-SA 4.0 (verified on the portal record; SA clause: licence-matrix check before redistribution); free registration/login then direct download
- **Redistribution**: unknown
- **Access route**: data.mrc.ox.ac.uk/lfp-dystonia (DOI 10.5287/bodleian:QRNQjNpV7)
- **Source**: <https://data.mrc.ox.ac.uk/lfp-dystonia>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A4 (cervical dystonia); M2 M5 M7
