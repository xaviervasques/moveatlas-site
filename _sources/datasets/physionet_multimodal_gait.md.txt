# PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults)",
 "description": "PhysioNet multimodal gait: EEG+EMG+kinematics+GRF (healthy young adults). MoveAtlas eeg family. 59 subjects. licence CC BY 4.0.",
 "identifier": "https://physionet.org/content/multimodal-gait-dataset/1.0.0/",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "C1 Normal adult movement",
  "M2 Inertial (IMU)",
  "M3 Plantar force",
  "M4 Silhouette",
  "M6 EEG"
 ],
 "url": "https://physionet.org/content/multimodal-gait-dataset/1.0.0/",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>physionet_multimodal_gait</code>

<span class="ma-tag">Normal adult movement</span><span class="ma-tag">Inertial (IMU)</span><span class="ma-tag">Plantar force</span><span class="ma-tag">Silhouette</span><span class="ma-tag">EEG</span>

| | |
|---|---|
| **Taxonomy cells** | C1; M2 M3 M4 M6 |
| **Subjects** | 59 |
| **Ages** | 24 +/- 5 y |
| **Status** | HARMONIZED 2026-09-08 on FOUR families (build_canonical_physionet_multimodal_gait.py): 176 EEG records (300 Hz uV, ref Pz as recorded, 1 file refused for a corrupt montage, railed channels flagged), 169 EMG (MAV envelope, 12 named muscles, rate measured 16.05 Hz), 167 IMU (free acceleration in g, 9... |
| **License** | CC BY 4.0 (page-verified at fetch 2026-09-07; open access) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("physionet_multimodal_gait")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (page-verified at fetch 2026-09-07; open access)
- **Redistribution**: yes
- **Access route**: physionet multimodal-gait-dataset
- **Source**: <https://physionet.org/content/multimodal-gait-dataset/1.0.0/>

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://physionet.org/content/multimodal-gait-dataset/1.0.0/
- License / access: "Creative Commons Attribution 4.0 International
  Public License", Open Access (no credentialing) - page-verified at
  fetch 2026-09-07. Citation: Katmah R, AlShehhi A, Kosaji D,
  Al-Rahmani N, Abdullah M, Hulleck AAV, Khalaf K (2026). A
  multimodal gait dataset of brain activity, muscle activity,
  kinematics and ground forces in young adults (v1.0.0). PhysioNet.
  doi:10.13026/r0ea-7161
- Version / retrieval date: v1.0.0; catalogued 2026-09-05 (deep-dive
  sweep); FETCH LAUNCHED 2026-09-07 (fetch_physionet.py, file by
  file from the record's SHA256SUMS.txt: 713 entries, every file
  verified against the server's sha256, journaled)
- Status (2026-09-07 16:03): IN HAND, raw - 713/713 files, 6.93 GB,
  every file verified against the record's SHA256SUMS.txt (0 bad),
  journaled in downloads.sha256; ~7.5 h under PhysioNet throttling
  (4 workers). Layout raw/Dataset/{EEG_Data,EMG_Data,FP_Data,
  IMU_Data} + README.md + RELEASE_NOTES.txt + subject-info.csv.
  Four-family canonical candidate (eeg/emg/imu/force) - a real
  integration job, plan as such. Cohort: 59 healthy adults (22 M /
  37 F, 24 +/- 5 y) walking at 0.5 / 0.75 / 1.0 m/s with synchronized
  EEG (19 channels, 300 Hz; CSV + EDF), EMG (12 muscles bilateral,
  CSV), IMU kinematics (17 sensors, 60 Hz, CSV in archives) and
  bilateral force plates (1000 Hz, CSV); 6.5 GB / 489 files per the
  page (713 SHA256SUMS lines incl. figures/docs). The healthy
  multimodal control corpus the pairing analyses lacked.
- Number of subjects: 59 (healthy young adults)
- MoveAtlas cells: C1; M2 M3 M4 M6

### Privacy gate (read 2026-09-07, before any redistribution)
raw/Dataset/subject-info.csv carries, per subject, GENDER, a full
DOB (dd/mm/yyyy), Age, and 18 anthropometric measures, for 64 rows
(the page says 59 participants; the 5 extra rows are BLANK trailing
rows - 59 rows carry H, 37 F / 22 M, matching the page exactly). A full date of birth is a direct identifier under
most de-identification standards even on an open record: MoveAtlas
must NOT carry DOB into any canonical record or deposit (the CODY
birthdate-prefix remediation of 2026-08 is the precedent) - keep
Age and sex, drop DOB, and say so on the record. Sex IS available
here for the demographics table.

### Retrieval notes
Licence re-verified on the record page at fetch (house rule). Route:
per-file HTTPS from physionet.org/files/ with the record's own
SHA256SUMS.txt as the hash source (the dynamic zip endpoint is not
used - pads_mirror precedent). PhysioNet throttles: 4 workers with
back-off, no retry storm.

### Processing (2026-09-08, build_canonical_physionet_multimodal_gait.py)

Four canonical families built from raw/Dataset/, source id
`physionet_multimodal_gait`, subject_ns `physionet_multimodal_gait:S<n>`,
task `walk_0.50ms` / `walk_0.75ms` / `walk_1.00ms` (the record page
describes 3-minute speed conditions with the middle minute recorded;
there is no sitting or rest file in the release). Containers are
moveatlas-record/1 .npz (moveatlas/records.py), no pickle anywhere.
Every declaration below was read from the file headers, the four
README files, EEG_referencing.m, or the PhysioNet record page
(re-read 2026-09-08); undeclared facts are stored as unknown.

| family | records | subjects | hours | native rate | unit stored | refused files |
|---|---|---|---|---|---|---|
| eeg | 176 | 59 | 2.93 | 300 Hz (csv header) | uV (csv header) | 1 (S32 at 1.0 m/s, corrupted montage line) |
| emg | 169 | 58 | 2.84 | 16.049 Hz, measured from the file's X [s] column (not declared) | mV (header says Volts, x1000) | 0 (8 files missing at source, README) |
| imu | 167 | 57 | 2.79 | 60 Hz (record page) | g (page declares free acceleration in m/s2, /9.80665) | 3 (S47: empty Sensor_Free_Acceleration.csv in the archive) |
| force | 173 | 59 | 2.88 | 1000 Hz (record page; file Timestamp columns are all zero) | unknown (declared nowhere) | 0 (4 files missing at source, README) |

Outputs: processed/canonical_eeg/<rid>.npz and processed/canonical_emg/
<rid>.npz (one file per record), processed/canonical_imu.npz and
processed/canonical_force.npz (one list each), processed/aux/
<rid>__<family>.npz (everything routed out of a contract, as recorded),
processed/ingest_audit.csv (one row per source file: n_frames, fs, unit,
routing, notes/refusal reason). Manifest rows merged by source into
datasets/_canonical_{eeg,emg,imu,force}_manifest.csv.
validate_canonical.py --family eeg,emg,imu,force: 0 errors (the only
warnings belong to pd_walking_eeg_ds007526, not to this source).

#### DOB policy (applied)
subject-info.csv is read through load_subjects(), which keeps ONLY
Subject, GENDER and Age; the DOB column and the 18 anthropometrics are
never loaded, so they cannot reach a record, an aux file, the audit or
a manifest. Every record carries `age` (years, int), `sex` (M/F) and a
`demographics_note` saying so. The five summary rows at the bottom of
the file (Average, Median, Min, Max, STD; the privacy-gate note above
called them blank) are skipped by the S<n> id pattern. A regex sweep
of the written meta.json headers found no dd/mm/yyyy string.

#### EEG
- Source file: EEG_Data/EEG.csv/S<n>_<speed>_raw.csv, the raw
  DSI-Streamer export (header: DSI-24, 300 Hz, uV, "Reference location:
  Pz", "Filter = Non-Filtered", Filter_Delay 40 ms, mains 50 Hz in 172
  files and 60 Hz in 5 files (S1 x3, S3 x2), kept on the record under
  filters.mains_hz). The .edf twin is a derivative: 29 x 2 s = 17400
  samples against 17960 in the csv, identical labels and unit; the csv
  is ingested and the edf is not.
- Montage stored AS RECORDED: 20 channels = 18 scalp sites (P3 C3 F3 FZ
  F4 C4 P4 CZ FP1 FP2 T7 P7 O1 O2 F7 F8 P8 T8; the old names
  T3/T5/T6/T4 are normalized by build_canonical_eeg.norm_site) + A1 +
  A2, every one with ref PZ. The README's "19 scalp channels" counts
  Pz, which is the hardware reference and is not a data column;
  EEG_referencing.m shows the authors reconstruct Pz as zeros and
  re-reference to the A1/A2 average - that transform is documented on
  the record (reference_note), NOT applied (C-EEG-1).
- Routed to aux (processed/aux/<rid>__eeg.npz): CM (common-mode
  trace), X1/X2/X3 (unused aux inputs, uV), Trigger, Time_Offset,
  ADC_Status, ADC_Sequence, Event. Comments is blank everywhere.
- Refused: S32_1_raw (csv AND edf carry the montage line
  P3,C3,F3,Fz,C4,T3,A2,F6,?,Fp1,?,?,C2,???,???,???,...: unknown labels,
  A2 twice, sites F6/C2 that the DSI-24 does not have; channel identity
  is uncertain, so the whole file is refused rather than positionally
  re-labelled).
- Quality flags, nothing altered: the exact extreme +/-9830.1 uV recurs
  in 30+ files with whole channels sitting on it (dry electrodes with
  poor contact, mostly Cz). Each record carries `railed_fraction` per
  channel and `railed_channels` (sites above 50%), and the audit note
  lists them per file (32 records carry a railed channel: CZ in 30,
  P4 in 2). 44 of 176 records
  have a p99 above 5000 uV for this reason. Large DC offsets (tens to
  hundreds of uV) are the unfiltered recording. S8_0.5 has 2
  Time-column steps off by more than half a sample (kept, no repair).

#### EMG
- Source file: EMG_Data/EMG_S<n>_<speed>.csv, header
  "<L|R> <MUSCLE>: EMG k->MAV [Volts]"; README: "mean absolute value,
  volts". The distributed signal is therefore an ENVELOPE (signal_kind
  envelope, envelope_kind MAV, window not declared); the raw EMG is not
  distributed. Volts -> mV at ingestion (unit_scale 1000.0). Delsys
  Trigno (record page). Filters undocumented (null).
- Rate: not declared anywhere; measured from the file's own X [s]
  column: dt 62.3077 ms in all 169 files, jitter 1.4e-14 s, i.e.
  16.0494 Hz, stored with `fps_provenance`.
- Muscle table (header name -> corpus vocabulary, side from the L/R
  prefix, all 12 channels resolved in all 169 files):
  TIBIALIS ANTERIOR -> tibialis_anterior; VASTUS LATERALIS ->
  vastus_lateralis; RECTUS FEMORIS -> rectus_femoris; GASTROCNEMIUS
  MEDIAL HEAD -> gastrocnemius_medialis; SEMITENDINOSUS ->
  semitendinosus; GASTROCNEMIUS LATERAL HEAD -> gastrocnemius_lateralis.
  No header fell outside this table, so no channel was refused.
- Missing at source (README, confirmed on disk): S3_0.75, S3_1, S8_0.5,
  S11_1, S43_1, S50_0.5, S50_0.75, S50_1 (S50 has no EMG at all: 58
  subjects). Record lengths 969-1129 samples (60-70 s). 17 files have a
  p99 above 0.5 mV (up to 4.6 mV, S39/S48/S52/S19); stored as recorded.

#### IMU
- Source: IMU_Data/IMU.tar.gz (3.9 GB), streamed with tarfile; per
  folder IMU_S<n>_<speed>/ an Xsens MVN 2023 export of 18 csv files.
  Only Sensor_Free_Acceleration.csv is a sensor signal with a declared
  unit ("Sensor Free Acceleration: 1x3 sensor free acceleration vector
  (x, y, z) of the sensor in [m/s2]" on the record page) -> acc_xyz in
  g, `acc_content = linear_no_gravity` (gravity removed by MVN; frame
  not stated by the dataset, MVN convention is the global frame, noted
  on the record as acc_frame_note). No sensor angular velocity is
  exported (Segment_Angular_Velocity is a model output): gyro absent.
  Sensor_Magnetic_Field is "[a.u.]", not uT: refused for the contract,
  kept in aux as recorded. Segment_* and Joint_Angles_* files are
  biomechanical-model outputs and are not ingested (pose-like
  derivatives, not signals of this contract).
- 60 Hz from the record page, cross-checked: 3601-4267 frames per
  record = 60.0-71.1 s for the 60 s recorded minute.
- Sensor -> 14-location grid mapping (MVN segment names; the release
  documents the sensors only by segment):
  Head -> head; T8 -> trunk; Pelvis -> lower_back; Right/Left Upper Leg
  -> thigh_R/L; Right/Left Lower Leg -> shank_R/L; Right/Left Foot ->
  foot_R/L (9 locations, acc only, channel_mask marks acc_xyz).
  Pelvis -> lower_back is the one judgment call (the grid has no pelvis
  slot; lower_back is the slot the other lumbar/sacral sensors of the
  corpus use) and is flagged on every record (sensor_map_note).
  Right/Left Shoulder, Upper Arm, Forearm, Hand (8 sensors): the release
  does not say where on the arm they sit, so they are NOT forced onto
  wrist_L/R; their free acceleration (m/s2) goes to aux
  (processed/aux/<rid>__imu.npz) with the segment name, alongside the
  a.u. magnetic field of all 17 sensors. The 6 MVN segments without a
  physical sensor (L5, L3, T12, Neck, Toes) are all-zero columns and
  are treated as absent.
- Refused: IMU_S47_0.5 / _0.75 / _1 (Sensor_Free_Acceleration.csv is
  empty inside the archive). Missing at source (README): S2_0.75,
  S2_1, S3_0.75, S3_1, S24 x3 (S24 and S47 have no IMU record: 57
  subjects). IMU_S46_1 has an empty magnetic-field file (aux only).

#### Force
- Source: FP_Data/FP_S<n>_<speed>.csv, 22 columns "1:Timestamp ...
  1:COPy, 2:Timestamp ... 2:COPy". Left/right is explicit twice
  (FP_Data/README.txt "Columns 1-6 ... left leg, columns 7-12 ... right
  leg", and the record page "columns whose headers begin with '1:'
  correspond to the left leg ... '2:' ... right leg"), so block 1 ->
  foot_L, block 2 -> foot_R. The README's column count ignores the
  Timestamp/Sync/Aux and COP columns; the order is the same.
- Contract layout: Fz (vertical GRF of the Bertec split-belt treadmill
  plate) -> per-foot total, sensor_mask totals-only (like gaitndd).
  Fx, Fy, Mx, My, Mz, COPx, COPy, Timestamp, Sync, Aux of both plates
  -> aux (processed/aux/<rid>__force.npz).
- Rate 1000 Hz from the record page ("All force and COP data were
  sampled at a high frequency of 1000 Hz"); the files' Timestamp and
  Sync columns are all zero, so the rate cannot be measured from them.
  Record lengths 50534-60000 samples (50.5-60 s).
- Unit: NOT declared on the page, in the README or in the header, so
  the records carry unit "unknown" with a unit_note. Consistency check
  only, never a promotion: the median Fz sum per record is 549-962 for
  most subjects, i.e. body weight in newtons (S1: 1055 for 107 kg).
  S21 (all three speeds) has a median Fz sum of about -7 with a p99 of
  250-320: the plates were barely loaded; stored as recorded, visible
  in the audit.
- FP_S2_0.5 / _0.75 / _1 have no header line (22 columns of data from
  row 1); the documented layout is applied and the audit says so.
  Missing at source (README): S3_0.75, S3_1, S8_0.75, S45_1.

#### Left out, and why
- EEG .edf twins (derivative cut of the csv), the S32_1 EEG file
  (corrupted montage), S47 IMU (empty export), the MVN segment/joint
  kinematics (model outputs, no contract), sensor magnetic field
  (a.u.), force plate Fx/Fy/moments/COP (no slot in the totals-only
  force contract; in aux), anthropometrics and DOB (privacy gate).
