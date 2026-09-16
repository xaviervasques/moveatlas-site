# Oxford STN LFP at rest: levodopa ON/OFF and 130 Hz DBS (MRC BNDU)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Oxford STN LFP at rest: levodopa ON/OFF and 130 Hz DBS (MRC BNDU)",
 "description": "Oxford STN LFP at rest: levodopa ON/OFF and 130 Hz DBS (MRC BNDU). MoveAtlas eeg family. licence CC BY-SA 4.0.",
 "identifier": "https://data.mrc.ox.ac.uk/stn-lfp-on-off-and-dbs",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B1 Rigidity",
  "B2 Bradykinesia",
  "M2 Inertial (IMU)",
  "M6 EEG",
  "M7 LFP / ECoG"
 ],
 "url": "https://data.mrc.ox.ac.uk/stn-lfp-on-off-and-dbs",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>oxford_stn_onoff_dbs</code>

<span class="ma-tag">Rigidity</span><span class="ma-tag">Bradykinesia</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">EEG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B1, B2; M2 (accelerometer), M6 (scalp EEG), M7 (STN LFP) |
| **Subjects** | ~16 |
| **Status** | catalogued (2026-09-01) |
| **License** | CC BY-SA 4.0 (verified on page 2026-09-01) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("oxford_stn_onoff_dbs")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: CC BY-SA 4.0 (verified on page 2026-09-01)
- **Redistribution**: yes
- **Access route**: MRC BNDU data portal: registration + login
- **Source**: <https://data.mrc.ox.ac.uk/stn-lfp-on-off-and-dbs>

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: oxford_stn_onoff_dbs
- **family**: eeg
- **MoveAtlas cells**: B1, B2; M2 (accelerometer), M6 (scalp EEG), M7 (STN LFP)
- **population**: 30 hemispheres ON/OFF levodopa, 26 during 130 Hz DBS; rest recordings with LFP + scalp EEG + accelerometer
- **n_subjects**: ~16
- **signal**: STN LFP + scalp EEG (Fz/Cz/F3...) + accelerometer at rest, three therapy states
- **license**: CC BY-SA 4.0 (verified on page 2026-09-01); redistribution: yes
- **access**: MRC BNDU data portal: registration + login
- **link**: https://data.mrc.ox.ac.uk/stn-lfp-on-off-and-dbs
