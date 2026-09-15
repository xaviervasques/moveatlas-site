# MODYS-video (dyskinetic cerebral palsy)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MODYS-video (dyskinetic cerebral palsy)",
 "description": "MODYS-video (dyskinetic cerebral palsy). MoveAtlas pose family. 63 subjects. licence Zenodo open.",
 "identifier": "https://zenodo.org/records/5638470",
 "license": "Zenodo open",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A4 Dystonia",
  "A6 Athetosis",
  "A7 Chorea",
  "D3 Pyramidal syndromes",
  "M1 Pose / video"
 ],
 "url": "https://zenodo.org/records/5638470",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Haberfehlner, Helga"
  },
  {
   "@type": "Person",
   "name": "Bonouvrié, Laura A."
  },
  {
   "@type": "Person",
   "name": "Stolk, Karen L."
  },
  {
   "@type": "Person",
   "name": "van der Ven, S. Shankara"
  },
  {
   "@type": "Person",
   "name": "Aleo, Ignazio"
  },
  {
   "@type": "Person",
   "name": "van der Burg, Sven A."
  },
  {
   "@type": "Person",
   "name": "van der Krogt, Marjolein M."
  },
  {
   "@type": "Person",
   "name": "Buizer, Annemieke I."
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>modys_video</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Athetosis</span><span class="ma-tag">Chorea</span><span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A4, A6, A7, D3 (pediatric dyskinetic CP is choreoathetosis; DIS scores athetosis explicitly; D3 covers the spastic component); M1 |
| **Subjects** | 63 |
| **Status** | INGESTED v1: 94 canonical records |
| **License** | Zenodo open |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("modys_video")
records, meta = ds.get_data()
```

## License and access

- **License**: Zenodo open
- **Redistribution**: yes
- **Access route**: downloaded
- **Source**: <https://zenodo.org/records/5638470>

## Publications

- Haberfehlner, Helga; Bonouvrié, Laura A.; Stolk, Karen L.; van der Ven, S. Shankara; Aleo, Ignazio; van der Burg, Sven A.; van der Krogt, Marjolein M.; Buizer, Annemieke I. (2021). *MODYS-video: 2D Human pose estimation data and Dyskinesia Impairment Scale scores from children and young adults with dyskinetic cerebral palsy*. Zenodo. DOI: [10.5281/zenodo.5638470](https://doi.org/10.5281/zenodo.5638470)

```bibtex
@misc{modys_video_data_2021,
  title = {MODYS-video: 2D Human pose estimation data and Dyskinesia Impairment Scale scores from children and young adults with dyskinetic cerebral palsy},
  author = {Haberfehlner, Helga and Bonouvrié, Laura A. and Stolk, Karen L. and van der Ven, S. Shankara and Aleo, Ignazio and van der Burg, Sven A. and van der Krogt, Marjolein M. and Buizer, Annemieke I.},
  year = {2021},
  doi = {10.5281/zenodo.5638470},
  howpublished = {Zenodo},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: modys_video
- family: pose  (physical path: datasets/pose/modys_video)
- MoveAtlas cells: A4, A6, A7, D3 (pediatric dyskinetic CP is choreoathetosis; DIS scores athetosis explicitly; D3 covers the spastic component); M1
- population: 63 children/adolescents with dyskinetic CP; clinical scoring in README xlsx
- n_subjects: 63
- signal: stick-figure pose video derivatives (Zenodo 5638470)
- license: Zenodo open ; redistribution: yes
- access: downloaded
- status (2026-08-22): INGESTED v1: 94 canonical records
- link: https://zenodo.org/records/5638470
- ingestion: build_canonical_modys.py
- notes: one of very few public dystonia-adjacent movement datasets
