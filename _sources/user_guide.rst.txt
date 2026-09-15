User guide
==========

This guide follows a researcher from an empty machine to an evaluation:
one complete walk per access case, executed as written on 2026-09-15 from
a fresh virtual environment with an empty store, then the record format,
the subject-level splits and the evaluation paradigms.

Walk 1: a hosted dataset
------------------------

Hosted means the licence allows redistribution and MoveAtlas serves a
published record, one per dataset, on Zenodo. Nothing to fetch, nothing
to configure.

.. code-block:: python

   import moveatlas

   ds = moveatlas.dataset("modys_video")
   records, meta = ds.get_data()
   # 94 records; meta (94, 6); 2.8 MB downloaded in 3 s, then cached

Behind ``get_data()``: the package looks the dataset up in its records
table (``moveatlas/data/zenodo_records.json``, shipped with the package),
downloads the record's ``files.csv`` manifest, then every file it needs,
resuming an interrupted transfer and verifying each file's sha256
against the manifest before opening it. A record that fails
verification is refused, not repaired.

``moveatlas info modys_video`` prints the record's DOI; cite the source
paper named on the data card, and the record when you redistribute
derived work.

Records that hold tables, not records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nineteen of the 53 published records carry what their dataset is: a
clinical table, a feature CSV, an archive, polygraphy PDFs, an ontology.
There is no canonical record to return, and ``get_data()`` says so and
lists the files. Every dataset exposes its files:

.. code-block:: python

   ds = moveatlas.dataset("alameda_tremor")
   ds.files()                                   # ['datasets/imu/alameda_tremor/raw/ALAMEDA_PD_tremor_dataset.csv']
   p = ds.path("ALAMEDA_PD_tremor_dataset.csv")  # downloaded from the record, sha256-verified
   pd.read_csv(p)                               # (rows, columns) of the source's features

The same on the command line: ``moveatlas files <id>`` and
``moveatlas get <id> <name>``. Read a table with pandas, an archive with
``zipfile``, an ``.npz`` container with ``moveatlas.records.load()``.

Walk 2: a recipe dataset
------------------------

Recipe means the origin host serves the raw data and MoveAtlas
harmonizes it on your machine with the same code that built the corpus.
Two calls before ``get_data()``:

.. code-block:: python

   import moveatlas

   moveatlas.fetch("fog_star")      # Zenodo 17838806: 120 MB, verified, 39 s
   moveatlas.ingest("fog_star")     # 106 canonical IMU records, 2 s
   records, meta = moveatlas.dataset("fog_star").get_data()

``fetch()`` downloads into ``<store>/datasets/imu/fog_star/raw/`` and
journals every file's sha256 in ``downloads.sha256`` beside it; run it
again and complete files are skipped. ``ingest()`` reads ``raw/`` and
writes ``processed/canonical_imu.npz``; the records it produced on
2026-09-15 were byte-identical to the corpus's own.

``fog_star`` is also hosted, which makes it the right dataset to check
the harmonization with: rebuild it from the origin and compare with the
record. The same two calls serve datasets that are not hosted:

.. code-block:: python

   moveatlas.recipe("ninapro")      # what this recipe needs, before running it

Every recipe answers one of three ways, and ``moveatlas.recipe(id)`` says
which before you start:

- **library**: both steps run in Python from the package (``fog_star``,
  ``daphnet``, ``hd_accel_jnet``, ``monipar`` and ``fog_turning_filho``
  today, each rebuilt from its origin and compared record by record with
  the corpus; more with each release);
- **script**: the dataset was harmonized by a repository script that is
  not ported yet. ``fetch()`` and ``ingest()`` then raise
  ``RecipeIsScript`` with the exact commands to run from a clone of the
  repository, and what the origin requires first (an account, an
  agreement, a size);
- **none**: hosted datasets need no recipe; barrier datasets have a
  route instead (walk 3).

Some hosts answer programs with a browser challenge (figshare does, as
of 2026-09-15). ``fetch()`` then raises ``ManualDownload`` naming the
URL, the path to save the file at, and the size and checksum it must
have; save it in the browser, run ``fetch()`` again, and it is accepted
and journaled. Nothing in MoveAtlas tries to defeat such a challenge.

The same verbs exist on the command line:

