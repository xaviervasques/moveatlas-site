# FMD perception-action hyperbinding EEG (OSF 7ke6r)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "FMD perception-action hyperbinding EEG (OSF 7ke6r)",
 "description": "FMD perception-action hyperbinding EEG (OSF 7ke6r). MoveAtlas eeg family. licence NO EXPLICIT LICENCE on the OSF project.",
 "identifier": "https://osf.io/7ke6r",
 "license": "NO EXPLICIT LICENCE on the OSF project (the goodwin_smm precedent: fetch for adjudication, INTERNAL-ONLY until terms are",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "D7 Functional movement disorders",
  "M5 EMG"
 ],
 "url": "https://osf.io/7ke6r",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>osf_fmd_eeg</code>

<span class="ma-tag">Functional movement disorders</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | D7 functional; M5 |
| **Subjects** | ~56 |
| **Status** | DOWNLOADED 2026-09-05: 92 files 217 MB, OSF sha256-verified; INTERNAL-ONLY pending licence adjudication. CATALOGUED 2026-09-05 (deep-dive): per-subject scalp time-frequency (.tfc BESA) + beamformer source files, FMD patients + matched controls - one of exactly TWO genuine open FMD deposits found any... |
| **License** | NO EXPLICIT LICENCE on the OSF project (the goodwin_smm precedent: fetch for adjudication, INTERNAL-ONLY until terms are established) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("osf_fmd_eeg")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NO EXPLICIT LICENCE on the OSF project (the goodwin_smm precedent: fetch for adjudication, INTERNAL-ONLY until terms are established)
- **Redistribution**: unknown
- **Access route**: osf.io/7ke6r
- **Source**: <https://osf.io/7ke6r>

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://osf.io/7ke6r
- License / access: NO EXPLICIT LICENCE on the OSF project (the goodwin_smm precedent: fetch for adjudication, INTERNAL-ONLY until terms are established)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  drug-induced/functional pass; records verified at file level
  by the catalogue sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): per-subject scalp time-frequency (.tfc BESA) + beamformer source files, FMD patients + matched controls - one of exactly TWO genuine open FMD deposits found anywhere (the D7 absence gets its first cracks)
- MoveAtlas cells: D7 functional; M5

### Retrieval notes
RE-VERIFY at fetch. The two OSF FMD deposits carry NO licence:
INTERNAL-ONLY after fetch until terms are adjudicated (goodwin_smm
precedent).

### Processing
None. Catalogue-tier.
