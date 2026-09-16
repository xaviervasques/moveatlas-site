# Human Phenotype Ontology (movement pivot)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Human Phenotype Ontology (movement pivot)",
 "description": "Human Phenotype Ontology (movement pivot). MoveAtlas ontology family. licence HPO free-use with attribution.",
 "identifier": "https://hpo.jax.org/",
 "license": "HPO free-use with attribution (hpo.jax.org/license, read 2026-09-16: cite the HPO, show the file version when displayed,",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "ontology",
  "M9 Genetics",
  "M12 Clinical scales"
 ],
 "url": "https://hpo.jax.org/",
 "isAccessibleForFree": true,
 "measurementTechnique": "ontology",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-ontology">ontology</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>hpo</code>

<span class="ma-tag">Genetics</span><span class="ma-tag">Clinical scales</span>

| | |
|---|---|
| **Taxonomy cells** | semantic pivot for stage C; M9, M12 |
| **Subjects** | n/a |
| **Status** | acquired (2026-08-22) |
| **License** | HPO free-use with attribution (hpo.jax.org/license, read 2026-09-16: cite the HPO, show the file version when displayed, do not alter the content) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("hpo")
records, meta = ds.get_data()
```

## License and access

- **License**: HPO free-use with attribution (hpo.jax.org/license, read 2026-09-16: cite the HPO, show the file version when displayed, do not alter the content)
- **Redistribution**: yes
- **Access route**: refresh lane in fetch_p2_lot.py
- **Source**: <https://hpo.jax.org/>

## Publications

- Gargano, Michael A; Matentzoglu, Nicolas; Coleman, Ben; Addo-Lartey, Eunice B; Anagnostopoulos, Anna V; Anderton, Joel; Avillach, Paul; Bagley, Anita M; Bakštein, Eduard; Balhoff, James P; Baynam, Gareth; Bello, Susan M; Berk, Michael; Bertram, Holli; Bishop, Somer; Blau, Hannah; Bodenstein, David F (2024). *The Human Phenotype Ontology in 2024: phenotypes around the world*. Nucleic Acids Research. DOI: [10.1093/nar/gkad1005](https://doi.org/10.1093/nar/gkad1005)

```bibtex
@article{hpo_paper_2024,
  title = {The Human Phenotype Ontology in 2024: phenotypes around the world},
  author = {Gargano, Michael A and Matentzoglu, Nicolas and Coleman, Ben and Addo-Lartey, Eunice B and Anagnostopoulos, Anna V and Anderton, Joel and Avillach, Paul and Bagley, Anita M and Bakštein, Eduard and Balhoff, James P and Baynam, Gareth and Bello, Susan M and Berk, Michael and Bertram, Holli and Bishop, Somer and Blau, Hannah and Bodenstein, David F and Botas, Pablo and Boztug, Kaan and Čady, Jolana and Callahan, Tiffany J and Cameron, Rhiannon and Carbon, Seth J and Castellanos, Francisco and Caufield, J Harry and Chan, Lauren E and Chute, Christopher G and Cruz-Rojo, Jaime and Dahan-Oliel, Noémi and Davids, Jon R and de Dieuleveult, Maud and de Souza, Vinicius and de Vries, Bert B A and de Vries, Esther and DePaulo, J Raymond and Derfalvi, Beata and Dhombres, Ferdinand and Diaz-Byrd, Claudia and Dingemans, Alexander J M and Donadille, Bruno and Duyzend, Michael and Elfeky, Reem and Essaid, Shahim and Fabrizzi, Carolina and Fico, Giovanna and Firth, Helen V and Freudenberg-Hua, Yun and Fullerton, Janice M and Gabriel, Davera L and Gilmour, Kimberly and Giordano, Jessica and Goes, Fernando S and Moses, Rachel Gore and Green, Ian and Griese, Matthias and Groza, Tudor and Gu, Weihong and Guthrie, Julia and Gyori, Benjamin and Hamosh, Ada and Hanauer, Marc and Hanušová, Kateřina and He, Yongqun (Oliver) and Hegde, Harshad and Helbig, Ingo and Holasová, Kateřina and Hoyt, Charles Tapley and Huang, Shangzhi and Hurwitz, Eric and Jacobsen, Julius O B and Jiang, Xiaofeng and Joseph, Lisa and Keramatian, Kamyar and King, Bryan and Knoflach, Katrin and Koolen, David A and Kraus, Megan L and Kroll, Carlo and Kusters, Maaike and Ladewig, Markus S and Lagorce, David and Lai, Meng-Chuan and Lapunzina, Pablo and Laraway, Bryan and Lewis-Smith, David and Li, Xiarong and Lucano, Caterina and Majd, Marzieh and Marazita, Mary L and Martinez-Glez, Victor and McHenry, Toby H and McInnis, Melvin G and McMurry, Julie A and Mihulová, Michaela and Millett, Caitlin E and Mitchell, Philip B and Moslerová, Veronika and Narutomi, Kenji and Nematollahi, Shahrzad and Nevado, Julian and Nierenberg, Andrew A and Čajbiková, Nikola Novák and Nurnberger, John I and Ogishima, Soichi and Olson, Daniel and Ortiz, Abigail and Pachajoa, Harry and Perez de Nanclares, Guiomar and Peters, Amy and Putman, Tim and Rapp, Christina K and Rath, Ana and Reese, Justin and Rekerle, Lauren and Roberts, Angharad M and Roy, Suzy and Sanders, Stephan J and Schuetz, Catharina and Schulte, Eva C and Schulze, Thomas G and Schwarz, Martin and Scott, Katie and Seelow, Dominik and Seitz, Berthold and Shen, Yiping and Similuk, Morgan N and Simon, Eric S and Singh, Balwinder and Smedley, Damian and Smith, Cynthia L and Smolinsky, Jake T and Sperry, Sarah and Stafford, Elizabeth and Stefancsik, Ray and Steinhaus, Robin and Strawbridge, Rebecca and Sundaramurthi, Jagadish Chandrabose and Talapova, Polina and Tenorio Castano, Jair A and Tesner, Pavel and Thomas, Rhys H and Thurm, Audrey and Turnovec, Marek and van Gijn, Marielle E and Vasilevsky, Nicole A and Vlčková, Markéta and Walden, Anita and Wang, Kai and Wapner, Ron and Ware, James S and Wiafe, Addo A and Wiafe, Samuel A and Wiggins, Lisa D and Williams, Andrew E and Wu, Chen and Wyrwoll, Margot J and Xiong, Hui and Yalin, Nefize and Yamamoto, Yasunori and Yatham, Lakshmi N and Yocum, Anastasia K and Young, Allan H and Yüksel, Zafer and Zandi, Peter P and Zankl, Andreas and Zarante, Ignacio and Zvolský, Miroslav and Toro, Sabrina and Carmody, Leigh C and Harris, Nomi L and Munoz-Torres, Monica C and Danis, Daniel and Mungall, Christopher J and Köhler, Sebastian and Haendel, Melissa A and Robinson, Peter N},
  year = {2024},
  doi = {10.1093/nar/gkad1005},
  journal = {Nucleic Acids Research}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: hpo
- **family**: ontology
- **MoveAtlas cells**: semantic pivot for stage C; M9, M12
- **population**: knowledge base: 19,034 active terms; movement subtree HP:0100022 = 197 terms, 68 inside the 13 MoveAtlas anchor subtrees
- **n_subjects**: n/a
- **signal**: hp.obo (10 MB) + genes_to_phenotype.txt (19.7 MB) + phenotype.hpoa.gz + phenotype_to_genes.txt.gz; release hp/2025-01-16
- **license**: HPO free-use with attribution (hpo.jax.org/license, read 2026-09-16: cite the HPO, show the file version when displayed, do not alter the content); redistribution: yes
- **access**: refresh lane in fetch_p2_lot.py
- **link**: https://hpo.jax.org/
- **ingestion**: build_hpo_movement_map.py -> docs/hpo_movement_terms.csv (id, name, depth, parents, MoveAtlas cells)
