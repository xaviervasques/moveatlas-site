# DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects)",
 "description": "DABI movement-disorder electrophysiology archive (BRAIN Initiative; ~20 projects). MoveAtlas eeg family. licence free DABI account + institutional agreement per project; two.",
 "identifier": "https://dabi.loni.usc.edu/projects/F3RE38A785JW",
 "license": "free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn c",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B5 Freezing of gait",
  "A1 Tremor",
  "A2 Myoclonus",
  "A3 Tics",
  "M7 LFP / ECoG"
 ],
 "url": "https://dabi.loni.usc.edu/projects/F3RE38A785JW",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>dabi_movement_ephys</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Freezing of gait</span><span class="ma-tag">Tremor</span><span class="ma-tag">Myoclonus</span><span class="ma-tag">Tics</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1-B5 A1 A2 A3 pediatric; M7 |
| **Status** | CATALOGUED 2026-09-05 (deep-dive): the invasive-ephys mother lode - aDBS gait trials (F3RE38A785JW 403 MB + Starr chronic aDBS 22 GB + 137 GB closed-loop), ET intraop (UTSW 8 GB), STN force coding, PD sleep LFP 207 GB, speech iEEG, AND the ONLY Tourette signal data found in any repository (1UH3NS119... |
| **License** | free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn coordinated-reset ET 9.5 GB) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dabi_movement_ephys")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn coordinated-reset ET 9.5 GB)
- **Redistribution**: no
- **Access route**: dabi.loni.usc.edu
- **Source**: <https://dabi.loni.usc.edu/projects/F3RE38A785JW>

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://dabi.loni.usc.edu/projects/F3RE38A785JW
- License / access: free DABI account + institutional agreement per project; two projects carry a PUBLIC file tier (UAB ERNA 155 MB, UMinn coordinated-reset ET 9.5 GB)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): the invasive-ephys mother lode - aDBS gait trials (F3RE38A785JW 403 MB + Starr chronic aDBS 22 GB + 137 GB closed-loop), ET intraop (UTSW 8 GB), STN force coding, PD sleep LFP 207 GB, speech iEEG, AND the ONLY Tourette signal data found in any repository (1UH3NS119844: CM-thalamus/GPi recordings, 221 GB / 212655 files); pediatric dystonia DBS (Sanger CHOC) is a placeholder to watch. The account+agreement tier is DABI's standard gate
- MoveAtlas cells: B1-B5 A1 A2 A3 pediatric; M7

### Retrieval notes
RE-VERIFY at fetch/request; no-emails policy for gated tiers.

### Processing
None. Catalogue-tier.
