# Effect of DBS on parkinsonian tremor (PhysioNet; laser Doppler velocity)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Effect of DBS on parkinsonian tremor (PhysioNet; laser Doppler velocity)",
 "description": "Effect of DBS on parkinsonian tremor (PhysioNet; laser Doppler velocity). MoveAtlas imu family. 15 (97 recordings) subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/tremordb/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A1 Tremor",
  "M2 Inertial (IMU)"
 ],
 "url": "https://physionet.org/content/tremordb/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Beutera, Anne"
  },
  {
   "@type": "Person",
   "name": "Titcombe, Michèle S."
  },
  {
   "@type": "Person",
   "name": "Richera, François"
  },
  {
   "@type": "Person",
   "name": "Gross, Christian"
  },
  {
   "@type": "Person",
   "name": "Guehl, Dominique"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>tremordb</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | A1; M2-adjacent (velocity aux) |
| **Subjects** | 15 (97 recordings) |
| **Status** | harmonized (2026-08-22) |
| **License** | ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16) |
| **MoveAtlas record** | [10.5281/zenodo.22310736](https://doi.org/10.5281/zenodo.22310736) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("tremordb")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://physionet.org/content/tremordb/>

## Publications

- Beutera, Anne; Titcombe, Michèle S.; Richera, François; Gross, Christian; Guehl, Dominique (2001). *Effect of Deep Brain Stimulation on Parkinsonian Tremor*. physionet.org. DOI: [10.13026/c2d097](https://doi.org/10.13026/c2d097)
- Pollard, Tom; Moody, Benjamin E.; Lehman, Li-wei H.; Gow, Brian J.; Fernandes, Chrystinne; Xie, Chen; Johnson, Alistair; Mark, Roger G.; Heldt, Thomas (2026). *PhysioNet as a global platform for biomedical research*. Nature Health. DOI: [10.1038/s44360-026-00096-z](https://doi.org/10.1038/s44360-026-00096-z)

```bibtex
@misc{tremordb_data_2001,
  title = {Effect of Deep Brain Stimulation on Parkinsonian Tremor},
  author = {Beutera, Anne and Titcombe, Michèle S. and Richera, François and Gross, Christian and Guehl, Dominique},
  year = {2001},
  doi = {10.13026/c2d097},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{tremordb_paper_2026,
  title = {PhysioNet as a global platform for biomedical research},
  author = {Pollard, Tom and Moody, Benjamin E. and Lehman, Li-wei H. and Gow, Brian J. and Fernandes, Chrystinne and Xie, Chen and Johnson, Alistair and Mark, Roger G. and Heldt, Thomas},
  year = {2026},
  doi = {10.1038/s44360-026-00096-z},
  journal = {Nature Health}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: tremordb
- **family**: imu
- **MoveAtlas cells**: A1; M2-adjacent (velocity aux)
- **population**: 15 PD with DBS (GPi n=5? / Vim / STN per prefix g/v/s), high- and low-amplitude tremor cohorts, DBS/medication conditions + 15/30/45/60-min post-off washout
- **n_subjects**: 15 (97 recordings)
- **signal**: hand tremor VELOCITY by laser Doppler at 100 Hz, one text file per subject per condition (.rit right /.let left), physical units mm/s (m/s converted)
- **license**: ODC-By 1.0 (Open Data Commons Attribution License v1.0, stated on the PhysioNet page, read 2026-09-16); redistribution: yes
- **access**: downloaded
- **link**: https://physionet.org/content/tremordb/
- **ingestion**: ingest_tremordb.py: processed/tremordb_velocity.pkl + subject table + audit. NOT the 9-channel IMU contract (velocity, not acc/gyro): aux asset for A1 severity dynamics under DBS on/off per target
