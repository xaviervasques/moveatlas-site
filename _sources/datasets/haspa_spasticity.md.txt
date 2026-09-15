# HASPA: kinematics and kinetics of spastic patients (Recherche Data Gouv)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "HASPA: kinematics and kinetics of spastic patients (Recherche Data Gouv)",
 "description": "HASPA: kinematics and kinetics of spastic patients (Recherche Data Gouv). MoveAtlas auxdata family. licence etalab 2.0.",
 "identifier": "https://doi.org/10.57745/lrpykb",
 "license": "https://www.etalab.gouv.fr/licence-ouverte-open-licence",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "M2 Inertial (IMU)",
  "M3 Plantar force"
 ],
 "url": "https://doi.org/10.57745/lrpykb",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>haspa_spasticity</code>

<span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | E context; M2 M3 |
| **Ages** | adults |
| **Status** | DOWNLOADED 2026-09-05 (fetch_dataverse.py): 2 files 60.1 MB, server-MD5 verified, sha256 journaled. CATALOGUED 2026-09-04 (closing sweep): lower-limb kinematics + kinetics + neurophysiological parameters of spastic resistance (hypertonia, scope-adjacent). RDG portal was DOWN (maintenance) during the... |
| **License** | etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("haspa_spasticity")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version)
- **Redistribution**: unknown
- **Access route**: rdg doi:10.57745/lrpykb
- **Source**: <https://doi.org/10.57745/lrpykb>

## Data card (verbatim, with its evidence trail)


- Modality: see registry family 'auxdata'
- Source / URL: https://doi.org/10.57745/lrpykb
- License (fetch-verified 2026-09-05): etalab 2.0 (VERIFIED at fetch 2026-09-05 from the dataset version)
- Sweep's original licence guess: open per DataCite (portal in maintenance 2026-09-04 - re-verify licence when RDG returns)
- Access: rdg doi:10.57745/lrpykb
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); fetch 2026-09-05 via fetch_dataverse.py (RDG back from maintenance)
- Status (2026-09-04): CATALOGUED 2026-09-04 (closing sweep): lower-limb kinematics + kinetics + neurophysiological parameters of spastic resistance (hypertonia, scope-adjacent). RDG portal was DOWN (maintenance) during the sweep - explains the owner queue's RDG retry failures
- Number of subjects: see record
- MoveAtlas cells: E context; M2 M3

### Retrieval notes
Found by the 2026-09-04 closing sweep. Every licence/access statement
above is a catalogue-time reading of the record page or the DataCite
index - RE-VERIFY AT FETCH TIME per house rule (verification dates go
in this card).

### Processing
None. Catalogue-tier until fetched and adjudicated.
