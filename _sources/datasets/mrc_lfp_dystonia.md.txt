# Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford)",
 "description": "Subthalamic/thalamic LFP + neck EMG + accelerometry in cervical dystonia (Wiest; MRC BNDU Oxford). MoveAtlas eeg family. 7 patients / 12 hemispheres subjects. licence CC BY-SA 4.0.",
 "identifier": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "A1 Tremor",
  "M2 Inertial (IMU)",
  "M4 Silhouette",
  "M7 LFP / ECoG"
 ],
 "url": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "isAccessibleForFree": false,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>mrc_lfp_dystonia</code>

<span class="ma-tag">Tremor</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Silhouette</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | A1; M2 M4 M7 |
| **Subjects** | 7 patients / 12 hemispheres |
| **Status** | CATALOGUED 2026-09-05 (deep-dive): STN/zona-incerta/VL-thalamus LFP + EEG + splenius/SCM EMG + accelerometer, MATLAB .mat, 3 zips - the strongest OPEN cervical-dystonia signal deposit found anywhere. SAME PORTAL as oxford_stn_onoff_dbs: the owner's pending MRC login session can collect BOTH |
| **License** | CC BY-SA 4.0 (verified on the portal record; SA clause: licence-matrix check before redistribution); free registration/login then direct download |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("mrc_lfp_dystonia")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-SA 4.0 (verified on the portal record; SA clause: licence-matrix check before redistribution); free registration/login then direct download
- **Redistribution**: share-alike
- **Access route**: data.mrc.ox.ac.uk/lfp-dystonia (DOI 10.5287/bodleian:QRNQjNpV7)
- **Source**: <https://data.mrc.ox.ac.uk/lfp-dystonia>

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://data.mrc.ox.ac.uk/lfp-dystonia
- License / access: CC BY-SA 4.0 (verified on the portal record; SA clause: licence-matrix check before redistribution); free registration/login then direct download
- Access route: data.mrc.ox.ac.uk/lfp-dystonia (DOI 10.5287/bodleian:QRNQjNpV7)
- Version / retrieval date: catalogued 2026-09-05 (deep-dive sweep,
  dystonia pass; record fetched and confirmed by the catalogue sweep)
- Status (2026-09-05): CATALOGUED 2026-09-05 (deep-dive): STN/zona-incerta/VL-thalamus LFP + EEG + splenius/SCM EMG + accelerometer, MATLAB .mat, 3 zips - the strongest OPEN cervical-dystonia signal deposit found anywhere. SAME PORTAL as oxford_stn_onoff_dbs: the owner's pending MRC login session can collect BOTH
- Number of subjects: 7 patients / 12 hemispheres
- MoveAtlas cells: A1; M2 M4 M7

### Retrieval notes
RE-VERIFY at fetch. mrc_lfp_dystonia: needs the owner's MRC portal
login (queue with oxford_stn_onoff_dbs - one session collects both).
dystonia_coalition: application tier - owner decision (no-emails
policy).

### Processing
None. Catalogue-tier.
