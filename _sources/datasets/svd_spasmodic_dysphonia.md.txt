# Saarbruecken Voice Database - spasmodic dysphonia subset (voice + EGG)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Saarbruecken Voice Database - spasmodic dysphonia subset (voice + EGG)",
 "description": "Saarbruecken Voice Database - spasmodic dysphonia subset (voice + EGG). MoveAtlas auxdata family. licence CC BY 4.0.",
 "identifier": "https://zenodo.org/records/16874898",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "auxdata",
  "A1 Tremor",
  "M8 Imaging"
 ],
 "url": "https://zenodo.org/records/16874898",
 "isAccessibleForFree": false,
 "measurementTechnique": "auxdata",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-auxdata">auxdata</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>svd_spasmodic_dysphonia</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Imaging</span>

| | |
|---|---|
| **Taxonomy cells** | A1 laryngeal; M8 |
| **Subjects** | see subset |
| **Status** | DOWNLOADED 2026-09-05: the SD subset zip (492.7 MB, 2031 files WAV+EGG, server-md5 verified, sha256 journaled, zip listing clean). CATALOGUED 2026-09-05 (deep-dive): vowels /a i u/ x3 pitches + sentence, WAV + simultaneous electroglottography - the ONLY fully open spasmodic-dysphonia signal deposit... |
| **License** | CC BY 4.0 (Zenodo 16874898), free direct download |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("svd_spasmodic_dysphonia")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY 4.0 (Zenodo 16874898), free direct download
- **Redistribution**: unknown
- **Access route**: zenodo 16874898 (full DB ~38 GB; SD zip 492.7 MB)
- **Source**: <https://zenodo.org/records/16874898>

## Data card (verbatim, with its evidence trail)


- Modality: family 'auxdata' (speech-motor signal)
- Source / URL: https://zenodo.org/records/16874898
- License / access: CC BY 4.0 (Zenodo 16874898), free direct download
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): vowels /a i u/ x3 pitches + sentence, WAV + simultaneous electroglottography - the ONLY fully open spasmodic-dysphonia signal deposit found; laryngeal dystonia joins the A1 holdings. Fetch = the SD subset zip only
- MoveAtlas cells: A1 laryngeal; M8

### Retrieval notes
RE-VERIFY at fetch/request; no-emails policy for gated tiers.

### Processing
None. Catalogue-tier.
