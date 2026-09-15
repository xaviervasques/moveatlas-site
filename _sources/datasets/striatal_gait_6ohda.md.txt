# Striatal D1/D2 MSN encoding of gait in 6-OHDA mice (Zenodo 8303087)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Striatal D1/D2 MSN encoding of gait in 6-OHDA mice (Zenodo 8303087)",
 "description": "Striatal D1/D2 MSN encoding of gait in 6-OHDA mice (Zenodo 8303087). MoveAtlas animal family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/8303087",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://zenodo.org/records/8303087",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>striatal_gait_6ohda</code>

| | |
|---|---|
| **Taxonomy cells** | animal: 6-OHDA lesion -> hypokinetic gait analog, with opto-tagged striatal ephys |
| **Subjects** | see record |
| **Status** | DOWNLOADED 2026-09-01 (animal hunt): data.zip 2.21 GB, cc-by-4.0 confirmed via the API on the retry (Zenodo had been 50x-ing earlier the same day), sha256 journaled |
| **License** | CC BY 4.0 (DataCite record; Zenodo page 50x-ing at verification) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("striatal_gait_6ohda")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (DataCite record; Zenodo page 50x-ing at verification)
- **Redistribution**: yes
- **Access route**: Zenodo direct download
- **Source**: <https://zenodo.org/records/8303087>

## Data card (verbatim, with its evidence trail)


- dataset: striatal_gait_6ohda
- family: animal  (physical path: datasets/animal/striatal_gait_6ohda)
- MoveAtlas cells: animal: 6-OHDA lesion -> hypokinetic gait analog, with opto-tagged striatal ephys
- population: mouse: unilateral 6-OHDA MFB lesion vs controls, open field
- n_subjects: see record
- signal: open-field gait/movement measures + striatal single-unit ephys
- license: CC BY 4.0 (DataCite record; Zenodo page 50x-ing at verification) ; redistribution: yes
- access: Zenodo direct download
- status (2026-08-22): DOWNLOADED 2026-09-01 (animal hunt): data.zip 2.21 GB, cc-by-4.0 confirmed via the API on the retry (Zenodo had been 50x-ing earlier the same day), sha256 journaled
- link: https://zenodo.org/records/8303087
