# PhysioNet gait in aging and disease

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PhysioNet gait in aging and disease",
 "description": "PhysioNet gait in aging and disease. MoveAtlas imu family. 15 subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/gaitdb/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://physionet.org/content/gaitdb/",
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
   "name": "Purdon, Patrick L"
  },
  {
   "@type": "Person",
   "name": "Peng, C-K"
  },
  {
   "@type": "Person",
   "name": "Ladin, Zvi"
  },
  {
   "@type": "Person",
   "name": "Wei, Jeanne Y"
  },
  {
   "@type": "Person",
   "name": "Goldberger, Ary L"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>gaitdb</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3, C3; M2 (derived) |
| **Subjects** | 15 |
| **Status** | acquired |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |
| **MoveAtlas record** | [10.5281/zenodo.22310489](https://doi.org/10.5281/zenodo.22310489) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gaitdb")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/gaitdb/>

## Publications

- Hausdorff, Jeffrey M; Purdon, Patrick L; Peng, C-K; Ladin, Zvi; Wei, Jeanne Y; Goldberger, Ary L (1999). *Gait in Aging and Disease Database*. physionet.org. DOI: [10.13026/c2c889](https://doi.org/10.13026/c2c889)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{gaitdb_data_1999,
  title = {Gait in Aging and Disease Database},
  author = {Hausdorff, Jeffrey M and Purdon, Patrick L and Peng, C-K and Ladin, Zvi and Wei, Jeanne Y and Goldberger, Ary L},
  year = {1999},
  doi = {10.13026/c2c889},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{gaitdb_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: gaitdb
- **family**: imu
- **MoveAtlas cells**: B2, B3, C3; M2 (derived)
- **population**: 5 young + 5 old + 5 PD
- **n_subjects**: 15
- **signal**: stride-interval series (derived, not raw signal)
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://physionet.org/content/gaitdb/
