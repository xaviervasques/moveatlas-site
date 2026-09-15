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
| **Status** | CATALOGUED 2026-09-05: EEG 1kHz + fNIRS + ECG/resp/skin-bloodflow, 20 min/subject, with a DEDICATED premanifest-HD group - the only downloadable-signal deposit found with preHD anywhere (not kinematic; the preHD KINEMATICS absence stands) |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://doi.org/10.17635/lancaster/researchdata/631
- License / access: hosted on the Lancaster Pure portal; licence/access mode NOT stated on the page - likely request-mediated, verify
- Access route: lancaster researchdata/631
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); not fetched at card creation
- Status (2026-09-05): CATALOGUED 2026-09-05: EEG 1kHz + fNIRS + ECG/resp/skin-bloodflow, 20 min/subject, with a DEDICATED premanifest-HD group - the only downloadable-signal deposit found with preHD anywhere (not kinematic; the preHD KINEMATICS absence stands)
- Number of subjects: 69
- MoveAtlas cells: A7 prodromal; M5 M6

### Retrieval notes
RE-VERIFY at fetch/request. No-emails policy for request tiers.

### Processing
None. Catalogue-tier.
