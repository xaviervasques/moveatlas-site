# Allen Human Brain Atlas (microarray + ISH histology)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Allen Human Brain Atlas (microarray + ISH histology)",
 "description": "Allen Human Brain Atlas (microarray + ISH histology). MoveAtlas bio family. 6 subjects. licence Allen Institute Terms of Use.",
 "identifier": "https://human.brain-map.org/static/download",
 "license": "Allen Institute Terms of Use (non-commercial, cite)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M10 Histology / transcr."
 ],
 "url": "https://human.brain-map.org/static/download",
 "isAccessibleForFree": false,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>allen_human_brain</code>

<span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | M10 |
| **Subjects** | 6 |
| **Status** | acquired (2026-08-24) |
| **License** | Allen Institute Terms of Use (non-commercial, cite) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("allen_human_brain")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: Allen Institute Terms of Use (non-commercial, cite)
- **Redistribution**: no (fetch from brain-map)
- **Access route**: direct_download (no registration)
- **Source**: <https://human.brain-map.org/static/download>

## Publications

- Hawrylycz, Michael J.; Lein, Ed S.; Guillozet-Bongaarts, Angela L.; Shen, Elaine H.; Ng, Lydia; Miller, Jeremy A.; van de Lagemaat, Louie N.; Smith, Kimberly A.; Ebbert, Amanda; Riley, Zackery L.; Abajian, Chris; Beckmann, Christian F.; Bernard, Amy; Bertagnolli, Darren; Boe, Andrew F.; Cartagena, P (2012). *An anatomically comprehensive atlas of the adult human brain transcriptome*. Nature. DOI: [10.1038/nature11405](https://doi.org/10.1038/nature11405)

```bibtex
@article{allen_human_brain_paper_2012,
  title = {An anatomically comprehensive atlas of the adult human brain transcriptome},
  author = {Hawrylycz, Michael J. and Lein, Ed S. and Guillozet-Bongaarts, Angela L. and Shen, Elaine H. and Ng, Lydia and Miller, Jeremy A. and van de Lagemaat, Louie N. and Smith, Kimberly A. and Ebbert, Amanda and Riley, Zackery L. and Abajian, Chris and Beckmann, Christian F. and Bernard, Amy and Bertagnolli, Darren and Boe, Andrew F. and Cartagena, Preston M. and Chakravarty, M. Mallar and Chapin, Mike and Chong, Jimmy and Dalley, Rachel A. and Daly, Barry David and Dang, Chinh and Datta, Suvro and Dee, Nick and Dolbeare, Tim A. and Faber, Vance and Feng, David and Fowler, David R. and Goldy, Jeff and Gregor, Benjamin W. and Haradon, Zeb and Haynor, David R. and Hohmann, John G. and Horvath, Steve and Howard, Robert E. and Jeromin, Andreas and Jochim, Jayson M. and Kinnunen, Marty and Lau, Christopher and Lazarz, Evan T. and Lee, Changkyu and Lemon, Tracy A. and Li, Ling and Li, Yang and Morris, John A. and Overly, Caroline C. and Parker, Patrick D. and Parry, Sheana E. and Reding, Melissa and Royall, Joshua J. and Schulkin, Jay and Sequeira, Pedro Adolfo and Slaughterbeck, Clifford R. and Smith, Simon C. and Sodt, Andy J. and Sunkin, Susan M. and Swanson, Beryl E. and Vawter, Marquis P. and Williams, Derric and Wohnoutka, Paul and Zielke, H. Ronald and Geschwind, Daniel H. and Hof, Patrick R. and Smith, Stephen M. and Koch, Christof and Grant, Seth G. N. and Jones, Allan R.},
  year = {2012},
  doi = {10.1038/nature11405},
  journal = {Nature}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: allen_human_brain
- **family**: bio
- **MoveAtlas cells**: M10
- **population**: 6 donors, whole-brain microarray (basal ganglia sampled), RNA-seq for 2, Nissl/ISH images via API
- **n_subjects**: 6
- **signal**: per-donor normalized microarray zips; histology per-image API
- **license**: Allen Institute Terms of Use (non-commercial, cite); redistribution: no, the ToU forbids redistribution; pointer to brain-map.org
- **access**: direct_download (no registration)
- **link**: https://human.brain-map.org/static/download
