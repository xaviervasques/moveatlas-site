# -*- coding: utf-8 -*-
"""
Explore the catalogue: families, pathologies, healthy cohorts, access
=====================================================================

The registry catalogues the movement datasets. This example shows every
way to slice it without downloading a byte: by modality family, by
access case, by clinical taxonomy cell (pathological axes A/B/D/E
against the healthy lifespan axis C), and what an honest failure looks
like when a dataset cannot be downloaded.
"""
import collections
import re

import matplotlib.pyplot as plt
import numpy as np

import moveatlas

cat = moveatlas.list_datasets()
print(f"{len(cat)} datasets")

# %%
# By access case: hosted downloads in one call; recipe fetches from the
# original host; barrier raises its documented route; local_only is the
# private tier.

counts = collections.Counter(r["access_case"] for r in cat)
print(dict(counts))

# %%
# By modality family, crossed with access case.

fams = sorted({r["family"] for r in cat})
cases = ["hosted", "recipe", "barrier", "local_only"]
table = {f: collections.Counter(r["access_case"] for r in cat
                                if r["family"] == f) for f in fams}
fig, ax = plt.subplots(figsize=(8, 3.4))
bottom = np.zeros(len(fams))
for case in cases:
    vals = np.array([table[f][case] for f in fams], float)
    ax.bar(fams, vals, bottom=bottom, label=case, width=0.6)
    bottom += vals
ax.set_ylabel("datasets")
ax.legend(frameon=False, ncol=4, fontsize=8)
ax.set_title("The catalogue by family and access case")
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=8)
fig.tight_layout()

# %%
# Filter helpers: one family at a time.

for r in moveatlas.list_datasets(family="emg"):
    print(f"{r['id']:28s} {r['access_case']:10s} {r['moveatlas_cells']}")

# %%
# Clinical slicing by taxonomy cell. Axes A (hyperkinetic), B
# (hypokinetic/parkinsonian), D (other clinical) and E (musculoskeletal)
# are pathology; axis C is the healthy lifespan; M axes are modalities.


def cells_of(r):
    return set(re.findall(r"[A-E]\d+|M\d+", r["moveatlas_cells"]))


def datasets_in(cell):
    return [r for r in cat if cell in cells_of(r)]


print("Parkinson/hypokinetic (B2):",
      [r["id"] for r in datasets_in("B2")][:8], "...")
print("Tremor (A1):", [r["id"] for r in datasets_in("A1")][:8], "...")
print("Healthy adults (C1):",
      [r["id"] for r in datasets_in("C1")][:8], "...")

# %%
# Pathological vs healthy-only datasets, at a glance.

patho_axes = set("ABDE")
patho = [r for r in cat
         if any(c[0] in patho_axes for c in cells_of(r))]
healthy_only = [r for r in cat
                if cells_of(r) and
                all(c[0] in "CM" for c in cells_of(r))]
print(f"{len(patho)} datasets carry at least one pathology cell;")
print(f"{len(healthy_only)} are healthy/modality-only (the pretraining "
      "socle and lifespan references)")

# %%
# Honesty check: a retracted dataset refuses politely, carrying its
# evidence, instead of failing obscurely.

try:
    moveatlas.dataset("tim_tremor").get_data()
except Exception as e:
    print(f"{type(e).__name__}: {str(e)[:180]}")
