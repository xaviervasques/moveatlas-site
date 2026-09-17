# GaitRec (bilateral GRF, 75k trials)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "GaitRec (bilateral GRF, 75k trials)",
 "description": "GaitRec (bilateral GRF, 75k trials). MoveAtlas imu family. 2,295 subjects. licence CC0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.4788012",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "E4 Musculoskeletal",
  "M3 Plantar force"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.c.4788012",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Horsak, Brian"
  },
  {
   "@type": "Person",
   "name": "Djordje Slijepcevic"
  },
  {
   "@type": "Person",
   "name": "Anna-Maria Raberger"
  },
  {
   "@type": "Person",
   "name": "Caterine Schwab"
  },
  {
   "@type": "Person",
   "name": "Worisch, Marianne"
  },
  {
   "@type": "Person",
   "name": "Zeppelzauer, Matthias"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>gaitrec</code>

<span class="ma-tag">Musculoskeletal</span><span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | E4; M3 |
| **Subjects** | 2,295 |
| **Status** | harmonized (2026-08-27) |
| **License** | CC0 (all 23 figshare collection items, verified 2026-08-22) |
| **MoveAtlas record** | [10.5281/zenodo.22313441](https://doi.org/10.5281/zenodo.22313441) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("gaitrec")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (all 23 figshare collection items, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download
- **Source**: <https://doi.org/10.6084/m9.figshare.c.4788012>

## Publications

- Horsak, Brian; Djordje Slijepcevic; Anna-Maria Raberger; Caterine Schwab; Worisch, Marianne; Zeppelzauer, Matthias (2020). *GaitRec: A large-scale ground reaction force dataset of healthy and impaired gait*. figshare. DOI: [10.6084/m9.figshare.c.4788012](https://doi.org/10.6084/m9.figshare.c.4788012)

```bibtex
@misc{gaitrec_data_2020,
  title = {GaitRec: A large-scale ground reaction force dataset of healthy and impaired gait},
  author = {Horsak, Brian and Djordje Slijepcevic and Anna-Maria Raberger and Caterine Schwab and Worisch, Marianne and Zeppelzauer, Matthias},
  year = {2020},
  doi = {10.6084/m9.figshare.c.4788012},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: gaitrec
- **family**: imu
- **MoveAtlas cells**: E4; M3
- **population**: 2,084 musculoskeletal patients (hip/knee/ankle/calcaneus classes) + 211 healthy
- **n_subjects**: 2,295
- **signal**: bilateral 3-component GRF + CoP, raw 250 Hz + stance-normalized (CSV)
- **license**: CC0 (all 23 figshare collection items, verified 2026-08-22); redistribution: yes
- **access**: direct_download
- **link**: https://doi.org/10.6084/m9.figshare.c.4788012
- **citation**: Sci Data 2020, doi 10.1038/s41597-020-0481-z
