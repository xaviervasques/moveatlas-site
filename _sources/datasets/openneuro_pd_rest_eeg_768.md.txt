# ds008768: resting EEG in PD and controls (312 subjects)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ds008768: resting EEG in PD and controls (312 subjects)",
 "description": "ds008768: resting EEG in PD and controls (312 subjects). MoveAtlas eeg family. 312 subjects. licence OpenNeuro.",
 "identifier": "https://openneuro.org/datasets/ds008768",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B4 Akinesia",
  "M6 EEG"
 ],
 "url": "https://openneuro.org/datasets/ds008768",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>openneuro_pd_rest_eeg_768</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4; M6 |
| **Subjects** | 312 |
| **Status** | catalogued (2026-09-05) |
| **License** | OpenNeuro (CC0 default, verify on record) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("openneuro_pd_rest_eeg_768")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: OpenNeuro (CC0 default, verify on record)
- **Redistribution**: unknown
- **Access route**: openneuro ds008768
- **Source**: <https://openneuro.org/datasets/ds008768>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4; M6
