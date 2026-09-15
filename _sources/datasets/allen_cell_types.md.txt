# Allen Cell Types Database (patch-clamp ephys + morphology)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Allen Cell Types Database (patch-clamp ephys + morphology)",
 "description": "Allen Cell Types Database (patch-clamp ephys + morphology). MoveAtlas bio family. licence Allen Institute terms: research/noncommercial use; NO commer.",
 "identifier": "https://celltypes.brain-map.org",
 "license": "Allen Institute terms: research/noncommercial use; NO commercial redistribution without written permission (verified 202",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M7 LFP / ECoG",
  "M10 Histology / transcr."
 ],
 "url": "https://celltypes.brain-map.org",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>allen_cell_types</code>

<span class="ma-tag">LFP / ECoG</span><span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | M7 (cellular ephys), M10 (morphology) |
| **Subjects** | database |
| **Status** | NEW 2026-09-01 (gap hunt, owner GO): POINTER/RECIPE TIER ONLY (redistribution restriction); local fetch allowed for internal use |
| **License** | Allen Institute terms: research/noncommercial use; NO commercial redistribution without written permission (verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("allen_cell_types")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: Allen Institute terms: research/noncommercial use; NO commercial redistribution without written permission (verified 2026-09-01)
- **Redistribution**: no
- **Access route**: open download via portal / AllenSDK, no registration
- **Source**: <https://celltypes.brain-map.org>

## Data card (verbatim, with its evidence trail)


- dataset: allen_cell_types
- family: bio  (physical path: datasets/bio/allen_cell_types)
- MoveAtlas cells: M7 (cellular ephys), M10 (morphology)
- population: human and mouse single neurons: patch-clamp electrophysiology + reconstructed morphologies
- n_subjects: database
- signal: patch-clamp traces + .swc morphologies via AllenSDK
- license: Allen Institute terms: research/noncommercial use; NO commercial redistribution without written permission (verified 2026-09-01) ; redistribution: no
- access: open download via portal / AllenSDK, no registration
- status (2026-08-22): NEW 2026-09-01 (gap hunt, owner GO): POINTER/RECIPE TIER ONLY (redistribution restriction); local fetch allowed for internal use
- link: https://celltypes.brain-map.org
