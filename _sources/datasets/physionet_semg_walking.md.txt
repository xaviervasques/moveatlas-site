# Long-term surface EMG during walking (PhysioNet semg 1.0.1)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Long-term surface EMG during walking (PhysioNet semg 1.0.1)",
 "description": "Long-term surface EMG during walking (PhysioNet semg 1.0.1). MoveAtlas emg family. 31 subjects. licence ODC-By 1.0.",
 "identifier": "https://physionet.org/content/semg/1.0.1/",
 "license": "https://opendatacommons.org/licenses/by/1-0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "emg",
  "C1 Normal adult movement",
  "M5 EMG"
 ],
 "url": "https://physionet.org/content/semg/1.0.1/",
 "isAccessibleForFree": true,
 "measurementTechnique": "emg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Di Nardo, Francesco"
  },
  {
   "@type": "Person",
   "name": "Morbidoni, Christian"
  },
  {
   "@type": "Person",
   "name": "Fioretti, Sandro"
  }
 ]
}
</script>
```

<span class="ma-fam ma-emg">emg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>physionet_semg_walking</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M5 |
| **Subjects** | 31 |
| **Status** | INGESTED AND VERIFIED 2026-08-22: 31 canonical EMG records, 14/14 channels resolved on every record, 0 unrecognized. The .hea vocabulary is closed and was read off all 31 headers: sensors semg/baso/gonio, sides LT/RT, EMG sites TIB.A LAT.G REC.F HAM LAT.V; footswitches and goniometers are routed to... |
| **License** | ODC-By 1.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("physionet_semg_walking")
records, meta = ds.get_data()
```

## License and access

- **License**: ODC-By 1.0
- **Redistribution**: yes
- **Access route**: direct_download (fetch_p2_lot.py --only semg_walking; 278.5 MB zip verified)
- **Source**: <https://physionet.org/content/semg/1.0.1/>

## Publications

- Di Nardo, Francesco; Morbidoni, Christian; Fioretti, Sandro (2024). *Surface electromyographic signals collected during long-lasting ground walking of young able-bodied subjects*. PhysioNet. DOI: [10.13026/grdj-qx06](https://doi.org/10.13026/grdj-qx06)
- Di Nardo, Francesco; Morbidoni, Christian; Cucchiarelli, Alessandro; Fioretti, Sandro (2021). *Influence of EMG-signal processing and experimental set-up on prediction of gait events by neural network*. Biomedical Signal Processing and Control. DOI: [10.1016/j.bspc.2020.102232](https://doi.org/10.1016/j.bspc.2020.102232)

```bibtex
@misc{physionet_semg_walking_data_2024,
  title = {Surface electromyographic signals collected during long-lasting ground walking of young able-bodied subjects},
  author = {Di Nardo, Francesco and Morbidoni, Christian and Fioretti, Sandro},
  year = {2024},
  doi = {10.13026/grdj-qx06},
  howpublished = {PhysioNet},
  note = {dataset}
}
@article{physionet_semg_walking_paper_2021,
  title = {Influence of EMG-signal processing and experimental set-up on prediction of gait events by neural network},
  author = {Di Nardo, Francesco and Morbidoni, Christian and Cucchiarelli, Alessandro and Fioretti, Sandro},
  year = {2021},
  doi = {10.1016/j.bspc.2020.102232},
  journal = {Biomedical Signal Processing and Control}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: physionet_semg_walking
- family: emg  (physical path: datasets/emg/physionet_semg_walking)
- MoveAtlas cells: C1; M5
- population: 31 healthy young adults, 5-min barefoot walking
- n_subjects: 31
- signal: sEMG of 10 leg muscles at 2 kHz, 12-bit + footswitch + electrogoniometer (WFDB)
- license: ODC-By 1.0 ; redistribution: yes
- access: direct_download (fetch_p2_lot.py --only semg_walking; 278.5 MB zip verified)
- status (2026-08-22): INGESTED AND VERIFIED 2026-08-22: 31 canonical EMG records, 14/14 channels resolved on every record, 0 unrecognized. The .hea vocabulary is closed and was read off all 31 headers: sensors semg/baso/gonio, sides LT/RT, EMG sites TIB.A LAT.G REC.F HAM LAT.V; footswitches and goniometers are routed to aux. FINDING: S01 and S21 declare mV in their header while their amplitudes are ~1000x the other 29 records (p99 155 mV vs 0.14 mV), so their header unit is wrong and the data is really uV; both are FLAGGED in the audit and deliberately NOT rescaled. Ingestion chain: build_canonical_emg.py --only semg_walking (wfdb reader, self-describing .hea enforced at run time; first real batch = the verification; extend the muscle alias table from the printed channel table)
- link: https://physionet.org/content/semg/1.0.1/
- notes: first socle of the EMG contract (WBS 1.3); preserve native rate
