# Enroll-HD / TRACK-HD / PREDICT-HD (CHDI application family)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Enroll-HD / TRACK-HD / PREDICT-HD (CHDI application family)",
 "description": "Enroll-HD / TRACK-HD / PREDICT-HD (CHDI application family). MoveAtlas auxdata family. licence verified-researcher account + DUA.",
 "identifier": "https://enroll-hd.org/for-researchers/datasets/",
 "license": "verified-researcher account + DUA (free); periodic datasets carry SCORES only - raw Q-Motor force/oculomotor traces need",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A7 Chorea",
  "M1 Pose / video",
  "M8 Imaging"
 ],
 "url": "https://enroll-hd.org/for-researchers/datasets/",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>enroll_hd_family</code>

<span class="ma-tag">Chorea</span><span class="ma-tag">Pose / video</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A7 incl. premanifest; M1 M8 context |
| **Subjects** | >20000 (Enroll-HD PDS) |
| **Status** | documented access barrier (2026-09-05) |
| **License** | verified-researcher account + DUA (free); periodic datasets carry SCORES only - raw Q-Motor force/oculomotor traces need a specified-dataset (SPS) application |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("enroll_hd_family")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: verified-researcher account + DUA (free); periodic datasets carry SCORES only - raw Q-Motor force/oculomotor traces need a specified-dataset (SPS) application
- **Redistribution**: no
- **Access route**: enroll-hd.org/for-researchers
- **Source**: <https://enroll-hd.org/for-researchers/datasets/>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **MoveAtlas cells**: A7 incl. premanifest; M1 M8 context
