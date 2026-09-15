# -*- coding: utf-8 -*-
"""
Patients and controls: cohorts, balance, and descriptive statistics
===================================================================

Most clinical questions start with "who is in the data". The Van
Criekinge stroke-gait dataset carries an eval-only cohort label on every
record (1 = stroke, 0 = able-bodied); this example builds the cohort
table a paper's Table 1 starts from, and two honest descriptive views.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import moveatlas

ds = moveatlas.dataset("stroke_gait_vancriekinge")
records, meta = ds.get_data()
groups = pd.Series([r["group"] for r in records], name="group")
meta = meta.join(groups)
print(meta.head())

# %%
# The cohort table: subjects, records, and recording time per group.

tab = (meta.assign(minutes=meta.n_frames / meta.fps / 60)
       .groupby("group")
       .agg(subjects=("subject_ns", "nunique"),
            records=("subject_ns", "size"),
            minutes=("minutes", "sum")).round(1))
print(tab)

# %%
# Records per subject: stroke subjects were recorded in fewer, longer
# walks; the distribution shows the protocol difference honestly.

per_subj = meta.groupby(["group", "subject_ns"]).size()
fig, ax = plt.subplots(figsize=(7, 3))
for i, g in enumerate(["able_bodied", "stroke"]):
    v = per_subj[g].to_numpy()
    x = np.random.default_rng(0).normal(i, 0.06, len(v))
    ax.plot(x, v, "o", ms=4, alpha=0.5)
    ax.hlines(np.median(v), i - 0.2, i + 0.2, color="black", lw=2)
ax.set_xticks([0, 1])
ax.set_xticklabels(["able-bodied", "stroke"])
ax.set_ylabel("records per subject")
ax.set_title("Per-subject record counts (bar = median)")
fig.tight_layout()

# %%
# Trial durations per group.

dur = meta.assign(seconds=meta.n_frames / meta.fps)
fig, ax = plt.subplots(figsize=(7, 3))
data = [dur[dur.group == g].seconds for g in ["able_bodied", "stroke"]]
ax.boxplot(data, tick_labels=["able-bodied", "stroke"], widths=0.4)
ax.set_ylabel("trial duration (s)")
ax.set_title("Walking-trial durations per cohort")
fig.tight_layout()

# %%
# Class balance matters for every evaluation that follows: 138 vs 50
# subjects is why MoveAtlas scores with balanced accuracy by default.

print(f"class balance (subjects): "
      f"{meta.groupby('group')['subject_ns'].nunique().to_dict()}")
