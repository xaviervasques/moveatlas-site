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
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (two-tier, like PPMI): the Huntington family's data mass - TRACK-HD (360 incl. preHD, oculomotor + Q-Motor force transducers), PREDICT-HD (~1000 prodromal), Enroll-HD PDS (>20k, scores) - all behind the CHDI application; raw signal per-request |
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

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata'
- Source / URL: https://enroll-hd.org/for-researchers/datasets/
- License / access: verified-researcher account + DUA (free); periodic datasets carry SCORES only - raw Q-Motor force/oculomotor traces need a specified-dataset (SPS) application
- Access route: enroll-hd.org/for-researchers
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep); not fetched at card creation
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (two-tier, like PPMI): the Huntington family's data mass - TRACK-HD (360 incl. preHD, oculomotor + Q-Motor force transducers), PREDICT-HD (~1000 prodromal), Enroll-HD PDS (>20k, scores) - all behind the CHDI application; raw signal per-request
- Number of subjects: >20000 (Enroll-HD PDS)
- MoveAtlas cells: A7 incl. premanifest; M1 M8 context

### Retrieval notes
RE-VERIFY at fetch/request. No-emails policy for request tiers.

### Processing
None. Catalogue-tier.
