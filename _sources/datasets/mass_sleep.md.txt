# MASS: Montreal Archive of Sleep Studies (PSG incl. chin EMG; RBD-detection literature)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MASS: Montreal Archive of Sleep Studies (PSG incl. chin EMG; RBD-detection literature)",
 "description": "MASS: Montreal Archive of Sleep Studies (PSG incl. chin EMG; RBD-detection literature). MoveAtlas eeg family. licence free but gated: submit ethics-approved protocol + proof of e.",
 "identifier": "http://ceams-carsm.ca/en/mass/",
 "license": "https://opensource.org/license/mit",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "M6 EEG"
 ],
 "url": "http://ceams-carsm.ca/en/mass/",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>mass_sleep</code>

<span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | prodromal context; M6 |
| **Subjects** | ~200 nights |
| **Status** | documented access barrier (2026-09-05) |
| **License** | free but gated: submit ethics-approved protocol + proof of ethics approval to CEAMS, then the PSG set is provided; not self-serve |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mass_sleep")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: free but gated: submit ethics-approved protocol + proof of ethics approval to CEAMS, then the PSG set is provided; not self-serve
- **Redistribution**: no
- **Access route**: ceams-carsm.ca + borealis
- **Source**: <http://ceams-carsm.ca/en/mass/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: prodromal context; M6
