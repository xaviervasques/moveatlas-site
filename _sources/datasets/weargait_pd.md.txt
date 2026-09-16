# WearGait-PD (FDA/CDRH, Synapse syn52540892)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "WearGait-PD (FDA/CDRH, Synapse syn52540892)",
 "description": "WearGait-PD (FDA/CDRH, Synapse syn52540892). MoveAtlas imu family. 185 subjects. licence CC BY 4.0.",
 "identifier": "https://www.synapse.org/Synapse:syn52540892",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "imu",
  "B2 Bradykinesia",
  "B3 Hypokinesia",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)",
  "M3 Plantar force"
 ],
 "url": "https://www.synapse.org/Synapse:syn52540892",
 "isAccessibleForFree": true,
 "measurementTechnique": "imu",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 },
 "creator": [
  {
   "@type": "Person",
   "name": "Kontson, Kimberly"
  },
  {
   "@type": "Person",
   "name": "Butala, Ankur"
  },
  {
   "@type": "Person",
   "name": "Muir, Brittney"
  },
  {
   "@type": "Person",
   "name": "Anderson, Anthony"
  },
  {
   "@type": "Person",
   "name": "Caiola, Michael"
  },
  {
   "@type": "Person",
   "name": "Eguren, David"
  },
  {
   "@type": "Person",
   "name": "Gonzalez, Michael"
  },
  {
   "@type": "Person",
   "name": "Motely, Seneca"
  },
  {
   "@type": "Person",
   "name": "Mills, Kelly"
  },
  {
   "@type": "Person",
   "name": "Moro Velazquez, Laureano"
  },
  {
   "@type": "Person",
   "name": "Dehak, Najim"
  },
  {
   "@type": "Person",
   "name": "Moukheiber, Emile"
  }
 ]
}
</script>
```

<span class="ma-fam ma-imu">imu</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>weargait_pd</code>

<span class="ma-tag">Bradykinesia</span><span class="ma-tag">Hypokinesia</span><span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Plantar force</span>

| | |
|---|---|
| **Taxonomy cells** | B2, B3, C1 (age-matched controls); M2, M3 |
| **Subjects** | 185 |
| **Status** | harmonized |
| **License** | CC BY 4.0 |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("weargait_pd")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0
- **Redistribution**: yes
- **Access route**: registration (free Synapse account + click-through)
- **Source**: <https://www.synapse.org/Synapse:syn52540892>

## Publications

- Kontson, Kimberly; Butala, Ankur; Muir, Brittney; Anderson, Anthony; Caiola, Michael; Eguren, David; Gonzalez, Michael; Motely, Seneca; Mills, Kelly; Moro Velazquez, Laureano; Dehak, Najim; Moukheiber, Emile (2024). *Wearables for gait in Parkinson's Disease and age-matched controls*. Synapse. DOI: [10.7303/syn52540892](https://doi.org/10.7303/syn52540892)

```bibtex
@misc{weargait_pd_data_2024,
  title = {Wearables for gait in Parkinson's Disease and age-matched controls},
  author = {Kontson, Kimberly and Butala, Ankur and Muir, Brittney and Anderson, Anthony and Caiola, Michael and Eguren, David and Gonzalez, Michael and Motely, Seneca and Mills, Kelly and Moro Velazquez, Laureano and Dehak, Najim and Moukheiber, Emile},
  year = {2024},
  doi = {10.7303/syn52540892},
  howpublished = {Synapse},
  note = {dataset}
}
```

## Data card

The dataset's card, factual lines; the full card with its verification dates, download journal and processing notes is in the repository.

- **dataset**: weargait_pd
- **family**: imu
- **MoveAtlas cells**: B2, B3, C1 (age-matched controls); M2, M3
- **population**: 100 PD + 85 age-matched controls, 1,458 gait/balance trials
- **n_subjects**: 185
- **signal**: 13 Xsens IMUs (full 9-axis) + Moticon insoles (16 cells/foot) + walkway + video, all 100 Hz
- **license**: CC BY 4.0; redistribution: yes
- **access**: registration (free Synapse account + click-through)
- **link**: https://www.synapse.org/Synapse:syn52540892
- **ingestion**: build_canonical_imu.py + build_canonical_force.py (totals-only)
