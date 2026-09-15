# Motion-X++ (healthy motion base)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Motion-X++ (healthy motion base)",
 "description": "Motion-X++ (healthy motion base). MoveAtlas socle family. licence non-commercial research.",
 "identifier": "https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus",
 "license": "non-commercial research",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "socle",
  "C1 Normal adult movement",
  "M1 Pose / video"
 ],
 "url": "https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus",
 "isAccessibleForFree": false,
 "measurementTechnique": "socle",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-socle">socle</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>motion_x</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M1 |
| **Subjects** | clip-indexed |
| **Status** | downloaded + INGESTED v1: 25,865 records |
| **License** | non-commercial research |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("motion_x")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: non-commercial research
- **Redistribution**: no
- **Access route**: public HuggingFace download
- **Source**: <https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus>

## Publications

- Lin, Jing; Zeng, Ailing; Lu, Shunlin; Cai, Yuanhao; Zhang, Ruimao; Wang, Haoqian; Zhang, Lei (2023). *Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset*. arXiv. DOI: [10.48550/arxiv.2307.00818](https://doi.org/10.48550/arxiv.2307.00818)

```bibtex
@article{motion_x_paper_2023,
  title = {Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset},
  author = {Lin, Jing and Zeng, Ailing and Lu, Shunlin and Cai, Yuanhao and Zhang, Ruimao and Wang, Haoqian and Zhang, Lei},
  year = {2023},
  doi = {10.48550/arxiv.2307.00818},
  journal = {arXiv}
}
```

## Data card (verbatim, with its evidence trail)


- Modality: motion (SMPL-X whole-body params, keypoints, mesh) + text labels
- Source / URL: https://huggingface.co/datasets/YuhongZhang/Motion-Xplusplus
  (Motion-X++, NeurIPS 2023 lineage). Original toolkit/repo also kept (see below).
- License: non-commercial research (Motion-X license). HuggingFace copy is public /
  non-gated. Mocap subsets (AMASS/GRAB) keep their own MPI licenses.
- Access: public HuggingFace download (no EULA, no form); owner account VasquesXavier
- Status: raw_downloaded (47 GB motion + 488 MB text + 89 MB video, download clean,
  0 incomplete files, no LFS pointers)
- Number of subjects: unknown at subject level (dataset is clip/motion-indexed;
  ~15.6M poses / 81.1K clips across subsets)
- Disorders covered: HEALTHY movement only (pretraining base). No pathology.
- Contenu present (motion_x_plusplus/) :
  - motion/keypoints, motion/mesh_recovery (global + local), motion/motion_generation
    (joint, new_joint, new_joint_vecs, smplx322, root_body_pos_vel_hand_pos_vel)
  - text/pose_description, text/semantic_label
  - video/ (sample visualization GIFs only)
  - subsets seen: idea400 (self-recorded, covers NTU-RGBD120 actions), music, haa500,
    and others, each as .zip per representation.
- Specifics:
  - IDEA400 is Motion-X's licensed replacement for NTU-RGBD120 (400 daily actions).
  - The IDEA Research team does NOT redistribute original RGB video; only motion +
    text. Stays within scope (no identifiable video).
  - Also on disk: `Motion-X-main/` = the original GitHub toolkit (processing scripts,
    split index files). Useful for reconstructing the mocap subsets against AMASS/GRAB
    (already in socle/amass/raw) if the original Motion-X format is ever needed.

### Retrieval notes
Downloaded 2026-07-10 via `hf download YuhongZhang/Motion-Xplusplus --repo-type dataset
--local-dir datasets/socle/motion_x/raw/motion_x_plusplus`. Log:
`datasets/_motionx_download.log`. Resumable; re-run to complete if interrupted.

### Processing
(pending) Unzip the chosen representation (smplx322 or keypoints), map to the canonical
skeleton (`configs/canonical_skeleton.yaml`). Keep per-subset provenance for the site
probe. Healthy base: pretraining only, no phenotype labels.
