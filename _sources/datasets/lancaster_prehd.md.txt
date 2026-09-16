# Huntington's disease and controls physiological dataset (Lancaster; incl. premanifest group)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Huntington's disease and controls physiological dataset (Lancaster; incl. premanifest group)",
 "description": "Huntington's disease and controls physiological dataset (Lancaster; incl. premanifest group). MoveAtlas eeg family. 69 subjects. licence hosted on the Lancaster Pure portal; licence/access mode NOT.",
 "identifier": "https://doi.org/10.17635/lancaster/researchdata/631",
 "license": "hosted on the Lancaster Pure portal; licence/access mode NOT stated on the page - likely request-mediated, verify",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "A7 Chorea",
  "M5 EMG",
  "M6 EEG"
 ],
 "url": "https://doi.org/10.17635/lancaster/researchdata/631",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>lancaster_prehd</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | A7 prodromal; M5 M6 |
| **Subjects** | 69 |
| **Status** | catalogued (2026-09-05) |
| **License** | hosted on the Lancaster Pure portal; licence/access mode NOT stated on the page - likely request-mediated, verify |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("lancaster_prehd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: hosted on the Lancaster Pure portal; licence/access mode NOT stated on the page - likely request-mediated, verify
- **Redistribution**: unknown
- **Access route**: lancaster researchdata/631
- **Source**: <https://doi.org/10.17635/lancaster/researchdata/631>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A7 prodromal; M5 M6
