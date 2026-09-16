Corpus statistics
=================

Everything on this page is computed from the canonical manifests (the
files ``datasets/_canonical_*_manifest*.csv`` that every ingestion
maintains); nothing is estimated or copied from papers. Counting rule:
one record = one canonical file entry (a trial, a night, a wear-block,
depending on the family); hours = sum of n_frames / native rate.
Regenerate with ``python site/gen_figures.py``.

The harmonized corpus at a glance
---------------------------------

.. raw:: html
   :file: _generated/corpus_stats.html

.. image:: _static/corpus_overview.png
   :alt: Hours and records per family
   :width: 100%
   :class: only-light

.. image:: _static/corpus_overview_dark.png
   :alt: Hours and records per family
   :width: 100%
   :class: only-dark

How to read these numbers
-------------------------

- **pose** is record-rich but hour-light: mocap and video-derived trials
  are short (seconds to minutes) and there are many of them, across
  27,000+ subjects (large-scale action corpora dominate the subject
  count).
- **imu** dominates the hours: wearable studies record days of free
  living per subject (weeks-long accelerometry in the ageing and
  Parkinson cohorts).
- **emg** and **eeg** hours are driven by long recordings (whole-night
  polysomnography, hours-long freezing-of-gait protocols) rather than by
  record counts.
- **force** is trial-shaped (a footstep pair per record), hence many
  records, few hours; **silhouette** is the smallest family today.
- These figures cover the INGESTED harmonized corpus: |n_harmonized|
  distinct datasets with measured records (a multimodal set counts in
  each family it feeds, so the per-family dataset counts sum higher).
  The full catalogue holds |n_catalogued|: the remainder splits into
  pointer-tier sets used through their original access routes, aux
  tables, and documented barriers; see :doc:`dataset_summary`.
- **What is downloadable**: |n_served_records| of the |n_records| records
  (|n_served_datasets| datasets) are served from the |n_published_records|
  published MoveAtlas records; |n_recipe_records| (|n_recipe_datasets|
  datasets, chiefly the large healthy 3D pose bases and the licence-held
  clinical sets) are harmonized on the ingestion machine only and are
  reproducible from the original host with ``moveatlas.fetch`` and
  ``moveatlas.ingest`` where the origin allows.
- Every number on this page is HUMAN data. The animal lane (|n_animal|
  catalogued datasets: mouse, rat and macaque models) is deliberately
  absent from every table here: animal entries map to symptom analogs
  in free text on their own cards and never enter the human clinical
  cells, so each matrix stays single-species.

What a record looks like
------------------------

.. image:: _static/sample_pose.png
   :alt: Real canonical gait skeletons
   :width: 100%
   :class: only-light

.. image:: _static/sample_pose_dark.png
   :alt: Real canonical gait skeletons
   :width: 100%
   :class: only-dark

.. image:: _static/sample_signals.png
   :alt: Real EMG and IMU snippets
   :width: 100%
   :class: only-light

.. image:: _static/sample_signals_dark.png
   :alt: Real EMG and IMU snippets
   :width: 100%
   :class: only-dark

Record durations
----------------

.. image:: _static/duration_distributions.png
   :alt: Record-duration histograms per family
   :width: 100%
   :class: only-light

.. image:: _static/duration_distributions_dark.png
   :alt: Record-duration histograms per family
   :width: 100%
   :class: only-dark

Each family has its own shape and the histograms show it honestly: pose
records live in the seconds range (trials); IMU is bimodal (short
protocol trials against multi-hour free-living wear blocks); EMG and EEG
mix short trials with whole-session and whole-night recordings; force
records are sub-second footstep pairs.

Modalities by symptom
---------------------

Which modality lanes carry data for each target symptom cell of the
taxonomy (hyperkinetic A1-A8, hypokinetic B1-B5; every code is defined
on the :doc:`taxonomy` page). A dataset counts in
every cell and lane it covers; the parenthesized number is the
open-access subset. An empty row means no open data exists there
today. Human datasets only; animal models never enter
these cells.

.. raw:: html
   :file: _generated/matrix_symptoms.html

Modalities by healthy context and comorbidity
---------------------------------------------

The same crossing for the age-conditioned normal axis (C) and the
neurological and systemic comorbidity axes (D, E).

.. raw:: html
   :file: _generated/matrix_context.html

Subjects with several modalities
--------------------------------

Datasets whose HARMONIZED records pair two or more families on the
same subjects (matched by subject namespace inside each dataset).
These are the subjects a multimodal model can actually align today.

.. raw:: html
   :file: _generated/multimodal_subjects.html

Interventions and state labels
------------------------------

Datasets carrying an intervention axis (a drug, deep brain
stimulation, or a treatment trial) with machine-usable state labels:
the raw material for "what does a molecule or a stimulator do to the
movement" questions. Curated in ``docs/interventions.csv`` with the
evidence for each claim.

.. raw:: html
   :file: _generated/interventions.html

Taxonomy coverage
-----------------

.. image:: _static/taxonomy_coverage.png
   :alt: Datasets per taxonomy cell
   :width: 100%
   :class: only-light

.. image:: _static/taxonomy_coverage_dark.png
   :alt: Datasets per taxonomy cell
   :width: 100%
   :class: only-dark

The rich cells (pose/video and wearable IMU among modalities,
bradykinesia and normal adult movement among the clinical axes) and the
sparse ones (tics, stereotypies, athetosis) are both visible at a
glance; the sparse cells are precisely where the CODY cohorts are the
only data in existence, which is why their derived release matters
(shipped: Zenodo, CC BY 4.0, 2026-09-01).

Signal usability (validity masks)
---------------------------------

How much of each record is USABLE signal, measured through each
family's own honesty mechanism: per-frame/per-joint validity masks
(pose), detection masks (silhouette), sample-validity and channel
masks (IMU), sensor masks (force), declared-bad channels and finite
fractions (EEG), finite fractions (EMG, a family without masks by
design). Datasets larger than the sampling cap are measured on a
fixed-seed sample and say so in the Sampled column; regenerate
exhaustively with ``python mask_statistics.py --cap 0``.

.. raw:: html
   :file: _generated/mask_stats.html

Demographics coverage
---------------------

.. raw:: html
   :file: _generated/demographics.html

Age and sex per harmonized dataset
----------------------------------

What each source states about its participants, quoted from the source
publication or the repository's own record (the reading date and the URL
are kept with every quote); "not reported by source" is the source's gap,
never filled in. A per-subject age and sex pyramid is possible only for
the datasets that ship a per-subject table, which the last column names.

.. raw:: html
   :file: _generated/demographics_sources.html
