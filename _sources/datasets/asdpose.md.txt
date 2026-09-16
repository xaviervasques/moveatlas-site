# ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024)",
 "description": "ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024). MoveAtlas pose family. 241 subjects. licence NOT YET VERIFIED.",
 "identifier": "https://github.com/Dinstein-Lab/ASDMotion",
 "license": "NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A5 Stereotypies",
  "M1 Pose / video"
 ],
 "url": "https://github.com/Dinstein-Lab/ASDMotion",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>asdpose</code>

<span class="ma-tag">Stereotypies</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A5; M1 |
| **Subjects** | 241 |
| **Ages** | children (ASD assessments) |
| **Status** | catalogued (2026-09-04) |
| **License** | NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data-sharing statement must be read before any redistribution decision |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("asdpose")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data-sharing statement must be read before any redistribution decision
- **Redistribution**: unknown
- **Access route**: github Dinstein-Lab/ASDMotion -> Google Drive links (raw video withheld for privacy)
- **Source**: <https://github.com/Dinstein-Lab/ASDMotion>
