# Ataxia gait Kinect (Summa 2020)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Ataxia gait Kinect (Summa 2020)",
 "description": "Ataxia gait Kinect (Summa 2020). MoveAtlas pose family. 51 subjects. licence Data in Brief.",
 "identifier": "https://doi.org/10.1016/j.dib.2020.106307",
 "license": "Data in Brief (Elsevier supplementary; no explicit data licence)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "D2 Ataxia",
  "M1 Pose / video"
 ],
 "url": "https://doi.org/10.1016/j.dib.2020.106307",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Summa, S."
  },
  {
   "@type": "Person",
   "name": "Tartarisco, G."
  },
  {
   "@type": "Person",
   "name": "Favetta, M."
  },
  {
   "@type": "Person",
   "name": "Buzachis, A."
  },
  {
   "@type": "Person",
   "name": "Romano, A."
  },
  {
   "@type": "Person",
   "name": "Bernava, G.M."
  },
  {
   "@type": "Person",
   "name": "Vasco, G."
  },
  {
   "@type": "Person",
   "name": "Pioggia, G."
  },
  {
   "@type": "Person",
   "name": "Petrarca, M."
  },
  {
   "@type": "Person",
   "name": "Castelli, E."
  },
  {
   "@type": "Person",
   "name": "Bertini, E."
  },
  {
   "@type": "Person",
   "name": "Schirinzi, T."
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ataxie_kinect_dib</code>

<span class="ma-tag">Ataxia</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | D2; M1 (table only on disk) |
| **Subjects** | 51 |
| **Status** | raw table on disk; skeleton data never fetched (source availability unclear) |
| **License** | Data in Brief (Elsevier supplementary; no explicit data licence) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ataxie_kinect_dib")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: Data in Brief (Elsevier supplementary; no explicit data licence)
- **Redistribution**: no, DECIDED 2026-08-28: pointer to the article
- **Access route**: downloaded (table only)
- **Source**: <https://doi.org/10.1016/j.dib.2020.106307>

## Publications

- Summa, S.; Tartarisco, G.; Favetta, M.; Buzachis, A.; Romano, A.; Bernava, G.M.; Vasco, G.; Pioggia, G.; Petrarca, M.; Castelli, E.; Bertini, E.; Schirinzi, T. (2020). *Spatio-temporal parameters of ataxia gait dataset obtained with the Kinect*. Data in Brief. DOI: [10.1016/j.dib.2020.106307](https://doi.org/10.1016/j.dib.2020.106307)

```bibtex
@misc{ataxie_kinect_dib_data_2020,
  title = {Spatio-temporal parameters of ataxia gait dataset obtained with the Kinect},
  author = {Summa, S. and Tartarisco, G. and Favetta, M. and Buzachis, A. and Romano, A. and Bernava, G.M. and Vasco, G. and Pioggia, G. and Petrarca, M. and Castelli, E. and Bertini, E. and Schirinzi, T.},
  year = {2020},
  doi = {10.1016/j.dib.2020.106307},
  howpublished = {Data in Brief},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: ataxie_kinect_dib
- family: pose  (physical path: datasets/pose/ataxie_kinect_dib)
- MoveAtlas cells: D2; M1 (table only on disk)
- population: ataxia patients + controls, SARA-scored
- n_subjects: 51
- signal: clinical table (supplementary mmc1.xlsx); Kinect skeleton signal NOT downloaded
- license: Data in Brief (Elsevier supplementary; no explicit data licence) ; redistribution: no, DECIDED 2026-08-28: pointer to the article
- access: downloaded (table only)
- status (2026-08-22): raw table on disk; skeleton data never fetched (source availability unclear)
- link: https://doi.org/10.1016/j.dib.2020.106307
- notes: subject-level SARA + diagnosis: subject-table source for D2
