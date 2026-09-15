# -*- coding: utf-8 -*-
"""
A second disease, the same recipe: Parkinson from ground-reaction forces
========================================================================

The cross-patient recipe generalizes across pathologies and modalities.
Here: Parkinson vs control from insole vertical GRF (PhysioNet gaitpdb,
93 patients / 72 controls), with the standardization step explicit in
the pipeline, a confusion matrix on held-out patients, and a permutation
test so chance cannot fool us.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import ConfusionMatrixDisplay, balanced_accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import moveatlas
from moveatlas.datasets.gaitpdb import cohort_of
from moveatlas.paradigms import FixedIntervalWindows
from moveatlas.pipelines import StatFeatures

records, meta = moveatlas.dataset("physionet_gaitpdb").get_data()
for r in records:                       # attach the eval-only label
    r["label"] = int(cohort_of(r["subject_ns"]) == "parkinson")
    r["signal"] = r["force"]            # windows read 'signal'
records = [r for r in records
           if cohort_of(r["subject_ns"]) != "unknown"]
print(f"{len(records)} walking records")

# %%
# Windows and groups; then a pipeline where StandardScaler is explicit:
# features are standardized on the TRAINING patients of each fold only,
# never on the test patients (the pipeline guarantees it).

X, y, groups = FixedIntervalWindows(5.0, label_from="record").get_data(
    records)
print(f"{len(y)} five-second windows; class balance "
      f"{np.bincount(y) / len(y)}")

pipe = Pipeline([("features", StatFeatures()),
                 ("standardize", StandardScaler()),
                 ("clf", LinearDiscriminantAnalysis())])

# %%
# Patient-level 5-fold, collecting held-out predictions.

from moveatlas.evaluations import cross_patient_folds
import pandas as pd

wmeta = pd.DataFrame({"subject_ns": groups})
y_true, y_pred, scores = [], [], []
for tr, te in cross_patient_folds(wmeta, n_splits=5):
    model = pipe.fit([X[i] for i in tr], y[tr])
    p = model.predict([X[i] for i in te])
    scores.append(balanced_accuracy_score(y[te], p))
    y_true.extend(y[te])
    y_pred.extend(p)
print(f"balanced accuracy: {np.mean(scores):.3f} +/- {np.std(scores):.3f}")

# %%
# The standardized report figure: a confusion matrix over all held-out
# windows.

fig, ax = plt.subplots(figsize=(4, 3.4))
ConfusionMatrixDisplay.from_predictions(
    y_true, y_pred, display_labels=["control", "parkinson"],
    cmap="Blues", colorbar=False, ax=ax)
ax.set_title("Held-out windows, all folds", fontsize=9)
fig.tight_layout()

# %%
# Don't fool yourself: a label-permutation test. Shuffle the labels AT
# THE SUBJECT LEVEL (a window permutation would leak), refit, and see
# where the real score sits in the null distribution.

rng = np.random.default_rng(0)
subjects = np.unique(groups)
null = []
for _ in range(10):                      # small for the docs build
    lab = dict(zip(subjects, rng.permutation(
        [int(cohort_of(s) == "parkinson") for s in subjects])))
    y_perm = np.array([lab[g] for g in groups])
    s = []
    for tr, te in cross_patient_folds(wmeta, n_splits=5):
        m = pipe.fit([X[i] for i in tr], y_perm[tr])
        s.append(balanced_accuracy_score(
            y_perm[te], m.predict([X[i] for i in te])))
    null.append(np.mean(s))
print(f"real {np.mean(scores):.3f} vs permuted "
      f"{np.mean(null):.3f} +/- {np.std(null):.3f} "
      f"(max over {len(null)} permutations: {max(null):.3f})")
