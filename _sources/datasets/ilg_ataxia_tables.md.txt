# Real-life gait in degenerative cerebellar ataxia (Ilg, aggregate tables)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Real-life gait in degenerative cerebellar ataxia (Ilg, aggregate tables)",
 "description": "Real-life gait in degenerative cerebellar ataxia (Ilg, aggregate tables). MoveAtlas auxdata family. 78 subjects. licence CC0.",
 "identifier": "https://datadryad.org/dataset/doi:10.5061/dryad.4tmpg4f62",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "D2 Ataxia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://datadryad.org/dataset/doi:10.5061/dryad.4tmpg4f62",
 "isAccessibleForFree": true,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Ilg, Winfried"
  },
  {
   "@type": "Person",
   "name": "Seemann, Jens"
  },
  {
   "@type": "Person",
   "name": "Giese, Martin"
  },
  {
   "@type": "Person",
   "name": "Traschuetz, Andreas"
  },
  {
   "@type": "Person",
   "name": "Schoels, Ludger"
  },
  {
   "@type": "Person",
   "name": "Timmann, Dagmar"
  },
  {
   "@type": "Person",
   "name": "Synofzik, Matthis"
  }
 ]
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>ilg_ataxia_tables</code>

<span class="ma-tag">Ataxia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | D2; M2 (derived) |
| **Subjects** | 78 |
| **Status** | DOWNLOADED 2026-08-22: 9 .docx tables (INAS + Tab_A..H), CC0 on Dryad. Aggregate step-variability tables, not signal: aux only, no canonical ingestion. Dryad answers 403 to a non-browser user agent, which is why the first attempt failed |
| **License** | CC0 (Dryad) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ilg_ataxia_tables")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (Dryad)
- **Redistribution**: yes
- **Access route**: direct_download (Dryad; tower queue)
- **Source**: <https://datadryad.org/dataset/doi:10.5061/dryad.4tmpg4f62>

## Publications

- Ilg, Winfried; Seemann, Jens; Giese, Martin; Traschuetz, Andreas; Schoels, Ludger; Timmann, Dagmar; Synofzik, Matthis (2021). *Towards ecologically valid biomarkers:real-life gait assessment in cerebellar ataxia*. Dryad. DOI: [10.5061/dryad.4tmpg4f62](https://doi.org/10.5061/dryad.4tmpg4f62)

```bibtex
@misc{ilg_ataxia_tables_data_2021,
  title = {Towards ecologically valid biomarkers:real-life gait assessment in cerebellar ataxia},
  author = {Ilg, Winfried and Seemann, Jens and Giese, Martin and Traschuetz, Andreas and Schoels, Ludger and Timmann, Dagmar and Synofzik, Matthis},
  year = {2021},
  doi = {10.5061/dryad.4tmpg4f62},
  howpublished = {Dryad},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: ilg_ataxia_tables
- family: auxdata  (physical path: datasets/auxdata/ilg_ataxia_tables)
- MoveAtlas cells: D2; M2 (derived)
- population: 43 degenerative cerebellar ataxia + 35 controls, lab + real life
- n_subjects: 78
- signal: aggregate step-variability/smoothness tables + SARA (172 KB, Word docs)
- license: CC0 (Dryad) ; redistribution: yes
- access: direct_download (Dryad; tower queue)
- status (2026-08-22): DOWNLOADED 2026-08-22: 9 .docx tables (INAS + Tab_A..H), CC0 on Dryad. Aggregate step-variability tables, not signal: aux only, no canonical ingestion. Dryad answers 403 to a non-browser user agent, which is why the first attempt failed
- link: https://datadryad.org/dataset/doi:10.5061/dryad.4tmpg4f62
- notes: reference statistics only, no raw signal; D2 anchor values
