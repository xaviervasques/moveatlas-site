# -*- coding: utf-8 -*-
"""
Joint angles from canonical skeletons: the knee, stroke vs able-bodied
======================================================================

Clinical gait analysis speaks in joint angles. The canonical 15-joint
skeleton supports them directly: the knee flexion angle is the angle at
the knee between the thigh (hip->knee) and shank (knee->ankle) vectors.
This example computes it for every trial and compares the distribution
of knee range-of-motion between cohorts, one of the most robust
hemiparesis markers.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

records, _ = moveatlas.dataset("stroke_gait_vancriekinge").get_data()
HIP, KNEE, ANKLE = 9, 11, 13          # left side


def knee_angle_deg(rec):
    """Per-frame left-knee flexion angle; NaN where any joint is masked."""
    c = rec["coords"].astype(float)
    v1 = c[:, HIP] - c[:, KNEE]
    v2 = c[:, ANKLE] - c[:, KNEE]
    cosang = np.sum(v1 * v2, axis=1) / (
        np.linalg.norm(v1, axis=1) * np.linalg.norm(v2, axis=1) + 1e-9)
    ang = np.degrees(np.arccos(np.clip(cosang, -1, 1)))
    bad = ~(rec["valid_mask"][:, [HIP, KNEE, ANKLE]].all(axis=1))
    ang[bad] = np.nan
    return 180 - ang                   # 0 = straight leg, larger = flexed


# %%
# The raw object first: a few seconds of knee angle for one subject of
# each cohort.

fig, ax = plt.subplots(figsize=(8, 3))
for group, color in (("able_bodied", "#2a78d6"), ("stroke", "#eb6834")):
    rec = next(r for r in records if r["group"] == group
               and r["n_frames"] > 400)
    a = knee_angle_deg(rec)[:400]
    ax.plot(np.arange(len(a)) / rec["fps"], a, lw=1.2, color=color,
            label=group.replace("_", "-"))
ax.set_xlabel("time (s)")
ax.set_ylabel("left knee flexion (deg)")
ax.legend(frameon=False)
ax.set_title("Knee flexion during walking, one subject per cohort",
             loc="left", fontsize=9)
fig.tight_layout()

# %%
# Population level: per-trial knee range of motion (5th-95th percentile
# span), the flat-knee signature of hemiparetic gait made quantitative.

rom = {"able-bodied": [], "stroke": []}
for r in records:
    a = knee_angle_deg(r)
    if np.isfinite(a).sum() < 50:
        continue
    rom[r["group"].replace("_", "-")].append(
        np.nanpercentile(a, 95) - np.nanpercentile(a, 5))
fig, ax = plt.subplots(figsize=(6.5, 3))
ax.hist(rom["able-bodied"], bins=40, alpha=0.65, density=True,
        label=f"able-bodied (n={len(rom['able-bodied'])})")
ax.hist(rom["stroke"], bins=40, alpha=0.65, density=True,
        label=f"stroke (n={len(rom['stroke'])})")
ax.set_xlabel("left-knee range of motion per trial (deg)")
ax.legend(frameon=False, fontsize=8)
ax.set_title("Knee ROM distributions", loc="left", fontsize=9)
fig.tight_layout()
print({k: f"median {np.median(v):.0f} deg" for k, v in rom.items()})
