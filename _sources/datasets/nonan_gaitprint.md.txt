# NONAN GaitPrint (older adults, 16 IMU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NONAN GaitPrint (older adults, 16 IMU)",
 "description": "NONAN GaitPrint (older adults, 16 IMU). MoveAtlas imu family. 41 (complete) subjects. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.27815034",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "C3 Aging",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.27815034",
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
   "name": "Kim, Seung Kyeom"
  },
  {
   "@type": "Person",
   "name": "Mangalam, Madhur"
  },
  {
   "@type": "Person",
   "name": "Sommerfeld, Joel H."
  },
  {
   "@type": "Person",
   "name": "Brink, Kolby"
  },
  {
   "@type": "Person",
   "name": "Grunkemeyer, Alli"
  },
  {
   "@type": "Person",
   "name": "manifrenti, marilena kalaitzi"
  },
  {
   "@type": "Person",
   "name": "Charles, Anaelle"
  },
  {
   "@type": "Person",
   "name": "Shakerian, Narges"
  },
  {
   "@type": "Person",
   "name": "Haghighatnejad, Mehrnoush"
  },
  {
   "@type": "Person",
   "name": "Mastorakis, Spyridon"
  },
  {
   "@type": "Person",
   "name": "Stergiou, Nick"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>nonan_gaitprint</code>

<span class="ma-tag">Aging</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | C3; M2 |
| **Subjects** | 41 (complete) |
| **Ages** | 56+ y (64.7 +/- 7.5) |
| **Status** | harmonized (2026-08-27) |
| **License** | CC BY 4.0 (figshare item metadata, verified 2026-08-22) |
| **MoveAtlas record** | [10.5281/zenodo.22310799](https://doi.org/10.5281/zenodo.22310799) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("nonan_gaitprint")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (figshare item metadata, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download
- **Source**: <https://doi.org/10.6084/m9.figshare.27815034>

## Publications

- Wiles, Tyler; Kim, Seung Kyeom; Mangalam, Madhur; Sommerfeld, Joel H.; Brink, Kolby; Grunkemeyer, Alli; manifrenti, marilena kalaitzi; Charles, Anaelle; Shakerian, Narges; Haghighatnejad, Mehrnoush; Mastorakis, Spyridon; Stergiou, Nick; Likens, Aaron (2025). *NONAN GaitPrint: An IMU gait database of healthy older adults*. figshare. DOI: [10.6084/m9.figshare.27815034](https://doi.org/10.6084/m9.figshare.27815034)

```bibtex
@misc{nonan_gaitprint_data_2025,
  title = {NONAN GaitPrint: An IMU gait database of healthy older adults},
  author = {Wiles, Tyler and Kim, Seung Kyeom and Mangalam, Madhur and Sommerfeld, Joel H. and Brink, Kolby and Grunkemeyer, Alli and manifrenti, marilena kalaitzi and Charles, Anaelle and Shakerian, Narges and Haghighatnejad, Mehrnoush and Mastorakis, Spyridon and Stergiou, Nick and Likens, Aaron},
  year = {2025},
  doi = {10.6084/m9.figshare.27815034},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: nonan_gaitprint
- **family**: imu
- **MoveAtlas cells**: C3; M2
- **population**: healthy older adults, 18 x 4-min overground trials over 2 days; SIBLING HUNT there are NO sibling articles, article 27815034 carries ALL 41 subjects (44 files, 57.8 GB); COMPLETE AND RE-INGESTED 2026-08-28: 719 canonical IMU records / 41 subjects / 47.7 h. The true sibling is the separate YOUNG-adults collection (nonan_gaitprint_young, own card)
- **n_subjects**: 41 (complete)
- **age**: 56+ y (64.7 +/- 7.5)
- **signal**: full-body 16-IMU at 200 Hz, raw kinematics + spatiotemporal variables
- **license**: CC BY 4.0 (figshare item metadata, verified 2026-08-22); redistribution: yes
- **access**: direct_download
- **link**: https://doi.org/10.6084/m9.figshare.27815034
