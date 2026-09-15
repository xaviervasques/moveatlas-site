# -*- coding: utf-8 -*-
"""
A complete cross-patient study: windows, pipelines, scores, statistics
======================================================================

The full research loop on one dataset, end to end: cut canonical records
into fixed windows, run pipelines under a patient-level evaluation, look
at the per-fold outputs, and test a pipeline comparison properly. Every
step is a tool a study can reuse as-is.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wilcoxon

import moveatlas
from moveatlas.evaluations import CrossPatientEvaluation
from moveatlas.paradigms import FixedIntervalWindows
from moveatlas.pipelines import baseline_pipelines

ds = moveatlas.dataset("stroke_gait_vancriekinge")
paradigm = FixedIntervalWindows(duration_s=2.0, label_from="record")
evaluation = CrossPatientEvaluation(n_splits=5, seed=0)
pipes = baseline_pipelines()

res = evaluation.evaluate(paradigm, ds, pipes)
print(res.head())

# %%
# The output is a tidy DataFrame: one row per (fold, pipeline), with the
# balanced-accuracy score and the fold's subject counts. Summarize it:

summary = (res.groupby("pipeline")["score"]
           .agg(["mean", "std", "count"]).round(3))
print(summary)

# %%
# Visualize the per-fold scores: distributions, not just means.

names = list(pipes)
fig, ax = plt.subplots(figsize=(7, 3.2))
for i, name in enumerate(names):
    v = res[res.pipeline == name].score.to_numpy()
    x = np.full(len(v), i) + np.linspace(-0.08, 0.08, len(v))
    ax.plot(x, v, "o", ms=6, alpha=0.7)
    ax.hlines(v.mean(), i - 0.2, i + 0.2, color="black", lw=2)
ax.axhline(0.5, color="gray", lw=0.8, ls="--")
ax.text(2.35, 0.505, "chance", fontsize=7, color="gray")
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, fontsize=8)
ax.set_ylabel("balanced accuracy")
ax.set_title("Stroke vs able-bodied, CrossPatient (5 folds)")
fig.tight_layout()

# %%
# Compare two pipelines the right way: paired on the SAME folds, with a
# nonparametric test. With only 5 folds the p-value is coarse; on a real
# study, combine evidence across datasets (Stouffer) rather than adding
# folds.

a = res[res.pipeline == "StatFeatures + LDA"].sort_values("fold").score
b = res[res.pipeline == "StatFeatures + LogReg"].sort_values("fold").score
stat, p = wilcoxon(a, b)
print(f"LDA vs LogReg, paired Wilcoxon over folds: p = {p:.3f}")
print(f"per-fold differences: {(b.to_numpy() - a.to_numpy()).round(3)}")

# %%
# The invariant that makes all of this trustworthy: no subject ever
# appears on both sides of a fold. Verify it yourself:

records, meta = ds.get_data()
X, y, groups = paradigm.get_data(records)
from moveatlas.evaluations import cross_patient_folds
for k, (tr, te) in enumerate(cross_patient_folds(meta, n_splits=5)):
    s1 = set(meta.iloc[tr].subject_ns)
    s2 = set(meta.iloc[te].subject_ns)
    assert not s1 & s2
print("all folds verified leak-free")
