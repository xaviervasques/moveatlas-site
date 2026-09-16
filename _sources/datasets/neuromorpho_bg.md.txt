# NeuroMorpho.Org basal-ganglia neuron morphologies

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NeuroMorpho.Org basal-ganglia neuron morphologies",
 "description": "NeuroMorpho.Org basal-ganglia neuron morphologies. MoveAtlas bio family. licence CC BY 4.0.",
 "identifier": "https://neuromorpho.org",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A7 Chorea",
  "B1 Rigidity",
  "B3 Hypokinesia",
  "M10 Histology / transcr."
 ],
 "url": "https://neuromorpho.org",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>neuromorpho_bg</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">Rigidity</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | A7 (HD models), B1-B3 (PD models), M10 (cellular morphology) |
| **Subjects** | region-filtered subset |
| **Status** | acquired (2026-09-01) |
| **License** | CC BY 4.0 (verified on useterm.jsp 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("neuromorpho_bg")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified on useterm.jsp 2026-09-01)
- **Redistribution**: yes
- **Access route**: NeuroMorpho API bulk download
- **Source**: <https://neuromorpho.org>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: neuromorpho_bg
- **family**: bio
- **MoveAtlas cells**: A7 (HD models), B1-B3 (PD models), M10 (cellular morphology)
- **population**: 7,842 striatal reconstructions; DISEASE-MODEL CONTENT measured from the metadata (processed/condition_breakdown.csv, analyze_neuromorpho_conditions.py, 2026-09-01): Huntington 823 (675 Q140 labeled Huntington's Disease + 148 zQ175/Q175) -> A7; Parkinson models 248 (139 alpha-synuclein BAC rat, 71 LRRK2, 38 6-OHDA) -> B lane; stroke MCAO 52; dopaminergic pharmacology ~330 (cocaine, nicotine+SCH23390, D2R-overexpression) -> the intervention axis; 124 HUMAN neurons (all controls: no human patient morphology exists here); ~6,640 healthy/control baseline. The symptom link is via the animal disease model, not measured movement
- **n_subjects**: region-filtered subset
- **signal**: .swc reconstructions via the public API (scraping forbidden, API allowed)
- **license**: CC BY 4.0 (verified on useterm.jsp 2026-09-01); redistribution: yes
- **access**: NeuroMorpho API bulk download
- **link**: https://neuromorpho.org
