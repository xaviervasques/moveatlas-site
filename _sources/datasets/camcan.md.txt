# Cam-CAN (healthy aging 18-88, MRI + MEG)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Cam-CAN (healthy aging 18-88, MRI + MEG)",
 "description": "Cam-CAN (healthy aging 18-88, MRI + MEG). MoveAtlas bio family. licence free with data usage agreement.",
 "identifier": "https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/",
 "license": "free with data usage agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "C1 Normal adult movement",
  "C3 Aging",
  "M8 Imaging"
 ],
 "url": "https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>camcan</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3; M8 |
| **Subjects** | ~700 |
| **Ages** | 18-88 y |
| **Status** | DOCUMENTED BARRIER (owner, 2026-08-28): the publication focuses on genuinely open data; application routes are not pursued. Procedure recorded as access-cost evidence: the old dataaccess URL 301-redirects to opendata.mrc-cbu.cam.ac.uk/projects/camcan; account + research proposal + data selection + 1... |
| **License** | free with data usage agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("camcan")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: free with data usage agreement
- **Redistribution**: no
- **Access route**: application (online DUA)
- **Source**: <https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/>

## Publications

- Taylor, Jason R.; Williams, Nitin; Cusack, Rhodri; Auer, Tibor; Shafto, Meredith A.; Dixon, Marie; Tyler, Lorraine K.; Cam-CAN; Henson, Richard N. (2017). *The Cambridge Centre for Ageing and Neuroscience (Cam-CAN) data repository: Structural and functional MRI, MEG, and cognitive data from a cross-sectional adult lifespan sample*. NeuroImage. DOI: [10.1016/j.neuroimage.2015.09.018](https://doi.org/10.1016/j.neuroimage.2015.09.018)

```bibtex
@article{camcan_paper_2017,
  title = {The Cambridge Centre for Ageing and Neuroscience (Cam-CAN) data repository: Structural and functional MRI, MEG, and cognitive data from a cross-sectional adult lifespan sample},
  author = {Taylor, Jason R. and Williams, Nitin and Cusack, Rhodri and Auer, Tibor and Shafto, Meredith A. and Dixon, Marie and Tyler, Lorraine K. and Cam-CAN and Henson, Richard N.},
  year = {2017},
  doi = {10.1016/j.neuroimage.2015.09.018},
  journal = {NeuroImage}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: camcan
- family: bio  (physical path: datasets/bio/camcan)
- MoveAtlas cells: C1, C3; M8
- population: ~700 scanned adults uniformly sampled 18-88 (100/decade), T1/T2/DWI/MT, rs- task- movie-fMRI, MEG, sensorimotor tasks
- n_subjects: ~700
- age: 18-88 y
- signal: multi-TB neuroimaging archive
- license: free with data usage agreement ; redistribution: no
- access: application (online DUA)
- status (2026-08-22): DOCUMENTED BARRIER (owner, 2026-08-28): the publication focuses on genuinely open data; application routes are not pursued. Procedure recorded as access-cost evidence: the old dataaccess URL 301-redirects to opendata.mrc-cbu.cam.ac.uk/projects/camcan; account + research proposal + data selection + 12-point T&C; academic affiliation required; up to 4 weeks review; delivery by SFTP
- link: https://opendata.mrc-cbu.cam.ac.uk/projects/camcan/
