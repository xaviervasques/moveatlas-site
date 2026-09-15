# SenseFOG: STN sensing + EMG during gait and FOG (Mendeley)

```{raw} html
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Dataset",
 "name": "SenseFOG: STN sensing + EMG during gait and FOG (Mendeley)",
 "description": "SenseFOG: STN sensing + EMG during gait and FOG (Mendeley). MoveAtlas eeg family. 11 (12 in the paper; 11 with BrainVision EEG on disk) subjects. licence CC BY 4.0.",
 "identifier": "https://doi.org/10.17632/c9ckcvjxc7.1",
 "license": "https://creativecommons.org/licenses/by/4.0/",
 "sdPublisher": {
  "@type": "Organization",
  "name": "MoveAtlas"
 },
 "keywords": [
  "eeg",
  "B5 Freezing of gait",
  "M6 EEG",
  "M7 LFP / ECoG"
 ],
 "url": "https://doi.org/10.17632/c9ckcvjxc7.1",
 "isAccessibleForFree": true,
 "measurementTechnique": "eeg",
 "includedInDataCatalog": {
  "@type": "DataCatalog",
  "name": "MoveAtlas"
 }
}
</script>
```

<span class="ma-fam ma-eeg">eeg</span>&nbsp; <span class="ma-badge ma-harmonized">harmonized</span>&nbsp; <span class="ma-badge ma-hosted">hosted</span>&nbsp; <code>sensefog</code>

<span class="ma-tag">Freezing of gait</span><span class="ma-tag">EEG</span><span class="ma-tag">LFP / ECoG</span>

| | |
|---|---|
| **Taxonomy cells** | B5; M6 M7 |
| **Subjects** | 11 (12 in the paper; 11 with BrainVision EEG on disk) |
| **Status** | HARMONIZED 2026-09-07 (canonical pass 1, build_canonical_sensefog.py): 45 scalp-EEG records (48 sites, 1000 Hz, uV, ref not documented at source) + 45 leg-EMG records (TA/GA bilateral) on 11 subjects, ~2.7 h, validate 0 errors; Percept LFP JSON, APDM motion h5 and FOG annotations deferred to their o... |
| **License** | CC BY 4.0 (verified at fetch 2026-09-07: DataCite + record page) |

Cell codes are defined on the {doc}`taxonomy page </taxonomy>`.

## How to load

```python
import moveatlas
ds = moveatlas.dataset("sensefog")
records, meta = ds.get_data()
```

## License and access

- **License**: CC BY 4.0 (verified at fetch 2026-09-07: DataCite + record page)
- **Redistribution**: yes
- **Access route**: mendeley doi:10.17632/c9ckcvjxc7.1
- **Source**: <https://doi.org/10.17632/c9ckcvjxc7.1>

## Data card (verbatim, with its evidence trail)


