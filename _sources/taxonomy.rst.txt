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
stays single-species. Empty cells are findings, not omissions: the
ledger further down records the dated searches behind each one.

Cell table
----------

.. raw:: html
   :file: _generated/taxonomy_cells.html

Confirmed absences ledger
-------------------------

The negative results of the dated data hunts, included verbatim from
``docs/hunt_confirmed_absences.md`` (the file the resource paper cites).
"Absent" means no public dataset was found by systematic search of the
named repositories and the literature at the stated date.

.. include:: _generated/hunt_confirmed_absences.md
   :parser: myst_parser.sphinx_

Access-barriers casebook
------------------------

How often "open" data is not practically open, documented case by case
with the evidence trail the paper cites. The casebook itself stays in
the repository; its case titles are listed here from the file at build
time.

.. include:: _generated/barriers_cases.rst

See also :doc:`statistics` for the coverage matrices drawn over these
cells and :doc:`dataset_summary` for the per-dataset cell strings.
