# Chorea-acanthocytosis Swedish cohort imaging (Dryad)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Chorea-acanthocytosis Swedish cohort imaging (Dryad)",
 "description": "Chorea-acanthocytosis Swedish cohort imaging (Dryad). MoveAtlas bio family. licence CC0.",
 "identifier": "https://doi.org/10.5061/dryad.7h44j0zr9",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A7 Chorea",
  "M8 Imaging"
 ],
 "url": "https://doi.org/10.5061/dryad.7h44j0zr9",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>chorea_acanthocytosis_mri</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A7; M8 |
| **Subjects** | cohort table |
| **Status** | DOWNLOADED 2026-09-01 (owner GO): dryad_dataset.zip 18,720,483 B (version-level endpoint), sha256 journaled; CC0 confirmed via the Dryad API at fetch |
| **License** | CC0 (Dryad, API-verified 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("chorea_acanthocytosis_mri")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (Dryad, API-verified 2026-09-01)
- **Redistribution**: yes
- **Access route**: Dryad direct download
- **Source**: <https://doi.org/10.5061/dryad.7h44j0zr9>

## Data card (verbatim, with its evidence trail)


- dataset: chorea_acanthocytosis_mri
- family: bio  (physical path: datasets/bio/chorea_acanthocytosis_mri)
- MoveAtlas cells: A7; M8
- population: chorea-acanthocytosis (VPS13A) patients: MRI/PET/DaTscan + phenotypes
- n_subjects: cohort table
- signal: imaging-derived measures + phenotypes (not kinematics)
- license: CC0 (Dryad, API-verified 2026-09-01) ; redistribution: yes
- access: Dryad direct download
- status (2026-08-22): DOWNLOADED 2026-09-01 (owner GO): dryad_dataset.zip 18,720,483 B (version-level endpoint), sha256 journaled; CC0 confirmed via the Dryad API at fetch
- link: https://doi.org/10.5061/dryad.7h44j0zr9
