# i-PROGNOSIS in-the-wild smartphone IMU

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "i-PROGNOSIS in-the-wild smartphone IMU",
 "description": "i-PROGNOSIS in-the-wild smartphone IMU. MoveAtlas imu family. 45 subjects. licence Zenodo open.",
 "identifier": "https://zenodo.org/records/3519213",
 "license": "Zenodo open",
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
 "url": "https://zenodo.org/records/3519213",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Papadopoulos, Alexandros"
  },
  {
   "@type": "Person",
   "name": "Kyritsis, Konstantinos"
  },
  {
   "@type": "Person",
   "name": "Bostantjopoulou, Sevasti"
  },
  {
   "@type": "Person",
   "name": "Klingelhoefer, Lisa"
  },
  {
   "@type": "Person",
   "name": "Chaudhuri, Kallol Ray"
  },
  {
   "@type": "Person",
   "name": "Delopoulos, Anastasios"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>imu_inthewild_iprognosis</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A1, B2; M2 |
| **Subjects** | 45 |
| **Status** | harmonized |
| **License** | Zenodo open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("imu_inthewild_iprognosis")
records, meta = ds.get_data()
```

## License and access

- **License**: Zenodo open
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://zenodo.org/records/3519213>

## Publications

- Papadopoulos, Alexandros; Kyritsis, Konstantinos; Bostantjopoulou, Sevasti; Klingelhoefer, Lisa; Chaudhuri, Kallol Ray; Delopoulos, Anastasios (2019). *IMU data captured unobtrusively and in-the-wild by Parkinson's disease patients and healthy controls*. Zenodo. DOI: [10.5281/zenodo.3519213](https://doi.org/10.5281/zenodo.3519213)

```bibtex
@misc{imu_inthewild_iprognosis_data_2019,
  title = {IMU data captured unobtrusively and in-the-wild by Parkinson's disease patients and healthy controls},
  author = {Papadopoulos, Alexandros and Kyritsis, Konstantinos and Bostantjopoulou, Sevasti and Klingelhoefer, Lisa and Chaudhuri, Kallol Ray and Delopoulos, Anastasios},
  year = {2019},
  doi = {10.5281/zenodo.3519213},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: imu_inthewild_iprognosis
- **family**: imu
- **MoveAtlas cells**: A1, B2; M2
- **population**: 31 PD + 14 controls, phone in pocket, daily life
- **n_subjects**: 45
- **signal**: smartphone accelerometry (pickle of 45 subjects)
- **license**: Zenodo open; redistribution: yes
- **access**: downloaded
- **link**: https://zenodo.org/records/3519213
- **ingestion**: build_canonical_imu.py (pocket location)
