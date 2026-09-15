Modalities
==========

What movement looks like in each family, shown on REAL records from the
corpus (regenerate with ``python site/gen_figures.py``). The six
harmonized families carry a canonical contract each
(``configs/canonical_*.yaml``): native sampling rates, honest validity
masks, no silent unit guesses. Beyond them, the catalogue documents six
more lanes (invasive electrophysiology, imaging, genetics, histology
and transcriptomics, digital proxies and clinical scales) with cards
and access routes; they get their own sections at the bottom of this
page.

Pose
----

3D optical mocap and video-derived 2D keypoints, mapped to a 15-joint
canonical skeleton with per-frame, per-joint validity masks. 10 datasets
ingested; the live per-family figures are on the
:doc:`statistics` page, which is generated from the manifests.

.. image:: _static/sample_pose.png
   :alt: Real canonical gait skeletons
   :width: 100%
   :class: only-light

.. image:: _static/sample_pose_dark.png
   :alt: Real canonical gait skeletons
   :width: 100%
   :class: only-dark

IMU
---

Wearable inertial sensing on a 14-location body grid (acc/gyro/mag
slots, per-channel masks): protocol trials and multi-day free living.
see the :doc:`statistics` page for the live figures.

.. image:: _static/modality_imu.png
   :alt: Real lower-back acceleration during walking
   :width: 100%
   :class: only-light

.. image:: _static/modality_imu_dark.png
   :alt: Real lower-back acceleration during walking
   :width: 100%
   :class: only-dark

EMG
---

Surface electromyography with a variable channel table naming each
muscle and side (identity resolved or explicitly unknown, never
guessed). 7 datasets; raw 2 kHz recordings like this one:

.. image:: _static/modality_emg.png
   :alt: Real tibialis anterior EMG during walking
   :width: 100%
   :class: only-light

.. image:: _static/modality_emg_dark.png
   :alt: Real tibialis anterior EMG during walking
   :width: 100%
   :class: only-dark

EEG
---

Scalp EEG during movement protocols and sleep, harmonized with channel
sites and units from the source headers. 5 datasets ingested.

.. image:: _static/modality_eeg.png
   :alt: Real scalp EEG channels
   :width: 100%
   :class: only-light

.. image:: _static/modality_eeg_dark.png
   :alt: Real scalp EEG channels
   :width: 100%
   :class: only-dark

Force
-----

Ground-reaction forces: instrumented insoles (8 sensors + total per
foot) and lab force plates. 4 datasets, 77,464 records.

.. image:: _static/modality_force.png
   :alt: Real vertical ground-reaction forces, both feet
   :width: 100%
   :class: only-light

.. image:: _static/modality_force_dark.png
   :alt: Real vertical ground-reaction forces, both feet
   :width: 100%
   :class: only-dark

Silhouette
----------

Privacy-preserving body contours (64 boundary points per frame) with
per-frame detection masks: the publishable face of clinical video.

.. image:: _static/modality_silhouette.png
   :alt: Real walking silhouette contours
   :width: 100%
   :class: only-light

.. image:: _static/modality_silhouette_dark.png
   :alt: Real walking silhouette contours
   :width: 100%
   :class: only-dark

The catalogue beyond the signal families
----------------------------------------

The six lanes below are catalogued with data cards, licences and access
routes, not harmonized signal (yet). They exist because a movement
foundation model eventually meets deep-brain electrophysiology,
anatomy, genetics and clinical scores; each card says exactly what may
be used and how. Three of these lanes can be explored on real data
today in the gallery's "Beyond the signal" section: invasive ECoG and
STN-LFP during a grip-force task, movement-gene expression across the
brain, and the PanelApp genetic landscape.

Invasive electrophysiology (LFP / ECoG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Real and partly on disk, not yet harmonized: deep-brain LFP from
dystonia patients (:doc:`datasets/oxford_dystonia_lfp`, the only open
dystonia LFP in existence, 14.7 GB held), subthalamic LFP with MEG in
Parkinson (:doc:`datasets/pd_meg_stn_lfp_ds004998`, 162 GB held), and
polysomnography with pallidal/thalamic LFP across five sleep disorders
(:doc:`datasets/beijing_sleep_lfp`, application-gated). The Merk and
Neumann ECoG+LFP decoding testbed completes the lane as tooling. Each
enters the EEG family's contract at its own ingestion pass.

MRI and imaging
~~~~~~~~~~~~~~~

Structural MRI cohorts as anatomical references:
:doc:`datasets/ixi_mri` (600 healthy adults 20-86),
:doc:`datasets/camcan` (700 subjects 18-88, MRI+MEG, documented
barrier) and the deep NINDS cohort :doc:`datasets/pdbp` (documented
barrier).

Genetics
~~~~~~~~

Movement-disorder gene panels and genotype-phenotype references:
:doc:`datasets/panelapp` (two signed-off panels, 207 + 986 genes),
:doc:`datasets/clinvar` (variant summaries for movement genes),
:doc:`datasets/hpo` (the phenotype ontology, on disk and verified),
:doc:`datasets/mdsgene` (reference only) and the questionnaire+genetics
cohort :doc:`datasets/foxinsight` (documented barrier).

Histology and transcriptomics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cellular substrate of movement disorders:
:doc:`datasets/allen_human_brain` (six-donor microarray + histology,
1.65 GB on disk), :doc:`datasets/kamath_snpc_geo` (single-nucleus
substantia nigra, PD vs controls, 5.1 GB on disk) and
:doc:`datasets/cellxgene_pd_multiregion` (2.1M-nucleus PD atlas).

Digital proxies (voice, writing, typing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Movement signal through everyday instruments:
:doc:`datasets/uci_parkinson_voix` (voice),
:doc:`datasets/kaggle_spiral` (Archimedes spirals),
:doc:`datasets/nqmitcsxpd` and :doc:`datasets/tappy_keystroke`
(keystroke dynamics, including prodromal cohorts).

Clinical scales
~~~~~~~~~~~~~~~

Machine-readable clinical scores that anchor every evaluation:
:doc:`datasets/clinical_scales` (NINDS common data elements),
:doc:`datasets/cdystonia` (TWSTRS over 16 weeks, three trial arms),
plus the scale tables riding inside :doc:`datasets/hpo`,
:doc:`datasets/foxinsight` and :doc:`datasets/pdbp`.
