# -*- coding: utf-8 -*-
"""
See your splits before you trust them
=====================================

The classic sin of clinical machine learning is subject leakage: windows
of the same patient on both sides of a split. This example draws the
split structure itself (the scikit-learn `plot_cv_indices` idea) for a
naive KFold and for MoveAtlas' patient-level folds, on real stroke-gait
windows, and counts the leaked subjects in each.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas
from moveatlas.evaluations import cross_patient_folds
from moveatlas.paradigms import FixedIntervalWindows

records, meta = moveatlas.dataset("stroke_gait_vancriekinge").get_data()
X, y, groups = FixedIntervalWindows(2.0, label_from="record").get_data(
    records)
order = np.argsort(groups, kind="stable")     # sort windows by subject
y, groups = y[order], groups[order]
print(f"{len(y)} windows from {len(set(groups))} subjects")


def naive_kfold(n, k=5):
    idx = np.array_split(np.arange(n), k)
    for te in idx:
        yield np.setdiff1d(np.arange(n), te), te


def window_meta():
    import pandas as pd
    return pd.DataFrame({"subject_ns": groups})


fig, axes = plt.subplots(2, 1, figsize=(8.5, 4.6), sharex=True)
for ax, folds, title in (
        (axes[0], list(naive_kfold(len(y))), "naive KFold over windows"),
        (axes[1], list(cross_patient_folds(window_meta(), 5)),
         "cross_patient_folds (subject-grouped)")):
    leaked = 0
    for k, (tr, te) in enumerate(folds):
        row = np.full(len(y), np.nan)
        row[tr], row[te] = 0, 1
        ax.scatter(np.arange(len(y)), np.full(len(y), k), c=row,
                   cmap="coolwarm", s=1.2, vmin=0, vmax=1, rasterized=True)
        leaked += len(set(groups[tr]) & set(groups[te]))
    # class band under the folds
    ax.scatter(np.arange(len(y)), np.full(len(y), -1.2), c=y,
               cmap="Greys", s=1.2, rasterized=True)
    ax.set_yticks(list(range(len(folds))) + [-1.2])
    ax.set_yticklabels([f"fold {k}" for k in range(len(folds))]
                       + ["class"], fontsize=7)
    ax.set_title(f"{title}: {leaked} leaked subject-fold pairs",
                 loc="left", fontsize=9)
axes[1].set_xlabel("window index (sorted by subject)")
fig.suptitle("Blue = train, red = test. Leakage is visible as folds "
             "that cut through a subject's block.", fontsize=9, y=0.99)
fig.tight_layout()

# %%
# The numbers behind the picture: the naive KFold splits subjects across
# train and test in every fold; the patient-level folds never do. This
# is why every MoveAtlas evaluation is built on the grouped primitive.
