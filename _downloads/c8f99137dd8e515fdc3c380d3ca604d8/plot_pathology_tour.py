# -*- coding: utf-8 -*-
"""
All the data for one pathology: a Parkinson tour
================================================

"Show me everything on disease X" is the first question a clinical
researcher asks. Cell B2 is the Parkinson/hypokinetic axis: this example
lists every B2 dataset with its access case, then opens REAL records
from two different modalities of the same disease.
"""
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import moveatlas

cat = moveatlas.list_datasets()
b2 = [r for r in cat if "B2" in re.findall(r"[A-E]\d+|M\d+",
                                           r["moveatlas_cells"])]
tour = pd.DataFrame([{ "id": r["id"], "family": r["family"],
                       "access": r["access_case"],
                       "subjects": r["n_subjects"][:12]} for r in b2])
print(f"{len(b2)} Parkinson-cell datasets:")
print(tour.to_string(index=False))

# %%
# The access column is the honest map: hosted ones load now; recipe ones
# fetch from their original home; barriers document why not.

print(tour.access.value_counts().to_dict())

# %%
# Modality 1 - force: vertical ground reaction of a Parkinson patient vs
# a control (PhysioNet gaitpdb; the cohort is encoded in the id by the
# source: Pt = patient, Co = control).

from moveatlas.datasets.gaitpdb import cohort_of

recs, meta = moveatlas.dataset("physionet_gaitpdb").get_data()
pt = next(r for r in recs if cohort_of(r["subject_ns"]) == "parkinson")
co = next(r for r in recs if cohort_of(r["subject_ns"]) == "control")
fig, axes = plt.subplots(2, 1, figsize=(8, 4), sharex=True, sharey=True)
for ax, rec, label in ((axes[0], co, "control"),
                       (axes[1], pt, "parkinson")):
    fs = rec["fps"]
    sl = slice(int(30 * fs), int(45 * fs))
    t = np.arange(rec["force"].shape[0])[sl] / fs
    ax.plot(t, rec["force"][sl, 0, 8], lw=0.8)
    ax.set_ylabel("N")
    ax.set_title(f"{label} ({rec['subject_ns']})", loc="left", fontsize=9)
axes[1].set_xlabel("time (s)")
fig.suptitle("Left-foot vertical GRF, 15 s of walking", fontsize=10)
fig.tight_layout()

# %%
# Modality 2 - EEG at rest from a Parkinson cohort (OpenNeuro ds004584),
# via the one-liner plotter.

from moveatlas.datasets.base import load_record
from moveatlas.store import LocalStore

rec = load_record(LocalStore().path(
    "datasets/eeg/pd_rest_eeg_ds004584/processed/canonical_eeg/"
    "pd_rest_eeg_ds004584__pd_rest_eeg_ds004584_sub-040__Rest.pkl"))
ax = moveatlas.viz.plot_trace(rec, n_channels=6, t_start=10, t_stop=20)
ax.set_title("Parkinson resting EEG, 6 channels (ds004584, "
             f"{rec['fps']:.0f} Hz)", loc="left", fontsize=9)
plt.tight_layout()

# %%
# The same pattern works for any cell: tremor is A1, dystonia A4,
# freezing of gait B5, stroke D3; `moveatlas.list_datasets()` plus a
# cell filter is the whole query language.
