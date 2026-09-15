# -*- coding: utf-8 -*-
"""
Time-frequency views: a walking EEG spectrogram
===============================================

The same subject of the Parkinson walking-protocol study (OpenNeuro
ds007526), at rest and walking, seen as spectrograms of one channel.
Movement writes itself into the spectrum: gait-locked low-frequency
power and broadband motion artifacts appear the moment walking starts,
which is exactly why movement EEG needs its own preprocessing care.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram

from moveatlas.datasets.base import load_record
from moveatlas.store import LocalStore

store = LocalStore()
base = ("datasets/eeg/pd_walking_eeg_ds007526/processed/canonical_eeg/"
        "pd_walking_eeg_ds007526__pd_walking_eeg_ds007526_sub-002__{}.pkl")
rest = load_record(store.path(base.format("rest")))
walk = load_record(store.path(base.format("walk")))
print("channels:", rest["channels"][:6], "... fs", rest["fps"])

# %%

CH = 2
fig, axes = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)
for ax, rec, label in ((axes[0], rest, "rest"), (axes[1], walk, "walk")):
    sig = np.nan_to_num(rec["signal"][:int(60 * rec["fps"]), CH])
    f, t, S = spectrogram(sig, fs=rec["fps"], nperseg=512, noverlap=384)
    keep = f <= 40
    ax.pcolormesh(t, f[keep], 10 * np.log10(S[keep] + 1e-12),
                  shading="gouraud", cmap="Blues")
    ax.set_title(f"{label} (channel {rec['channels'][CH]})", fontsize=9)
    ax.set_xlabel("time (s)")
axes[0].set_ylabel("frequency (Hz)")
fig.suptitle("60 s spectrograms, same subject, dB scale", fontsize=10)
fig.tight_layout()
