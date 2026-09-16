# REMAP open subset (Bristol)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "REMAP open subset (Bristol)",
 "description": "REMAP open subset (Bristol). MoveAtlas pose family. 24 subjects. licence CC BY 4.0.",
 "identifier": "https://data.bris.ac.uk/data/dataset/21h9f9e30v9cl2fapjggz4q1x7",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "M1 Pose / video"
 ],
 "url": "https://data.bris.ac.uk/data/dataset/21h9f9e30v9cl2fapjggz4q1x7",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Craddock, Ian"
  },
  {
   "@type": "Person",
   "name": "Mirmehdi, Majid"
  },
  {
   "@type": "Person",
   "name": "Tonkin, Emma"
  },
  {
   "@type": "Person",
   "name": "Tourte, Gregory"
  },
  {
   "@type": "Person",
   "name": "Masullo, Alessandro"
  },
  {
   "@type": "Person",
   "name": "McConville, Ryan"
  },
  {
   "@type": "Person",
   "name": "Whone, Alan"
  },
  {
   "@type": "Person",
   "name": "Morgan, Catherine"
  },
  {
   "@type": "Person",
   "name": "Ferdian Jovan"
  },
  {
   "@type": "Person",
   "name": "Arindam Sikdar"
  },
  {
   "@type": "Person",
   "name": "Pushpajit Khaire"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>remap_open</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3; M1 |
| **Subjects** | 24 |
| **Status** | harmonized (2026-08-25) |
| **License** | CC BY 4.0 (warranty disclaimer) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("remap_open")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (warranty disclaimer)
- **Redistribution**: yes
- **Access route**: direct_download (single 351.4 MiB zip; fetch_p2_lot.py --only remap_open)
- **Source**: <https://data.bris.ac.uk/data/dataset/21h9f9e30v9cl2fapjggz4q1x7>

## Publications

- Craddock, Ian; Mirmehdi, Majid; Tonkin, Emma; Tourte, Gregory; Masullo, Alessandro; McConville, Ryan; Whone, Alan; Morgan, Catherine; Ferdian Jovan; Arindam Sikdar; Pushpajit Khaire (2023). *REMAP Open dataset*. University of Bristol. DOI: [10.5523/bris.21h9f9e30v9cl2fapjggz4q1x7](https://doi.org/10.5523/bris.21h9f9e30v9cl2fapjggz4q1x7)
- Morgan, Catherine; Tonkin, Emma L.; Masullo, Alessandro; Jovan, Ferdian; Sikdar, Arindam; Khaire, Pushpajit; Mirmehdi, Majid; McConville, Ryan; Tourte, Gregory J. L.; Whone, Alan; Craddock, Ian (2023). *A multimodal dataset of real world mobility activities in Parkinson’s disease*. Scientific Data. DOI: [10.1038/s41597-023-02663-5](https://doi.org/10.1038/s41597-023-02663-5)

```bibtex
@misc{remap_open_data_2023,
  title = {REMAP Open dataset},
  author = {Craddock, Ian and Mirmehdi, Majid and Tonkin, Emma and Tourte, Gregory and Masullo, Alessandro and McConville, Ryan and Whone, Alan and Morgan, Catherine and Ferdian Jovan and Arindam Sikdar and Pushpajit Khaire},
  year = {2023},
  doi = {10.5523/bris.21h9f9e30v9cl2fapjggz4q1x7},
  howpublished = {University of Bristol},
  note = {dataset}
}
@article{remap_open_paper_2023,
  title = {A multimodal dataset of real world mobility activities in Parkinson’s disease},
  author = {Morgan, Catherine and Tonkin, Emma L. and Masullo, Alessandro and Jovan, Ferdian and Sikdar, Arindam and Khaire, Pushpajit and Mirmehdi, Majid and McConville, Ryan and Tourte, Gregory J. L. and Whone, Alan and Craddock, Ian},
  year = {2023},
  doi = {10.1038/s41597-023-02663-5},
  journal = {Scientific Data}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: remap_open
- **family**: pose
- **MoveAtlas cells**: B2, B3; M1
- **population**: 12 PD (mean 61.25 y) + 12 controls (mean 59.25 y); home free-living + clinical assessment; PD on/off labels
- **n_subjects**: 24
- **signal**: coarsened 2D skeletons (sit-to-stand + turns) and coarsened 3D (turns)
- **license**: CC BY 4.0 (warranty disclaimer); redistribution: yes
- **access**: direct_download (single 351.4 MiB zip; fetch_p2_lot.py --only remap_open)
- **link**: https://data.bris.ac.uk/data/dataset/21h9f9e30v9cl2fapjggz4q1x7
- **citation**: Sci Data 2023, doi 10.1038/s41597-023-02663-5
