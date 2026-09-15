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

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>nlb_mc_maze</code>

| | |
|---|---|
| **Taxonomy cells** | animal: healthy macaque reach socle - continuous hand/cursor kinematics + spiking (complements the MPTP event-coded sets) |
| **Subjects** | 1 (many sessions) |
| **Status** | DOWNLOADED 2026-09-01 (animal hunt): both NWB assets of the published version via the DANDI API, sha256 journaled |
| **License** | CC BY 4.0 (DANDI, verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nlb_mc_maze")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (DANDI, verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: DANDI open download
- **Source**: <https://dandiarchive.org/dandiset/000128>

## Data card (verbatim, with its evidence trail)


- dataset: nlb_mc_maze
- family: animal  (physical path: datasets/animal/nlb_mc_maze)
- MoveAtlas cells: animal: healthy macaque reach socle - continuous hand/cursor kinematics + spiking (complements the MPTP event-coded sets)
- population: macaque, delayed center-out reaching in mazes
- n_subjects: 1 (many sessions)
- signal: spiking + continuous behavioral kinematics (NWB, 694 MB)
- license: CC BY 4.0 (DANDI, verified 2026-09-01) ; redistribution: yes
- access: DANDI open download
- status (2026-08-22): DOWNLOADED 2026-09-01 (animal hunt): both NWB assets of the published version via the DANDI API, sha256 journaled
- link: https://dandiarchive.org/dandiset/000128
