# Genetic dystonia pallidal single-unit features (Zenodo 13269430)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Genetic dystonia pallidal single-unit features (Zenodo 13269430)",
 "description": "Genetic dystonia pallidal single-unit features (Zenodo 13269430). MoveAtlas bio family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/13269430",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A4 Dystonia",
  "M7 LFP / ECoG",
  "M9 Genetics"
 ],
 "url": "https://zenodo.org/records/13269430",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Kaymak, Ahmet"
  },
  {
   "@type": "Person",
   "name": "Romito, Luigi Michele"
  },
  {
   "@type": "Person",
   "name": "Mazzoni, Alberto"
  }
 ]
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>pallidal_units_dystonia</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">LFP / ECoG</span><span class="ma-tag">Genetics</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M7 (microelectrode single units), M9-adjacent (per-patient gene labels) |
| **Subjects** | unknown (per-unit CSV) |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pallidal_units_dystonia")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: Zenodo direct download
- **Source**: <https://zenodo.org/records/13269430>

## Publications

- Kaymak, Ahmet; Romito, Luigi Michele; Mazzoni, Alberto (2024). *Replication Data For: Spiking patterns in the globus pallidus highlight convergent neural dynamics across diverse genetic dystonia syndromes*. Zenodo. DOI: [10.5281/zenodo.13269430](https://doi.org/10.5281/zenodo.13269430)
- Kaymak, Ahmet; Colucci, Fabiana; Ahmadipour, Mahboubeh; Andreasi, Nico Golfrè; Rinaldo, Sara; Israel, Zvi; Arkadir, David; Telese, Roberta; Levi, Vincenzo; Zorzi, Giovanna; Carpaneto, Jacopo; Carecchio, Miryam; Prokisch, Holger; Zech, Michael; Garavaglia, Barbara; Bergman, Hagai; Eleopra, Roberto; M (2025). *Spiking Patterns in the Globus Pallidus Highlight Convergent Neural Dynamics across Diverse Genetic Dystonia Syndromes*. Annals of Neurology. DOI: [10.1002/ana.27185](https://doi.org/10.1002/ana.27185)

```bibtex
@misc{pallidal_units_dystonia_data_2024,
  title = {Replication Data For: Spiking patterns in the globus pallidus highlight convergent neural dynamics across diverse genetic dystonia syndromes},
  author = {Kaymak, Ahmet and Romito, Luigi Michele and Mazzoni, Alberto},
  year = {2024},
  doi = {10.5281/zenodo.13269430},
  howpublished = {Zenodo},
  note = {dataset}
}
@article{pallidal_units_dystonia_paper_2025,
  title = {Spiking Patterns in the Globus Pallidus Highlight Convergent Neural Dynamics across Diverse Genetic Dystonia Syndromes},
  author = {Kaymak, Ahmet and Colucci, Fabiana and Ahmadipour, Mahboubeh and Andreasi, Nico Golfrè and Rinaldo, Sara and Israel, Zvi and Arkadir, David and Telese, Roberta and Levi, Vincenzo and Zorzi, Giovanna and Carpaneto, Jacopo and Carecchio, Miryam and Prokisch, Holger and Zech, Michael and Garavaglia, Barbara and Bergman, Hagai and Eleopra, Roberto and Mazzoni, Alberto and Romito, Luigi M.},
  year = {2025},
  doi = {10.1002/ana.27185},
  journal = {Annals of Neurology}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: pallidal_units_dystonia
- **family**: bio
- **MoveAtlas cells**: A4; M7 (microelectrode single units), M9-adjacent (per-patient gene labels)
- **population**: GPi microelectrode recordings during DBS surgery across genetic dystonia syndromes, per-patient mutation labels
- **n_subjects**: unknown (per-unit CSV)
- **signal**: single-unit features: firing rate, bursts, oscillations, pauses (CSV) + MATLAB code
- **license**: CC BY 4.0 (verified on page 2026-09-01); redistribution: yes
- **access**: Zenodo direct download
- **link**: https://zenodo.org/records/13269430
