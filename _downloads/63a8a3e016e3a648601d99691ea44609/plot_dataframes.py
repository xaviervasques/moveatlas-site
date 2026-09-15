# -*- coding: utf-8 -*-
"""
Every record is a DataFrame away
================================

`moveatlas.to_frame(record)` turns any canonical record into a tidy,
time-indexed pandas DataFrame with named columns, and the masks become
NaN (never silent zeros). From there the whole pandas toolbox applies:
`.head()`, `.describe()`, resampling, rolling statistics, joins.
"""
import matplotlib.pyplot as plt

import moveatlas

# %%
# EMG: columns are muscles (name_side), index is seconds at 2000 Hz.

recs, _ = moveatlas.dataset("gait120").get_data(subjects=["gait120:S001"])
df = moveatlas.to_frame(recs[0])
print(df.head())

# %%
# `.describe()` is an instant per-muscle amplitude report (mV):

print(df.describe().T[["mean", "std", "min", "max"]].round(4).head(6))

# %%
# Force: a two-level column index (foot, sensor).

recs, _ = moveatlas.dataset("physionet_gaitpdb").get_data(
    subjects=["gaitpdb:GaCo01"])
fdf = moveatlas.to_frame(recs[0])
print(fdf[[("left", "total"), ("right", "total")]].head())

# %%
# Pandas machinery for free: a 1-second rolling mean of the total load,
# plotted straight from the frame.

ax = (fdf[("left", "total")].rolling(100, center=True).mean()
      .loc[20:40].plot(figsize=(7, 2.6), lw=1))
ax.set_ylabel("left-foot load (N), 1 s rolling mean")
plt.tight_layout()

# %%
# Pose: (joint, axis) columns, and the mask discipline travels with the
# frame: the stroke subject whose head marker is missing has NaN there,
# so pandas statistics are honest by construction.

recs, _ = moveatlas.dataset("stroke_gait_vancriekinge").get_data()
rec = next(r for r in recs if not r["valid_mask"].all())
pdf = moveatlas.to_frame(rec)
print(pdf.isna().mean().groupby("joint").mean().sort_values(
    ascending=False).head(4).rename("fraction NaN"))

# %%
# IMU: (location, channel) columns for instrumented slots only.

recs, _ = moveatlas.dataset("nonan_gaitprint").get_data(
    subjects=["nonan_gaitprint:S102"])
idf = moveatlas.to_frame(recs[0])
print(idf.head(3))
