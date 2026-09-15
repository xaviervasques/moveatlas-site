# AMASS (healthy mocap base)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "AMASS (healthy mocap base)",
 "description": "AMASS (healthy mocap base). MoveAtlas socle family. licence non-commercial research.",
 "identifier": "https://amass.is.tue.mpg.de",
 "license": "non-commercial research (per sub-dataset MPI EULA)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://amass.is.tue.mpg.de",
 "isAccessibleForFree": false,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>amass</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1 |
| **Subjects** | ~344 |
| **Status** | downloaded + INGESTED v1: 17,154 canonical records |
| **License** | non-commercial research (per sub-dataset MPI EULA) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("amass")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: non-commercial research (per sub-dataset MPI EULA)
- **Redistribution**: no
- **Access route**: account + EULA
- **Source**: <https://amass.is.tue.mpg.de>

## Publications

- Mahmood, Naureen; Ghorbani, Nima; Troje, Nikolaus F.; Pons-Moll, Gerard; Black, Michael (2019). *AMASS: Archive of Motion Capture As Surface Shapes*. 2019 IEEE/CVF International Conference on Computer Vision (ICCV). DOI: [10.1109/iccv.2019.00554](https://doi.org/10.1109/iccv.2019.00554)

```bibtex
@article{amass_paper_2019,
  title = {AMASS: Archive of Motion Capture As Surface Shapes},
  author = {Mahmood, Naureen and Ghorbani, Nima and Troje, Nikolaus F. and Pons-Moll, Gerard and Black, Michael},
  year = {2019},
  doi = {10.1109/iccv.2019.00554},
  journal = {2019 IEEE/CVF International Conference on Computer Vision (ICCV)}
}
```

## Data card (verbatim, with its evidence trail)


- Modality: mocap (SMPL-X / SMPL+H body parameters, .npz per motion)
- Source / URL: https://amass.is.tue.mpg.de (Max Planck IS), per-sub-dataset EULA
- License: non-commercial research (per sub-dataset license, MPI)
- Access: account + EULA accepted by owner (2026-07-10)
- Status: raw_downloaded (24 sub-datasets as .tar.bz2, ~31 GB, integrity-checked)
- Number of subjects: ~344 (aggregate over the full AMASS corpus; per-sub-dataset
  counts vary, to be confirmed per sub-base after extraction)
- Disorders covered: HEALTHY movement only (pretraining base). No pathology.
- Frequency / resolution: mocap-derived, high frame rate; SMPL-X/SMPL+H params
- Sub-datasets present (24) : ACCAD, BMLhandball, BMLmovi, BMLrub, CMU, CNRS, DFaust,
  DanceDB, EKUT, EyesJapanDataset, GRAB, HDM05, HUMAN4D, HumanEva, KIT, MoSh, PosePrior,
  SFU, SOMA, SSM, TCDHands, TotalCapture, Transitions, WEIZMANN.
- Specifics:
  - Postural / non-locomotor diversity: this is the priority-1 healthy base that the
    locomotor-only corpus was missing (Handoff 3). Conditions generalization to dystonia.
  - GRAB (grab.is.tue.mpg.de) is stored here in AMASS SMPL-X format; it also feeds the
    Motion-X mocap pipeline (see socle/motion_x).
  - To USE the data (not just store it) the SMPL+H and DMPL body models are required
    (mano.is.tue.mpg.de, smpl.is.tue.mpg.de). The project already has SMPL_NEUTRAL.

### Retrieval notes
Downloaded by the owner via the AMASS website (SMPL-X G per sub-dataset), staged in
`temporary/`, filed into `raw/` on 2026-07-10. Integrity of all 24 archives verified
with `tar -tjf` (see `datasets/_amass_integrity.log`).

### Processing
(pending) Extract each .tar.bz2, load SMPL-X/SMPL+H .npz, map to the canonical skeleton
(`configs/canonical_skeleton.yaml`). Keep per-sub-dataset provenance for the site probe.
Healthy base: pretraining only, no phenotype labels.
