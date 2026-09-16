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

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>gavd</code>

<span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | multi-pathology labels; M1 (annotations only) |
| **Subjects** | ~382 segments |
| **Status** | catalogued |
| **License** | MIT (LICENSE file in the repo, read 2026-08-28); videos remain YouTube-hosted |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gavd")
ds.info   # recipe: get_data() explains the route
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: gavd
- **family**: pose
- **MoveAtlas cells**: multi-pathology labels; M1 (annotations only)
- **population**: ~382 annotated YouTube video segments (video-level, not subjects)
- **n_subjects**: ~382 segments
- **signal**: clinical annotation CSVs of YouTube gait videos; NO video redistributed
- **license**: MIT (LICENSE file in the repo, read 2026-08-28); videos remain YouTube-hosted; redistribution: yes (the annotation CSVs we hold are MIT; videos never distributed)
- **access**: downloaded
- **link**: https://github.com/Rahmyyy/GAVD
