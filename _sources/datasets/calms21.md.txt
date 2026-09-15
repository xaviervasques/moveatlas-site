# CalMS21 mouse social behavior pose corpus (Caltech)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "CalMS21 mouse social behavior pose corpus (Caltech)",
 "description": "CalMS21 mouse social behavior pose corpus (Caltech). MoveAtlas animal family. licence CC BY 4.0. VERIFIED 2026-09-02 on the CaltechDATA record pag.",
 "identifier": "https://data.caltech.edu/records/s0vdx-0k302",
 "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "animal"
 ],
 "url": "https://data.caltech.edu/records/s0vdx-0k302",
 "isAccessibleForFree": true,
 "measurementTechnique": "animal",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-animal">animal</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>calms21</code>

| | |
|---|---|
| **Taxonomy cells** | animal: healthy mouse pose/behavior socle (6M unlabeled + 1M annotated pose frames) |
| **Subjects** | many sessions |
| **Status** | DOWNLOADED 2026-09-02: the pose corpus WITHOUT the videos - task1_classic_classification.zip 457.4 MB + task1_MARS_features.zip 1.8 GB + task2_annotation_styles.zip 912.1 MB + task3_new_behaviors.zip 556.2 MB + readme + converter script, every file md5-checked against the record page, sha256 journal... |
| **License** | CC BY 4.0. VERIFIED 2026-09-02 on the CaltechDATA record page in a browser: 'Rights / License: Creative Commons Attribution 4.0 International', record marked Open, DOI 10.22002/D1.1991; the deposit readme carries ZERO rights language, so the record licence governs everything in it. The MIXED CC BY-NC-SA caution came from the project website, not the deposit; retired with evidence |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("calms21")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0. VERIFIED 2026-09-02 on the CaltechDATA record page in a browser: 'Rights / License: Creative Commons Attribution 4.0 International', record marked Open, DOI 10.22002/D1.1991; the deposit readme carries ZERO rights language, so the record licence governs everything in it. The MIXED CC BY-NC-SA caution came from the project website, not the deposit; retired with evidence
- **Redistribution**: yes (CC BY 4.0)
- **Access route**: CaltechDATA direct download (s0vdx-0k302); the 2026-08-22 403s were network/UA-specific, plain curl works from the Mac side
- **Source**: <https://data.caltech.edu/records/s0vdx-0k302>

## Data card (verbatim, with its evidence trail)


- dataset: calms21
- family: animal  (physical path: datasets/animal/calms21)
- MoveAtlas cells: animal: healthy mouse pose/behavior socle (6M unlabeled + 1M annotated pose frames)
- population: mouse dyads, resident-intruder assays
- n_subjects: many sessions
- signal: pose estimates + TREBA features + behavior annotations
- license: CC BY 4.0. VERIFIED 2026-09-02 on the CaltechDATA record page in a browser: 'Rights / License: Creative Commons Attribution 4.0 International', record marked Open, DOI 10.22002/D1.1991; the deposit readme carries ZERO rights language, so the record licence governs everything in it. The MIXED CC BY-NC-SA caution came from the project website, not the deposit; retired with evidence ; redistribution: yes (CC BY 4.0)
- access: CaltechDATA direct download (s0vdx-0k302); the 2026-08-22 403s were network/UA-specific, plain curl works from the Mac side
- status (2026-08-22): DOWNLOADED 2026-09-02: the pose corpus WITHOUT the videos - task1_classic_classification.zip 457.4 MB + task1_MARS_features.zip 1.8 GB + task2_annotation_styles.zip 912.1 MB + task3_new_behaviors.zip 556.2 MB + readme + converter script, every file md5-checked against the record page, sha256 journaled. Video zips (28.3 + 74.2 + 3.5 GB) deliberately NOT fetched: the pose socle needs trajectories, not pixels
- link: https://data.caltech.edu/records/s0vdx-0k302
