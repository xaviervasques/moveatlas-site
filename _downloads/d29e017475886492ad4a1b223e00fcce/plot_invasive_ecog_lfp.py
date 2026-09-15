# -*- coding: utf-8 -*-
"""
Inside the loop: ECoG and STN-LFP during a grip-force task
==========================================================

The invasive lane is real and on disk: the Merk and Neumann decoding
testbed holds 73 BIDS iEEG recordings of Parkinson patients performing
a grip-force task, with sensorimotor ECoG strips AND subthalamic LFP
recorded together, plus the measured force trace. This is the signal a
movement foundation model eventually meets at the electrode end of the
loop. Nothing here is harmonized yet (rule R1 keeps invasive data out
of the movement-pretraining contracts); the lane enters the EEG
family's contract at its own ingestion pass.
"""
import glob
import os

import matplotlib.pyplot as plt
import mne
import numpy as np
import pandas as pd

from moveatlas.store import LocalStore

BLUE, ORANGE, INK, GRID = "#2a78d6", "#eb6834", "#0b0b0b", "#e1e0d9"

base = LocalStore().path(
    "datasets/inversion_testbed/merk_neumann_ecog_lfp/raw")

subjects = pd.read_csv(os.path.join(base, "participants.tsv"), sep="\t")
runs = glob.glob(os.path.join(base, "*_ieeg.vhdr"))
print(f"{len(runs)} iEEG recordings from {len(subjects)} subjects "
      "(Merk & Neumann testbed, BIDS)")

# %%
# One run, all three signals at once: cortex, subthalamic nucleus, and
# the hand. sub-000, right hemisphere, run 3 carries a 6-contact ECoG
# strip, 3 STN-LFP contacts and the cleaned force trace at 1 kHz.

stem = "sub-000_ses-right_task-force_run-3"
raw = mne.io.read_raw_brainvision(
    os.path.join(base, f"{stem}_ieeg.vhdr"), preload=True,
    verbose="ERROR")
ch = pd.read_csv(os.path.join(base, f"{stem}_channels.tsv"), sep="\t")
ecog = ch.loc[ch["type"] == "ECOG", "name"].tolist()
lfp = ch.loc[ch["type"] == "SEEG", "name"].tolist()
mov = [n for n in raw.ch_names if n.endswith("_CLEAN")]
print(f"{len(ecog)} ECoG + {len(lfp)} STN-LFP contacts; "
      f"movement channels: {mov}")

fs = raw.info["sfreq"]
sl = slice(int(30 * fs), int(42 * fs))
t = raw.times[sl]
# the hand that actually moved in this run is the one with variance
forces = {n: raw.get_data(picks=[n])[0, sl] for n in mov}
hand = max(forces, key=lambda n: np.nanstd(forces[n]))

fig, ax = plt.subplots(figsize=(8.5, 5.2))
offset = 0
for name in lfp:
    v = raw.get_data(picks=[name])[0, sl]
    v = (v - v.mean()) / v.std()
    ax.plot(t, v + offset, lw=0.5, color=ORANGE)
    ax.text(t[0] - 0.35, offset, name, fontsize=6.5, ha="right",
            va="center", color=ORANGE)
    offset += 4
for name in ecog:
    v = raw.get_data(picks=[name])[0, sl]
    v = (v - v.mean()) / v.std()
    ax.plot(t, v + offset, lw=0.5, color=BLUE)
    ax.text(t[0] - 0.35, offset, name, fontsize=6.5, ha="right",
            va="center", color=BLUE)
    offset += 4
f = forces[hand]
f = (f - f.min()) / (f.max() - f.min() + 1e-12) * 3
ax.plot(t, f + offset, lw=1.2, color=INK)
ax.text(t[0] - 0.35, offset + 1.5, f"grip force\n({hand})", fontsize=6.5,
        ha="right", va="center", color=INK)
ax.set_xlabel("time (s)")
ax.set_yticks([])
ax.spines[["top", "right", "left"]].set_visible(False)
ax.set_title("12 s of a grip-force run: STN-LFP, sensorimotor ECoG, "
             "and the hand (z-scored)", loc="left", fontsize=10)
fig.tight_layout()

# %%
# Where the electrodes sit, in MNI space. The coordinates are BIDS
# metadata, not an illustration: an ECoG strip over sensorimotor
# cortex and three LFP contacts deep in the subthalamic region.

el = pd.read_csv(os.path.join(base, "sub-000_electrodes.tsv"), sep="\t")
is_ecog = el["name"].str.startswith("ECOG")
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6))
for ax, (a, b, la, lb) in zip(axes, [("x", "z", "MNI x (mm)", "MNI z (mm)"),
                                     ("y", "z", "MNI y (mm)", "MNI z (mm)")]):
    ax.scatter(el.loc[is_ecog, a], el.loc[is_ecog, b], s=42, color=BLUE,
               label="ECoG strip", zorder=3)
    ax.scatter(el.loc[~is_ecog, a], el.loc[~is_ecog, b], s=42,
               color=ORANGE, label="STN-LFP", zorder=3)
    ax.axhline(0, color=GRID, lw=0.8)
    ax.axvline(0, color=GRID, lw=0.8)
    ax.set_xlabel(la)
    ax.set_ylabel(lb)
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
axes[0].legend(fontsize=7.5, frameon=False, loc="lower left")
fig.suptitle("sub-000 electrode positions (coronal and sagittal views)",
             fontsize=10, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.94))

# %%
# The rest of the invasive lane, waiting for its contract: the Oxford
# cervical-dystonia LFP deposit (the only open dystonia LFP in
# existence, 14.7 GB held) and OpenNeuro ds004998 (MEG + STN-LFP in
# Parkinson, 162 GB held). Their cards document exactly what each
# holds and how it was verified.
