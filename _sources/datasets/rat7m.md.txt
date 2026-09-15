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

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>rat7m</code>

| | |
|---|---|
| **Taxonomy cells** | animal: healthy rat 3D kinematics socle |
| **Subjects** | several animals |
| **Status** | MOCAP CORE DOWNLOADED 2026-09-01 (7 .mat + camera parameters, 255 MB, sha256 journaled) - the kinematics essential. VIDEOS 403 2026-09-03: figshare answers 403 Forbidden to scripted clients on the video files (browser UA included; the mocap article had served from the same client) - the casebook cas... |
| **License** | CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("rat7m")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01)
- **Redistribution**: yes
- **Access route**: figshare collection 10.6084/m9.figshare.c.5295370
- **Source**: <https://doi.org/10.6084/m9.figshare.c.5295370.v3>

## Data card (verbatim, with its evidence trail)


- dataset: rat7m
- family: animal  (physical path: datasets/animal/rat7m)
- MoveAtlas cells: animal: healthy rat 3D kinematics socle
- population: rat, ~7M frames / 10.8 h of 20-marker mocap with multi-camera video
- n_subjects: several animals
- signal: 3D mocap (20 markers) + synchronized multi-camera video
- license: CC BY 4.0 (CONFIRMED via the figshare API on all 8 collection articles at fetch, 2026-09-01) ; redistribution: yes
- access: figshare collection 10.6084/m9.figshare.c.5295370
- status (2026-09-04): COMPLETE. Mocap core downloaded 2026-09-01 (7 .mat + camera parameters, 255 MB); videos downloaded 2026-09-04 night (2028 .mp4, 15.35 GB, all 7 video articles, sha256 journaled, zero errors). The 2026-09-03 figshare 403 (case-5 pattern) cleared on its own: one spaced probe ~14 h later got HTTP 206 and the full pull ran clean - no retry storm needed, doctrine validated
- link: https://doi.org/10.6084/m9.figshare.c.5295370.v3
