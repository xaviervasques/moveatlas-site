# NatMEG-PD: Swedish national MEG PD dataset (EBRAINS)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "NatMEG-PD: Swedish national MEG PD dataset (EBRAINS)",
 "description": "NatMEG-PD: Swedish national MEG PD dataset (EBRAINS). MoveAtlas eeg family. licence controlled access: EBRAINS Data Use Agreement.",
 "identifier": "https://search.kg.ebrains.eu/instances/d55146e8-fc86-44dd-95db-7191fdca7f30",
 "license": "controlled access: EBRAINS Data Use Agreement",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B4 Akinesia",
  "M5 EMG",
  "M6 EEG",
  "M4 Silhouette"
 ],
 "url": "https://search.kg.ebrains.eu/instances/d55146e8-fc86-44dd-95db-7191fdca7f30",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>natmeg_pd</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Akinesia</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B4; M5 M6 M4 |
| **Status** | documented access barrier (2026-09-05) |
| **License** | controlled access: EBRAINS Data Use Agreement |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("natmeg_pd")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: controlled access: EBRAINS Data Use Agreement
- **Redistribution**: no
- **Access route**: ebrains DOI 10.25493/DSY2-W2P
- **Source**: <https://search.kg.ebrains.eu/instances/d55146e8-fc86-44dd-95db-7191fdca7f30>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: B1-B4; M5 M6 M4
