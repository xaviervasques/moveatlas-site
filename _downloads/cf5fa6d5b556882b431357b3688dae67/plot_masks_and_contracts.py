# -*- coding: utf-8 -*-
"""
Consuming records correctly: masks, channel tables, native rates
================================================================

The canonical contracts never guess: what a sensor did not capture is
masked, not invented. This example is the safety briefing every analysis
should follow, on three real records from three families.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

# %%
# Pose: per-frame, per-joint validity. A missing marker stays missing.

records, _ = moveatlas.dataset("stroke_gait_vancriekinge").get_data()
rec = next(r for r in records if not r["valid_mask"].all())
JOINTS = ["pelvis", "neck", "head", "l_shoulder", "r_shoulder",
          "l_elbow", "r_elbow", "l_wrist", "r_wrist", "l_hip", "r_hip",
          "l_knee", "r_knee", "l_ankle", "r_ankle"]
valid_pct = rec["valid_mask"].mean(axis=0) * 100
fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(range(15), valid_pct, width=0.6)
ax.set_xticks(range(15))
ax.set_xticklabels(JOINTS, rotation=45, ha="right", fontsize=7)
ax.set_ylabel("% frames valid")
ax.set_title(f"{rec['subject_ns']}: joint validity in one trial "
             "(a missing marker is masked, never interpolated)")
fig.tight_layout()

# %%
# Averaging without the mask silently mixes zeros into your statistic.
# The contract makes the correct version one line:

coords = rec["coords"]                       # (T, 15, 3), zeros where invalid
mask = rec["valid_mask"][:, :, None]         # (T, 15, 1)
naive_mean = coords.mean(axis=0)             # WRONG where mask has holes
safe_mean = (coords * mask).sum(axis=0) / np.maximum(mask.sum(axis=0), 1)
worst = np.abs(naive_mean - safe_mean).max()
print(f"largest naive-vs-masked mean error in this trial: {worst:.3f} "
      "(torso-normalized units)")

# %%
# EMG: the channel table IS the identity. Never assume column order;
# read muscle, side and the resolved flag.

recs, _ = moveatlas.dataset("gait120").get_data(
    subjects=["gait120:S001"])
for c in recs[0]["channels"][:4]:
    print(c)
print("...")

# %%
# IMU: a fixed 14-location grid with explicit channel masks; locations
# a dataset does not instrument simply are not there.

recs, _ = moveatlas.dataset("nonan_gaitprint").get_data(
    subjects=["nonan_gaitprint:S102"])
r = recs[0]
LOCS = ["head", "trunk", "lower_back", "wrist_L", "wrist_R", "thigh_L",
        "thigh_R", "shank_L", "shank_R", "ankle_L", "ankle_R", "foot_L",
        "foot_R", "pocket"]
present = [LOCS[i] for i in r["location_ids"]]
print(f"instrumented locations in this record: {present}")
print(f"signal shape (T, n_locations, channels): {r['signal'].shape}; "
      f"native rate {r['fps']} Hz; gravity "
      f"{'included' if r['acc_content'] == 'with_gravity' else 'removed'}")
