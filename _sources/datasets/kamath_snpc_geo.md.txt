# Kamath 2022 human SNpc snRNA-seq (GEO GSE178265)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Kamath 2022 human SNpc snRNA-seq (GEO GSE178265)",
 "description": "Kamath 2022 human SNpc snRNA-seq (GEO GSE178265). MoveAtlas bio family. licence GEO open supplementary.",
 "identifier": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178265",
 "license": "GEO open supplementary (public-domain-like)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M10 Histology / transcr."
 ],
 "url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178265",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>kamath_snpc_geo</code>

<span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | M10 (parkinsonism substrate) |
| **Subjects** | donors per GEO record |
| **Status** | acquired (2026-08-26) |
| **License** | GEO open supplementary (public-domain-like) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("kamath_snpc_geo")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: GEO open supplementary (public-domain-like)
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only kamath_snpc_geo)
- **Source**: <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178265>

## Publications

- Kamath, Tushar; Abdulraouf, Abdulraouf; Burris, S. J.; Langlieb, Jonah; Gazestani, Vahid; Nadaf, Naeem M.; Balderrama, Karol; Vanderburg, Charles; Macosko, Evan Z. (2022). *Single-cell genomic profiling of human dopamine neurons identifies a population that selectively degenerates in Parkinson’s disease*. Nature Neuroscience. DOI: [10.1038/s41593-022-01061-1](https://doi.org/10.1038/s41593-022-01061-1)

```bibtex
@article{kamath_snpc_geo_paper_2022,
  title = {Single-cell genomic profiling of human dopamine neurons identifies a population that selectively degenerates in Parkinson’s disease},
  author = {Kamath, Tushar and Abdulraouf, Abdulraouf and Burris, S. J. and Langlieb, Jonah and Gazestani, Vahid and Nadaf, Naeem M. and Balderrama, Karol and Vanderburg, Charles and Macosko, Evan Z.},
  year = {2022},
  doi = {10.1038/s41593-022-01061-1},
  journal = {Nature Neuroscience}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: kamath_snpc_geo
- **family**: bio
- **MoveAtlas cells**: M10 (parkinsonism substrate)
- **population**: PD vs control post-mortem SNpc; 101 samples; 22,048 DA neurons among 387k nuclei (human portion)
- **n_subjects**: donors per GEO record
- **signal**: count matrix + barcodes + features (mtx.gz, ~4.8 GB human)
- **license**: GEO open supplementary (public-domain-like); redistribution: yes
- **access**: direct_download (fetch_p2_lot.py --only kamath_snpc_geo)
- **link**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE178265
- **citation**: Nat Neurosci 2022, doi 10.1038/s41593-022-01061-1
