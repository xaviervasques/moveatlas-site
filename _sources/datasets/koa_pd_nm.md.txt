# KOA-PD-NM (gait video -> SAM3 silhouettes)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "KOA-PD-NM (gait video -> SAM3 silhouettes)",
 "description": "KOA-PD-NM (gait video -> SAM3 silhouettes). MoveAtlas pose family. 96 subjects. licence research only.",
 "identifier": "https://data.mendeley.com/datasets/44pfnysy89",
 "license": "research only, non-commercial",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "C1 Normal adult movement",
  "E4 Musculoskeletal",
  "M4 Silhouette"
 ],
 "url": "https://data.mendeley.com/datasets/44pfnysy89",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Kour, Navleen"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>koa_pd_nm</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Musculoskeletal</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3, C1, E4; M4 |
| **Subjects** | 96 |
| **Status** | INGESTED v1 (silhouette contract): 190 records / 96 subjects, 111,002 frames, 97.7% detected |
| **License** | research only, non-commercial |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("koa_pd_nm")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: research only, non-commercial
- **Redistribution**: no (video); derived silhouettes internal
- **Access route**: direct download (research use)
- **Source**: <https://data.mendeley.com/datasets/44pfnysy89>

## Publications

- Kour, Navleen (2020). *Gait Dataset for Knee Osteoarthritis and Parkinson's Disease Analysis With Severity Levels*. Mendeley. DOI: [10.17632/44pfnysy89.1](https://doi.org/10.17632/44pfnysy89.1)

```bibtex
@misc{koa_pd_nm_data_2020,
  title = {Gait Dataset for Knee Osteoarthritis and Parkinson's Disease Analysis With Severity Levels},
  author = {Kour, Navleen},
  year = {2020},
  doi = {10.17632/44pfnysy89.1},
  howpublished = {Mendeley},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: koa_pd_nm
- family: pose  (physical path: datasets/pose/koa_pd_nm)
- MoveAtlas cells: B2, B3, C1, E4; M4
- population: 50 knee osteoarthritis + 16 PD + 30 healthy; severity grades partition subjects (numbering RESTARTS per severity group: 001_KOA_EL and 001_KOA_MD are different people)
- n_subjects: 96
- signal: frontal/sagittal gait video (2 sequences per subject) -> SAM3 body-outline silhouette timeseries (64-pt contour + 8 shape scalars), 30.3/50 fps native
- license: research only, non-commercial ; redistribution: no (video); derived silhouettes internal
- access: direct download (research use)
- status (2026-08-22): INGESTED v1 (silhouette contract): 190 records / 96 subjects, 111,002 frames, 97.7% detected
- link: https://data.mendeley.com/datasets/44pfnysy89
- ingestion: SAM3 by owner -> build_canonical_silhouette.py; patient key koa_<COHORT>_<SEV>_<num>; sequences 01/02 = same subject, never split
- notes: 1 NM video of 191 not processed by SAM3 (59/60 NM); all 96 subjects covered. Link resolved 2026-08-23 from download_data.py, whose Mendeley public-file URLs all live under dataset id 44pfnysy89
