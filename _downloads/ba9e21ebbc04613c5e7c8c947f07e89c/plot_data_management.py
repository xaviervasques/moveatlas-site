# -*- coding: utf-8 -*-
"""
Data management: the record store
=================================

Where does the data come from? The hosted tier is served by the MoveAtlas
record store. Today that store is LOCAL (nothing is published yet); after
the public launch the same interface fronts MoveAtlas's Zenodo records
and Hugging Face datasets, and this example will not change.
"""
import os

from moveatlas.store import LocalStore

store = LocalStore()
# the root is a local path on whichever machine ran the build; print
# only that it resolved, never the path itself
print("store root resolved:", os.path.isdir(store.root))

# %%
# ``MOVEATLAS_REPO`` overrides the root when the package is installed
# outside the repository:

print("override via MOVEATLAS_REPO:",
      os.environ.get("MOVEATLAS_REPO", "(not set, auto-detected)"))

# %%
# The store hands out verified paths and can check a sha256 manifest;
# a missing record is a clear error naming the ingestion recipe to run,
# never a silent empty result.

try:
    store.path("datasets/pose/nonexistent/processed/canonical.npz")
except FileNotFoundError as e:
    # the message names the local root, so show only its first sentence
    print("FileNotFoundError:", str(e).split(" (root")[0])
