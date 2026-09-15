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
| **Status** | CATALOGUED 2026-09-05: 63.6 GB, 312 subjects - the largest open PD resting-EEG found; heads the OpenNeuro triage list (with the Narayanan Iowa siblings ds004574/79/80 of our held ds004584, PD-mortality ds007020, ET MRI ds008336) - full list in HUNT_DEEPDIVE |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://openneuro.org/datasets/ds008768
- License / access: OpenNeuro (CC0 default, verify on record)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: 63.6 GB, 312 subjects - the largest open PD resting-EEG found; heads the OpenNeuro triage list (with the Narayanan Iowa siblings ds004574/79/80 of our held ds004584, PD-mortality ds007020, ET MRI ds008336) - full list in HUNT_DEEPDIVE
- MoveAtlas cells: B1-B4; M6

### Retrieval notes
RE-VERIFY at fetch/request; no-emails policy for gated tiers.

### Processing
None. Catalogue-tier.
