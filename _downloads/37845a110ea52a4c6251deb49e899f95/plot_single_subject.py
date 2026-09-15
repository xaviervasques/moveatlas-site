# -*- coding: utf-8 -*-
"""
One patient, in depth: trials, trajectories, asymmetry
======================================================

The complement of cohort statistics is the single-subject view every
clinician starts from. One stroke survivor from the Van Criekinge
dataset: all their walking trials, their knee trajectories, and the
left-right asymmetry that hemiparesis produces.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

records, meta = moveatlas.dataset("stroke_gait_vancriekinge").get_data()
strokes = sorted({r["subject_ns"] for r in records
                  if r["group"] == "stroke"})
subj = strokes[2]
trials = [r for r in records if r["subject_ns"] == subj]
print(f"{subj}: {len(trials)} walking trials, "
      f"{sum(t['n_frames'] for t in trials) / trials[0]['fps']:.0f} s "
      "of gait")

# %%
# Their skeleton, via the one-liner plotter.

fig, axes = plt.subplots(1, 5, figsize=(8, 2.8))
rec = trials[0]
for ax, fr in zip(axes, np.linspace(30, rec["n_frames"] - 30, 5)):
    moveatlas.viz.plot_skeleton(rec, int(fr), ax=ax)
fig.suptitle(f"{subj}, one trial, five instants", fontsize=10)
fig.tight_layout()

# %%
# Vertical knee trajectories, left vs right, across every trial: in
# hemiparetic gait one knee typically travels flatter than the other.

L_KNEE, R_KNEE = 11, 12
fig, ax = plt.subplots(figsize=(8, 3))
for t in trials:
    fps = t["fps"]
    time = np.arange(t["n_frames"]) / fps
    for j, (name, color) in ((L_KNEE, ("left knee", "#2a78d6")),
                             (R_KNEE, ("right knee", "#eb6834"))):
        z = t["coords"][:, j, 2].astype(float)
        z[~t["valid_mask"][:, j]] = np.nan
        ax.plot(time, z, lw=0.7, color=color, alpha=0.6)
ax.set_xlabel("time (s)")
ax.set_ylabel("knee height (torso-normalized)")
ax.set_title(f"{subj}: knee vertical trajectories, all trials "
             "(blue = left, orange = right)", loc="left", fontsize=9)
fig.tight_layout()

# %%
# Quantify it: a simple asymmetry index, abs(std_L - std_R) / mean, of
# the vertical knee excursion per trial, compared against the
# able-bodied distribution.


def knee_asymmetry(rec):
    out = []
    for j in (L_KNEE, R_KNEE):
        z = rec["coords"][:, j, 2].astype(float)
        z[~rec["valid_mask"][:, j]] = np.nan
        out.append(np.nanstd(z))
    l, r = out
    return abs(l - r) / ((l + r) / 2 + 1e-9)


asym_subj = [knee_asymmetry(t) for t in trials]
asym_able = [knee_asymmetry(r) for r in records
             if r["group"] == "able_bodied"][:200]
fig, ax = plt.subplots(figsize=(6.5, 3))
ax.hist(asym_able, bins=30, alpha=0.7, label="able-bodied trials",
        density=True)
for a in asym_subj:
    ax.axvline(a, color="#eb6834", lw=1.5)
ax.set_xlabel("knee excursion asymmetry index")
ax.legend(frameon=False, fontsize=8)
ax.set_title(f"{subj}'s trials (orange lines) against the able-bodied "
             "distribution", loc="left", fontsize=9)
fig.tight_layout()
print(f"median asymmetry: subject {np.median(asym_subj):.2f} vs "
      f"able-bodied {np.median(asym_able):.2f}")
