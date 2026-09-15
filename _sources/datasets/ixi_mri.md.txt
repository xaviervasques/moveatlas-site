# IXI (healthy adult/aging brain MRI)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "IXI (healthy adult/aging brain MRI)",
 "description": "IXI (healthy adult/aging brain MRI). MoveAtlas bio family. licence CC BY-SA 3.0.",
 "identifier": "https://brain-development.org/ixi-dataset/",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "C1 Normal adult movement",
  "C3 Aging",
  "M8 Imaging"
 ],
 "url": "https://brain-development.org/ixi-dataset/",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>ixi_mri</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Aging</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | C1, C3; M8 |
| **Subjects** | ~600 |
| **Ages** | 20-86 y |
| **Status** | RETESTED 2026-08-28: biomedic.doc.ic.ac.uk still 403s this IP over both schemes; retry from another network or write off |
| **License** | CC BY-SA 3.0 (stated) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ixi_mri")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY-SA 3.0 (stated)
- **Redistribution**: yes (share-alike)
- **Access route**: direct_download (fetch_p2_lot.py --only ixi_mri; T1+T2+demographics queued)
- **Source**: <https://brain-development.org/ixi-dataset/>

## Publications

-  (). **. .

## Data card (verbatim, with its evidence trail)


- dataset: ixi_mri
- family: bio  (physical path: datasets/bio/ixi_mri)
- MoveAtlas cells: C1, C3; M8
- population: ~600 healthy subjects, 3 London sites, T1/T2/PD + MRA + DTI + demographics
- n_subjects: ~600
- age: 20-86 y
- signal: NIfTI tarballs (~10-15 GB total)
- license: CC BY-SA 3.0 (stated) ; redistribution: yes (share-alike)
- access: direct_download (fetch_p2_lot.py --only ixi_mri; T1+T2+demographics queued)
- status (2026-08-22): RETESTED 2026-08-28: biomedic.doc.ic.ac.uk still 403s this IP over both schemes; retry from another network or write off
- link: https://brain-development.org/ixi-dataset/
- notes: healthy aging imaging reference for M8
