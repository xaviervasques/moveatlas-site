# -*- coding: utf-8 -*-
"""
Gait events and stride-time variability: the classic Parkinson marker
=====================================================================

Heel strikes are visible in insole forces as load onsets; the series of
stride times they define is one of the most replicated Parkinson
markers: patients walk with MORE VARIABLE stride times. This example
detects events with a plain threshold, builds the stride-time series,
and compares the variability across the two gaitpdb cohorts.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas
from moveatlas.datasets.gaitpdb import cohort_of

records, _ = moveatlas.dataset("physionet_gaitpdb").get_data()


def stride_times(rec, foot=0):
    """Load-onset times (s) of one foot -> stride durations (s)."""
    f = rec["force"][:, foot, 8].astype(float)
    thr = 0.05 * np.nanmax(f)
    on = (f > thr).astype(int)
    onsets = np.where(np.diff(on) == 1)[0] / rec["fps"]
    st = np.diff(onsets)
    return st[(st > 0.6) & (st < 2.5)]   # physiologic strides only


# %%
# The object itself: one control's stride-time series, with the events
# marked on the raw force.

rec = next(r for r in records if cohort_of(r["subject_ns"]) == "control")
f = rec["force"][:, 0, 8]
fs = rec["fps"]
sl = slice(int(20 * fs), int(35 * fs))
t = np.arange(len(f))[sl] / fs
thr = 0.05 * np.nanmax(f)
onsets = np.where(np.diff((f > thr).astype(int)) == 1)[0] / fs
fig, ax = plt.subplots(figsize=(8, 2.6))
ax.plot(t, f[sl], lw=0.7)
for o in onsets[(onsets > 20) & (onsets < 35)]:
    ax.axvline(o, color="#eb6834", lw=0.8, alpha=0.7)
ax.set_xlabel("time (s)")
ax.set_ylabel("N")
ax.set_title(f"{rec['subject_ns']}: left-foot load with detected "
             "heel strikes", loc="left", fontsize=9)
fig.tight_layout()

# %%
# Per-subject stride-time coefficient of variation (CV%), the marker.

cv = {"control": [], "parkinson": []}
for r in records:
    g = cohort_of(r["subject_ns"])
    if g == "unknown":
        continue
    st = stride_times(r)
    if len(st) >= 20:
        cv[g].append(100 * np.std(st) / np.mean(st))
fig, ax = plt.subplots(figsize=(6, 3.2))
for i, g in enumerate(["control", "parkinson"]):
    v = np.array(cv[g])
    x = np.full(len(v), i) + np.random.default_rng(0).normal(
        0, 0.05, len(v))
    ax.plot(x, v, "o", ms=3.5, alpha=0.45)
    ax.hlines(np.median(v), i - 0.2, i + 0.2, color="black", lw=2)
ax.set_xticks([0, 1])
ax.set_xticklabels([f"control (n={len(cv['control'])})",
                    f"parkinson (n={len(cv['parkinson'])})"])
ax.set_ylabel("stride-time CV (%)")
ax.set_ylim(0, np.nanpercentile(cv["control"] + cv["parkinson"], 98))
ax.set_title("Stride-time variability per walking record "
             "(bar = median)", loc="left", fontsize=9)
fig.tight_layout()

# %%
# A rank test across records (subject-level aggregation and covariates
# are the next step a real study would add):

from scipy.stats import mannwhitneyu

u, p = mannwhitneyu(cv["control"], cv["parkinson"],
                    alternative="less")
print(f"control median {np.median(cv['control']):.1f}% vs parkinson "
      f"{np.median(cv['parkinson']):.1f}%; Mann-Whitney p = {p:.2e}")
