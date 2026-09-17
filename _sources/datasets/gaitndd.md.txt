# PhysioNet gait in neurodegenerative disease

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PhysioNet gait in neurodegenerative disease",
 "description": "PhysioNet gait in neurodegenerative disease. MoveAtlas imu family. 64 subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/gaitndd/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A7 Chorea",
  "B2 Bradykinesia",
  "C1 Normal adult movement",
  "D3 Pyramidal syndromes",
  "M3 Plantar force"
 ],
 "url": "https://physionet.org/content/gaitndd/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Hausdorff, Jeffrey M"
  },
  {
   "@type": "Person",
   "name": "Lertratanakul, Apinya"
  },
  {
   "@type": "Person",
   "name": "Cudkowicz, Merit E"
  },
  {
   "@type": "Person",
   "name": "Peterson, Amie L"
  },
  {
   "@type": "Person",
   "name": "Kaliton, David"
  },
  {
   "@type": "Person",
   "name": "Goldberger, Ary L"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>gaitndd</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | A7 (HD), B2 (PD), C1 (controls), D3; M3 |
| **Subjects** | 64 |
| **Status** | harmonized |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |
| **MoveAtlas record** | [10.5281/zenodo.22806862](https://doi.org/10.5281/zenodo.22806862) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gaitndd")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/gaitndd/>

## Publications

- Hausdorff, Jeffrey M; Lertratanakul, Apinya; Cudkowicz, Merit E; Peterson, Amie L; Kaliton, David; Goldberger, Ary L (2000). *Gait Dynamics in Neuro-Degenerative Disease Data Base*. physionet.org. DOI: [10.13026/c27g6c](https://doi.org/10.13026/c27g6c)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{gaitndd_data_2000,
  title = {Gait Dynamics in Neuro-Degenerative Disease Data Base},
  author = {Hausdorff, Jeffrey M and Lertratanakul, Apinya and Cudkowicz, Merit E and Peterson, Amie L and Kaliton, David and Goldberger, Ary L},
  year = {2000},
  doi = {10.13026/c27g6c},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{gaitndd_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: gaitndd
- **family**: imu
- **MoveAtlas cells**: A7 (HD), B2 (PD), C1 (controls), D3; M3
- **population**: 16 controls + 15 PD + 20 Huntington + 13 ALS
- **n_subjects**: 64
- **signal**: force-sensitive resistor gait series
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://physionet.org/content/gaitndd/
- **ingestion**: build_canonical_force.py
- **known issues**: the force values are the outputs of uncalibrated force-sensitive resistors (about -2 to 1.1), not newtons; records built from 2026-09-17 declare unit unknown and name the calibration, and the values are never rescaled
