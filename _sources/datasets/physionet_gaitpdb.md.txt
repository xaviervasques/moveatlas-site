# PhysioNet gaitpdb (Hausdorff)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PhysioNet gaitpdb (Hausdorff)",
 "description": "PhysioNet gaitpdb (Hausdorff). MoveAtlas imu family. 165 subjects. licence PhysioNet open.",
 "identifier": "https://physionet.org/content/gaitpdb/",
 "license": "PhysioNet open",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "M3 Plantar force"
 ],
 "url": "https://physionet.org/content/gaitpdb/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Hausdorff, Jeffrey M."
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>physionet_gaitpdb</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3; M3 |
| **Subjects** | 165 |
| **Status** | INGESTED v1 (force contract): 306 records |
| **License** | PhysioNet open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("physionet_gaitpdb")
records, meta = ds.get_data()
```

## License and access

- **License**: PhysioNet open
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/gaitpdb/>

## Publications

- Hausdorff, Jeffrey M. (2008). *Gait in Parkinson’s Disease*. physionet.org. DOI: [10.13026/c24h3n](https://doi.org/10.13026/c24h3n)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{physionet_gaitpdb_data_2008,
  title = {Gait in Parkinson’s Disease},
  author = {Hausdorff, Jeffrey M.},
  year = {2008},
  doi = {10.13026/c24h3n},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{physionet_gaitpdb_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: physionet_gaitpdb
- family: imu  (physical path: datasets/imu/physionet_gaitpdb)
- MoveAtlas cells: B2, B3; M3
- population: ~93 PD + ~73 controls (165 on-disk codes)
- n_subjects: 165
- signal: vertical ground-reaction force, 8 sensors per foot, 100 Hz
- license: PhysioNet open ; redistribution: yes
- access: downloaded
- status (2026-08-22): INGESTED v1 (force contract): 306 records
- link: https://physionet.org/content/gaitpdb/
- ingestion: build_canonical_force.py
