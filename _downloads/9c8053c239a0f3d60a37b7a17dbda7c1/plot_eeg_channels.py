# -*- coding: utf-8 -*-
"""
EEG during movement protocols
=============================

Scalp EEG from a Parkinson walking-protocol study (OpenNeuro ds007526),
harmonized to the canonical EEG contract: signal in microvolts at the
native 250 Hz, channel sites from the source headers, bad channels
carried explicitly.
"""

import matplotlib.pyplot as plt
import numpy as np

from moveatlas.datasets.base import load_record
from moveatlas.store import LocalStore

store = LocalStore()
rec = load_record(store.path(
    "datasets/eeg/pd_walking_eeg_ds007526/processed/canonical_eeg/"
    "pd_walking_eeg_ds007526__pd_walking_eeg_ds007526_sub-001__rest.pkl"))
print(rec["subject_ns"], rec["task"], rec["signal"].shape,
      rec["fps"], "Hz,", rec["unit"])
print("first channels:", rec["channels"][:8])

# %%
# A ten-second stack of the first eight channels, mean-centered.

fs = rec["fps"]
sl = slice(int(10 * fs), int(20 * fs))
t = np.arange(rec["signal"].shape[0])[sl] / fs
fig, ax = plt.subplots(figsize=(8, 4))
for k in range(8):
    v = rec["signal"][sl, k] - np.nanmean(rec["signal"][sl, k])
    ax.plot(t, v + k * 120, lw=0.5)
    ax.text(t[0] - 0.3, k * 120, str(rec["channels"][k]), fontsize=7,
            ha="right", va="center")
ax.set_yticks([])
ax.set_xlabel("time (s)")
ax.set_title("8 of 60 channels at rest (offsets 120 uV)")
fig.tight_layout()
