# Reach-related single units in parkinsonian macaque (DANDI 000947)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Reach-related single units in parkinsonian macaque (DANDI 000947)",
 "description": "Reach-related single units in parkinsonian macaque (DANDI 000947). MoveAtlas bio family. 2 macaques subjects. licence CC BY 4.0.",
 "identifier": "https://dandiarchive.org/dandiset/000947",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "bio",
  "B1 Rigidity",
  "B2 Bradykinesia",
  "M7 LFP / ECoG"
 ],
 "url": "https://dandiarchive.org/dandiset/000947",
 "isAccessibleForFree": true,
 "measurementTechnique": "bio",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-bio">bio</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>dandi_pd_macaque_units</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1, B2 (MPTP parkinsonian model); M7 (single units) |
| **Subjects** | 2 macaques |
| **Status** | COMPLETE 2026-09-07, DIGEST-VERIFIED: 378/378 NWB assets, 976.8 GB, verify_dandi_local.py 378 OK / 0 BAD against DANDI's per-asset sha2-256; six-day pull 2026-09-01 -> 09-07 (PC ethernet + Mac Wi-Fi weekend, two frozen-socket kills, one DANDI API 503 outage). History: DEFERRED 2026-09-01 (owner GO s... |
| **License** | CC BY 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dandi_pd_macaque_units")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: DANDI open download (dandi CLI)
- **Source**: <https://dandiarchive.org/dandiset/000947>

## Data card (verbatim, with its evidence trail)


- dataset: dandi_pd_macaque_units
- family: bio  (physical path: datasets/bio/dandi_pd_macaque_units)
- MoveAtlas cells: B1, B2 (MPTP parkinsonian model); M7 (single units)
- population: 2 MPTP macaques; GPi, VL thalamus and M1 single units during reaching
- n_subjects: 2 macaques
- signal: spike-sorted single units across the BG-thalamo-cortical circuit (NWB, ~1 TB)
- license: CC BY 4.0 (verified on page 2026-09-01) ; redistribution: yes
- access: DANDI open download (dandi CLI)
- status (2026-09-07): COMPLETE AND DIGEST-VERIFIED. 378/378 NWB assets on disk, 976.8 GB, every file verified against DANDI's own per-asset sha2-256 (verify_dandi_local.py, 2026-09-07: 378 OK / 0 BAD / 0 unverifiable / 0 orphan). Pulled 2026-09-01 -> 2026-09-07 across the PC ethernet line and a Mac Wi-Fi weekend (H16-H19: frozen-socket watchdog, DANDI API 503 outage 2026-09-04, self-restarting wrapper; the last 23 files landed on the PC overnight 2026-09-06/07). History: DEFERRED 2026-09-01 (owner GO stood): ~1 TB (378 monolithic NWB sessions, median ~2 GB) vs 273 GB free at the time; needed the external disk. SAMPLE FETCHED same day (raw_sample/: the 2 smallest pre-MPTP + 2 smallest post-MPTP sessions, 360 MB, sha256 journaled) and its schema READ: trials carry cue_onset / movement_start / reward times + target, i.e. EVENT-CODED movement (reaction and movement times = a primate bradykinesia readout pre vs post MPTP), no continuous hand kinematics in the sampled sessions
- link: https://dandiarchive.org/dandiset/000947
