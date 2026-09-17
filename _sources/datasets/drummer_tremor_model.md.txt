# Expert drummers replicate physiological tremor signatures (Recherche Data Gouv)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Expert drummers replicate physiological tremor signatures (Recherche Data Gouv)",
 "description": "Expert drummers replicate physiological tremor signatures (Recherche Data Gouv). MoveAtlas imu family. 18 subjects. licence etalab 2.0.",
 "identifier": "https://doi.org/10.57745/thhwp2",
 "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "A1 Tremor",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.57745/thhwp2",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>drummer_tremor_model</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | A1 context (physiological tremor); C1; M2 M5 |
| **Subjects** | 18 |
| **Status** | acquired (2026-09-05) |
| **License** | etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version) |
| **MoveAtlas record** | [10.5281/zenodo.22358617](https://doi.org/10.5281/zenodo.22358617) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("drummer_tremor_model")
records, meta = ds.get_data()
```

## License and access

- **License**: etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version)
- **Redistribution**: yes (etalab 2.0: attribution obligatoire - fetch-verified 2026-09-05)
- **Access route**: rdg doi:10.57745/thhwp2
- **Source**: <https://doi.org/10.57745/thhwp2>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A1 context (physiological tremor); C1; M2 M5
