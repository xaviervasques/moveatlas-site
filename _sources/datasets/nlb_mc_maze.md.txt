# Neural Latents MC_Maze: macaque reaching with hand kinematics (DANDI 000128)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Neural Latents MC_Maze: macaque reaching with hand kinematics (DANDI 000128)",
 "description": "Neural Latents MC_Maze: macaque reaching with hand kinematics (DANDI 000128). MoveAtlas animal family. 1 (many sessions) subjects. licence CC BY 4.0.",
 "identifier": "https://dandiarchive.org/dandiset/000128",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://dandiarchive.org/dandiset/000128",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>nlb_mc_maze</code>

| | |
|---|---|
| **Taxonomy cells** | animal: healthy macaque reach socle - continuous hand/cursor kinematics + spiking (complements the MPTP event-coded sets) |
| **Subjects** | 1 |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (DANDI, verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nlb_mc_maze")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (DANDI, verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: DANDI open download
- **Source**: <https://dandiarchive.org/dandiset/000128>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: nlb_mc_maze
- **family**: animal
- **MoveAtlas cells**: animal: healthy macaque reach socle - continuous hand/cursor kinematics + spiking (complements the MPTP event-coded sets)
- **population**: macaque, delayed center-out reaching in mazes
- **n_subjects**: 1
- **signal**: spiking + continuous behavioral kinematics (NWB, 694 MB)
- **license**: CC BY 4.0 (DANDI, verified 2026-09-01); redistribution: yes
- **access**: DANDI open download
- **link**: https://dandiarchive.org/dandiset/000128
