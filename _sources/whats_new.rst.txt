Release notes
=============

In development (2026-09-08)
---------------------------

- New :doc:`taxonomy` page: the cell table (A1-A8 hyperkinetic, B1-B5
  hypokinetic, C, D and E context lanes, M1-M12 modality codes) with
  the HPO terms mapped to each cell, the confirmed-absences ledger
  included verbatim, and the titles of the access-barrier cases. Codes
  are read from ``build_taxonomy_map.py`` and names from
  ``build_portal.py`` at build time; a disagreement fails the build.
- One number, one source: every dataset count on the site is now a
  substitution computed in ``conf.py`` from the registry
  (``docs/datasets_index.csv``) and the mask statistics
  (``docs/mask_statistics.csv``). Today they read |n_catalogued|
  catalogued (|n_human| human, |n_animal| animal), |n_harmonized|
  harmonized, |n_records| records. Dated figures in older entries
  below are kept as historical record.
- Dataset pages carry a schema.org ``Dataset`` JSON-LD block and their
  key-facts table now shows status and license, as the cards do.

In development (2026-09-01)
---------------------------

The catalogue grows from 83 to 99 datasets (the count at that date;
the live count is |n_catalogued|) and the taxonomy gets one source of
truth:

- Taxonomy adjudication: 21 owner rulings applied (the standing B2/B3
  rule for parkinsonian gait; modys_video recognized as
  choreoathetosis, giving athetosis its first open dataset; gaitndd's
  ALS arm corrected from ataxia to pyramidal; accel_fluctuations
  recovered as the only akinesia-cell candidate). taxonomy_map.csv is
  now emitted from the registry: drift is impossible by construction.
- tremordb clarified: ingested as an AUX velocity asset by design
  (laser-Doppler, outside the acc/gyro contract), not missing.
- 16 new catalogued datasets from a licence-verified gap hunt,
  including: the only open stereotypy corpora anywhere (SSBD
  annotations; Goodwin SMM accelerometry, internal-only), the first
  open dystonia MRI (OpenNeuro ds006395, CC0), pallidal single-unit
  electrophysiology with gene labels, DANDI macaque circuit
  recordings, NeuroMorpho striatal morphologies, within-subject
  levodopa ON/OFF EEG, an alcohol-responsiveness dystonia table, and
  real (non-synthetic) infant pose. Five confirmed open-data deserts
  (tics, akinesia, rigidity-as-signal, kinematic Huntington chorea,
  pharmacological-challenge kinematics) are recorded as findings.
- Scientific Data groundwork: conformity check against the live
  journal policies, the descriptor outline, and a licence gate in the
  release lint.

In development (2026-08-31)
---------------------------

New gallery section **Beyond the signal** (three executed examples on
real data): ECoG + STN-LFP traces and MNI electrode maps from the
Merk and Neumann grip-force testbed; movement-disorder gene expression
across one Allen donor's 946 sampled brain sites (streamed from the
raw archive, mapped on the donor's own MNI coordinates); the genetic
landscape across five signed-off PanelApp panels. No MRI appears
because none is on disk; everything shown is measured.

Site design pass, guided by the field's reference sites (scikit-learn,
MOABB, PhysioNet, MNE, the Allen Institute portals):

- Every figure now ships light and dark variants paired to the site
  theme, under the validated palette.
- The landing page shows the FULL catalogue: a 12-lane modality glance
  (invasive LFP/ECoG, MRI, genetics, histology, digital proxies and
  clinical scales are now first-class), a live stat band, six
  family cards drawn from real records, and a provenance chip row.
- The master table gained sortable columns, CSV export, a live match
  count, and two badges per row: access case and harmonization status.
  Harmonization status is measured from the canonical manifests, never
  from prose.
- Dataset pages follow one scholarly order: identity badges, key facts,
  how to load, license and access, publications with BibTeX, then the
  verbatim data card as the evidence trail. Copy buttons on all code.
- Taxonomy coverage is drawn as six named small multiples (Tremor,
  Bradykinesia, ...), replacing the cryptic cell codes.
- Corpus-count correction surfaced by the pass: the main family
  manifests already contain the datasets that also keep a dedicated
  manifest file (capture24, ltmm, pads, pd_biostamprc21,
  sixmwt_lifespan, multimodal_fog, cervical_motion), and the site's
  statistics read both, double-counting 27,147 records and ~16,500
  hours (IMU hours were literally doubled). Measured truth, each
  dataset counted once: **293,288 records / 32,764 subjects / 40,303
  hours across 40 distinct ingested datasets**. Per-dataset record
  counts in the data cards were always correct; only the family
  aggregates were inflated.

Version 0.1.0.dev0 (2026-08-28)
-------------------------------

The founding release, local-only (pre-launch).

Late-day additions (same date)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``moveatlas.to_frame``: any canonical record as a tidy time-indexed
  pandas DataFrame, masks rendered as NaN.
- ``moveatlas.viz``: ``plot_skeleton`` and ``plot_trace`` one-liners.
- ``physionet_gaitpdb`` adapter (VGRF insoles; cohort encoded in the
  source ids: 93 Parkinson, 72 controls).
- The example gallery grew to 24 executed pages in 7 curriculum
  sections, including split-structure visualization, a subject-level
  permutation test, and cross-pathology descriptive studies.
- Subject-filtered shard loading: asking for 3 subjects reads 3 files.
- Data-card correction: the cdystonia table is a gzip-compressed R save
  file mislabeled ``.sav`` by its host; read with ``pyreadr``.

Enhancements
~~~~~~~~~~~~

- The ``moveatlas`` package exists: registry over 83 catalogued datasets,
  four enforced access cases (51 hosted / 17 recipe / 12 barrier /
  3 local_only), BSD-3-Clause.
- Pilot dataset adapters: ``nonan_gaitprint`` (41 older adults, 16-IMU),
  ``nonan_gaitprint_young`` (35 young adults, same protocol),
  ``gait120`` (multimodal identity, EMG stream, 120 subjects),
  ``cody_3`` (private tier, labels eval-only).
- Patient-level split primitive ``cross_patient_folds`` (leak-free by
  construction).
- This documentation site (pydata-sphinx-theme + sphinx-gallery), built
  and served locally.

API changes
~~~~~~~~~~~

- First API; everything is new.

Naming
~~~~~~

- The project was renamed from MOAMB to **MoveAtlas** on 2026-08-28
  (PyPI and trademark collision checks ruled out OpenMove; MoveAtlas is
  free and echoes the project's original working title "Atlas du
  mouvement"). Historical documents keep the old name.