.. code-block:: bash

   moveatlas fetch fog_star
   moveatlas ingest fog_star
   moveatlas info fog_star

Walk 3: a barrier dataset
-------------------------

Barrier means access needs a human step that no program should take for
you: an application, a data-use agreement, a registration with review.
The package does not pretend:

.. code-block:: python

   import moveatlas

   moveatlas.dataset("tuh_eeg").get_data()
   # AccessError: 'tuh_eeg' is a documented access barrier, not a download.
   # Route on record: registration + signed form, then ... Card: datasets/eeg/tuh_eeg/datacard.md

The route on record is what the data card documents: where to apply,
what to sign, what the corpus recorded when it went through the same
door (the access-barriers casebook keeps every case with its dates).
Once you hold the data, place it under ``<store>/datasets/<family>/<id>/raw/``
and the card names the ingestion script; ``moveatlas.recipe(id)`` repeats
it.

The record format
-----------------

A canonical record is a Python dict saved in a ``.npz`` container
(format ``moveatlas-record/1``, no pickle: every member is numpy's own
format plus a ``meta.json``). The keys every family shares:

- ``subject_ns``: the subject, namespaced ``source:subject`` so one person
  never straddles a split;
- ``task``, ``source``, ``fps``, ``n_frames``, ``modality``;
- a signal array and its validity masks, per family.

Per family, in short (the contracts are the YAML files under
``configs/``; :doc:`modalities` shows real records):

.. list-table::
   :header-rows: 1
   :widths: 14 30 56

   * - family
     - signal
     - masks and units
   * - pose
     - ``coords`` (T, J, 2 or 3)
     - ``joint_mask`` (J), ``coord_mask`` (T, J); canonical 15-joint skeleton,
       ``dim``, ``scale``
   * - imu
     - ``signal`` (T, L, 9)
     - ``location_ids`` (L), ``channel_mask`` (L, 9), ``sample_valid``
       (T, L); g, deg/s, uT; native sampling rate
   * - emg
     - ``emg`` (T, C)
     - channel table with site vocabulary; mV, native rate; aux streams
       kept apart
   * - force
     - ``force`` (T, 2, S)
     - ``sensor_mask``; newtons, per foot
   * - silhouette
     - ``contour`` (T, 64, 2)
     - dense 64-point contours at video rate; derived, never the video
   * - eeg
     - ``eeg`` (T, C)
     - channel names on the 10-20 vocabulary, reference recorded, uV;
       ``aux`` for EOG/ECG

The rule behind every mask: the package refuses to guess. A channel
without a finite sample is absent, not zero; a header that declares a
unit the values contradict is flagged on the record, not silently
rescaled.

Subject-level splits
--------------------

Random splits over records leak patients between train and test.
``moveatlas.paradigms`` and ``moveatlas.evaluations`` split on
``subject_ns``, never on records, and the cross-dataset evaluations
combine evidence by meta-analysis rather than pooling. See the executed
examples under *Classification* in the :doc:`gallery <auto_examples/index>`
and the :doc:`API <api>`.

Paradigms and pipelines
-----------------------

A paradigm turns records into (X, y, groups) for one question (a
diagnosis, a severity, a task); a pipeline is a scikit-learn estimator
over X; an evaluation runs the pipeline under a subject-level scheme and
reports per-dataset and pooled scores with confidence intervals. The
decomposition is MOABB's, transposed to movement data.

.. code-block:: python

   from moveatlas.paradigms.windows import FixedIntervalWindows
   from moveatlas.evaluations.splits import cross_patient_folds
   from moveatlas.evaluations.evaluation import CrossPatientEvaluation

   paradigm = FixedIntervalWindows(duration_s=5.0, label_from="record")
   X, y, groups = paradigm.get_data(records)     # windows, labels, subject ids
   for train, test in cross_patient_folds(meta, n_splits=5):
       ...                                       # no subject on both sides, ever
   CrossPatientEvaluation(n_splits=5).evaluate(paradigm, ds, pipelines)

The executed example *Cross-patient benchmark* in the gallery runs this
end to end on real records.

Errors are documentation
------------------------

Every error a researcher can hit names the next thing to do: the access
route, the recipe to run, the environment variable to set, the file to
save. :doc:`troubleshooting` lists them all by situation. If one does not
tell you what to do next, it is a bug: open an issue with the message.
