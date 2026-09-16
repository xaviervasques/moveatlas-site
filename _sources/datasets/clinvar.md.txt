# ClinVar bulk (movement-disorder gene subset)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ClinVar bulk (movement-disorder gene subset)",
 "description": "ClinVar bulk (movement-disorder gene subset). MoveAtlas bio family. licence NCBI public data.",
 "identifier": "https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/",
 "license": "NCBI public data (attribution requested)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M9 Genetics"
 ],
 "url": "https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>clinvar</code>

<span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | M9 |
| **Subjects** | n/a |
| **Status** | acquired (2026-08-26) |
| **License** | NCBI public data (attribution requested) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("clinvar")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NCBI public data (attribution requested)
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only clinvar_summary)
- **Source**: <https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/>

## Publications

- Landrum, Melissa J; Lee, Jennifer M; Benson, Mark; Brown, Garth R; Chao, Chen; Chitipiralla, Shanmuga; Gu, Baoshan; Hart, Jennifer; Hoffman, Douglas; Jang, Wonhee; Karapetyan, Karen; Katz, Kenneth; Liu, Chunlei; Maddipatla, Zenith; Malheiro, Adriana; McDaniel, Kurt; Ovetsky, Michael; Riley, George;  (2018). *ClinVar: improving access to variant interpretations and supporting evidence*. Nucleic Acids Research. DOI: [10.1093/nar/gkx1153](https://doi.org/10.1093/nar/gkx1153)

```bibtex
@article{clinvar_paper_2018,
  title = {ClinVar: improving access to variant interpretations and supporting evidence},
  author = {Landrum, Melissa J and Lee, Jennifer M and Benson, Mark and Brown, Garth R and Chao, Chen and Chitipiralla, Shanmuga and Gu, Baoshan and Hart, Jennifer and Hoffman, Douglas and Jang, Wonhee and Karapetyan, Karen and Katz, Kenneth and Liu, Chunlei and Maddipatla, Zenith and Malheiro, Adriana and McDaniel, Kurt and Ovetsky, Michael and Riley, George and Zhou, George and Holmes, J Bradley and Kattman, Brandi L and Maglott, Donna R},
  year = {2018},
  doi = {10.1093/nar/gkx1153},
  journal = {Nucleic Acids Research}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: clinvar
- **family**: bio
- **MoveAtlas cells**: M9
- **population**: variant-disease interpretations, millions of records; filter to movement genes (PRKN, LRRK2, GBA1, HTT, TOR1A, THAP1, ATXN*,...)
- **n_subjects**: n/a
- **signal**: variant_summary.txt.gz (~0.5 GB) + optional VCFs
- **license**: NCBI public data (attribution requested); redistribution: yes
- **access**: direct_download (fetch_p2_lot.py --only clinvar_summary)
- **link**: https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/
