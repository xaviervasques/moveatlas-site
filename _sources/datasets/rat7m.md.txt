# Rat 7M: 3D rat motion capture (Dunn/Olveczky)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Rat 7M: 3D rat motion capture (Dunn/Olveczky)",
 "description": "Rat 7M: 3D rat motion capture (Dunn/Olveczky). MoveAtlas animal family. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.5295370.v3",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.c.5295370.v3",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>rat7m</code>

| | |
|---|---|
| **Taxonomy cells** | animal: healthy rat 3D kinematics socle |
| **Subjects** | several animals |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("rat7m")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01)
- **Redistribution**: yes
- **Access route**: figshare collection 10.6084/m9.figshare.c.5295370
- **Source**: <https://doi.org/10.6084/m9.figshare.c.5295370.v3>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: rat7m
- **family**: animal
- **MoveAtlas cells**: animal: healthy rat 3D kinematics socle
- **population**: rat, ~7M frames / 10.8 h of 20-marker mocap with multi-camera video
- **n_subjects**: several animals
- **signal**: 3D mocap (20 markers) + synchronized multi-camera video
- **license**: CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01); redistribution: yes
- **access**: figshare collection 10.6084/m9.figshare.c.5295370
- **link**: https://doi.org/10.6084/m9.figshare.c.5295370.v3
