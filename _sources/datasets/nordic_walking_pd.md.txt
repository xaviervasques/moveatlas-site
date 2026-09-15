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
  "M2 Inertial (IMU)",
  "M3 Plantar force",
  "M4 Silhouette"
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

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Plantar force</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | B2; M2 M3 M4 |
| **Subjects** | 24 |
| **Ages** | H&Y 1-3 |
| **Status** | CATALOGUED 2026-09-05 (deep-dive): the FIRST open PD gait set combining full mocap + force plates + 16-channel surface EMG (pre/post intervention). Fetch-verify the repo host through the Nature link |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'emg'
- Source / URL: https://doi.org/10.1038/s41597-025-06209-9
- License / access: public per the descriptor (Sci Data 2025, 10.1038/s41597-025-06209-9; c3d/csv/mot/trc) - REPOSITORY HOST AND LICENCE TO VERIFY AT FETCH
- Access route: SciData descriptor -> repo per paper
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): the FIRST open PD gait set combining full mocap + force plates + 16-channel surface EMG (pre/post intervention). Fetch-verify the repo host through the Nature link
- Number of subjects: 24
- MoveAtlas cells: B2; M2 M3 M4

### Retrieval notes
Found by the 2026-09-05 deep-dive sweep. RE-VERIFY licence and access
at fetch (this sweep's fetch-time reads corrected half the previous
sweep's guesses). No-emails policy: request-tier routes are
documented, not exercised, unless the owner decides.

### Processing
None. Catalogue-tier.
