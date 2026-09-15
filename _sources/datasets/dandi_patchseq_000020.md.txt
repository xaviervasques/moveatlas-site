# Patch-seq mouse visual cortex, 1,040 cells (DANDI 000020, Allen)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Patch-seq mouse visual cortex, 1,040 cells (DANDI 000020, Allen)",
 "description": "Patch-seq mouse visual cortex, 1,040 cells (DANDI 000020, Allen). MoveAtlas bio family. 1,040 cells subjects. licence CC BY 4.0.",
 "identifier": "https://dandiarchive.org/dandiset/000020",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "M7 LFP / ECoG",
  "M10 Histology / transcr."
 ],
 "url": "https://dandiarchive.org/dandiset/000020",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>dandi_patchseq_000020</code>

<span class="ma-tag">LFP / ECoG</span><span class="ma-tag">Histology / transcr.</span>

| | |
|---|---|
| **Taxonomy cells** | M7 (cellular ephys), M10 (transcriptome + morphology) |
| **Subjects** | 1,040 cells |
| **Status** | DOWNLOADED AND DIGEST-VERIFIED 2026-09-03 (post-migration disk, ethernet): 4,435/4,435 assets of published version 0.210913.1639, 132.1 GB, EVERY file re-hashed against the archive's own dandi:sha2-256 digests (verify_dandi_local.py) - 4,435 OK / 0 bad. The overnight pull also survived a mid-transfe... |
| **License** | CC BY 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dandi_patchseq_000020")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: DANDI open download (dandi CLI)
- **Source**: <https://dandiarchive.org/dandiset/000020>

## Data card (verbatim, with its evidence trail)


- dataset: dandi_patchseq_000020
- family: bio  (physical path: datasets/bio/dandi_patchseq_000020)
- MoveAtlas cells: M7 (cellular ephys), M10 (transcriptome + morphology)
- population: 1,040 mouse VISp neurons with joint transcriptome + electrophysiology + morphology
- n_subjects: 1,040 cells
- signal: patch-seq triplets (NWB, 141.9 GB)
- license: CC BY 4.0 (verified on page 2026-09-01) ; redistribution: yes
- access: DANDI open download (dandi CLI)
- status (2026-08-22): DOWNLOADED AND DIGEST-VERIFIED 2026-09-03 (post-migration disk, ethernet): 4,435/4,435 assets of published version 0.210913.1639, 132.1 GB, EVERY file re-hashed against the archive's own dandi:sha2-256 digests (verify_dandi_local.py) - 4,435 OK / 0 bad. The overnight pull also survived a mid-transfer network-interface switch (the frozen partial was deleted and re-pulled)
- link: https://dandiarchive.org/dandiset/000020
