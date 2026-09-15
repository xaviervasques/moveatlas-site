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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (ethics-proof tier): 256 Hz lab PSG (EEG+EOG+chin EMG+ECG) across SS1-SS5, the reference for automated RBD-detection work. Our open RBD-EMG needs are covered by cap_sleep (held); MASS documents the ethics-gate model |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: http://ceams-carsm.ca/en/mass/
- License / access regime: free but gated: submit ethics-approved protocol + proof of ethics approval to CEAMS, then the PSG set is provided; not self-serve
- Access route: ceams-carsm.ca + borealis
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (ethics-proof tier): 256 Hz lab PSG (EEG+EOG+chin EMG+ECG) across SS1-SS5, the reference for automated RBD-detection work. Our open RBD-EMG needs are covered by cap_sleep (held); MASS documents the ethics-gate model
- Number of subjects: ~200 nights
- MoveAtlas cells: prodromal context; M6

### Retrieval notes
Found/adjudicated by the 2026-09-05 deep-dive sweep (big-cohort
platforms). Access regimes are a catalogue-time web reading, cross-checked
where a page answered; RE-VERIFY AT REQUEST TIME. The no-emails house
policy applies: request-tier routes are documented, not exercised,
unless the owner decides otherwise.

### Processing
None. Catalogue-tier.
