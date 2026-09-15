Troubleshooting
===============

Every error MoveAtlas raises names the next thing to do. This page lists
them by the situation a researcher meets, with the message's first words
so you can find yours. If you hit an error that does not tell you what to
do next, that is a bug: open an issue with the full message.

Loading a dataset
-----------------

**"... is a documented access barrier, not a download"** (``AccessError``)
   The dataset needs a human step: an application, a signed agreement,
   a registration with review. The message carries the route on record
   and the data card; ``moveatlas info <id>`` prints both. Once you hold
   the data, put it under ``<store>/datasets/<family>/<id>/raw/`` and the
   card names the ingestion script.

**"... is not ingested on this machine: run ..."** (``FileNotFoundError``)
   A recipe dataset with nothing harmonized here yet. Run
   ``moveatlas.fetch(id)`` then ``moveatlas.ingest(id)``; when the recipe
   is not in the library, the message names the repository script to run
   instead (see *RecipeIsScript* below).

**"... holds files, not canonical records: ..."** (``FileNotFoundError``)
   The published record carries tables, archives or documents, which is
   what that dataset is. ``ds.files()`` lists them; ``ds.path(name)``
   downloads one, verifies it and returns a local path. Read a table with
   pandas, an archive with ``zipfile``, an ``.npz`` container with
   ``moveatlas.records.load()``.

**"... is hosted but no canonical container is under .../processed/"**
   The dataset is served from a record but nothing is listed for it, and
   nothing is on this machine: no network, or a record table older than
   the release. Check ``moveatlas info <id>`` for the record's DOI and
   your connection.

**"unknown dataset '...'; known: ..."** (``KeyError``)
   A typo in the id. ``moveatlas list`` prints every id; ids are the
   lower-case snake-case names of the catalogue.

**"... carries (...), not '...'"** (``ValueError``)
   The ``modality=`` you asked for is not one of the streams that
   dataset holds; the message lists them.

Downloading from a record
-------------------------

**"record needs network: connect, or point MOVEATLAS_REPO at ..."** (``OfflineError``)
   The record is not in the cache and the network is unreachable after
   the retries. ``OfflineError`` is a ``FileNotFoundError``, so code that
   handles "not here" keeps working.

**"sha256 mismatch for ..."** (``IOError``)
   A downloaded file did not match the record's manifest. It was removed,
   not served; run again. If it repeats, the record is damaged: report
   it with the file name.

**"the record manifest carries no sha256 for this file"** (``IOError``)
   The record's own ``files.csv`` lacks a digest, so the download cannot
   be verified and is refused. Report the record as malformed.

**"... has no published MoveAtlas record in this release's table"**
   The package's records table does not list the dataset: the dataset is
   recipe or barrier tier, or your package predates the record. Upgrade
   the package or use the recipe.

Fetching and ingesting a recipe
-------------------------------

**"...: the fetch step is not in the library yet. From a clone of the repository ..."** (``RecipeIsScript``)
   The dataset was harmonized by a repository script not ported to the
   library. The message is the exact command line to run from a clone,
   plus what the origin requires first (an account, an agreement, a
   size). ``moveatlas.recipe(id)`` prints the same before you start.

**"...: the host answers clients with a browser challenge ..."** (``ManualDownload``)
   The origin host (figshare, as of 2026-09-15) serves a bot challenge to
   programs. The message names the URL, the exact path to save the file
   at, its size and md5. Save it in a browser, run the same ``fetch()``
   again: the file is verified and journaled, and ``ingest()`` proceeds.
   MoveAtlas never tries to defeat such a challenge.

**"...: md5 mismatch after download"** (``FetchError``)
   The origin served bytes that do not match its own listing. The file
   was removed; run again. A repeat means the origin changed the file:
   check the source's page and the data card's journal.

**"...: no IMU.zip under raw/; run moveatlas.fetch(...) first"** (``FileNotFoundError``)
   ``ingest()`` before ``fetch()``; run the fetch.

**"curl is not installed; figshare refuses python's TLS stack"** (``FetchError``)
   Install curl (it ships with macOS and Windows 10+; ``apt install curl``
   elsewhere).

**"... is hosted: moveatlas.dataset(...).get_data() downloads it ...; no recipe needed"** (``NoRecipe``)
   You asked for a recipe of a hosted dataset that has none in the
   library: just call ``get_data()``.

Where things are
----------------

**"MoveAtlas record store not found"** or an empty store
   A pip-installed package keeps everything under ``~/.moveatlas/store``
   (``moveatlas where`` prints it). ``$MOVEATLAS_STORE`` moves it;
   ``$MOVEATLAS_REPO`` points at a repository checkout that already holds
   harmonized data; ``$MOVEATLAS_CACHE`` moves the record download cache.

**"datasets_index.csv not found; set MOVEATLAS_REPO ..."**
   The registry snapshot is missing from the package: a broken install.
   ``pip install --force-reinstall moveatlas``.

**"...: not a moveatlas-record/1 container (no meta.json)"** (``ValueError``)
   The ``.npz`` you opened is not a MoveAtlas record container (a raw
   numpy archive, or a file from another tool). Records are written by
   ``moveatlas.records.save()``; legacy ``.pkl`` records are read through
   ``moveatlas.records.load_any()`` with a deprecation warning.
