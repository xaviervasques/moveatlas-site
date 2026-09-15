# PEARL-PD: personalized gait rehabilitation in PD (DANS)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PEARL-PD: personalized gait rehabilitation in PD (DANS)",
 "description": "PEARL-PD: personalized gait rehabilitation in PD (DANS). MoveAtlas imu family. licence gated: DANS registration/request.",
 "identifier": "https://doi.org/10.17026/DANS-X94-WDK6",
 "license": "gated: DANS registration/request (licence at grant)",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "M2 Inertial (IMU)"
 ],
 "url": "https://doi.org/10.17026/DANS-X94-WDK6",
 "isAccessibleForFree": false,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>pearl_pd</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Inertial (IMU)</span>

| | |
|---|---|
| **Taxonomy cells** | B2 B3; M2 |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): mocap spatiotemporal gait under 5 compensation strategies + clinimetrics (NFOG-Q), 5 files. Request-tier: journal the request if pursued (no-emails policy applies - document instead) |
| **License** | gated: DANS registration/request (licence at grant) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("pearl_pd")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: gated: DANS registration/request (licence at grant)
- **Redistribution**: unknown
- **Access route**: dans doi:10.17026/DANS-X94-WDK6
- **Source**: <https://doi.org/10.17026/DANS-X94-WDK6>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'imu'
- Source / URL: https://doi.org/10.17026/DANS-X94-WDK6
- License: gated: DANS registration/request (licence at grant)
- Access: dans doi:10.17026/DANS-X94-WDK6
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); NOT fetched
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): mocap spatiotemporal gait under 5 compensation strategies + clinimetrics (NFOG-Q), 5 files. Request-tier: journal the request if pursued (no-emails policy applies - document instead)
- Number of subjects: see record
- MoveAtlas cells: B2 B3; M2

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
