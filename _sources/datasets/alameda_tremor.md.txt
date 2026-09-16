# ALAMEDA wrist tremor features

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ALAMEDA wrist tremor features",
 "description": "ALAMEDA wrist tremor features. MoveAtlas imu family. 11 subjects. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/10782573",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A1 Tremor",
  "M2 Inertial (IMU)"
 ],
 "url": "https://zenodo.org/records/10782573",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Giannakopoulou, Konstantina-Maria"
  },
  {
   "@type": "Person",
   "name": "National and Kapodistrian University of Athens"
  },
  {
   "@type": "Person",
   "name": "Stefanis, leonidas"
  },
  {
   "@type": "Person",
   "name": "Papagiannakis, Nikolaos"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>alameda_tremor</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A1; M2 (derived) |
| **Subjects** | 11 |
| **Status** | acquired |
| **License** | CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("alameda_tremor")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://zenodo.org/records/10782573>

## Publications

- Giannakopoulou, Konstantina-Maria; National and Kapodistrian University of Athens; Stefanis, leonidas; Papagiannakis, Nikolaos (2024). *Parkinson's Disease Tremor Dataset - ALAMEDA*. Zenodo. DOI: [10.5281/zenodo.10782573](https://doi.org/10.5281/zenodo.10782573)

```bibtex
@misc{alameda_tremor_data_2024,
  title = {Parkinson's Disease Tremor Dataset - ALAMEDA},
  author = {Giannakopoulou, Konstantina-Maria and National and Kapodistrian University of Athens and Stefanis, leonidas and Papagiannakis, Nikolaos},
  year = {2024},
  doi = {10.5281/zenodo.10782573},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: alameda_tremor
- **family**: imu
- **MoveAtlas cells**: A1; M2 (derived)
- **population**: PD tremor, precomputed features
- **n_subjects**: 11
- **signal**: 99 precomputed features per window (CSV)
- **license**: CC BY 4.0 (stated on the source Zenodo record, read through DataCite 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://zenodo.org/records/10782573
