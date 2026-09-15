# Leuven/Pellenberg 3D gait of children with CP (figshare)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Leuven/Pellenberg 3D gait of children with CP (figshare)",
 "description": "Leuven/Pellenberg 3D gait of children with CP (figshare). MoveAtlas pose family. licence open on figshare.",
 "identifier": "https://doi.org/10.6084/m9.figshare.4877432",
 "license": "open on figshare (licence on record, verify at fetch)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "M3 Plantar force"
 ],
 "url": "https://doi.org/10.6084/m9.figshare.4877432",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>leuven_cp_gait</code>

<span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | D CP; M3 |
| **Status** | DOWNLOADED 2026-09-06: 35.8 MB xlsx (stratified fold kinematic parameters + curves), CC0 API-verified, server-md5 verified. NOTE: parameters/curves workbook, not raw marker trajectories - card the content verdict. CATALOGUED 2026-09-05: Vicon Plug-In-Gait 3D kinematics, spastic uni/bilateral CP 3-18... |
| **License** | open on figshare (licence on record, verify at fetch) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("leuven_cp_gait")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: open on figshare (licence on record, verify at fetch)
- **Redistribution**: unknown
- **Access route**: figshare 4877432
- **Source**: <https://doi.org/10.6084/m9.figshare.4877432>

## Data card (verbatim, with its evidence trail)


- Modality: family 'pose'
- Source / URL: https://doi.org/10.6084/m9.figshare.4877432
- License / access: open on figshare (licence on record, verify at fetch)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  pediatric/genetic-rare pass); NOT fetched
- Status (2026-09-05): CATALOGUED 2026-09-05: Vicon Plug-In-Gait 3D kinematics, spastic uni/bilateral CP 3-18 y GMFCS I-III - mocap complement to mobile_gaitlab
- MoveAtlas cells: D CP; M3

### Retrieval notes
RE-VERIFY at fetch. No-emails policy for application tiers.

### Processing
None. Catalogue-tier.
