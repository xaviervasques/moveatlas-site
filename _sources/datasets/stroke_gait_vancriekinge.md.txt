# Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge)",
 "description": "Full-body mocap gait: 50 stroke + 138 able-bodied (Van Criekinge). MoveAtlas pose family. 188 subjects. licence CC0.",
 "identifier": "https://doi.org/10.6084/m9.figshare.c.6503791",
 "license": "https://creativecommons.org/publicdomain/zero/1.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "D3 Pyramidal syndromes",
  "M1 Pose / video",
  "M3 Plantar force",
  "M5 EMG"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.c.6503791",
 "isAccessibleForFree": true,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Van Criekinge, Tamaya"
  },
  {
   "@type": "Person",
   "name": "Saeys, Wim"
  },
  {
   "@type": "Person",
   "name": "Truijen, Steven"
  },
  {
   "@type": "Person",
   "name": "Vereeck, Luc"
  },
  {
   "@type": "Person",
   "name": "Sloot, Lizeth"
  },
  {
   "@type": "Person",
   "name": "Hallemans, Ann"
  }
 ]
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>stroke_gait_vancriekinge</code>

<span class="ma-tag">Pyramidal syndromes</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Plantar force</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | D3; M1, M3, M5 (pathological EMG) |
| **Subjects** | 188 |
| **Ages** | 19-85 y |
| **Status** | DOWNLOADED (13/13, md5-verified); RE-INGESTED 2026-08-28: 737 canonical 3D pose records / 188 subjects at native 100 Hz, PiG joint identities established by measured geometry (configs entry pig_vancriekinge). The 2026-08-27 pass had refused 199 C3Ds as marker-only; the census showed 192 of them carr... |
| **License** | CC0 (all 13 figshare collection items, verified 2026-08-22) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("stroke_gait_vancriekinge")
records, meta = ds.get_data()
```

## License and access

- **License**: CC0 (all 13 figshare collection items, verified 2026-08-22)
- **Redistribution**: yes
- **Access route**: direct_download (figshare collection; landed via the owner's browser)
- **Source**: <https://doi.org/10.6084/m9.figshare.c.6503791>

## Publications

- Van Criekinge, Tamaya; Saeys, Wim; Truijen, Steven; Vereeck, Luc; Sloot, Lizeth; Hallemans, Ann (2023). *A full-body motion capture gait dataset of 138 able-bodied adults across the life span and 50 stroke survivors*. figshare. DOI: [10.6084/m9.figshare.c.6503791](https://doi.org/10.6084/m9.figshare.c.6503791)

```bibtex
@misc{stroke_gait_vancriekinge_data_2023,
  title = {A full-body motion capture gait dataset of 138 able-bodied adults across the life span and 50 stroke survivors},
  author = {Van Criekinge, Tamaya and Saeys, Wim and Truijen, Steven and Vereeck, Luc and Sloot, Lizeth and Hallemans, Ann},
  year = {2023},
  doi = {10.6084/m9.figshare.c.6503791},
  howpublished = {figshare},
  note = {dataset}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: stroke_gait_vancriekinge
- family: pose  (physical path: datasets/pose/stroke_gait_vancriekinge)
- MoveAtlas cells: D3; M1, M3, M5 (pathological EMG)
- population: 50 stroke survivors + 138 able-bodied adults across the lifespan
- n_subjects: 188
- age: 19-85 y
- signal: 3D marker trajectories, joint angles, GRF, joint moments/powers + EMG of 14 back/lower-limb muscles (C3D + MAT/XLSX)
- license: CC0 (all 13 figshare collection items, verified 2026-08-22) ; redistribution: yes
- access: direct_download (figshare collection; landed via the owner's browser)
- status (2026-08-22): DOWNLOADED (13/13, md5-verified); RE-INGESTED 2026-08-28: 737 canonical 3D pose records / 188 subjects at native 100 Hz, PiG joint identities established by measured geometry (configs entry pig_vancriekinge). The 2026-08-27 pass had refused 199 C3Ds as marker-only; the census showed 192 of them carry the FULL model outputs under a 'SUBJECTID:' label prefix (geometry re-verified on the prefixed files) and 5 more lack only head/elbow/wrist outputs (those joints NaN-filled, masked invalid). PRIVACY NOTE: the prefixes look like birthdate-based Vicon IDs; they are stripped at ingestion and never propagated, and any raw-zip redistribution must account for them. 2 truly unusable C3Ds stay refused, 49 calibration/unparseable skipped. The MAT/XLSX time-normalized files are derivatives and stay raw. ANALOG PASS 2026-09-03 (ingest_stroke_gait_analogs.py, per the scoping doc): 559 canonical EMG records / 163 subjects (14 named muscles L+R via the ERS/RF/VL/ST/BF/TA/GAS alias table; anonymous Voltage.NN channels REFUSED and audited; AMPLITUDE FLAG on the records: the declared V converts to ~476 mV p99, ~1000x surface-EMG range, i.e. amplifier-output volts with undeclared gain or mislabeled mV - NOT rescaled, electrode-referred scale UNRESOLVED) + 557 canonical force records / 185 subjects (plate-to-foot assignment by ankle proximity to FORCE_PLATFORM centers during the loaded window, ambiguous strikes refused: 179 trials; per-foot |Fz| totals at 1000 Hz; full 24-channel plate arrays under processed/aux_force/). 160 subjects are now POSE+EMG+FORCE tri-modal. Pose validation: no errors. ingest_stroke_gait.py
- link: https://doi.org/10.6084/m9.figshare.c.6503791
- citation: Sci Data 2023, doi 10.1038/s41597-023-02767-y
- notes: hemiparetic/spastic gait WITH pathological EMG: D3 anchor and an EMG contract pathology source
