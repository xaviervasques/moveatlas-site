Getting started
===============

MoveAtlas is a Python package over a catalogue of movement datasets. In
three lines you have canonical records of a real dataset in memory; the
rest of this page is what those lines did and where the data went.

Install
-------

MoveAtlas targets Python 3.9+ and depends on numpy and pandas only.

.. code-block:: bash

   pip install moveatlas            # from PyPI, at the public launch
   pip install 'moveatlas[bench]'   # adds scikit-learn and scipy for the baselines

Until the launch, install from the repository:

.. code-block:: bash

   pip install git+https://github.com/xaviervasques/moveatlas.git

Check the install and see the catalogue:

.. code-block:: bash

   moveatlas --version
   moveatlas list                   # 170 datasets, one access case each
   moveatlas info modys_video       # one dataset: licence, route, record, recipe

First dataset, three lines
--------------------------

.. code-block:: python

   import moveatlas

   ds = moveatlas.dataset("modys_video")     # a hosted dataset (CC BY 4.0)
   records, meta = ds.get_data()             # 94 records, downloaded once

What happened: the registry classified ``modys_video`` as **hosted**, so
``get_data()`` fetched the dataset's published MoveAtlas record from
Zenodo (2.8 MB), verified every byte against the record's sha256
manifest, cached it under ``~/.moveatlas`` and opened the canonical
container. The second call reads the cache.

``records`` is a list of dicts, one per recording; ``meta`` is a
``pandas.DataFrame`` with one row per record (dataset, subject, task,
modality, frames, sampling rate). Every record is self-describing:

.. code-block:: python

   r = records[0]
   r["subject_ns"], r["n_frames"]              # 'modys_video:...', 501
   r["coords"].shape                           # (501, 15, 3): frames, joints, x/y/conf
   r["modality"], r["dim"], r["scale"]         # '2d_pixel', 2, the pixel scale
   r["joint_mask"], r["coord_mask"]            # what is present, per joint / sample

Each canonical family has its own contract (pose, IMU, EMG, force,
silhouette, EEG); :doc:`modalities` shows what the records look like and
:doc:`user_guide` lists the fields.

Where the data lives
--------------------

Everything the package downloads or builds goes to one directory, the
**store**:

.. code-block:: bash

   moveatlas where                  # ~/.moveatlas/store by default

- ``$MOVEATLAS_STORE`` moves it (a big disk, a shared mount);
- ``$MOVEATLAS_REPO`` points the package at a clone of the repository
  that already holds harmonized data (a developer's checkout);
- ``$MOVEATLAS_CACHE`` moves the download cache of the hosted records.

The store is laid out like the repository, ``datasets/<family>/<id>/``
with ``raw/`` and ``processed/`` inside, so a dataset built on one
machine is a directory you can copy to another.

The three access cases
----------------------

Not every catalogued dataset can be served: licences differ. The registry
says which case applies and the package enforces it; the
:doc:`user guide <user_guide>` walks one complete example of each.

.. list-table::
   :header-rows: 1
   :widths: 14 46 40

   * - case
     - what it means
     - what you do
   * - hosted
     - the licence allows redistribution; MoveAtlas serves a verified
       record
     - ``moveatlas.dataset(id).get_data()``
   * - recipe
     - the licence does not allow redistribution, or the record is not
       published yet; the origin host serves the raw data and MoveAtlas
       harmonizes it locally
     - ``moveatlas.fetch(id)``, ``moveatlas.ingest(id)``, then
       ``get_data()``
   * - barrier
     - access needs a human step (an application, a signed agreement); the
       route is documented
     - ``get_data()`` raises the route; follow it, then the card says how
       to ingest

Next
----

- :doc:`user_guide`: the three walks, the record format, subject-level
  splits, the evaluation paradigms.
- :doc:`auto_examples/index`: executed examples, each downloadable as
  ``.py`` and ``.ipynb``.
- :doc:`datasets/index`: every dataset's card, licence and access route.
- :doc:`api`: the reference.
