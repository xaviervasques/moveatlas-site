Datasets
========

|n_catalogued| movement datasets are catalogued across twelve human
modality lanes and one animal lane: |n_human| human, |n_animal| animal
(counts read from the registry at build time). The cell codes in the
tables are defined on the :doc:`taxonomy` page.
Every dataset keeps ONE identity (one name, one card, one download)
however many modality streams it carries; multimodal sets appear in
each family table they contribute to. Animal entries (mouse, rat and
macaque models of movement disorders) carry species and model
metadata and map to symptom analogs in free text; they never mix
into the human clinical taxonomy cells.

Access cases
------------

- **hosted**: served from MoveAtlas's own verified records; one call
  downloads. (Today: the local record store; MoveAtlas's public Zenodo /
  Hugging Face records open with the public launch.)
- **recipe**: fetched from the original host by our ingestion recipe.
- **local_only**: private-tier data; nothing downloads, a local path
  is required. Empty since 2026-09-01: the CODY derived release is
  public on Zenodo (CC BY 4.0, 10.5281/zenodo.22232609) and the CODY
  entries sit in the hosted tier; raw patient video stays in-house,
  outside the atlas.
- **barrier**: a documented access barrier; the package raises the
  documented route instead of a download.

Master table
------------

.. raw:: html
   :file: _generated/dataset_table.html

Per-family detail tables
------------------------

.. raw:: html
   :file: _generated/family_tables.html

Submit a new dataset
--------------------

See :doc:`submit_dataset` for the full flow. In one line: signal your
dataset on the pinned wishlist issue, host it openly (Zenodo / Hugging
Face / Kaggle) if you own it, write the adapter, and pass the two
MoveAtlas gates (license triage and the privacy gate) before merge.
