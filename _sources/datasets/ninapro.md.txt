# Ninapro (hand/forearm sEMG)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "Ninapro (hand/forearm sEMG)",
 "description": "Ninapro (hand/forearm sEMG). MoveAtlas emg family. licence registration; per-database terms.",
 "identifier": "https://ninapro.hevs.ch/",
 "license": "registration; per-database terms",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "emg",
  "C1 Normal adult movement",
  "M5 EMG"
 ],
 "url": "https://ninapro.hevs.ch/",
 "isAccessibleForFree": false,
 "measurementTechnique": "emg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-emg">emg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>ninapro</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">EMG</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M5 |
| **Subjects** | per sub-database |
| **Status** | DOWNLOADED 2026-08-25: all 67 preprocessed zips, 17.6 GB, sha256 journaled, integrity sampled clean. DB1: 27 subjects, 10 Otto Bock electrodes + Cyberglove. DB2: 40 subjects, 12 Delsys electrodes at 2 kHz. INGESTED 2026-08-26: 201 canonical EMG records / 67 subjects / 64 h (build_canonical_emg.py --... |
| **License** | registration; per-database terms |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("ninapro")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: registration; per-database terms
- **Redistribution**: no, DECIDED 2026-08-28: no written licence anywhere on the site; pointer to ninapro.hevs.ch
- **Access route**: direct download (the registration wall is gone, verified 2026-08-25)
- **Source**: <https://ninapro.hevs.ch/>

## Publications

- Atzori, Manfredo; Gijsberts, Arjan; Castellini, Claudio; Caputo, Barbara; Hager, Anne-Gabrielle Mittaz; Elsig, Simone; Giatsidis, Giorgio; Bassetto, Franco; Müller, Henning (2014). *Electromyography data for non-invasive naturally-controlled robotic hand prostheses*. Scientific Data. DOI: [10.1038/sdata.2014.53](https://doi.org/10.1038/sdata.2014.53)

```bibtex
@article{ninapro_paper_2014,
  title = {Electromyography data for non-invasive naturally-controlled robotic hand prostheses},
  author = {Atzori, Manfredo and Gijsberts, Arjan and Castellini, Claudio and Caputo, Barbara and Hager, Anne-Gabrielle Mittaz and Elsig, Simone and Giatsidis, Giorgio and Bassetto, Franco and Müller, Henning},
  year = {2014},
  doi = {10.1038/sdata.2014.53},
  journal = {Scientific Data}
}
```

## Data card (verbatim, with its evidence trail)


- dataset: ninapro
- family: emg  (physical path: datasets/emg/ninapro)
- MoveAtlas cells: C1; M5
- population: healthy and amputee subjects, hand movement batteries
- n_subjects: per sub-database
- signal: multi-channel forearm sEMG arrays + hand kinematics
- license: registration; per-database terms ; redistribution: no, DECIDED 2026-08-28: no written licence anywhere on the site; pointer to ninapro.hevs.ch
- access: direct download (the registration wall is gone, verified 2026-08-25)
- status (2026-08-22): DOWNLOADED 2026-08-25: all 67 preprocessed zips, 17.6 GB, sha256 journaled, integrity sampled clean. DB1: 27 subjects, 10 Otto Bock electrodes + Cyberglove. DB2: 40 subjects, 12 Delsys electrodes at 2 kHz. INGESTED 2026-08-26: 201 canonical EMG records / 67 subjects / 64 h (build_canonical_emg.py --only ninapro). DB1 kept as the RMS envelope it is (unit unknown, C-EMG-1); DB2 V converted to mV, p99 0.15-0.20 mV, physiological. restimulus rides as the eval-only label; glove, accelerometer and inclinometer streams in aux. No explicit licence text on the site: cite Atzori 2014, redistribution stays flagged
- link: https://ninapro.hevs.ch/
- notes: distal complement of the EMG socle; electrode arrays map to muscle forearm_array in the EMG contract
