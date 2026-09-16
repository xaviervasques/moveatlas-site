# Fox Insight / Fox DEN (PD mega-cohort)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Fox Insight / Fox DEN (PD mega-cohort)",
 "description": "Fox Insight / Fox DEN (PD mega-cohort). MoveAtlas bio family. licence DUA + publication policy.",
 "identifier": "https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp",
 "license": "DUA + publication policy",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "B2 Bradykinesia",
  "M9 Genetics",
  "M12 Clinical scales"
 ],
 "url": "https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>foxinsight</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Genetics</span><span class="ma-tag">Clinical scales</span>

| | |
|---|---|
| **Taxonomy cells** | B2 self-report + genetics; M9, M12 |
| **Subjects** | >50,000 |
| **Status** | documented access barrier (2026-08-22) |
| **License** | DUA + publication policy |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("foxinsight")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: DUA + publication policy
- **Redistribution**: no
- **Access route**: application (Fox DEN)
- **Source**: <https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp>

## Publications

- Smolensky, Luba; Amondikar, Ninad; Crawford, Karen; Neu, Scott; Kopil, Catherine M.; Daeschler, Margaret; Riley, Lindsey; Agee, Michelle; Alipanahi, Babak; Auton, Adam; Bell, Robert K.; Bryc, Katarzyna; Cannon, Paul; Clarke, Sarah; Elson, Sarah L.; Fonseca, Peter; Fontanillas, Pierre; Furlotte, Nich (2020). *Fox Insight collects online, longitudinal patient-reported outcomes and genetic data on Parkinson’s disease*. Scientific Data. DOI: [10.1038/s41597-020-0401-2](https://doi.org/10.1038/s41597-020-0401-2)

```bibtex
@article{foxinsight_paper_2020,
  title = {Fox Insight collects online, longitudinal patient-reported outcomes and genetic data on Parkinson’s disease},
  author = {Smolensky, Luba and Amondikar, Ninad and Crawford, Karen and Neu, Scott and Kopil, Catherine M. and Daeschler, Margaret and Riley, Lindsey and Agee, Michelle and Alipanahi, Babak and Auton, Adam and Bell, Robert K. and Bryc, Katarzyna and Cannon, Paul and Clarke, Sarah and Elson, Sarah L. and Fonseca, Peter and Fontanillas, Pierre and Furlotte, Nicholas A. and Hicks, Barry and Hinds, David A. and Heilbron, Karl and Huber, Karen E. and Jewett, Ethan M. and Jiang, Yunxuan and Kleinman, Aaron and Lin, Keng-Han and Litterman, Nadia K. and Luff, Marie and McIntyre, Matthew H. and McManus, Kimberly F. and Mountain, Joanna L. and Noblin, Elizabeth S. and Northover, Carrie A. M. and Pitts, Steven J. and Poznik, G. David and Rowbotham, Helen M. and Sathirapongsasuti, J. Fah and Schloetter, Madeleine and Shelton, Janie F. and Shringarpure, Suyash and Tian, Chao and Tung, Joyce Y. and Vacic, Vladimir and Wang, Xin and Wilson, Catherine H. and Wojcicki, Anne and Yu, Linda P. C. and Brown, Ethan and Toga, Arthur W. and Tanner, Caroline},
  year = {2020},
  doi = {10.1038/s41597-020-0401-2},
  journal = {Scientific Data}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: foxinsight
- **family**: bio
- **MoveAtlas cells**: B2 self-report + genetics; M9, M12
- **population**: >50,000 PD participants, longitudinal questionnaires + 23andMe genetics + microbiome
- **n_subjects**: >50,000
- **signal**: tabular questionnaire cuts + genetic data (institutional gating)
- **license**: DUA + publication policy; redistribution: no
- **access**: application (Fox DEN)
- **link**: https://foxinsight-info.michaeljfox.org/insight/explore/insight.jsp
