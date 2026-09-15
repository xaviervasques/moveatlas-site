# High-resolution rat LFP atlas incl. hemiparkinsonian + levodopa states (EBRAINS)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "High-resolution rat LFP atlas incl. hemiparkinsonian + levodopa states (EBRAINS)",
 "description": "High-resolution rat LFP atlas incl. hemiparkinsonian + levodopa states (EBRAINS). MoveAtlas animal family. 23 rats subjects. licence CC BY 4.0.",
 "identifier": "https://search.kg.ebrains.eu/instances/41673110-f3eb-43cd-9d9c-c845c6f0573c",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal",
  "M7 LFP / ECoG"
 ],
 "url": "https://search.kg.ebrains.eu/instances/41673110-f3eb-43cd-9d9c-c845c6f0573c",
 "isAccessibleForFree": false,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ebrains_rat_lfp_atlas</code>

<span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | animal PD models; M7 |
| **Subjects** | 23 rats |
| **Status** | CATALOGUED 2026-09-05: 29983 LFP recordings across >2000 sites in free behavior, healthy + hemiparkinsonian + levodopa/ketamine states, micro-CT registered (2026-04 release) - animal-lane candidate for the post-paper implementation |
| **License** | CC BY 4.0 (EBRAINS free access, re-verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ebrains_rat_lfp_atlas")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (EBRAINS free access, re-verify at fetch)
- **Redistribution**: unknown
- **Access route**: ebrains DOI 10.25493/QNVD-9M2
- **Source**: <https://search.kg.ebrains.eu/instances/41673110-f3eb-43cd-9d9c-c845c6f0573c>

## Data card (verbatim, with its evidence trail)


- Modality: family 'animal'
- Source / URL: https://search.kg.ebrains.eu/instances/41673110-f3eb-43cd-9d9c-c845c6f0573c
- License / access: CC BY 4.0 (EBRAINS free access, re-verify at fetch)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: 29983 LFP recordings across >2000 sites in free behavior, healthy + hemiparkinsonian + levodopa/ketamine states, micro-CT registered (2026-04 release) - animal-lane candidate for the post-paper implementation
- MoveAtlas cells: animal PD models; M7

### Retrieval notes
RE-VERIFY at fetch/request; no-emails policy for gated tiers.

### Processing
None. Catalogue-tier.
