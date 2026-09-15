# -*- coding: utf-8 -*-
"""
Clinical scales are data too: a botulinum-toxin trial in dystonia
=================================================================

Movement science is not only signals: the auxdata tier carries clinical
scale tables. The cdystonia table is a classic randomized trial of
botulinum toxin in cervical dystonia (TWSTRS severity scores over 16
weeks, three arms). Longitudinal spaghetti + group means in a few pandas
lines.
"""
import matplotlib.pyplot as plt
import pandas as pd
import pyreadr

from moveatlas.store import LocalStore

# access-barrier miniature, worth savoring: hbiostat serves this as
# '.sav', which suggests SPSS; it is actually a gzip-compressed R save
# file (RDX2). pyreadr reads it in one line. The data card records this.
df = pyreadr.read_r(LocalStore().path(
    "datasets/auxdata/cdystonia/raw/cdystonia.sav"))["cdystonia"]
df["patient"] = df["site"].astype(str) + ":" + df["id"].astype(str)
print(df.head())
print(f"\n{df['patient'].nunique()} patients across "
      f"{df['site'].nunique()} sites; arms: "
      f"{sorted(df['treat'].unique())}")

# %%
# Individual trajectories (thin) and arm means (thick): the shape of a
# treatment effect, straight from the table.

fig, ax = plt.subplots(figsize=(7.5, 3.6))
colors = {}
palette = ["#2a78d6", "#eb6834", "#1baf7a"]
for i, (arm, g) in enumerate(df.groupby("treat", observed=True)):
    colors[arm] = palette[i % 3]
    for _, traj in g.groupby("patient"):
        ax.plot(traj["week"], traj["twstrs"], lw=0.4,
                color=colors[arm], alpha=0.25)
    mean = g.groupby("week", observed=True)["twstrs"].mean()
    ax.plot(mean.index, mean.values, lw=2.6, color=colors[arm],
            label=str(arm))
ax.set_xlabel("week")
ax.set_ylabel("TWSTRS severity")
ax.legend(frameon=False, fontsize=8, title="arm")
ax.set_title("Cervical dystonia trial: individual and mean trajectories",
             loc="left", fontsize=9)
fig.tight_layout()

# %%
# The same table answers Table-2 questions in one line each:

print(df.groupby(["treat", "week"], observed=True)["twstrs"]
      .mean().unstack().round(1))
