# -*- coding: utf-8 -*-
"""
Four cohorts, one measure: cadence across health, aging and disease
===================================================================

One walking-rate measure computed on four cohorts from THREE datasets
and two modalities: young and older healthy adults (NONAN, lower-back
accelerometry), Parkinson patients and their controls (gaitpdb, insole
forces). The point is methodological as much as clinical: MoveAtlas
lets you line cohorts up in minutes, and the caveat at the end is part
of the lesson.
"""
import os

import matplotlib.pyplot as plt
import numpy as np

import moveatlas
from moveatlas.datasets.gaitpdb import cohort_of
from moveatlas.store import LocalStore

N_NONAN = 10


def imu_step_freq(rec):
    sig = rec["signal"][:, 2, 0] - rec["signal"][:, 2, 0].mean()
    spec = np.abs(np.fft.rfft(sig * np.hanning(len(sig))))
    freqs = np.fft.rfftfreq(len(sig), 1 / rec["fps"])
    band = (freqs >= 1.2) & (freqs <= 3.5)
    return freqs[band][np.argmax(spec[band])]


def grf_step_freq(rec):
    """Steps per second from alternating-foot load onsets."""
    both = []
    for foot in (0, 1):
        f = rec["force"][:, foot, 8].astype(float)
        on = (f > 0.05 * np.nanmax(f)).astype(int)
        both.extend(np.where(np.diff(on) == 1)[0] / rec["fps"])
    both = np.sort(both)
    steps = np.diff(both)
    steps = steps[(steps > 0.25) & (steps < 1.5)]
    return 1.0 / np.median(steps) if len(steps) > 10 else np.nan


cohorts = {}
for code, label in (("nonan_gaitprint_young", "healthy young"),
                    ("nonan_gaitprint", "healthy older")):
    ds = moveatlas.dataset(code)
    shards = LocalStore().glob_dir(ds._reldir)[:N_NONAN]
    subs = [f"{code}:{os.path.basename(p)[:-4]}" for p in shards]
    recs, _ = ds.get_data(subjects=subs)
    vals = []
    for s in subs:
        rr = [r for r in recs if r["subject_ns"] == s][:3]
        vals.append(np.mean([imu_step_freq(r) for r in rr]))
    cohorts[label] = np.array(vals)

recs, _ = moveatlas.dataset("physionet_gaitpdb").get_data()
for group, label in (("control", "gaitpdb control"),
                     ("parkinson", "parkinson")):
    per_subj = {}
    for r in recs:
        if cohort_of(r["subject_ns"]) != group:
            continue
        v = grf_step_freq(r)
        if np.isfinite(v):
            per_subj.setdefault(r["subject_ns"], []).append(v)
    cohorts[label] = np.array([np.mean(v) for v in per_subj.values()])

for k, v in cohorts.items():
    print(f"{k:16s} n={len(v):3d}  median {np.median(v):.2f} steps/s")

# %%

fig, ax = plt.subplots(figsize=(7.5, 3.4))
for i, (label, v) in enumerate(cohorts.items()):
    x = np.full(len(v), i) + np.random.default_rng(0).normal(
        0, 0.05, len(v))
    ax.plot(x, v, "o", ms=3.5, alpha=0.5)
    ax.hlines(np.median(v), i - 0.22, i + 0.22, color="black", lw=2)
ax.set_xticks(range(len(cohorts)))
ax.set_xticklabels([f"{k}\n(n={len(v)})" for k, v in cohorts.items()],
                   fontsize=8)
ax.set_ylabel("step frequency (steps/s)")
ax.set_title("Walking cadence across four cohorts (bar = median)",
             loc="left", fontsize=9)
fig.tight_layout()

# %%
# THE CAVEAT, which is the meta-analysis lesson: these cohorts come from
# different devices, protocols and walking instructions, so the
# between-DATASET offsets are not a biological finding; only
# within-dataset contrasts (parkinson vs its own controls) support
# clinical claims, and cross-dataset evidence must be combined by
# meta-analysis, never by pooling. MoveAtlas' evaluation layer exists
# precisely to keep that honest.
