# Upper-limb and cervical dystonia MRI (OpenNeuro ds006395)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Upper-limb and cervical dystonia MRI (OpenNeuro ds006395)",
 "description": "Upper-limb and cervical dystonia MRI (OpenNeuro ds006395). MoveAtlas bio family. 91 subjects. licence CC0.",
 "identifier": "https://openneuro.org/datasets/ds006395",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "A4 Dystonia",
  "M8 Imaging"
 ],
 "url": "https://openneuro.org/datasets/ds006395",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>dystonia_mri_ds006395</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M8 |
| **Subjects** | 91 |
| **Status** | DOWNLOADED 2026-09-01 (owner GO): full S3 sync COMPLETE, 1,368/1,368 files / 61.9 GiB size-verified against the bucket listing (BIDS validation at ingestion). The first truly open MRI for the imaging lane (ixi_mri still 403s) |
| **License** | CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dystonia_mri_ds006395")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01)
- **Redistribution**: yes
- **Access route**: OpenNeuro / S3 direct download
- **Source**: <https://openneuro.org/datasets/ds006395>

## Data card (verbatim, with its evidence trail)


- dataset: dystonia_mri_ds006395
- family: bio  (physical path: datasets/bio/dystonia_mri_ds006395)
- MoveAtlas cells: A4; M8
- population: 37 healthy controls + 25 cervical dystonia + 29 upper-limb dystonia; T1, 60-dir DWI, rs-fMRI, finger-tapping task fMRI
- n_subjects: 91
- signal: structural + diffusion + functional MRI (BIDS)
- license: CC0 (verified via the OpenNeuroDatasets mirror 2026-09-01) ; redistribution: yes
- access: OpenNeuro / S3 direct download
- status (2026-08-22): DOWNLOADED 2026-09-01 (owner GO): full S3 sync COMPLETE, 1,368/1,368 files / 61.9 GiB size-verified against the bucket listing (BIDS validation at ingestion). The first truly open MRI for the imaging lane (ixi_mri still 403s)
- link: https://openneuro.org/datasets/ds006395
