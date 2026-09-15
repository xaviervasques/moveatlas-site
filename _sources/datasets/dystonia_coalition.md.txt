# Dystonia Coalition natural-history video + clinical repository (Emory/NIH RDCRN)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Dystonia Coalition natural-history video + clinical repository (Emory/NIH RDCRN)",
 "description": "Dystonia Coalition natural-history video + clinical repository (Emory/NIH RDCRN). MoveAtlas video family. licence application: data-access form + 1-page proposal + committee .",
 "identifier": "https://dc.rarediseasesnetwork.org/resources-researchers-and-clinicians",
 "license": "https://opensource.org/license/mit",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "video",
  "A1 Tremor",
  "M1 Pose / video"
 ],
 "url": "https://dc.rarediseasesnetwork.org/resources-researchers-and-clinicians",
 "isAccessibleForFree": false,
 "measurementTechnique": "video",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-video">video</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-barrier">barrier</span>&nbsp; <code>dystonia_coalition</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A1 all focal dystonias; M1 |
| **Subjects** | >3000 participants |
| **Status** | CATALOGUED 2026-09-05: DOCUMENTED BARRIER (application tier): standardized 2-min exam videos across ALL isolated dystonias - 38+68 blepharospasm, ~185 cervical (93 with head tremor), writing tasks - the source corpus behind published CV severity work. THE reference route if the owner ever wants dyst... |
| **License** | application: data-access form + 1-page proposal + committee review + DUA (~1 month); video requests historically via NINDS |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("dystonia_coalition")
ds.info   # barrier: get_data() explains the route
```

## License and access

- **License**: application: data-access form + 1-page proposal + committee review + DUA (~1 month); video requests historically via NINDS
- **Redistribution**: no
- **Access route**: dc.rarediseasesnetwork.org
- **Source**: <https://dc.rarediseasesnetwork.org/resources-researchers-and-clinicians>

## Data card (verbatim, with its evidence trail)


- Modality: family 'video'
- Source / URL: https://dc.rarediseasesnetwork.org/resources-researchers-and-clinicians
- License / access: application: data-access form + 1-page proposal + committee review + DUA (~1 month); video requests historically via NINDS
- Access route: dc.rarediseasesnetwork.org
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  dystonia pass; record fetched and confirmed by the catalogue sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05: DOCUMENTED BARRIER (application tier): standardized 2-min exam videos across ALL isolated dystonias - 38+68 blepharospasm, ~185 cervical (93 with head tremor), writing tasks - the source corpus behind published CV severity work. THE reference route if the owner ever wants dystonia video mass; actively distributed to outside researchers
- Number of subjects: >3000 participants
- MoveAtlas cells: A1 all focal dystonias; M1

### Retrieval notes
RE-VERIFY at fetch. mrc_lfp_dystonia: needs the owner's MRC portal
login (queue with oxford_stn_onoff_dbs - one session collects both).
dystonia_coalition: application tier - owner decision (no-emails
policy).

### Processing
None. Catalogue-tier.
