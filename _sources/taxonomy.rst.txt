Taxonomy
========

Every dataset in the registry carries one ``moveatlas_cells`` string,
for example ``B2, D3; M2``: the clinical or context cells it covers,
then the modality lanes it records. This page defines the codes. The
table below is generated at build time: the cell codes come from
``build_taxonomy_map.py`` (the validator every mapping passes through),
the names from ``build_portal.py`` (the portal's canonical mapping), and
the HPO column from ``docs/hpo_movement_terms.csv``, the subtree of
HP:0100022 "Abnormality of movement" projected onto the cells by
``build_hpo_movement_map.py``. If the code and name tables ever
disagree, the site build fails instead of picking one.

Five classes, one modality axis
-------------------------------

- **A, hyperkinetic (A1-A8)**: tremor, myoclonus, tics, dystonia,
  stereotypies, athetosis, chorea, ballismus. The atlas's centre of
  gravity: this is where open data is scarcest.
- **B, hypokinetic (B1-B5)**: rigidity, bradykinesia, hypokinesia,
  akinesia, freezing of gait.
- **C, age-conditioned normal (C1-C3)**: the healthy lifespan axis
  (adult, infant, aging) that every pathological cell is read against.
- **D, neurological comorbidity (D1-D7)** and **E, systemic comorbidity
  (E1-E7)**: context lanes, never targets on their own.
- **M, modality codes (M1-M12)**: the recording lane, from pose and
  inertial signals to clinical scales.

A dataset counts in every cell and lane it covers. Animal entries
(mouse, rat and macaque models) map to symptom analogs in free text on
their own cards and never enter the human cells, so each coverage matrix
stays single-species. An empty cell means no open dataset was found by
the dated searches recorded in the repository; the table further down
lists them.

Cell table
----------

.. raw:: html
   :file: _generated/taxonomy_cells.html

Confirmed absences
------------------

Cells where systematic, dated searches of the repositories and the
literature found no open dataset. "Absent" is a result: the search
protocol, the repositories covered and the dated search reports are
versioned in the repository, and a cell leaves this list the day a
dataset is found.

.. raw:: html
   :file: _generated/absences.html

Access-barriers casebook
------------------------

How often "open" data is not practically open, documented case by case
with its evidence in the repository. The kinds of case met so far, each
a pattern a data user may meet again:

.. include:: _generated/barriers_cases.rst

See also :doc:`statistics` for the coverage matrices drawn over these
cells and :doc:`dataset_summary` for the per-dataset cell strings.
