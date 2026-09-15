# Multi-region PD single-nucleus atlas (2.1M nuclei)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Multi-region PD single-nucleus atlas (2.1M nuclei)",
 "description": "Multi-region PD single-nucleus atlas (2.1M nuclei). MoveAtlas bio family. 100 subjects. licence CELLxGENE policy CC BY 4.0.",
 "identifier": "https://cellxgene.cziscience.com/collections/d5d0df8f-4eee-49d8-a221-a288f50a1590",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M10 Histology / transcr."
 ],
 "url": "https://cellxgene.cziscience.com/collections/d5d0df8f-4eee-49d8-a221-a288f50a1590",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>cellxgene_pd_multiregion</code>

<span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | M10 |
| **Subjects** | 100 |
| **Status** | NEW 2026-08-22 (second hunt): HUMAN QUEUE (size decision before download) |
| **License** | CELLxGENE policy CC BY 4.0 (confirm on collection page) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("cellxgene_pd_multiregion")
records, meta = ds.get_data()
```

## License and access

- **License**: CELLxGENE policy CC BY 4.0 (confirm on collection page)
- **Redistribution**: yes if CC BY
- **Access route**: direct_download (30.5 GB, deliberate pull)
- **Source**: <https://cellxgene.cziscience.com/collections/d5d0df8f-4eee-49d8-a221-a288f50a1590>

## Publications

- N. M., Prashant; Fullard, John F.; Clarence, Tereza; Mathur, Deepika; Casey, Clara; Hennigan, Evelyn; Alvia, Marcela; Krause-Massaguer, Joana; Barreda, Ayled; Davis, David A.; Vontell, Regina T.; Garamszegi, Susanna P.; Vance, Jeffery M.; Sang, Lorelle; Chatigny, Michael; Vismer, David; Landin, Barr (2024). *A multi-region single nucleus transcriptomic atlas of Parkinson’s disease*. Scientific Data. DOI: [10.1038/s41597-024-04117-y](https://doi.org/10.1038/s41597-024-04117-y)

```bibtex
@article{cellxgene_pd_multiregion_paper_2024,
  title = {A multi-region single nucleus transcriptomic atlas of Parkinson’s disease},
  author = {N. M., Prashant and Fullard, John F. and Clarence, Tereza and Mathur, Deepika and Casey, Clara and Hennigan, Evelyn and Alvia, Marcela and Krause-Massaguer, Joana and Barreda, Ayled and Davis, David A. and Vontell, Regina T. and Garamszegi, Susanna P. and Vance, Jeffery M. and Sang, Lorelle and Chatigny, Michael and Vismer, David and Landin, Barry and Burstein, David and Lee, Donghoon and Voloudakis, Georgios and Berretta, Sabina and Haroutunian, Vahram and Scott, William K. and Bendl, Jaroslav and Roussos, Panos},
  year = {2024},
  doi = {10.1038/s41597-024-04117-y},
  journal = {Scientific Data}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: cellxgene_pd_multiregion
- family: bio  (physical path: datasets/bio/cellxgene_pd_multiregion)
- MoveAtlas cells: M10
- population: 100 post-mortem PD cases + controls, 5 regions incl. GPm and dorsal motor vagus
- n_subjects: 100
- signal: single h5ad ~30.5 GB
- license: CELLxGENE policy CC BY 4.0 (confirm on collection page) ; redistribution: yes if CC BY
- access: direct_download (30.5 GB, deliberate pull)
- status (2026-08-22): NEW 2026-08-22 (second hunt): HUMAN QUEUE (size decision before download)
- link: https://cellxgene.cziscience.com/collections/d5d0df8f-4eee-49d8-a221-a288f50a1590
- citation: Sci Data 2024, doi 10.1038/s41597-024-04117-y
