# FoG turning-in-place (Filho 2022)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "FoG turning-in-place (Filho 2022)",
 "description": "FoG turning-in-place (Filho 2022). MoveAtlas pose family. 50 subjects. licence CC0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.14984667",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B5 Freezing of gait",
  "M1 Pose / video",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.14984667",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Boari, Daniel"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>fog_turning_filho</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M1, M2 (video + IMU synchronized) |
| **Subjects** | 50 |
| **Status** | INGESTED v1: 106 + 106 records; one of the two real pose<->IMU pairs on disk (stage B table) |
| **License** | CC0 (figshare item 14984667) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("fog_turning_filho")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (figshare item 14984667)
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://doi.org/10.6084/m9.figshare.14984667>

## Publications

- Boari, Daniel (2022). *A public dataset of video, acceleration, angular velocity, and clinical scales in individuals with Parkinson's disease during the turning-in-place task*. figshare. DOI: [10.6084/m9.figshare.14984667](https://doi.org/10.6084/m9.figshare.14984667)
- Ribeiro De Souza, Caroline; Miao, Runfeng; Ávila De Oliveira, Júlia; Cristina De Lima-Pardini, Andrea; Fragoso De Campos, Débora; Silva-Batista, Carla; Teixeira, Luis; Shokur, Solaiman; Mohamed, Bouri; Coelho, Daniel Boari (2022). *A Public Data Set of Videos, Inertial Measurement Unit, and Clinical Scales of Freezing of Gait in Individuals With Parkinson's Disease During a Turning-In-Place Task*. Frontiers in Neuroscience. DOI: [10.3389/fnins.2022.832463](https://doi.org/10.3389/fnins.2022.832463)

```bibtex
@misc{fog_turning_filho_data_2022,
  title = {A public dataset of video, acceleration, angular velocity, and clinical scales in individuals with Parkinson's disease during the turning-in-place task},
  author = {Boari, Daniel},
  year = {2022},
  doi = {10.6084/m9.figshare.14984667},
  howpublished = {figshare},
  note = {dataset}
}
@article{fog_turning_filho_paper_2022,
  title = {A Public Data Set of Videos, Inertial Measurement Unit, and Clinical Scales of Freezing of Gait in Individuals With Parkinson's Disease During a Turning-In-Place Task},
  author = {Ribeiro De Souza, Caroline and Miao, Runfeng and Ávila De Oliveira, Júlia and Cristina De Lima-Pardini, Andrea and Fragoso De Campos, Débora and Silva-Batista, Carla and Teixeira, Luis and Shokur, Solaiman and Mohamed, Bouri and Coelho, Daniel Boari},
  year = {2022},
  doi = {10.3389/fnins.2022.832463},
  journal = {Frontiers in Neuroscience}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: fog_turning_filho
- family: pose  (physical path: datasets/pose/fog_turning_filho)
- MoveAtlas cells: B5; M1, M2 (video + IMU synchronized)
- population: 50 PD (35 with usable synchronized pairs per v1 ingestion); age, disease duration, LEDD, more-affected side
- n_subjects: 50
- signal: video + IMU (ACC ML/AP/SI in g, GYR ML/AP in deg/s) turning protocol
- license: CC0 (figshare item 14984667) ; redistribution: yes
- access: downloaded
- status (2026-08-22): INGESTED v1: 106 + 106 records; one of the two real pose<->IMU pairs on disk (stage B table)
- link: https://doi.org/10.6084/m9.figshare.14984667
- citation: Frontiers in Neuroscience 2022, doi 10.3389/fnins.2022.832463
- ingestion: build_canonical_imu.py (fog_turning mapping). SPLIT FOLDER, same as capture24: card and raw/ under datasets/pose/fog_turning_filho, the 106 canonical records under datasets/imu/fog_turning_filho/processed/. These two are the only datasets in the repo whose raw and processed sit in different family folders (checked 2026-08-23)
- notes: link resolved 2026-08-23: the download_data.py file ids 33413717 (IMU.zip) and 31544582 (PDFEinfo.csv) both belong to figshare article 14984667 per api.figshare.com; Videos.zip (5.0 GB, same article) was never downloaded
