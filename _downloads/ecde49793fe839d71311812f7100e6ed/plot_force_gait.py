# -*- coding: utf-8 -*-
"""
Force plates and insoles: the gait cycle in newtons
===================================================

Vertical ground-reaction forces from the PhysioNet gait-in-Parkinson
database (gaitpdb): 8 insole sensors plus the per-foot total at 100 Hz.
The alternating left/right pattern IS the gait cycle; its timing
irregularity is one of the oldest quantitative Parkinson markers.
"""
import os

import matplotlib.pyplot as plt
import numpy as np

from moveatlas.datasets.base import load_record
from moveatlas.store import LocalStore

store = LocalStore()
recs = load_record(store.path(
    "datasets/imu/physionet_gaitpdb/processed/canonical_force.pkl"))
print(f"{len(recs)} force records; first subject:",
      recs[0]["subject_ns"], recs[0]["force"].shape)

# %%
# Ten seconds of double-support walking, both feet's totals.

rec = recs[0]
fs = rec["fps"]
sl = slice(int(20 * fs), int(30 * fs))
t = np.arange(rec["force"].shape[0])[sl] / fs
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, rec["force"][sl, 0, 8], lw=1.0, label="left foot")
ax.plot(t, rec["force"][sl, 1, 8], lw=1.0, label="right foot")
ax.set_xlabel("time (s)")
ax.set_ylabel("vertical GRF (N)")
ax.legend(frameon=False)
ax.set_title(f"{rec['subject_ns']} - alternating stance phases")
fig.tight_layout()
