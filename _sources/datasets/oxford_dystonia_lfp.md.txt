# Oxford BNDU cervical dystonia STN/thalamic LFP + EEG + neck EMG + ACC

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Oxford BNDU cervical dystonia STN/thalamic LFP + EEG + neck EMG + ACC",
 "description": "Oxford BNDU cervical dystonia STN/thalamic LFP + EEG + neck EMG + ACC. MoveAtlas eeg family. 7 subjects. licence CC BY-SA 4.0.",
 "identifier": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "license": "https://creativecommons.org/licenses/by-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "A4 Dystonia",
  "M5 EMG",
  "M6 EEG",
  "M7 LFP / ECoG"
 ],
 "url": "https://data.mrc.ox.ac.uk/lfp-dystonia",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>oxford_dystonia_lfp</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M5 (pathological neck EMG), M6, M7 |
| **Subjects** | 7 |
| **Status** | DOWNLOADED 2026-08-25 via the owner's MRC account, after several browser retries on a contended line: 3 zips, 14.7 GB total, CRC clean (P1,P2 / P3,P4 / P5,P6,P7 with per-hemisphere folders). RULE R1: invasive LFP, so NO movement-pretraining ingestion; joins ds004998 in the phase 2.4 invasive-contrac... |
| **License** | CC BY-SA 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("oxford_dystonia_lfp")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY-SA 4.0
- **Redistribution**: yes (share-alike)
- **Access route**: registration (free MRC data portal account), then direct download
- **Source**: <https://data.mrc.ox.ac.uk/lfp-dystonia>

## Publications

- Wiest, Christoph; Morgante, Francesca; Torrecillos, Flavie; Pogosyan, Alek; He, Shenghong; Baig, Fahd; Bertaina, Ilaria; Hart, Michael G.; Edwards, Mark J.; Pereira, Erlick A.; Tan, Huiling (2023). *Subthalamic Nucleus Stimulation–Induced Local Field Potential Changes in Dystonia*. Movement Disorders. DOI: [10.1002/mds.29302](https://doi.org/10.1002/mds.29302)

```bibtex
@article{oxford_dystonia_lfp_paper_2023,
  title = {Subthalamic Nucleus Stimulation–Induced Local Field Potential Changes in Dystonia},
  author = {Wiest, Christoph and Morgante, Francesca and Torrecillos, Flavie and Pogosyan, Alek and He, Shenghong and Baig, Fahd and Bertaina, Ilaria and Hart, Michael G. and Edwards, Mark J. and Pereira, Erlick A. and Tan, Huiling},
  year = {2023},
  doi = {10.1002/mds.29302},
  journal = {Movement Disorders}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: oxford_dystonia_lfp
- family: eeg  (physical path: datasets/eeg/oxford_dystonia_lfp)
- MoveAtlas cells: A4; M5 (pathological neck EMG), M6, M7
- population: 7 cervical dystonia patients (12 hemispheres), Boston Vercise leads in STN/ZI/VL thalamus, stimulation ramps
- n_subjects: 7
- signal: LFP + scalp EEG + neck EMG + accelerometer (.mat, 3 zips)
- license: CC BY-SA 4.0 ; redistribution: yes (share-alike)
- access: registration (free MRC data portal account), then direct download
- status (2026-08-22): DOWNLOADED 2026-08-25 via the owner's MRC account, after several browser retries on a contended line: 3 zips, 14.7 GB total, CRC clean (P1,P2 / P3,P4 / P5,P6,P7 with per-hemisphere folders). RULE R1: invasive LFP, so NO movement-pretraining ingestion; joins ds004998 in the phase 2.4 invasive-contract queue. The only open dystonia LFP in existence is now on this disk
- link: https://data.mrc.ox.ac.uk/lfp-dystonia
- citation: Wiest et al. 2022, Mov Disord, doi 10.1002/mds.29302
- notes: the only public dystonia LFP+EMG pairing found; distinct from the Tan/Oxford 2016 PD testbed set. R1 scoping applies
