# DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects)",
 "description": "DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects). MoveAtlas eeg family. licence free DABI account + institutional agreement per project; two.",
 "identifier": "https://dabi.loni.usc.edu/projects/F3RE38A785JW",
 "license": "free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn c",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B5 Freezing of gait",
  "A1 Tremor",
  "A3 Tics",
  "A4 Dystonia",
  "M7 LFP / ECoG"
 ],
 "url": "https://dabi.loni.usc.edu/projects/F3RE38A785JW",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dabi_movement_ephys</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Freezing of gait</span><span class="ma-tag">Tremor</span><span class="ma-tag">Tics</span><span class="ma-tag">Dystonia</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B5 A1 A3 A4 context (paediatric archive); M7 |
| **Status** | catalogued (2026-09-05) |
| **License** | free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn coordinated-reset ET 9.5 GB) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dabi_movement_ephys")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn coordinated-reset ET 9.5 GB)
- **Redistribution**: no
- **Access route**: dabi.loni.usc.edu
- **Source**: <https://dabi.loni.usc.edu/projects/F3RE38A785JW>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B5 A1 A3 A4 context (paediatric archive); M7
