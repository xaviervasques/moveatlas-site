# -*- coding: utf-8 -*-
"""
Muscle-by-task activity maps from a multimodal dataset
======================================================

Gait120 records 12 named right-leg muscles across 7 locomotion tasks.
One matrix answers "which muscle works in which task": median RMS
activity per (muscle, task), computed over subjects. This is also the
template for any channels-by-conditions map (EEG bands by task, IMU
locations by activity).
"""
import re

import matplotlib.pyplot as plt
import numpy as np

import moveatlas

N_SUBJECTS = 10       # raise freely; 120 available
subs = [f"gait120:S{i:03d}" for i in range(1, N_SUBJECTS + 1)]
records, meta = moveatlas.dataset("gait120").get_data(subjects=subs)
muscles = [c["muscle"] for c in records[0]["channels"]]
tasks = sorted({re.sub(r"_trial\d+$", "", r["task"]) for r in records})
print(len(records), "records,", len(tasks), "tasks,", len(muscles),
      "muscles")

# %%
# Median RMS per muscle and task (mV), across all trials of all loaded
# subjects.

grid = np.zeros((len(muscles), len(tasks)))
for j, task in enumerate(tasks):
    recs = [r for r in records
            if re.sub(r"_trial\d+$", "", r["task"]) == task]
    rms = np.array([np.sqrt(np.mean(r["signal"] ** 2, axis=0))
                    for r in recs])          # (n_trials, 12)
    grid[:, j] = np.median(rms, axis=0)

fig, ax = plt.subplots(figsize=(8, 4.4))
im = ax.imshow(grid, aspect="auto", cmap="Blues")
ax.set_xticks(range(len(tasks)))
ax.set_xticklabels([t.replace("_", " ") for t in tasks], rotation=30,
                   ha="right", fontsize=8)
ax.set_yticks(range(len(muscles)))
ax.set_yticklabels(muscles, fontsize=8)
fig.colorbar(im, ax=ax, label="median RMS (mV)", shrink=0.8)
ax.set_title(f"Right-leg muscle activity by task "
             f"({N_SUBJECTS} subjects, all trials)")
fig.tight_layout()

# %%
# Read it off the matrix (data, not narrative): tibialis anterior is the
# busiest muscle across every task; the calf group (gastrocnemius,
# soleus, peroneus) rises for slope and stair work; the vasti wake up
# for sit-to-stand. Rerun with more subjects and it sharpens.
