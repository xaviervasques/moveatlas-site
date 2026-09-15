# JAX stride-level mouse gait (62 strains + SOD1 ALS, Rett, Ts65Dn)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "JAX stride-level mouse gait (62 strains + SOD1 ALS, Rett, Ts65Dn)",
 "description": "JAX stride-level mouse gait (62 strains + SOD1 ALS, Rett, Ts65Dn). MoveAtlas animal family. 62 strains subjects. licence CC BY-NC-ND 4.0.",
 "identifier": "https://doi.org/10.5281/zenodo.5636430",
 "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal",
  "D1 Epilepsy"
 ],
 "url": "https://doi.org/10.5281/zenodo.5636430",
 "isAccessibleForFree": false,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>kumar_stride_gait</code>

<span class="ma-tag">Epilepsy</span>

| | |
|---|---|
| **Taxonomy cells** | animal: strain-survey gait reference + disease-model gait summaries (SOD1 ALS -> hypokinetic-adjacent analog) |
| **Subjects** | 62 strains |
| **Status** | DOWNLOADED 2026-09-01 (animal hunt): 9 files including the stride-summary CSV, pose annotations (428 MB) and the HRNet weights; the 3.6 GB container image skipped by filter. Record 5708437 is an empty stub (0 files), 6380163 is the real deposit |
| **License** | CC BY-NC-ND 4.0 (the deposit's own LICENSE file, read verbatim on disk 2026-09-01; Zenodo API said only other-nc) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("kumar_stride_gait")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-NC-ND 4.0 (the deposit's own LICENSE file, read verbatim on disk 2026-09-01; Zenodo API said only other-nc)
- **Redistribution**: no (ND: care_pd precedent applies - internal, eval-only, excluded from releases and from training that publishes weights)
- **Access route**: Zenodo direct download (10.5281/zenodo.5636430)
- **Source**: <https://doi.org/10.5281/zenodo.5636430>

## Data card (verbatim, with its evidence trail)


- dataset: kumar_stride_gait
- family: animal  (physical path: datasets/animal/kumar_stride_gait)
- MoveAtlas cells: animal: strain-survey gait reference + disease-model gait summaries (SOD1 ALS -> hypokinetic-adjacent analog)
- population: mouse, 62 strains + disease models, open field
- n_subjects: 62 strains
- signal: HRNet pose model + training annotations + stride-level gait summary tables (raw videos not deposited)
- license: CC BY-NC-ND 4.0 (the deposit's own LICENSE file, read verbatim on disk 2026-09-01; Zenodo API said only other-nc) ; redistribution: no (ND: care_pd precedent applies - internal, eval-only, excluded from releases and from training that publishes weights)
- access: Zenodo direct download (10.5281/zenodo.5636430)
- status (2026-08-22): DOWNLOADED 2026-09-01 (animal hunt): 9 files including the stride-summary CSV, pose annotations (428 MB) and the HRNet weights; the 3.6 GB container image skipped by filter. Record 5708437 is an empty stub (0 files), 6380163 is the real deposit
- link: https://doi.org/10.5281/zenodo.5636430
