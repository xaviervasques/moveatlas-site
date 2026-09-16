# 6-minute walk test across the adult lifespan (single lower-back IMU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "6-minute walk test across the adult lifespan (single lower-back IMU)",
 "description": "6-minute walk test across the adult lifespan (single lower-back IMU). MoveAtlas imu family. 60 subjects. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.7954157",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "C1 Normal adult movement",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.c.7954157",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Carpinella, Ilaria"
  },
  {
   "@type": "Person",
   "name": "Ferrarin, Maurizio"
  },
  {
   "@type": "Person",
   "name": "Bailo, Gaia"
  },
  {
   "@type": "Person",
   "name": "Lencioni, Tiziana"
  },
  {
   "@type": "Person",
   "name": "Lucchetti, Francesca"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>sixmwt_lifespan</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3 (explicit age conditioning); M2 |
| **Subjects** | 60 |
| **Ages** | 21-75 y, decade bins |
| **Status** | harmonized (2026-08-22) |
| **License** | CC BY 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("sixmwt_lifespan")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: direct_download (figshare collection)
- **Source**: <https://doi.org/10.6084/m9.figshare.c.7954157>

## Publications

- Carpinella, Ilaria; Ferrarin, Maurizio; Bailo, Gaia; Lencioni, Tiziana; Lucchetti, Francesca (2025). *Six-minute walk test instrumented with a single inertial sensor: dataset from healthy adults of different ages*. figshare. DOI: [10.6084/m9.figshare.c.7954157](https://doi.org/10.6084/m9.figshare.c.7954157)

```bibtex
@misc{sixmwt_lifespan_data_2025,
  title = {Six-minute walk test instrumented with a single inertial sensor: dataset from healthy adults of different ages},
  author = {Carpinella, Ilaria and Ferrarin, Maurizio and Bailo, Gaia and Lencioni, Tiziana and Lucchetti, Francesca},
  year = {2025},
  doi = {10.6084/m9.figshare.c.7954157},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: sixmwt_lifespan
- **family**: imu
- **MoveAtlas cells**: C1, C3 (explicit age conditioning); M2
- **population**: 60 healthy, 10 per decade, 21-75 y
- **n_subjects**: 60
- **age**: 21-75 y, decade bins
- **signal**: acc+gyro 100 Hz at L5 + 15 gait metrics + events + MATLAB code
- **license**: CC BY 4.0; redistribution: yes
- **access**: direct_download (figshare collection)
- **link**: https://doi.org/10.6084/m9.figshare.c.7954157
- **citation**: Sci Data 2025, doi 10.1038/s41597-025-06506-3
