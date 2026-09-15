# MMASD (ASD therapy movement derivatives)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "MMASD (ASD therapy movement derivatives)",
 "description": "MMASD (ASD therapy movement derivatives). MoveAtlas pose family. 32 subjects. licence not specified by the authors for the DATA.",
 "identifier": "https://github.com/Li-Jicheng/MMASD-A-Multimodal-Dataset-for-Autism-Intervention-Analysis",
 "license": "https://www.apache.org/licenses/LICENSE-2.0",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A5 Stereotypies",
  "D5 Neurodevelopmental",
  "M1 Pose / video",
  "M4 Silhouette"
 ],
 "url": "https://github.com/Li-Jicheng/MMASD-A-Multimodal-Dataset-for-Autism-Intervention-Analysis",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mmasd</code>

<span class="ma-tag">Stereotypies</span><span class="ma-tag">Neurodevelopmental</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Silhouette</span>

| | |
|---|---|
| **Taxonomy cells** | A5 proxy (stereotypies), D5; M1, M4 |
| **Subjects** | 32 |
| **Ages** | school-age children |
| **Status** | DOWNLOADED 2026-08-28 (owner risk call: INTERNAL training only, never in any release tree): 7.1 GB via gdown from the README's Drive folder, all 5 zips integrity-tested (optical_flow 481,176 entries; 2D_openpose 256,379; ROMP 2D/3D/3D-71 312,773 each) + ADOS_rating.xlsx + README. Ingestion is its ow... |
| **License** | not specified by the authors for the DATA (the GitHub repo carries an Apache-2.0 badge, which covers the repo, not necessarily the Drive payload) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mmasd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: not specified by the authors for the DATA (the GitHub repo carries an Apache-2.0 badge, which covers the repo, not necessarily the Drive payload)
- **Redistribution**: no, DECIDED 2026-08-28: unspecified licence = pointer; the never-sent licence email stays in the barriers file
- **Access route**: direct download via Google Drive link (no form)
- **Source**: <https://github.com/Li-Jicheng/MMASD-A-Multimodal-Dataset-for-Autism-Intervention-Analysis>

## Publications

- Li, Jicheng; Chheang, Vuthea; Kullu, Pinar; Brignac, Eli; Guo, Zhang; Bhat, Anjana; Barner, Kenneth E.; Barmaki, Roghayeh Leila (2023). *MMASD: A Multimodal Dataset for Autism Intervention Analysis*. INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION. DOI: [10.1145/3577190.3614117](https://doi.org/10.1145/3577190.3614117)

```bibtex
@article{mmasd_paper_2023,
  title = {MMASD: A Multimodal Dataset for Autism Intervention Analysis},
  author = {Li, Jicheng and Chheang, Vuthea and Kullu, Pinar and Brignac, Eli and Guo, Zhang and Bhat, Anjana and Barner, Kenneth E. and Barmaki, Roghayeh Leila},
  year = {2023},
  doi = {10.1145/3577190.3614117},
  journal = {INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: mmasd
- family: pose  (physical path: datasets/pose/mmasd)
- MoveAtlas cells: A5 proxy (stereotypies), D5; M1, M4
- population: 32 children with ASD, >100 h therapy video as privacy-preserving derivatives; ADOS-2 scores
- n_subjects: 32
- age: school-age children
- signal: optical flow JPGs + 2D skeleton (OpenPose 25) + 3D skeleton (ROMP 71), 1,315 samples, 11 activities
- license: not specified by the authors for the DATA (the GitHub repo carries an Apache-2.0 badge, which covers the repo, not necessarily the Drive payload) ; redistribution: no, DECIDED 2026-08-28: unspecified licence = pointer; the never-sent licence email stays in the barriers file
- access: direct download via Google Drive link (no form)
- status (2026-08-22): DOWNLOADED 2026-08-28 (owner risk call: INTERNAL training only, never in any release tree): 7.1 GB via gdown from the README's Drive folder, all 5 zips integrity-tested (optical_flow 481,176 entries; 2D_openpose 256,379; ROMP 2D/3D/3D-71 312,773 each) + ADOS_rating.xlsx + README. Ingestion is its own future pass: needs OpenPose-25 and ROMP-71 joint maps in the skeleton contract
- link: https://github.com/Li-Jicheng/MMASD-A-Multimodal-Dataset-for-Autism-Intervention-Analysis
- notes: best available substitute for the empty stereotypies cell alongside ethics-gated SSBD/AV-ASD; derivatives only, no raw video
