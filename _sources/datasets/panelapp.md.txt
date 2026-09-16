# Genomics England PanelApp movement panels

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Genomics England PanelApp movement panels",
 "description": "Genomics England PanelApp movement panels. MoveAtlas bio family. licence NHS GMS governance; no explicit open license shown.",
 "identifier": "https://panelapp.genomicsengland.co.uk/panels/540/",
 "license": "NHS GMS governance; no explicit open license shown",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M9 Genetics"
 ],
 "url": "https://panelapp.genomicsengland.co.uk/panels/540/",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>panelapp</code>

<span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | M9 |
| **Subjects** | n/a |
| **Status** | acquired (2026-08-22) |
| **License** | NHS GMS governance; no explicit open license shown |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("panelapp")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NHS GMS governance; no explicit open license shown
- **Redistribution**: no
- **Access route**: direct_download (panel pages; API robots-blocked to our fetcher)
- **Source**: <https://panelapp.genomicsengland.co.uk/panels/540/>

## Publications

- Martin, Antonio Rueda; Williams, Eleanor; Foulger, Rebecca E.; Leigh, Sarah; Daugherty, Louise C.; Niblock, Olivia; Leong, Ivone U. S.; Smith, Katherine R.; Gerasimenko, Oleg; Haraldsdottir, Eik; Thomas, Ellen; Scott, Richard H.; Baple, Emma; Tucci, Arianna; Brittain, Helen; de Burca, Anna; Ibañez,  (2019). *PanelApp crowdsources expert knowledge to establish consensus diagnostic gene panels*. Nature Genetics. DOI: [10.1038/s41588-019-0528-2](https://doi.org/10.1038/s41588-019-0528-2)

```bibtex
@article{panelapp_paper_2019,
  title = {PanelApp crowdsources expert knowledge to establish consensus diagnostic gene panels},
  author = {Martin, Antonio Rueda and Williams, Eleanor and Foulger, Rebecca E. and Leigh, Sarah and Daugherty, Louise C. and Niblock, Olivia and Leong, Ivone U. S. and Smith, Katherine R. and Gerasimenko, Oleg and Haraldsdottir, Eik and Thomas, Ellen and Scott, Richard H. and Baple, Emma and Tucci, Arianna and Brittain, Helen and de Burca, Anna and Ibañez, Kristina and Kasperaviciute, Dalia and Smedley, Damian and Caulfield, Mark and Rendon, Augusto and McDonagh, Ellen M.},
  year = {2019},
  doi = {10.1038/s41588-019-0528-2},
  journal = {Nature Genetics}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: panelapp
- **family**: bio
- **MoveAtlas cells**: M9
- **population**: curated diagnostic gene panels: 540 + 847 dystonia/chorea (adult + childhood), 192 early-onset dystonia, 477 childhood ataxia, 1669 adult neurology superpanel
- **n_subjects**: n/a
- **signal**: signed-off panel TSVs
- **license**: NHS GMS governance; no explicit open license shown; redistribution: no, no written licence = pointer; the panels re-fetch freely from the PanelApp pages
- **access**: direct_download (panel pages; API robots-blocked to our fetcher)
- **link**: https://panelapp.genomicsengland.co.uk/panels/540/
