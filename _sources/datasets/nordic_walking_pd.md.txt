# Nordic Walking parkinsonian gait: mocap + force plates + 16-ch sEMG (Sci Data 2025)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Nordic Walking parkinsonian gait: mocap + force plates + 16-ch sEMG (Sci Data 2025)",
 "description": "Nordic Walking parkinsonian gait: mocap + force plates + 16-ch sEMG (Sci Data 2025). MoveAtlas emg family. 24 subjects. licence public per the descriptor.",
 "identifier": "https://doi.org/10.1038/s41597-025-06209-9",
 "license": "public per the descriptor (Sci Data 2025, 10.1038/s41597-025-06209-9; c3d/csv/mot/trc) - REPOSITORY HOST AND LICENCE TO ",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "emg",
  "B2 Bradykinesia",
  "M1 Pose / video",
  "M3 Plantar force",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.1038/s41597-025-06209-9",
 "isAccessibleForFree": false,
 "measurementTechnique": "emg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-emg">emg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>nordic_walking_pd</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Plantar force</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M1 M3 M5 |
| **Subjects** | 24 |
| **Ages** | H&Y 1-3 |
| **Status** | catalogued (2026-09-05) |
| **License** | public per the descriptor (Sci Data 2025, 10.1038/s41597-025-06209-9; c3d/csv/mot/trc) - REPOSITORY HOST AND LICENCE TO VERIFY AT FETCH |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nordic_walking_pd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: public per the descriptor (Sci Data 2025, 10.1038/s41597-025-06209-9; c3d/csv/mot/trc) - REPOSITORY HOST AND LICENCE TO VERIFY AT FETCH
- **Redistribution**: unknown
- **Access route**: SciData descriptor -> repo per paper
- **Source**: <https://doi.org/10.1038/s41597-025-06209-9>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B2; M1 M3 M5
