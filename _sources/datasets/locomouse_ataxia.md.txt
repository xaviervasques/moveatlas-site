# LocoMouse ataxic locomotion (reeler, pcd) stride kinematics

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "LocoMouse ataxic locomotion (reeler, pcd) stride kinematics",
 "description": "LocoMouse ataxic locomotion (reeler, pcd) stride kinematics. MoveAtlas animal family. 22 subjects. licence CC BY.",
 "identifier": "https://elifesciences.org/articles/55356",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://elifesciences.org/articles/55356",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>locomouse_ataxia</code>

| | |
|---|---|
| **Taxonomy cells** | animal: cerebellar-ataxia gait analogs (differential context for the dystonia/chorea gait question) |
| **Subjects** | 22 |
| **Status** | NEW 2026-09-01 (animal hunt): queued, light |
| **License** | CC BY (eLife source data) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("locomouse_ataxia")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY (eLife source data)
- **Redistribution**: yes
- **Access route**: eLife article source data (10.7554/eLife.55356)
- **Source**: <https://elifesciences.org/articles/55356>

## Data card (verbatim, with its evidence trail)


- dataset: locomouse_ataxia
- family: animal  (physical path: datasets/animal/locomouse_ataxia)
- MoveAtlas cells: animal: cerebellar-ataxia gait analogs (differential context for the dystonia/chorea gait question)
- population: mouse: reeler N=7 (9,392 strides), pcd N=3 (3,052 strides), controls N=12
- n_subjects: 22
- signal: 3D paw/nose/tail tracking-derived stride data (per-figure source data; raw 400-fps video not deposited)
- license: CC BY (eLife source data) ; redistribution: yes
- access: eLife article source data (10.7554/eLife.55356)
- status (2026-08-22): NEW 2026-09-01 (animal hunt): queued, light
- link: https://elifesciences.org/articles/55356
