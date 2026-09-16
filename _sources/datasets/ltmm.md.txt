# Long-Term Movement Monitoring (PhysioNet)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Long-Term Movement Monitoring (PhysioNet)",
 "description": "Long-Term Movement Monitoring (PhysioNet). MoveAtlas imu family. 79 distinct ids in the release (42 CO + 37 FL; the paper's 71 is its analysis cohort) subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/ltmm/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://physionet.org/content/ltmm/",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Weiss, Aner"
  },
  {
   "@type": "Person",
   "name": "Brozgol, Marina"
  },
  {
   "@type": "Person",
   "name": "Dorfman, Moran"
  },
  {
   "@type": "Person",
   "name": "Herman, Talia"
  },
  {
   "@type": "Person",
   "name": "Shema, Shirley"
  },
  {
   "@type": "Person",
   "name": "Giladi, Nir"
  },
  {
   "@type": "Person",
   "name": "Hausdorff, Jeffrey M."
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>ltmm</code>

<span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C3; M2 |
| **Subjects** | 79 distinct ids in the release |
| **Ages** | 65-87 y (mean 78.4) |
| **Status** | harmonized (2026-08-25) |
| **License** | ODC-By 1.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ltmm")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only ltmm)
- **Source**: <https://physionet.org/content/ltmm/>

## Publications

- Weiss, Aner; Brozgol, Marina; Dorfman, Moran; Herman, Talia; Shema, Shirley; Giladi, Nir; Hausdorff, Jeffrey M. (2016). *Long Term Movement Monitoring Database*. physionet.org. DOI: [10.13026/c2s59c](https://doi.org/10.13026/c2s59c)
- Weiss, Aner; Brozgol, Marina; Dorfman, Moran; Herman, Talia; Shema, Shirley; Giladi, Nir; Hausdorff, Jeffrey M. (2013). *Does the Evaluation of Gait Quality During Daily Life Provide Insight Into Fall Risk? A Novel Approach Using 3-Day Accelerometer Recordings*. Neurorehabilitation and Neural Repair. DOI: [10.1177/1545968313491004](https://doi.org/10.1177/1545968313491004)

```bibtex
@misc{ltmm_data_2016,
  title = {Long Term Movement Monitoring Database},
  author = {Weiss, Aner and Brozgol, Marina and Dorfman, Moran and Herman, Talia and Shema, Shirley and Giladi, Nir and Hausdorff, Jeffrey M.},
  year = {2016},
  doi = {10.13026/c2s59c},
  howpublished = {physionet.org},
  note = {dataset}
}
@article{ltmm_paper_2013,
  title = {Does the Evaluation of Gait Quality During Daily Life Provide Insight Into Fall Risk? A Novel Approach Using 3-Day Accelerometer Recordings},
  author = {Weiss, Aner and Brozgol, Marina and Dorfman, Moran and Herman, Talia and Shema, Shirley and Giladi, Nir and Hausdorff, Jeffrey M.},
  year = {2013},
  doi = {10.1177/1545968313491004},
  journal = {Neurorehabilitation and Neural Repair}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: ltmm
- **family**: imu
- **MoveAtlas cells**: C3; M2
- **population**: community-dwelling older adults 65-87 y, 3 days free living plus 1-minute lab walks, fallers vs non-fallers
- **n_subjects**: 79 distinct ids in the release
- **age**: 65-87 y (mean 78.4)
- **signal**: lower-back 6-channel IMU: v/ml/ap acceleration (g) + yaw/pitch/roll angular velocity (deg/s) at 100 Hz (WFDB, self-describing headers)
- **license**: ODC-By 1.0; redistribution: yes
- **access**: direct_download (fetch_p2_lot.py --only ltmm)
- **link**: https://physionet.org/content/ltmm/
- **ingestion**: ingest_ltmm.py (WFDB reader, units enforced per header) -> processed/canonical/<record>.pkl shards + --merge into the IMU manifest
