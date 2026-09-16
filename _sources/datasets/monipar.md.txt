# MoniPAR smartwatch PD

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MoniPAR smartwatch PD",
 "description": "MoniPAR smartwatch PD. MoveAtlas imu family. 28 subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/8104853",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A1 Tremor",
  "B2 Bradykinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/8104853",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Sigcha, Luis"
  },
  {
   "@type": "Person",
   "name": "Pavón, Ignacio"
  },
  {
   "@type": "Person",
   "name": "De Arcas, Guillermo"
  },
  {
   "@type": "Person",
   "name": "Costa, Nélson"
  },
  {
   "@type": "Person",
   "name": "Costa, Susana"
  },
  {
   "@type": "Person",
   "name": "Arezes, Pedro"
  },
  {
   "@type": "Person",
   "name": "López, Juan Manuel"
  },
  {
   "@type": "Person",
   "name": "Polvorinos, Carlos"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>monipar</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A1, B2; M2 |
| **Subjects** | 28 |
| **Status** | harmonized |
| **License** | CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("monipar")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://zenodo.org/records/8104853>

## Publications

- Sigcha, Luis; Pavón, Ignacio; De Arcas, Guillermo; Costa, Nélson; Costa, Susana; Arezes, Pedro; López, Juan Manuel; Polvorinos, Carlos (2023). *Monipar Database: smartwatch movement data to monitor motor competency in subjects with Parkinson's disease*. Zenodo. DOI: [10.5281/zenodo.8104853](https://doi.org/10.5281/zenodo.8104853)

```bibtex
@misc{monipar_data_2023,
  title = {Monipar Database: smartwatch movement data to monitor motor competency in subjects with Parkinson's disease},
  author = {Sigcha, Luis and Pavón, Ignacio and De Arcas, Guillermo and Costa, Nélson and Costa, Susana and Arezes, Pedro and López, Juan Manuel and Polvorinos, Carlos},
  year = {2023},
  doi = {10.5281/zenodo.8104853},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: monipar
- **family**: imu
- **MoveAtlas cells**: A1, B2; M2
- **population**: 28 PD; Hoehn & Yahr, symptom onset, weekly tests
- **n_subjects**: 28
- **signal**: smartwatch IMU (.mat) + tremor labels
- **license**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://zenodo.org/records/8104853
- **ingestion**: build_canonical_imu.py (monipar mapping)
