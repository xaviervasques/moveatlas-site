# -*- coding: utf-8 -*-
"""
CODY: dystonia in the atlas's own cohort
========================================

MoveAtlas exists because open hyperkinetic data is scarce - and CODY is
the project's own contribution: the public, dystonia-centred release of
adult and pediatric hyperkinetic pose data (CC BY 4.0, concept DOI
`10.5281/zenodo.22232609 <https://doi.org/10.5281/zenodo.22232609>`_,
v1.1.0). This example loads the canonical records of one dystonic
patient and one control, compares their right-wrist kinematics, and
shows the per-frame expert phenomenology ratings that ride on every
patient record (eval-only by standing rule R1: never pretraining).
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

ds = moveatlas.dataset("cody_3")
print(ds)

records, meta = ds.get_data(subjects=["adult:P1", "adult:C1"])
print(meta)

# %%
# Pick one labeled take per subject. Records carry 2D COCO-derived
# canonical skeletons (15 joints, pixels, ~33 fps) with a per-frame,
# per-joint validity mask; patient records add two independent raters'
# per-frame ordinal ratings for seven hyperkinetic phenomena.

patient = next(r for r in records
               if r["subject_ns"] == "adult:P1"
               and r["take"] == "20231005_120101_merged")
control = next(r for r in records if r["subject_ns"] == "adult:C1")

R_WRIST = 8  # canonical joint index (configs/canonical_skeleton.yaml)


def wrist_speed(rec, seconds=30.0):
    """Right-wrist speed (units of body scale per s), masked frames NaN."""
    n = int(seconds * rec["fps"])
    xy = rec["coords"][:n, R_WRIST, :2].astype(float)
    ok = rec["valid_mask"][:n, R_WRIST]
    xy[~ok] = np.nan
    v = np.linalg.norm(np.diff(xy, axis=0), axis=1) * rec["fps"]
    return v / rec["scale"]


t = np.arange(len(wrist_speed(patient))) / patient["fps"]

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 6), height_ratios=[2, 1],
    gridspec_kw={"hspace": 0.35})

ax1.plot(t, wrist_speed(control), lw=0.6, label="control (C1)")
ax1.plot(t, wrist_speed(patient), lw=0.6, label="dystonic patient (P1)")
ax1.set_xlabel("time (s)")
ax1.set_ylabel("right-wrist speed\n(body scale / s)")
ax1.legend(loc="upper right", fontsize=8)
ax1.set_title("Right-wrist kinematics, 30 s, same task family")

# %%
# The expert layer: rater DD's per-frame ordinal ratings (0-2) for the
# same patient take. Dystonia is the dominant phenomenon in this
# subject; the strip shows when the rater saw it, frame by frame.

dd = patient["labels"]["dd"]
n = int(30.0 * patient["fps"])
strip = dd["values"][:n].T  # (7 symptoms, frames)

im = ax2.imshow(strip, aspect="auto", interpolation="nearest",
                extent=[0, 30, len(dd["names"]) - 0.5, -0.5],
                cmap="Reds", vmin=0, vmax=2)
ax2.set_yticks(range(len(dd["names"])))
ax2.set_yticklabels(dd["names"], fontsize=7)
ax2.set_xlabel("time (s)")
ax2.set_title("Per-frame expert ratings (rater DD, ordinal 0-2)")
fig.colorbar(im, ax=ax2, shrink=0.8, ticks=[0, 1, 2])

fig.suptitle("CODY adult cohort: signal and expert phenomenology",
             y=0.99)
plt.show()

# %%
# Both layers - canonical skeleton kinematics and frame-level expert
# labels - download on demand from the public record for anyone
# without the corpus machine (`pip install moveatlas`), and the labels
# stay quarantined to evaluation by construction.
