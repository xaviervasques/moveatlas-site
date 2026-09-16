# Reach-related single units in parkinsonian macaque (DANDI 000947)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Reach-related single units in parkinsonian macaque (DANDI 000947)",
 "description": "Reach-related single units in parkinsonian macaque (DANDI 000947). MoveAtlas bio family. 2 macaques subjects. licence CC BY 4.0.",
 "identifier": "https://dandiarchive.org/dandiset/000947",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "B1 Rigidity",
  "B2 Bradykinesia",
  "M7 LFP / ECoG"
 ],
 "url": "https://dandiarchive.org/dandiset/000947",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dandi_pd_macaque_units</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1, B2 (MPTP parkinsonian model); M7 (single units) |
| **Subjects** | 2 macaques |
| **Status** | catalogued (2026-09-07) |
| **License** | CC BY 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dandi_pd_macaque_units")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: DANDI open download (dandi CLI)
- **Source**: <https://dandiarchive.org/dandiset/000947>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: dandi_pd_macaque_units
- **family**: bio
- **MoveAtlas cells**: B1, B2 (MPTP parkinsonian model); M7 (single units)
- **population**: 2 MPTP macaques; GPi, VL thalamus and M1 single units during reaching
- **n_subjects**: 2 macaques
- **signal**: spike-sorted single units across the BG-thalamo-cortical circuit (NWB, ~1 TB)
- **license**: CC BY 4.0 (verified on page 2026-09-01); redistribution: yes
- **access**: DANDI open download (dandi CLI)
- **link**: https://dandiarchive.org/dandiset/000947