- Modality: family 'eeg'
- Source / URL: https://doi.org/10.17632/c9ckcvjxc7.1
- License: CC BY 4.0, verified at fetch 2026-09-07 (DataCite
  rightsList + the record page's Licence panel, browser-read)
- Access: mendeley doi:10.17632/c9ckcvjxc7.1
- Version / retrieval date: V1 (2024-02-01), DOWNLOADED 2026-09-07:
  277 files / 2.45 GB, every file verified against Mendeley's own
  per-file sha256, journaled in downloads.sha256. The 2026-09-05
  "EMPTY via API" verdict was a FALSE case-11: the record keeps all
  files in a BIDS-like folder tree (sub-*/ses-*/{eeg,ieeg,motion})
  and the public API lists one folder level at a time, so the root
  listing legitimately answers zero files - resolved by the scheduled
  browser check and a folder-walking fetch_mendeley.py (see the
  case-11 addendum in docs/ACCESS_BARRIERS_CASES.md). Transport
  notes: the record-level "Download All" zip 403s to every scripted
  client (per-file URLs are the route); one remote folder name
  carries a trailing space, illegal on Windows, sanitized at fetch.
- Status (2026-09-07): IN HAND, raw. Paired subthalamic LFP
  (Percept) + EEG + ambulatory motion/EMG during real walking with
  FOG and voluntary-stop events - rare invasive-sensing-during-gait
  data; documented pipeline at github.com/PKlocke/SenseFOG-Documentation.
  Candidate for canonical ingestion (eeg family + motion; the .mat/.h5
  layout is per-subject per-session)
- Number of subjects: see record
- MoveAtlas cells: B5; M6 M7

### Retrieval notes
Found by the 2026-09-04 closing sweep. All licence/access/content
statements are a catalogue-time reading - RE-VERIFY AT FETCH per
house rule; for the two A3 (tic) candidates the ethics/
de-identification check comes FIRST (video of minors: the SSBD
precedent).

### Processing
CANONICAL PASS 1 (2026-09-07, build_canonical_sensefog.py): the
unambiguous half of the dataset - 45 scalp-EEG records (48 10-10
sites, 1000 Hz, uV explicit in the BrainVision header at 0.1 uV
resolution, ref REF_COMMON_UNKNOWN because the source documents the
amplifier but no reference electrode) + 45 leg-EMG records (TA/GA
bilateral, two electrodes per muscle kept with an electrode suffix,
uV as recorded) + IPG monitor traces as aux; 11 subjects, 9.83 M
frames (~2.7 h); tasks sitting 11 / standing 10 / walk 9 /
walk_with_stops 9 / walk_dualtask 5 / walk_dualtask_2 1. Every
session parsed clean (no unrecognized channel, no read failure);
two sessions carry p99 > 1000 uV and are flagged "review" in
processed/eeg_ingest_audit.csv. validate_canonical --family eeg,emg:
0 errors (sampled), and the --full pass of 2026-09-07 (every eeg +
emg record of the corpus opened) raised ZERO warnings on sensefog -
the 262 corpus warnings all sit on ds007526 / ds002778 / ds004584
amplitude bands (case 3 territory). BrainVision markers ride verbatim as events; NO FOG label
array was emitted (the .vmrk holds Moblab/Toggle sync markers only -
a per-frame FOG label would be a guess). Subject-count note: the
documentation says 12 patients, the release has 16 sub-* folders,
11 of them with BrainVision EEG; the others hold derived .mat only.
DEFERRED to their own verified readers: STN Percept LFP
(ieeg/*.json, Medtronic export -> intracranial family), APDM Opal
motion (motion/*.h5, ankles + L5 -> imu family), FOG annotation
source (likely the motion .mat side), and the three derived-analysis
folders (Coherence-Data, Kinematic-Data, Time-Frequency-Data, Table
& Figures) which are not raw signal.

PASS-2 PREP, Percept LFP inventory (read 2026-09-07, 44 JSON):
43/44 sessions carry BrainSenseTimeDomain: 86 packets, ALL 250 Hz,
bipolar STN pairs per hemisphere (ONE_THREE_LEFT 32 / _RIGHT 30,
ZERO_TWO_L 9 / _R 5, ZERO_THREE_L 2 / _R 8), packet durations 14 s
to 407 s, 18,013 s total (~5.0 h of LFP). Stimulation status
initial/final: OFF/OFF in 41 sessions, OFF->ON 2, ON->OFF 1 - the
recordings are essentially stim-OFF sensing. Each packet ships
TicksInMses (250 ms ticks), GlobalSequences + GlobalPacketSizes
(62/63 samples per tick) and a Gain: the reader MUST rebuild the
time axis from the sequence counters and MASK the missing ticks
(Percept packet loss is the known pitfall; the corpus's validity
mask is the right home for it), and must convert TimeDomainData via
the documented Gain rather than assume uV. Also present: BrainSenseLfp
(2 Hz power stream), LeadConfiguration, Impedance, Groups (program
settings), DiagnosticData. PatientEvents (8 files) are clinical
state markers in German ("Off Anfang", "On Anfang", "Dyskinesien
Anfang", "Off" = medication OFF/ON/dyskinesia onsets), NOT FOG
annotations.

FOG ANNOTATION SOURCE LOCATED (2026-09-07 afternoon): NOT in the
Mendeley deposit at all. The per-subject MATLAB files of the
documentation repo (github.com/PKlocke/SenseFOG-Documentation,
"Matlab_scripts/A) Subject Files/sub-XX-datafile.m", 12 subjects =
the paper's cohort: 01,05,09,10,11,13,14,15,17,18,19,20) hold, per
session, hand-set segment start/end times in SECONDS with a task
label: 'Walk', 'Selected_stop', 'Freezing_walk',
'Freezing_walk_initiation' (sub-10: 14+2+3 freezing segments,
sub-14: 11, sub-01: none - it did not freeze). The same files hold
the EEG<->LFP ALIGNMENT: a manually read sample index per session
where the DBS stimulation artifact ends in the EEG (1000 Hz) and in
the LFP (250 Hz) stream, from which the scripts derive the delay
(alignsignals_new.m). TIME-BASE CAVEAT for pass 2: the segment
seconds are on the scripts' aligned timeline, so a label array on
our canonical EEG record needs the alignment offset applied
verbatim from the subject file - never eyeballed. The motion .mat
files carry GaitEvents (rf_events/lf_events = right/left foot gait
events), a third clock. Cloned copy of the doc repo (with LICENSE):
datasets/eeg/sensefog/raw/_doc_repo/ (under the ignored raw/ tree, for the reader; NOT part of the Mendeley journal). The
doc repo's LICENSE is CC BY 4.0 (read 2026-09-07), the same licence
as the deposit, so a label array derived from those segments is
redistributable with attribution to Klocke/Loeffler/Weiss. The
three derived-analysis folders in the deposit (Coherence-Data,
Kinematic-Data, Time-Frequency-Data) are placeholder.txt only;
"Table & Figures" holds MATLAB helpers + a license.txt. Pass-2
dependency: h5py is NOT in the PC miniconda env (needed for the
APDM .h5).

### Processing pass 2 (2026-09-08, build_canonical_sensefog.py --pass2 =
build_canonical_sensefog_pass2.py; audit processed/pass2_audit.csv, 258 rows)

TASK A, FOG LABEL ARRAYS on the pass-1 EEG + EMG records. Source: the 12
subject files of the documentation repo (CC BY 4.0), parsed with a
MATLAB-assignment regex after stripping % comments (a commented-out
segment such as sub-10 WalkWS(13) never enters). Every events_filt line
of every file matched the parser (an unparsed line refuses the file).
ALIGNMENT RULE APPLIED, from the authors' scripts: 1.5_Data_Alignment.m
line 100 cuts the raw EEG at the first 'M  1' marker (the IMU start,
lines 75-76): `EEG_pre_signal = EEG_File.dat.dataset(:,(sample_M1(1,1):
end))`; then ONLY in the branch EEG_signal > LFP_signal (line 146) it cuts
EEG_pre_signal again by delay = EEG_signal - LFP_signal (line 147),
otherwise the LFP is cut (lines 140-142). 1.6_Sub_GrandActivity_Log.m
lines 82-88 apply the SAME subtraction to the segment seconds in the SAME
branch only (`start = start - (signaldelay/EEG_File.fs_eeg)`), so the
events_filt seconds are on EEG_pre_signal = raw EEG after the M1 cut =
the native IMU clock; relative to the raw EEG the delay cancels in both
branches and the only offset is M1. With the 1-based time vectors of 1.5
line 101 (sample k at k/fs), segment time t is raw 0-based frame
round(t*1000) + M1 - 2 (M1 = the .vmrk position of the first 'M  1').
EMPIRICAL CONFIRMATION (clock_check rows of the audit, 25 sessions): the
authors' reviewed heel-strike times (motion/*_gaitfilt_cor.mat, used by
1.6 on the aligned clock, with the gyro value at each strike stored as
Heelstrike_Peak) land on the native h5 sagittal gyro only when shifted by
+delay in every EEG-cut session (median |gyro - peak| 2-32 deg/s vs
30-123 unshifted, e.g. sub-13 walkws delay 9.695 s: 7.0 vs 78.0) and
unshifted in the LFP-cut sessions (sub-01, sub-05: 12-14 deg/s). This
is exactly the rule of 1.6 and also fixes the sensor-to-side mapping
(SI-001683 = rf_events = right, SI-001710 = lf_events = left). Note the
prose of 1.6 line 80 ("if LFP recording was started before EEG") reads
opposite to its own condition; the code was followed, and the label
placement does not depend on the branch anyway.
RESULT: 24 sessions labelled (24 EEG + 24 EMG records re-saved in place,
same file names; every non-label field verified identical with
records.equal, the second run is idempotent): int8 `label` (0
unlabelled, 1 Walk, 2 Selected_stop, 3 Freezing_walk, 4
Freezing_walk_initiation; legend in `label_codes`), `label_source`
"SenseFOG-Documentation sub-XX-datafile.m, CC BY 4.0, alignment sample N",
`label_note` with the rule and the session's delay. Labelled frames: 6.65
M (1.85 h) of which Walk 1,672,111 (0.464 h), Selected_stop 168,568
(0.047 h), Freezing_walk 197,962 (0.055 h = 198 s: sub-14 90.1 s,
sub-17 60.1 s, sub-15 43.4 s, sub-20 4.3 s), Freezing_walk_initiation 0;
no segment clipped at a record edge, no conflicting overlap (same-label
overlaps exist and are harmless). label None kept on 42 records (the 21
sitting/standing sessions, which have no events_filt). REFUSED,
counted: 4 segments, because 1.6 selects tasks with an exact ismember()
so the authors' own pipeline ignored them: 'Selected_stop_start' (sub-11
WalkWS(2)), 'Selected stop' with a space (sub-15 WalkWS(34), (38)), and
sub-13 WalkWS(34) with end 160.151 < start 255.715; sub-10 (the cohort's
main freezer: 23 + 37 + 15 segments incl. the only two
Freezing_walk_initiation ones, both with end = 0) has NO BrainVision EEG
in the deposit (derived _eegalg.mat only, Instructions.md: ECG-artefact
preprocessed), so its segments are not placed on any record; sub-05
standing likewise has no raw file. sub-01 sitting and sub-13
sitting/standing have no 'M  1' marker (no IMU) and no segments.

TASK B, APDM OPAL .h5 -> canonical imu: 43 sessions -> 43 records in ONE
list container processed/canonical_imu.npz (1,172,631 frames, 2.54 h,
all at 128 Hz as declared by the per-sensor SampleRate attribute; 43 rows
of source sensefog in datasets/_canonical_imu_manifest.csv). h5 layout
(FileFormatVersion 4, "Streamed wirelessly"): root attrs CaseIdList +
MonitorLabelList index-aligned (as 1.4_Import_HDF.m lines 25-27 read
them), one group per sensor with Calibrated/{Accelerometers, Gyroscopes,
Magnetometers} [n, 3] float64, Time (us since epoch), SyncValue; the
three sensors are co-sampled (identical n, identical Time except the
glitches below). Mapping table (verbatim labels -> grid slot of
configs/canonical_imu.yaml, ankle per the doc-repo README line 94
"attached to both left and right ankles and lumbar spine (L5)"; the
h5 label and case id are kept per location in `placement`):
    SI-001726  'Lumbar'                    -> lower_back (id 2)
    SI-001710  'Left Leg'  ('Left Foot'*)  -> ankle_L    (id 9)
    SI-001683  'Right Leg' ('Right Foot'*) -> ankle_R    (id 10)
  (* sub-05 only; 1.4/1.6 call them right/left foot). Nothing refused.
UNITS, explicit in the dataset attributes, so converted: acc m/s^2 /
9.80665 -> g (the file's own Gravity attr 9.806 is recorded; median |acc|
0.98-1.04 g), gyro rad/s * 180/pi -> deg/s (as 1.6 rad2deg), mag
microtesla -> uT (x1). channel_mask all 9 True (Accelerometers/
Gyroscopes/MagnetometersEnabled = 1). 2 records carry sample_valid
(sub-09 standing 24 NaN rows, sub-17 standing 27, zeroed and masked).
14 files show a single-sample Time-column glitch in one sensor (one
timestamp off by up to 22.9 s, net zero after the next step; sample
counts identical) noted in `time_column_note`; samples kept co-indexed
as 1.4 does (it never reads Time). Per record `events`: the accepted
events_filt segments in seconds, verbatim (onset_s, offset_s, task,
code) on the native IMU clock = sample 0 at the EEG 'M  1' marker
(`eeg_m1_sample` keeps the marker), 24 records with events; no dense IMU
label was derived (not asked; the segments are the source of truth).
validate_canonical --family imu: 0 errors.

TASK C, PERCEPT LFP -> aux only (no family): 43 JSON with
BrainSenseTimeDomain -> 43 processed/aux/<rid>_lfp.npz, 86 streams
(2 per session, one bipolar STN pair per hemisphere), 4,503,620 samples
(5.00 h) at the declared 250 Hz. Per stream: TimeDomainData verbatim as
float32 with unit "unknown" (the JSON declares NO unit for it) and the
shipped Gain (219-230), channel name, FirstPacketDateTime, per-sample
`valid` mask, `stats`; per file Stimulation, LeadConfiguration,
SessionDate, device. AXIS RULE: packets are concatenated in order; the
250 ms TicksInMses clock is the reference, a gap of g ms > 250 inserts
(g-250)/4 masked samples (62.5 per lost tick). GlobalSequences are NOT
a plain packet counter: they run 0-255 and skip one value every fourth
packet by design (diff 2 in 25 % of steps while ticks stay at 250 ms and
sizes 62/63 sum to exactly 250 samples/s), so they serve only as a
cross-check (no anomaly beyond the tick gaps). GAP STATISTICS: 4 lost
ticks in the whole corpus, all in sub-15 walkws (one 750 ms tick gap in
both channels: 2 ticks, 125 samples masked per channel = 0.19 % of that
stream); every other stream 0 masked; corpus masked fraction 5.6e-5. One
packet-size anomaly: sub-19 sitting starts with sizes 115 and 73 (the
sample total still equals the size list, so the axis is 63 samples long
against the tick clock from packet 2 on; flagged in stats and the audit,
nothing dropped). Not exported: sub-11 sitting JSON (no
BrainSenseTimeDomain), and the 3 sessions with _lfpalg.mat only (sub-05
standing, sub-17 sitting, all of sub-10). The LFP is NOT aligned to the
EEG records: the subject files' LFP_signal samples are on the 1000 Hz
resampled LFP of 1.3_Import_JSON.m, a post-paper owner decision together
with the intracranial contract. BrainSenseLfp (2 Hz power) not exported.

Validation 2026-09-08 (validate_canonical --family eeg,emg,imu): 0
errors, the 3 warnings are the known ds007526 amplitude bands. The EEG
and EMG manifests were not touched (record paths and counts unchanged);
the IMU manifest merge replaced the sensefog rows only, and preserved the
167 physionet_multimodal_gait rows another builder appended meanwhile.
