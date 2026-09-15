# -*- coding: utf-8 -*-
"""
Amplitude distributions and when to log them
============================================

Raw sEMG amplitudes are heavy-tailed: histograms of the rectified signal
look nothing like a Gaussian, and become tractable in log space. Seeing
the distribution BEFORE modeling is the cheapest protection against
mis-specified features.
"""
import matplotlib.pyplot as plt
import numpy as np

import moveatlas

subs = [f"gait120:S{i:03d}" for i in range(1, 6)]
records, _ = moveatlas.dataset("gait120").get_data(subjects=subs)
walk = [r for r in records if r["task"].startswith("level_walking")]
sig = np.concatenate([r["signal"] for r in walk])   # (N, 12) in mV
print(f"{sig.shape[0]:,} samples from {len(walk)} walking trials")

# %%
# Rectified amplitude histograms, linear vs log axis, for one muscle.

MU = 3   # tibialis anterior
amp = np.abs(sig[:, MU]) + 1e-6
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3))
axes[0].hist(amp, bins=200, density=True)
axes[0].set_xlim(0, np.percentile(amp, 99))
axes[0].set_title("linear scale", fontsize=9)
axes[1].hist(np.log10(amp), bins=200, density=True)
axes[1].set_title("log10 scale", fontsize=9)
for ax in axes:
    ax.set_xlabel("|amplitude| (mV)")
fig.suptitle("Tibialis anterior rectified amplitude, walking",
             fontsize=10)
fig.tight_layout()

# %%
# All twelve muscles at once, as log-amplitude box plots: a compact
# per-channel amplitude audit (and a sanity check that no channel sits
# at an implausible gain).

logamp = np.log10(np.abs(sig) + 1e-6)
names = [c["muscle"] for c in walk[0]["channels"]]
fig, ax = plt.subplots(figsize=(8.5, 3.4))
ax.boxplot([logamp[:, k] for k in range(12)], tick_labels=names,
           showfliers=False)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=7)
ax.set_ylabel("log10 |mV|")
ax.set_title("Per-muscle amplitude distributions, 5 subjects walking",
             loc="left", fontsize=9)
fig.tight_layout()
