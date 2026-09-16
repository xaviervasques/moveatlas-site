# CARE-PD (9-cohort PD gait, canonicalized SMPL)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CARE-PD (9-cohort PD gait, canonicalized SMPL)",
 "description": "CARE-PD (9-cohort PD gait, canonicalized SMPL). MoveAtlas pose family. 362 subjects. licence CC BY-NC-ND 4.0.",
 "identifier": "https://neurips2025.care-pd.ca/index.html",
 "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "M1 Pose / video"
 ],
 "url": "https://neurips2025.care-pd.ca/index.html",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Adeli, Vida"
  },
  {
   "@type": "Person",
   "name": "Klabučar, Ivan"
  },
  {
   "@type": "Person",
   "name": "Rajabi, Javad"
  },
  {
   "@type": "Person",
   "name": "Filtjens, Benjamin"
  },
  {
   "@type": "Person",
   "name": "Mehraban, Soroush"
  },
  {
   "@type": "Person",
   "name": "Diwei Wang"
  },
  {
   "@type": "Person",
   "name": "Trung-Hieu Hoang"
  },
  {
   "@type": "Person",
   "name": "N. Do, Minh"
  },
  {
   "@type": "Person",
   "name": "Hyewon Seo"
  },
  {
   "@type": "Person",
   "name": "Muller, Candice"
  },
  {
   "@type": "Person",
   "name": "Boari Coelho, Daniel"
  },
  {
   "@type": "Person",
   "name": "es de Oliveira, Claudia Eunice de"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>care_pd</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3; M1 |
| **Subjects** | 362 |
| **Status** | harmonized (2026-08-25) |
| **License** | CC BY-NC-ND 4.0, 'Creative Commons Attribution-NonCommercial-NoDerivatives 4.0... may be used for non-commercial research and educational purposes with appropriate citation but may not be modified or redistributed in altered form'. The old tag-vs-README ambiguity (pinned 2026-08-22) is resolved in the tag's favour. Per-cohort originals differ (BMCLab and DNE are CC BY 4.0); the GitHub MIT covers t... |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("care_pd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-NC-ND 4.0, 'Creative Commons Attribution-NonCommercial-NoDerivatives 4.0... may be used for non-commercial research and educational purposes with appropriate citation but may not be modified or redistributed in altered form'. The old tag-vs-README ambiguity (pinned 2026-08-22) is resolved in the tag's favour. Per-cohort originals differ (BMCLab and DNE are CC BY 4.0); the GitHub MIT covers t
- **Redistribution**: no
- **Access route**: free download (moved 2026-08-25: HuggingFace vida-adl/CARE-PD is public again, plus UofT Borealis doi:10.5683/SP3/TWIKMK; the old TaatiTeam slug 404s, which looked like a lockdown and was a relocation)
- **Source**: <https://neurips2025.care-pd.ca/index.html>

## Publications

- Adeli, Vida; Klabučar, Ivan; Rajabi, Javad; Filtjens, Benjamin; Mehraban, Soroush; Diwei Wang; Trung-Hieu Hoang; N. Do, Minh; Hyewon Seo; Muller, Candice; Boari Coelho, Daniel; es de Oliveira, Claudia Eunice de; Ginis, Pieter; Gilat, Moran; Nieuwboer, Alice; Spildooren, Joke; as Mckay, Lucas; Hyeokh (2025). *Care-PD*. Borealis. DOI: [10.5683/sp3/twikmk](https://doi.org/10.5683/sp3/twikmk)
- Adeli, Vida; Klabucar, Ivan; Rajabi, Javad; Filtjens, Benjamin; Mehraban, Soroush; Wang, Diwei; Seo, Hyewon; Hoang, Trung-Hieu; Do, Minh N.; Muller, Candice; Oliveira, Claudia; Coelho, Daniel Boari; Ginis, Pieter; Gilat, Moran; Nieuwboer, Alice; Spildooren, Joke; Mckay, Lucas; Kwon, Hyeokhyen; Cliff (2025). *CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson's Disease Gait Assessment*. arXiv. DOI: [10.48550/arxiv.2510.04312](https://doi.org/10.48550/arxiv.2510.04312)

```bibtex
@misc{care_pd_data_2025,
  title = {Care-PD},
  author = {Adeli, Vida and Klabučar, Ivan and Rajabi, Javad and Filtjens, Benjamin and Mehraban, Soroush and Diwei Wang and Trung-Hieu Hoang and N. Do, Minh and Hyewon Seo and Muller, Candice and Boari Coelho, Daniel and es de Oliveira, Claudia Eunice de and Ginis, Pieter and Gilat, Moran and Nieuwboer, Alice and Spildooren, Joke and as Mckay, Lucas and Hyeokhyen Kwon and Clifford, Gari and D Esper, Christine and A Factor, Stewart and Genias, Imari and Amirhossein Dadashzadeh and C Shum, Leia and Alan L. Whone and Mirmehdi, Majid and Iaboni, Andrea and Taati, Babak},
  year = {2025},
  doi = {10.5683/sp3/twikmk},
  howpublished = {Borealis},
  note = {dataset}
}
@article{care_pd_paper_2025,
  title = {CARE-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson's Disease Gait Assessment},
  author = {Adeli, Vida and Klabucar, Ivan and Rajabi, Javad and Filtjens, Benjamin and Mehraban, Soroush and Wang, Diwei and Seo, Hyewon and Hoang, Trung-Hieu and Do, Minh N. and Muller, Candice and Oliveira, Claudia and Coelho, Daniel Boari and Ginis, Pieter and Gilat, Moran and Nieuwboer, Alice and Spildooren, Joke and Mckay, Lucas and Kwon, Hyeokhyen and Clifford, Gari and Esper, Christine and Factor, Stewart and Genias, Imari and Dadashzadeh, Amirhossein and Shum, Leia and Whone, Alan and Mirmehdi, Majid and Iaboni, Andrea and Taati, Babak},
  year = {2025},
  doi = {10.48550/arxiv.2510.04312},
  journal = {arXiv}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: care_pd
- **family**: pose
- **MoveAtlas cells**: B2, B3; M1
- **population**: 362 subjects, 9 cohorts, 8 sites; UPDRS_GAIT labels on 4 cohorts (3DGait, BMCLab, PD-GaM, T-SDU-PD)
- **n_subjects**: 362
- **signal**: 3D positions derived from canonicalized SMPL (24 joints), 25-150 fps per cohort, ~3.72 M frames, 8,476 walks
- **license**: CC BY-NC-ND 4.0, 'Creative Commons Attribution-NonCommercial-NoDerivatives 4.0... may be used for non-commercial research and educational purposes with appropriate citation but may not be modified or redistributed in altered form'. The old tag-vs-README ambiguity (pinned 2026-08-22) is resolved in the tag's favour. Per-cohort originals differ (BMCLab and DNE are CC BY 4.0); the GitHub MIT covers the CODE only; redistribution: NO: ND. Harmonized/derived tensors must never be redistributed, and training that publishes a model is a derivative-work risk: EVAL ONLY
- **access**: free download (moved 2026-08-25: HuggingFace vida-adl/CARE-PD is public again, plus UofT Borealis doi:10.5683/SP3/TWIKMK; the old TaatiTeam slug 404s, which looked like a lockdown and was a relocation)
- **link**: https://neurips2025.care-pd.ca/index.html
- **ingestion**: extract_care_pd.py (SMPL -> 24-joint positions, conda env smpl) then build_canonical.py (smpl_carepd mapping). Verification: floor y~0, head y~1.5 m, UPDRS_GAIT distribution conform (3DGait {0:24,1:42,2:14,3:10})
