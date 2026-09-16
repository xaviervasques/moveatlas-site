# NONAN GaitPrint young adults (16 IMU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NONAN GaitPrint young adults (16 IMU)",
 "description": "NONAN GaitPrint young adults (16 IMU). MoveAtlas imu family. 35 subjects. licence CC0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.6415061",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
 "url": "https://doi.org/10.6084/m9.figshare.c.6415061",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Wiles, Tyler"
  },
  {
   "@type": "Person",
   "name": "Mangalam, Madhur"
  },
  {
   "@type": "Person",
   "name": "Sommerfeld, Joel"
  },
  {
   "@type": "Person",
   "name": "Kim, Seung"
  },
  {
   "@type": "Person",
   "name": "Brink, Kolby"
  },
  {
   "@type": "Person",
   "name": "Charles, Anaelle"
  },
  {
   "@type": "Person",
   "name": "Grunkemeyer, Alli"
  },
  {
   "@type": "Person",
   "name": "Manifrenti, Marilena"
  },
  {
   "@type": "Person",
   "name": "Mastorakis, Spyridon"
  },
  {
   "@type": "Person",
   "name": "Stergiou, Nicholas"
  },
  {
   "@type": "Person",
   "name": "Likens, Aaron"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>nonan_gaitprint_young</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3 (young end of the age axis); M2 |
| **Subjects** | 35 |
| **Ages** | young adults (exact range: read the descriptor at ingestion) |
| **Status** | harmonized (2026-08-28) |
| **License** | CC0 (verified per article on the figshare API, 2026-08-28) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nonan_gaitprint_young")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (verified per article on the figshare API, 2026-08-28)
- **Redistribution**: yes
- **Access route**: direct_download (figshare collection, one article per subject)
- **Source**: <https://doi.org/10.6084/m9.figshare.c.6415061>

## Publications

- Wiles, Tyler; Mangalam, Madhur; Sommerfeld, Joel; Kim, Seung; Brink, Kolby; Charles, Anaelle; Grunkemeyer, Alli; Manifrenti, Marilena; Mastorakis, Spyridon; Stergiou, Nicholas; Likens, Aaron (2023). *NONAN GaitPrint: An IMU gait database of healthy young adults*. figshare. DOI: [10.6084/m9.figshare.c.6415061](https://doi.org/10.6084/m9.figshare.c.6415061)

```bibtex
@misc{nonan_gaitprint_young_data_2023,
  title = {NONAN GaitPrint: An IMU gait database of healthy young adults},
  author = {Wiles, Tyler and Mangalam, Madhur and Sommerfeld, Joel and Kim, Seung and Brink, Kolby and Charles, Anaelle and Grunkemeyer, Alli and Manifrenti, Marilena and Mastorakis, Spyridon and Stergiou, Nicholas and Likens, Aaron},
  year = {2023},
  doi = {10.6084/m9.figshare.c.6415061},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: nonan_gaitprint_young
- **family**: imu
- **MoveAtlas cells**: C1, C3 (young end of the age axis); M2
- **population**: healthy young adults, same Noraxon 16-IMU 200 Hz overground protocol as the older cohort, 18 x 4-min trials over 2 days; published as one figshare article per subject (collection 6415061)
- **n_subjects**: 35
- **age**: young adults (exact range: read the descriptor at ingestion)
- **signal**: full-body 16-IMU at 200 Hz, raw kinematics + spatiotemporal variables
- **license**: CC0 (verified per article on the figshare API, 2026-08-28); redistribution: yes
- **access**: direct_download (figshare collection, one article per subject)
- **link**: https://doi.org/10.6084/m9.figshare.c.6415061
- **citation**: Sci Data 2023, doi 10.1038/s41597-023-02704-z
