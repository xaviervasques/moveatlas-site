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
 }
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
