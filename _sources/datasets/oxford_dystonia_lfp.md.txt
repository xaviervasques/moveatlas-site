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

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>oxford_dystonia_lfp</code>

<span class="ma-tag">Dystonia</span><span class="ma-tag">EMG</span><span class="ma-tag">EEG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | A4; M5 (pathological neck EMG), M6, M7 |
| **Subjects** | 7 |
| **Status** | acquired (2026-08-25) |
| **License** | CC BY-SA 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("oxford_dystonia_lfp")
ds.info   # recipe: get_data() explains the route
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

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: oxford_dystonia_lfp
- **family**: eeg
- **MoveAtlas cells**: A4; M5 (pathological neck EMG), M6, M7
- **population**: 7 cervical dystonia patients (12 hemispheres), Boston Vercise leads in STN/ZI/VL thalamus, stimulation ramps
- **n_subjects**: 7
- **signal**: LFP + scalp EEG + neck EMG + accelerometer (.mat, 3 zips)
- **license**: CC BY-SA 4.0; redistribution: yes (share-alike)
- **access**: registration (free MRC data portal account), then direct download
- **link**: https://data.mrc.ox.ac.uk/lfp-dystonia
- **citation**: Wiest et al. 2022, Mov Disord, doi 10.1002/mds.29302
