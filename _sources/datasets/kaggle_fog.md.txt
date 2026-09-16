# Kaggle tlVMC Freezing of Gait

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Kaggle tlVMC Freezing of Gait",
 "description": "Kaggle tlVMC Freezing of Gait. MoveAtlas imu family. 136 subjects. licence Kaggle competition terms.",
 "identifier": "https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction",
 "license": "Kaggle competition terms",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B5 Freezing of gait",
  "M2 Inertial (IMU)"
 ],
 "url": "https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>kaggle_fog</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M2 |
| **Subjects** | 136 |
| **Status** | harmonized |
| **License** | Kaggle competition terms |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("kaggle_fog")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: Kaggle competition terms
- **Redistribution**: no
- **Access route**: Kaggle account download
- **Source**: <https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction>

## Publications

- Salomon, Amit; Gazit, Eran; Ginis, Pieter; Urazalinov, Baurzhan; Takoi, Hirokazu; Yamaguchi, Taiki; Goda, Shuhei; Lander, David; Lacombe, Julien; Sinha, Aditya Kumar; Nieuwboer, Alice; Kirsch, Leslie C.; Holbrook, Ryan; Manor, Brad; Hausdorff, Jeffrey M. (2024). *A machine learning contest enhances automated freezing of gait detection and reveals time-of-day effects*. Nature Communications. DOI: [10.1038/s41467-024-49027-0](https://doi.org/10.1038/s41467-024-49027-0)

```bibtex
@article{kaggle_fog_paper_2024,
  title = {A machine learning contest enhances automated freezing of gait detection and reveals time-of-day effects},
  author = {Salomon, Amit and Gazit, Eran and Ginis, Pieter and Urazalinov, Baurzhan and Takoi, Hirokazu and Yamaguchi, Taiki and Goda, Shuhei and Lander, David and Lacombe, Julien and Sinha, Aditya Kumar and Nieuwboer, Alice and Kirsch, Leslie C. and Holbrook, Ryan and Manor, Brad and Hausdorff, Jeffrey M.},
  year = {2024},
  doi = {10.1038/s41467-024-49027-0},
  journal = {Nature Communications}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: kaggle_fog
- **family**: imu
- **MoveAtlas cells**: B5; M2
- **population**: 136 unique PD subjects (173 subject-visits); UPDRS-III on/off, NFOGQ
- **n_subjects**: 136
- **signal**: lower-back accelerometer: tdcsfog 128 Hz, defog 100 Hz, daily
- **license**: Kaggle competition terms; redistribution: NO (competition data, redistribution restricted)
- **access**: Kaggle account download
- **link**: https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction
- **ingestion**: build_canonical_imu.py (kaggle_fog mapping)
