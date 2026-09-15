# -*- coding: utf-8 -*-
"""
Getting started: load a hosted dataset
======================================

Load one subject of Gait120 (120 healthy adults, 7 locomotion tasks,
surface EMG of 12 named right-leg muscles at 2000 Hz) and look at one
level-walking trial. Gait120 is a *hosted* dataset: one call returns
canonical records.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

ds = moveatlas.dataset("gait120")
print(ds)

records, meta = ds.get_data(subjects=["gait120:S001"])
print(meta.head())

# %%
# Each record is a canonical EMG record: signal (T, C) in mV at the native
# 2000 Hz, and a channel table naming every muscle.

rec = next(r for r in records if r["task"] == "level_walking_trial01")
sig = rec["signal"]
names = [c["muscle"] for c in rec["channels"]]
t = np.arange(sig.shape[0]) / rec["fps"]

fig, axes = plt.subplots(4, 1, figsize=(8, 6), sharex=True)
for ax, k in zip(axes, range(4)):
    ax.plot(t, sig[:, k], lw=0.4)
    ax.set_ylabel(names[k], fontsize=7, rotation=0, ha="right")
axes[-1].set_xlabel("time (s)")
fig.suptitle("Gait120 S001, level walking, first 4 of 12 muscles")
fig.tight_layout()
