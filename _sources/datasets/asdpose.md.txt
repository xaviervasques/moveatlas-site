# ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024)",
 "description": "ASDPose stereotypy skeletons (Dinstein lab; JAMA Netw Open 2024). MoveAtlas pose family. 241 subjects. licence NOT YET VERIFIED.",
 "identifier": "https://github.com/Dinstein-Lab/ASDMotion",
 "license": "NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "pose",
  "A5 Stereotypies",
  "M1 Pose / video"
 ],
 "url": "https://github.com/Dinstein-Lab/ASDMotion",
 "isAccessibleForFree": false,
 "measurementTechnique": "pose",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-pose">pose</span>&nbsp; <span class="ma-badge ma-catalogued">catalogued</span>&nbsp; <span class="ma-badge ma-recipe">recipe</span>&nbsp; <code>asdpose</code>

<span class="ma-tag">Stereotypies</span><span class="ma-tag">Pose / video</span>

| | |
|---|---|
| **Taxonomy cells** | A5; M1 |
| **Subjects** | 241 |
| **Ages** | children (ASD assessments) |
| **Status** | CATALOGUED 2026-09-04 (closing sweep): 319 assessments / 241 children / 7,352 manually annotated SMM segments (~21 h of SMM in 580 h of footage) distributed as OpenPose skeleton time-series. REFUTES the A5 'no open stereotypy pose data' absence at the skeleton level (raw video stays absent). NEXT: v... |
| **License** | NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data-sharing statement must be read before any redistribution decision |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("asdpose")
ds.info   # recipe: get_data() explains the route
```

## License and access

- **License**: NOT YET VERIFIED (2026-09-04 closing sweep): no DUA advertised on the GitHub distribution page; the JAMA supplement data-sharing statement must be read before any redistribution decision
- **Redistribution**: unknown
- **Access route**: github Dinstein-Lab/ASDMotion -> Google Drive links (raw video withheld for privacy)
- **Source**: <https://github.com/Dinstein-Lab/ASDMotion>

## Data card (verbatim, with its evidence trail)


- Modality: pose (OpenPose skeletons from multi-camera behavioral
  assessments; raw video deliberately withheld for privacy)
- Source / URL: https://github.com/Dinstein-Lab/ASDMotion (Google
  Drive download links); paper JAMA Netw Open 2024 (PMC11393723)
- License: JAMA Supplement-2 Data Sharing Statement READ 2026-09-07
  (evidence: JAMA_data_sharing_statement_s002.pdf in this dossier,
  sha256 aa9a87ea..., retrieved via the Europe PMC supplementaryFiles
  API - the PMC direct PDF sits behind a secure-cookie interstitial).
  Verbatim terms: "Data available: Yes; Data types: Deidentified
  participant data; Who can access the data: For everyone; Types of
  analyses: For any purpose; Mechanisms of data availability: Online"
  via github.com/Dinstein-Lab/ASDMotion. Maximally permissive in
  scope but NOT a formal licence instrument (no CC/SPDX named for the
  DATA; the repo's MIT is the code licence). INTERNAL USE + EVAL
  clearly covered. Redistribution/derivative-deposit decision:
  OWNER CALL - "for any purpose, for everyone" arguably covers it,
  but house policy (better unknown than wrong) wants an explicit
  instrument or author ack before we redeposit; without it asdpose
  stays internal like the FMD pair.
- Access: direct download links (Google Drive), no account advertised
- Version / retrieval date: catalogued 2026-09-04 (closing sweep); not yet fetched
- Status (2026-09-05): DOWNLOADED via the Drive links (one probe,
  no interstitial fight needed): asdmotion_dataset_no_annotations.zip
  (7.85 GB, zip integrity-tested clean) + asdmotion_annotated_training
  (5.09 GB - a raw pickle protocol-4 file despite the link's framing,
  renamed .pkl), own-sha256 journaled (Drive publishes no hashes).
  2026-09-07: the JAMA Supplement-2 data-sharing terms are READ (see
  License above) - internal/eval use cleared; redistribution stays an
  owner decision pending a formal instrument.
  Originally: 319 assessments / 241 children
  with ASD / 7,352 manually annotated stereotypical-motor-movement
  (SMM) segments, ~21 h of SMM inside ~580 h of assessment footage,
  distributed as OpenPose skeleton time-series.
- Number of subjects: 241 (children, autism assessments)
- Disorders covered: motor stereotypies (A5), ASD context
- Why this card matters: it REFUTES, at the skeleton-data level, the
  corpus's confirmed-absence finding for open stereotypy recordings
  (hunt_confirmed_absences.md A5). The absence claim survives only
  for raw video. The paper's scarcity section must carry the revised
  wording.
- Caveats to resolve at fetch time: (a) do the Drive links resolve to
  scripted clients (the figshare case-5 lesson applies: one probe,
  no retry storm; Drive often requires the browser route for large
  files); (b) exact licence/reuse terms; (c) skeleton format and
  frame rate (OpenPose JSON vs packed arrays) for a future
  canonical-skeleton ingestion.

### Retrieval notes
Not yet fetched. Found by the 2026-09-04 closing sweep (recency
agent), which also surfaced a Sept-2025 bioRxiv quantifying SMMs
across pose + accelerometer modalities (10.1101/2025.09.03.674008) -
a candidate second source for A5.

### Processing
None yet. Candidate for canonical-skeleton ingestion after licence
verification; would join goodwin_smm (accelerometer) as the second
open A5 dataset, first in pose.
