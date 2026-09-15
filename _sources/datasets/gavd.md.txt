# GAVD (gait abnormality video annotations)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "GAVD (gait abnormality video annotations)",
 "description": "GAVD (gait abnormality video annotations). MoveAtlas pose family. licence MIT.",
 "identifier": "https://github.com/Rahmyyy/GAVD",
 "license": "https://opensource.org/license/mit",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "M1 Pose / video"
 ],
 "url": "https://github.com/Rahmyyy/GAVD",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>gavd</code>

<span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | multi-pathology labels; M1 (annotations only) |
| **Subjects** | ~382 segments |
| **Status** | raw annotations on disk; label/reference source, NOT a signal corpus (documented exclusion) |
| **License** | MIT (LICENSE file in the repo, read 2026-08-28); videos remain YouTube-hosted |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gavd")
records, meta = ds.get_data()
```

## License and access

- **License**: MIT (LICENSE file in the repo, read 2026-08-28); videos remain YouTube-hosted
- **Redistribution**: yes (the annotation CSVs we hold are MIT; videos never distributed)
- **Access route**: downloaded
- **Source**: <https://github.com/Rahmyyy/GAVD>

## Publications

- Ranjan, Rahm; Ahmedt-Aristizabal, David; Ali Armin, Mohammad; Kim, Juno (2025). *Computer Vision for Clinical Gait Analysis: A Gait Abnormality Video Dataset*. IEEE Access. DOI: [10.1109/access.2025.3545787](https://doi.org/10.1109/access.2025.3545787)

```bibtex
@article{gavd_paper_2025,
  title = {Computer Vision for Clinical Gait Analysis: A Gait Abnormality Video Dataset},
  author = {Ranjan, Rahm and Ahmedt-Aristizabal, David and Ali Armin, Mohammad and Kim, Juno},
  year = {2025},
  doi = {10.1109/access.2025.3545787},
  journal = {IEEE Access}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: gavd
- family: pose  (physical path: datasets/pose/gavd)
- MoveAtlas cells: multi-pathology labels; M1 (annotations only)
- population: ~382 annotated YouTube video segments (video-level, not subjects)
- n_subjects: ~382 segments
- signal: clinical annotation CSVs of YouTube gait videos; NO video redistributed
- license: MIT (LICENSE file in the repo, read 2026-08-28); videos remain YouTube-hosted ; redistribution: yes (the annotation CSVs we hold are MIT; videos never distributed)
- access: downloaded
- status (2026-08-22): raw annotations on disk; label/reference source, NOT a signal corpus (documented exclusion)
- link: https://github.com/Rahmyyy/GAVD
- notes: usable as a taxonomy-cell label source and video-reference list. Link resolved 2026-08-23 from the clone's own .git/config
