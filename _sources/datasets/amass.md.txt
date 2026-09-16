# AMASS (healthy mocap base)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "AMASS (healthy mocap base)",
 "description": "AMASS (healthy mocap base). MoveAtlas socle family. licence non-commercial research.",
 "identifier": "https://amass.is.tue.mpg.de",
 "license": "non-commercial research (per sub-dataset MPI EULA)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://amass.is.tue.mpg.de",
 "isAccessibleForFree": false,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>amass</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1 |
| **Subjects** | ~344 |
| **Status** | harmonized |
| **License** | non-commercial research (per sub-dataset MPI EULA) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("amass")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: non-commercial research (per sub-dataset MPI EULA)
- **Redistribution**: no
- **Access route**: account + EULA
- **Source**: <https://amass.is.tue.mpg.de>

## Publications

- Mahmood, Naureen; Ghorbani, Nima; Troje, Nikolaus F.; Pons-Moll, Gerard; Black, Michael (2019). *AMASS: Archive of Motion Capture As Surface Shapes*. 2019 IEEE/CVF International Conference on Computer Vision (ICCV). DOI: [10.1109/iccv.2019.00554](https://doi.org/10.1109/iccv.2019.00554)

```bibtex
@article{amass_paper_2019,
  title = {AMASS: Archive of Motion Capture As Surface Shapes},
  author = {Mahmood, Naureen and Ghorbani, Nima and Troje, Nikolaus F. and Pons-Moll, Gerard and Black, Michael},
  year = {2019},
  doi = {10.1109/iccv.2019.00554},
  journal = {2019 IEEE/CVF International Conference on Computer Vision (ICCV)}
}
```
